import sys
import argparse
import httpx
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
from synqly.management.client import SynqlyManagement

TENANT_NAME = "Tenant ABC"

def clean_example(app: utils.App, synqly_org_token: str):
    if app != None and len(app.tenants) > 0:
        app._cleanup_handler()
    elif synqly_org_token != None:
        transport = httpx.HTTPTransport(retries=3)
        management_client = SynqlyManagement(
            token=synqly_org_token,
            httpx_client=httpx.Client(transport=transport),
        )

        available_accounts = management_client.accounts.list()
        
        for account in available_accounts.result:
            if account.fullname == TENANT_NAME:
                try:
                    management_client.accounts.delete(account.id)
                    print("Cleaned up account '{}'".format(account.id))
                except Exception as e:
                    print("Error deleting account '{}': {}".format(account.name, str(e)))


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

        # Set a limit on the number of application pages to retrieve to keep the
        # example manageable
        pagesRetrieved = 0
        currentCursor = ""
        while pagesRetrieved < pagesToRetrieve:
            response = tenant.synqly_engine_client.edr.query_applications(
                cursor=currentCursor
            )
            resultsPage = response.result
            if resultsPage is None:
                print("Unable to retrieve applications")
                break

            currentCursor = response.cursor
            pagesRetrieved += 1
            for application in resultsPage:
                print()
                pprint.pp(application)

            # If the returned cursor is empty, it means we've retrieved all results
            if currentCursor == "":
                break

        # Retrieve a single endpoint
        print("\nEndpoint:")
        endpointResponse = tenant.synqly_engine_client.edr.query_endpoints()
        if endpointResponse.result is None:
            print("Unable to retrieve endpoints")
        else:
            if len(endpointResponse.result) < 1:
                print("No endpoints found")
            else:
                pprint.pp(endpointResponse.result[0])


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
        app.new_tenant(synqly_org_token, TENANT_NAME)
        print("{} created".format(TENANT_NAME))
    except Exception as e:
        print("Error creating {}: {}".format(TENANT_NAME, str(e)))
        clean_example(app, synqly_org_token)

    # Placeholder variables for the IDs of the Credentials we will create
    abc_credential_id = ""

    # Create a Synqly Credential for splunk connector.
    try:
        abc_credential_id = app.create_credential(
            TENANT_NAME,
            "edr",
            sentinelone_credential_config(sentinelone_token),
        )
    except Exception as e:
        print("Error creating Credential for {}: {}".format(TENANT_NAME, str(e)))
        clean_example(app, synqly_org_token)
        raise e

    # Use the stored credential ID to configure a SentinelOne Integration for Tenant ABC
    try:
        app.configure_integration(
            TENANT_NAME,
            sentinelone_provider_config(sentinelone_url, abc_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for {}: {}".format(TENANT_NAME, str(e)))
        clean_example(app, synqly_org_token)
        raise e

    # Start a background job to simulate data generation
    try:
        demo_edr(app, 5)
    except Exception as e:
        print("Error running background job: " + str(e))
        clean_example(app, synqly_org_token)
        raise e

    # Clean up Synqly Accounts and Integrations
    clean_example(app, synqly_org_token)


try:
    main()
except:
    sys.exit(1)
