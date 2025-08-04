"""
Synqly Python SDK Ticketing Example

This example demonstrates how to use the Synqly Python SDK to create a
Ticketing Integration
"""

# Standard imports
import argparse
import base64
import httpx
from pathlib import Path
import sys
import time

# Add the root directory to the system path so that we can import common
# Application logic.
current_script = Path(__file__).resolve()
root = current_script.parents[1]
sys.path.append(str(root))

from shared import utils

# Synqly Python SDK imports
from synqly import engine
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement

TENANT_NAME = "Golden Ticket Solutions"

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
        required=False,
        default="",
        help="URL of target JIRA instance, example: 'https://company.atlassian.net'",
    )
    parser.add_argument(
        "--jira-username",
        dest="jira_username",
        type=str,
        required=False,
        default="",
        help="Username for authenticating with JIRA, example: 'name@company.com'",
    )
    parser.add_argument(
        "--jira-token",
        dest="jira_token",
        type=str,
        required=False,
        default="",
        help="Token for authenticating with JIRA, for more information see https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/",
    )
    parser.add_argument(
        "--project-key",
        dest="project_key",
        type=str,
        required=True,
        default="",
        help="Key of target JIRA project, example: 'TST'",
    )
    args = parser.parse_args()
    return args


def jira_credential_config(jira_username: str, jira_token: str):
    """
    Helper method to construct an AWS CredentialConfig object.
    """
    return mgmt.CredentialConfig_Basic(
        type="basic", username=jira_username, secret=jira_token
    )


def mock_provider_config():
    return mgmt.ProviderConfig_TicketingMockTicketing(
        type="ticketing_mock_ticketing",
    )


def jira_provider_config(jira_url: str, jira_username: str, jira_token: str):
    return mgmt.ProviderConfig_TicketingJira(
        type="ticketing_jira",
        url=jira_url,
        default_issue_type="Bug",
        credential=mgmt.JiraCredential_Basic(
            type="basic",
            username=jira_username,
            secret=jira_token,
        )
    )


def ticketing_actions(tenant: utils.Tenant, project_key: str, username: str):
    """
    Performs a few operations with the ticketing connector to show what operations
    are supported by the Synqly API
    """
    # Iterate through each tenant and send an event to their Event Logger
    if tenant.synqly_engine_client is None:
        raise Exception("no Synqly client for tenant")

    # Create a new ticket
    print("\nCreating ticket")
    new_ticket = create_sample_ticket(tenant, project_key, username)
    create_response = tenant.synqly_engine_client.ticketing.create_ticket(
        request=new_ticket
    )
    print("Created ticket: {}".format(create_response.result.name))

    # Query ticket details using Synqly
    print("\nQuerying ticket details")
    get_response = tenant.synqly_engine_client.ticketing.get_ticket(
        ticket_id=create_response.result.id
    )
    print("Retrieved ticket details: {}".format(get_response.result))

    print("\nWaiting 4 seconds before marking ticket as done...")
    time.sleep(4)

    # Ticket querying examples
    tickets_in_project = tenant.synqly_engine_client.ticketing.query_tickets(
        filter='project[eq]'+project_key,
    )
    print('\nQuerying all tickets in project '+project_key)
    print('Got {} tickets in project {}'.format(len(tickets_in_project.result), project_key))

    # Query for all tickets created by the user that are not "Done"
    q = tenant.synqly_engine_client.ticketing.query_tickets(
        filter=[
            'creator[eq]'+username,
            'status[ne]Done'
        ],
    )
    print('\nQuerying all tickets created by '+username+' that are not "Done"')
    print('Got {} tickets created by {}'.format(len(q.result), username))

    # Perform attachment actions
    # attachment_actions(tenant, create_response.result.id)

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

    # Query for all tickets created by the user that are "Done"
    q = tenant.synqly_engine_client.ticketing.query_tickets(
        filter=[
            'creator[eq]'+username,
            'status[eq]Done'
        ],
    )
    print('\nQuerying all tickets created by '+username+' that are "Done"')
    print('Got {} tickets created by {}'.format(len(q.result), username))


def attachment_actions(tenant: utils.Tenant, ticket_id: str):
    """
    Performs a few operations with the attachment connector to show what operations
    are supported by the Synqly API
    """
    # Use the README as an example file to attach
    file = open(current_script.parents[0] / "README.md", "rb")
    content = base64.b64encode(file.read())

    # Create a new attachment
    print("\nCreating attachment")
    tenant.synqly_engine_client.ticketing.create_attachment(ticket_id=ticket_id,
        request=engine.CreateAttachmentRequest(
            file_name="README.md",
            content=content,
        ),
    )
    print("Added an attachment to ticket {}".format(ticket_id))

    # Query attachment details using Synqly
    print("\nQuerying attachment details")
    attachments = tenant.synqly_engine_client.ticketing.list_attachments_metadata(ticket_id)
    print("Retrieved attachment details: {}".format(attachments.result))

    # Download the attachment
    print("\nDownloading attachment")
    download_response = tenant.synqly_engine_client.ticketing.download_attachment(
        ticket_id=ticket_id, attachment_id=attachments.result[0].id)

    # Write attachment contents to a file -- using /tmp so we don't clutter the repo
    outfile = "/tmp/"+download_response.result.file_name
    with open(outfile, "wb") as f:
        f.write(base64.b64decode(download_response.result.content))
    print("Downloaded attachment: {} and wrote its contents to {}".format(download_response.result.file_name, outfile))


def create_sample_ticket(tenant: utils.Tenant, project_key: str, username: str):
    """
    Creates a sample ticket for use in the background job.
    """
    return engine.CreateTicketRequest(
        # Required fields for all ticket providers
        id="SDK Example Ticket",
        name="SDK Example Ticket",
        summary="Sample ticket created by the Synqly Python SDK",
        project=project_key,
        creator=username,
        issue_type="Bug",
        priority="LOW",
        # Optional fields
        description=tenant.tenant_name + " requires maintenance.",
        status="To Do",
    )


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    jira_url = args.jira_url
    jira_username = args.jira_username
    jira_token = args.jira_token
    project_key = args.project_key

    if synqly_org_token == "":
        raise ValueError("Synqly Organization Token is required")

    # Initialize an empty application to store our simulated tenants
    app = utils.App("ticketing")

    # Initialize tenants within our Application
    try:
        app.new_tenant(synqly_org_token, TENANT_NAME)
        print("Tenant {} created".format(TENANT_NAME))
    except Exception as e:
        print("Error creating tenant {}: ".format(TENANT_NAME) + str(e))
        clean_example(app, synqly_org_token)
        raise e

    # Configure a ticketing integration based on the configuration. If no jira credentials
    # are provided, then mock ticket provider is used
    provider_config: mgmt.ProviderConfig
    if jira_url != "" and jira_username != "" and jira_token != "":
        print("Using Jira as the ticketing provider\n")
        provider_config = jira_provider_config(jira_url, jira_username, jira_token)
    else:
        print("WARNING: no Jira credentials provided\nUsing Mock Ticketing as the ticketing provider\n")
        provider_config = mock_provider_config()

    try:
        app.configure_integration(TENANT_NAME, provider_config)
    except Exception as e:
        print("Error configuring provider integration for tenant {}: ".format(TENANT_NAME) + str(e))
        clean_example(app, synqly_org_token)
        raise e

    try:
        ticketing_actions(app.tenants[TENANT_NAME], project_key, jira_username)
    except Exception as e:
        print("Error running background job: " + str(e))
        clean_example(app, synqly_org_token)
        raise e

    clean_example(app, synqly_org_token)


try:
    main()
except Exception as e:
    print("Error: " + str(e))
    sys.exit(1)
