import sys
import argparse
import pprint
from pathlib import Path

# Add the root directory to the system path so that we can import "shared".
# "shared" contains common Application logic used throughout the SDK examples.
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
        "--sentinelone-url",
        dest="sentinelone_url",
        type=str,
        required=True,
        default="",
        help="URL of target SentinelOne instance. Example: 'https://company.sentinelone.net'",
    )
    parser.add_argument(
        "--sentinelone-token",
        dest="sentinelone_token",
        type=str,
        required=True,
        default="",
        help="SentinelOne API token.",
    )
    args = parser.parse_args()
    return args


def sentinelone_credential_config(
    sentinelone_token: str,
) -> mgmt.CredentialConfig_Token:
    """
    Helper method to construct a Token CredentialConfig object.
    """
    return mgmt.CredentialConfig_Token(type="token", secret=sentinelone_token)


def sentinelone_provider_config(
    sentinelone_url: str, credential_id: str
) -> mgmt.ProviderConfig:
    """
    Helper method to construct the Provider Config needed to register a
    SentinelOne Integration with Synqly.
    """
    return mgmt.ProviderConfig_EdrSentinelone(
        type="edr_sentinelone",
        credential=mgmt.SentinelOneCredential_TokenId(
            type="token_id", value=credential_id
        ),
        url=sentinelone_url,
    )


def demo_edr(app: utils.App, pagesToRetrieve: int):
    # Iterate through each tenant and query applications if they have an EDR
    # Integration defined
    for tenant in app.tenants.values():
        print("Doing some work for tenant {}".format(tenant.tenant_name))

        # Fallthrough logic in case the engine client has not been registered yet
        if tenant.synqly_engine_client is None:
            continue

        # Set a limit on the number of pages to retrieve to keep the example manageable
        pagesRetrieved = 0
        currentCursor = ""

        while pagesRetrieved < pagesToRetrieve:
            response = tenant.synqly_engine_client.edr.query_applications(
                cursor=currentCursor
            )
            resultsPage = response.result
            currentCursor = response.cursor
            pagesRetrieved += 1
            for application in resultsPage:
                pprint.pp(application)

            # If the returned cursor is empty, it means we've retrieved all results
            if currentCursor == "":
                break


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    sentinelone_url = args.sentinelone_url
    sentinelone_token = args.sentinelone_token

    # Initialize an empty application to store tenants
    app = utils.App(connector_type="edr")

    # Create tenants within the Application
    try:
        app.new_tenant(synqly_org_token, "Tenant ABC")
        print("Tenant ABC created")
    except Exception as e:
        print("Error creating Tenant ABC:" + str(e))
        app._cleanup_handler()

    # Placeholder variables for the IDs of the Credentials we will create
    abc_credential_id = ""

    # Create a Synqly Credential for splunk connector.
    try:
        abc_credential_id = app.create_credential(
            "Tenant ABC",
            "edr",
            sentinelone_credential_config(sentinelone_token),
        )
    except Exception as e:
        print("Error creating Credential for Tenant ABC: " + str(e))
        app._cleanup_handler()
        raise e

    # Use the stored credential ID to configure a SentinelOne Integration for Tenant ABC
    try:
        app.configure_integration(
            "Tenant ABC",
            sentinelone_provider_config(sentinelone_url, abc_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant ABC: " + str(e))
        app._cleanup_handler()
        raise e

    # Start a background job to simulate data generation
    try:
        demo_edr(app, 5)
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
