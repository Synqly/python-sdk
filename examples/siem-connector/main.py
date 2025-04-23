import sys
import time
import argparse
from pathlib import Path

# Add the root directory to the system path so that we can import common
# Application logic.
current_script = Path(__file__).resolve()
root = current_script.parents[1]
sys.path.append(str(root))

from shared import utils

# Synqly Python SDK imports
from synqly import engine
from synqly import management as mgmt


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK SIEM Connector Example"
    )
    parser.add_argument(
        "--synqly-org-token",
        dest="synqly_org_token",
        type=str,
        required=True,
        default="",
        help="Token for authenticating with a Synqly Organization. For more information, see https://docs.synqly.com/reference/api-authentication.",
    )
    parser.add_argument(
        "--splunk-url",
        dest="splunk_url",
        type=str,
        required=True,
        default="",
        help="URL of target Splunk HTTP Event Collector (HEC) endpoint, example: 'https://splunk.synqly.com/services/collector/event'",
    )
    parser.add_argument(
        "--splunk-token",
        dest="splunk_hec_token",
        type=str,
        required=True,
        default="",
        help="Splunk HTTP Event Collector (HEC) token. For more information, see https://docs.splunk.com/Documentation/Splunk/9.1.2/Data/UsetheHTTPEventCollector.",
    )
    parser.add_argument(
        "--duration-seconds",
        dest="duration_seconds",
        type=int,
        required=False,
        default=3600,
        help="Duration in seconds for the data generation loop",
    )
    args = parser.parse_args()
    return args


def splunk_credential_config(splunk_token):
    """
    Helper method to construct a Token CredentialConfig object.
    """
    return mgmt.CredentialConfig_Token(type="token", secret=splunk_token)


def mock_provider_config():
    return mgmt.ProviderConfig_SiemMockSiem(
        type="siem_mock_siem",
    )


def splunk_provider_config(splunk_url, credential_id):
    return mgmt.ProviderConfig_SiemSplunk(
        type="siem_splunk",
        search_service_credential=mgmt.SplunkSearchCredential_Token(
            type="token", secret="abc"
        ),
        search_service_url=splunk_url,
        hec_credential=mgmt.SplunkHecToken_TokenId(
            type="token_id", value=credential_id
        ),
        hec_url=splunk_url,
        skip_tls_verify=True,
    )


def background_job(app, duration_seconds):
    start_time = time.time()
    end_time = start_time + duration_seconds

    while not app.terminated:
        # Check if we have reached the provided duration
        if end_time < time.time():
            print(
                "Max duration of {} seconds reached, terminating...".format(
                    duration_seconds
                )
            )
            app._cleanup_handler()
            return

        # Iterate through each tenant and send an event to their Event Logger
        for tenant in app.tenants.values():
            print("Doing some work for tenant {}".format(tenant.tenant_name))

            if tenant.synqly_engine_client is None:
                continue

            new_event = create_sample_event()
            # Send an event to the tenant's Event Logger
            tenant.synqly_engine_client.siem.post_events(
                request=[new_event],
            )
            print("{}: Logged event".format(tenant.tenant_name))

        time.sleep(2)
        print("")


def create_sample_event():
    # Currently uses hard-coded numbers to represent OCSF Enums. We aim to add
    # enums for these values in the future to make OCSF objects easier to work with.
    return engine.Event_ScheduledJobActivity(
        # OCSF Activity_Update
        activity_id=2,
        # OCSF Action_Update - the action is allowed
        action_id=1,
        # OCSF CategoryUID: 1 - SystemActivity
        category_uid=1,
        # OCSF ClassUID: 1006 - ScheduledJobActivity:
        class_uid=1006,
        class_name="Scheduled Job Activity",
        cloud={
            "provider": "AWS",
            "region": "us-east-1",
        },
        disposition_id=99,
        # OCSF DeviceType_Server
        device={
            "type_id": 1,
        },
        # OCSF scheduledJobActivity.Job
        job={
            # OCSF scheduledJobActivity.File
            "file": {
                "name": "main.py",
                "type_id": 1,
            },
            "name": "Background Job",
        },
        # OCSF scheduledJobActivity.Metadata
        metadata={
            # OCSF scheduledJobActivity.Product
            "product": {
                "vendor_name": "Synqly Python SDK",
            },
            "version": "1.1.0",
        },
        time=time.time(),
        # OCSF Severity_Informational
        severity_id=1,
        # OCSF Type_ScheduledJobActivity_Update
        type_uid=100602,
    )


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    splunk_url = args.splunk_url
    splunk_hec_token = args.splunk_hec_token
    duration_seconds = args.duration_seconds

    # Initialize an empty application to store tenants
    app = utils.App(connector_type="siem")

    # Create tenants within the Application
    try:
        app.new_tenant(synqly_org_token, "Tenant ABC")
        print("Tenant ABC created")
    except Exception as e:
        print("Error creating Tenant ABC:" + str(e))
        app._cleanup_handler()

    try:
        app.new_tenant(synqly_org_token, "Tenant XYZ")
        print("Tenant XYZ created")
    except Exception as e:
        print("Error creating Tenant XYZ:" + str(e))
        app._cleanup_handler()

    # Placeholder variables for the IDs of the Credentials we will create
    xyz_credential_id = ""

    # Create a Synqly Credential for splunk connector.
    try:
        xyz_credential_id = app.create_credential(
            "Tenant XYZ",
            "siem",
            splunk_credential_config(splunk_hec_token),
        )
    except Exception as e:
        print("Error creating Credential for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        raise e

    # Configure a mock integration for tenant ABC and an S3 Integration for Tenant XYZ
    try:
        app.configure_integration(
            "Tenant ABC",
            mock_provider_config(),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant ABC: " + str(e))
        app._cleanup_handler()
        raise e

    try:
        app.configure_integration(
            "Tenant XYZ",
            splunk_provider_config(splunk_url, xyz_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        raise e

    # Start a background job to generate data
    try:
        background_job(app, duration_seconds)
    except Exception as e:
        print("Error running background job: " + str(e))
        app._cleanup_handler()
        raise e

    # Clean up Synqly Accounts and Integrations
    app._cleanup_handler()


try:
    main()
except:
    sys.exit(1)
