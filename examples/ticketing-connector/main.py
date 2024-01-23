"""
Synqly Python SDK Ticketing Example

This example demonstrates how to use the Synqly Python SDK to create a
Ticketing Integration for a tenant.
"""

# Standard imports
import time
import sys
import argparse
from pathlib import Path

# Add the root directory to the system path so that we can import common
# Application logic.
current_script = Path(__file__).resolve()
root = current_script.parents[1]
sys.path.append(str(root))

from shared import utils

# Synqly Python SDK imports
import engine
import management as mgmt


def parse_args():
    """
    Parses command line arguments for this example.
    """
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK Ticketing Connector Example"
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
        "--jira-url",
        dest="jira_url",
        type=str,
        required=True,
        default="",
        help="URL of target JIRA instance, example: 'https://company.atlassian.net'",
    )
    parser.add_argument(
        "--jira-username",
        dest="jira_username",
        type=str,
        required=True,
        default="",
        help="Username for authenticating with JIRA, example: 'name@company.com'",
    )
    parser.add_argument(
        "--jira-token",
        dest="jira_token",
        type=str,
        required=True,
        default="",
        help="Token for authenticating with JIRA, for more information see https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/",
    )
    parser.add_argument(
        "--jira-project-key",
        dest="jira_project_key",
        type=str,
        required=True,
        default="",
        help="Key of target JIRA project, example: 'TST'",
    )
    args = parser.parse_args()
    return args


def mock_credential_config():
    """
    Helper method to construct a mock CredentialConfig object.
    """
    return mgmt.CredentialConfig_Basic(type="basic", username="mock", secret="mock")


def jira_credential_config(jira_username, jira_token):
    """
    Helper method to construct an AWS CredentialConfig object.
    """
    return mgmt.CredentialConfig_Basic(
        type="basic", username=jira_username, secret=jira_token
    )


def mock_provider_config(credential_id):
    return mgmt.ProviderConfig_Ticketing(
        type="ticketing",
        endpoint="mock",
        credential_id=credential_id,
    )


def jira_provider_config(jira_url, credential_id):
    return mgmt.ProviderConfig_Ticketing(
        type="ticketing",
        endpoint=jira_url,
        credential_id=credential_id,
    )


def background_job(app, jira_project_key, jira_username):
    """
    Simulates a background process performing work on behalf of tenants.
    Iterates through all tenants and, for any tenant with a Synqly Engine
    Client defined, creates a new ticket. After a short delay,
    background_job will update the ticket's status to "Done".
    """
    # Iterate through each tenant and send an event to their Event Logger
    for tenant in app.tenants.values():
        # Skip tenants that don't have a Synqly Engine Client initialized
        if tenant.synqly_engine_client is None:
            continue

        # Create a new ticket
        print("\nCreating ticket")
        new_ticket = create_sample_ticket(tenant, jira_project_key, jira_username)
        create_response = tenant.synqly_engine_client.ticketing.create_ticket(
            request=new_ticket
        )
        print("Created ticket: {}".format(create_response.result.name))

        # Query ticket details using Synqly
        print("\nQuerying ticket details")
        get_response = tenant.synqly_engine_client.ticketing.get_ticket(
            ticket_id=create_response.result.id
        )
        print(get_response)
        # print("Retrieved ticket details: {}".format(get_response.result))

        print("\nWaiting 4 seconds before marking ticket as done...")
        time.sleep(4)

        # Use a JSON Patch to update the ticket status
        print('\nUpdating ticket status to "Done"')
        update_response = tenant.synqly_engine_client.ticketing.patch_ticket(
            ticket_id=create_response.result.id,
            request=[{"op": "replace", "path": "/status", "value": "Done"}],
        )
        print(
            'Updated ticket {} status to "{}"'.format(
                update_response.result.id, update_response.result.status
            )
        )


def create_sample_ticket(tenant, jira_project_key, jira_username):
    """
    Creates a sample ticket for use in the background job.
    """
    return engine.CreateTicketRequest(
        # Required fields for all ticket providers
        id="SDK Example Ticket",
        name="SDK Example Ticket",
        summary="Sample ticket created by the Synqly Python SDK",
        # JIRA required fields. These fields are optional at the connector level
        # (i.e. for all ticketing providers), but must be set when submitting a
        # ticket to a JIRA integration.
        project=jira_project_key,
        creator=jira_username,
        issue_type="Bug",
        priority="LOW",
        # Optional fields
        description=tenant.tenant_name + " requires maintenance.",
    )


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    jira_url = args.jira_url
    jira_username = args.jira_username
    jira_token = args.jira_token
    jira_project_key = args.jira_project_key

    # Initialize an empty application to store our simulated tenants
    app = utils.App("ticketing")

    # Initialize tenants within our Application
    try:
        app.new_tenant(synqly_org_token, "Tenant ABC")
        print("Tenant ABC created")
    except Exception as e:
        print("Error creating Tenant ABC:" + str(e))
        app._cleanup_handler()
        raise e
    try:
        app.new_tenant(synqly_org_token, "Tenant XYZ")
        print("Tenant XYZ created")
    except Exception as e:
        print("Error creating Tenant XYZ:" + str(e))
        app._cleanup_handler()
        raise e

    # Placeholder variables for the IDs of the Credentials we will create
    abc_credential_id = ""
    xyz_credential_id = ""

    # Create a Synqly Credential for each tenant.
    try:
        abc_credential_id = app.create_credential(
            "Tenant ABC", "mock_ticketing", mock_credential_config()
        )
    except Exception as e:
        print("Error creating Credential for Tenant ABC: " + str(e))
        app._cleanup_handler()
        raise e
    try:
        xyz_credential_id = app.create_credential(
            "Tenant XYZ",
            "jira",
            jira_credential_config(jira_username, jira_token),
        )
    except Exception as e:
        print("Error creating Credential for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        raise e

    # Configure a mock integration for tenant ABC and a JIRA Integration for Tenant XYZ
    try:
        app.configure_integration(
            "Tenant ABC",
            "mock_ticketing",
            mock_provider_config(abc_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant ABC: " + str(e))
        app._cleanup_handler()
        raise e
    try:
        app.configure_integration(
            "Tenant XYZ",
            "jira",
            jira_provider_config(jira_url, xyz_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        raise e

    # Start a background job to generate data
    try:
        background_job(app, jira_project_key, jira_username)
    except Exception as e:
        print("Error running background job: " + str(e))
        app._cleanup_handler()
        raise e

    app._cleanup_handler()


try:
    main()
except:
    sys.exit(1)
