"""
Synqly Python SDK PagerDuty Incident Response Example

This example demonstrates how to use the Synqly Python SDK to create a
PagerDuty Incident Response Integration
"""

# Standard imports
import argparse
import json
import httpx
from pathlib import Path
import sys
import time
from typing import Any

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

TENANT_NAME = "PagerDuty Incident Response Demo"


def parse_args() -> argparse.Namespace:
    """
    Parses command line arguments for this example.
    """
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK PagerDuty Incident Response Example"
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
        "--pagerduty-url",
        dest="pagerduty_url",
        type=str,
        required=False,
        default="https://api.pagerduty.com",
        help="URL of PagerDuty instance, example: 'https://api.pagerduty.com'",
    )
    parser.add_argument(
        "--pagerduty-token",
        dest="pagerduty_token",
        type=str,
        required=True,
        default="",
        help="Token for authenticating with PagerDuty",
    )
    parser.add_argument(
        "--service-id",
        dest="service_id",
        type=str,
        required=False,
        default="",
        help="ID of target PagerDuty service",
    )
    parser.add_argument(
        "--creator-email",
        dest="creator_email",
        type=str,
        required=False,
        default="",
        help="Email address of a valid PagerDuty user to create incidents as",
    )
    args = parser.parse_args()
    return args


def clean_example(app: utils.App, synqly_org_token: str) -> None:
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


def pagerduty_provider_config(pagerduty_url: str, pagerduty_token: str) -> mgmt.ProviderConfig_TicketingPagerduty:
    return mgmt.ProviderConfig_TicketingPagerduty(
        type="ticketing_pagerduty",
        url=pagerduty_url,
        credential=mgmt.PagerDutyCredential_Token(
            type="token",
            secret=pagerduty_token,
        )
    )


def ticketing_actions(tenant: utils.Tenant, service_id: str, email: str) -> None:
    """
    Performs a few operations with the ticketing connector to show what operations
    are supported by the Synqly API
    """
    # Iterate through each tenant and send an event to their Event Logger
    if tenant.synqly_engine_client is None:
        raise Exception("no Synqly client for tenant")

    # Create a new incident
    print("\nCreating incident")
    new_ticket = create_sample_ticket(tenant, service_id, email)
    create_response = tenant.synqly_engine_client.ticketing.create_ticket(
        **new_ticket.dict()
    )
    print("Created incident: {}".format(create_response.result.name))

    # Query incident details using Synqly
    print("\nQuerying incident details")
    get_response = tenant.synqly_engine_client.ticketing.get_ticket(
        ticket_id=create_response.result.id
    )
    print("Retrieved incident details: {}".format(get_response.result))

    print("\nWaiting 4 seconds before resolving incident...")
    time.sleep(4)

    # Incident querying examples
    # For PagerDuty, query all incidents since service filtering works differently
    incidents = tenant.synqly_engine_client.ticketing.query_tickets()
    print('\nQuerying all PagerDuty incidents')
    print('Got {} incidents'.format(len(incidents.result)))

    # Query for all incidents created by the user that are not "resolved"
    q = tenant.synqly_engine_client.ticketing.query_tickets(
        filter=[
            'creator[eq]'+email,
            'status[ne]resolved'
        ],
    )
    print('\nQuerying all incidents created by '+email+' that are not "resolved"')
    print('Got {} incidents created by {}'.format(len(q.result), email))

    # Use a JSON Patch to update the incident status to acknowledged first
    print('\nUpdating incident status to "acknowledged"')
    update_response = tenant.synqly_engine_client.ticketing.patch_ticket(
        ticket_id=create_response.result.id,
        request=[
            {"op": "replace", "path": "/status", "value": "acknowledged"},
            {"op": "replace", "path": "/creator", "value": email}
        ],
    )
    print(
        'Updated incident {} status to "{}"'.format(
            update_response.result.id, update_response.result.status
        )
    )

    # Wait a moment then resolve the incident
    print('\nWaiting 2 seconds before resolving incident...')
    time.sleep(2)

    print('\nUpdating incident status to "resolved"')
    update_response = tenant.synqly_engine_client.ticketing.patch_ticket(
        ticket_id=create_response.result.id,
        request=[
            {"op": "replace", "path": "/status", "value": "resolved"},
            {"op": "replace", "path": "/creator", "value": email}
        ],
    )
    print(
        'Updated incident {} status to "{}"'.format(
            update_response.result.id, update_response.result.status
        )
    )

    # Query for all incidents created by the user that are "resolved"
    q = tenant.synqly_engine_client.ticketing.query_tickets(
        filter=[
            'creator[eq]"'+email+'"',
            'status[eq]"resolved"'
        ],
    )
    print('\nQuerying all incidents created by '+email+' that are "resolved"')
    print('Got {} incidents created by {}'.format(len(q.result), email))


def create_sample_ticket(tenant: utils.Tenant, service_id: str, email: str) -> engine.CreateTicketRequest:
    """
    Creates a sample incident for use in the background job.
    """
    return engine.CreateTicketRequest(
        # Required fields for all ticket providers
        name="SDK Example Incident",
        summary="Sample incident created by the Synqly Python SDK",
        project=service_id,
        creator=email,
        priority="HIGH",
        # Optional fields
        description=tenant.tenant_name + " requires incident response.",
        status="Triggered",
    )


def incident_response_actions(tenant: utils.Tenant) -> None:
    """
    Performs a few operations with the incident response connector to show what operations
    are supported by the Synqly API
    """
    escalation_policies = tenant.synqly_engine_client.ticketing.query_escalation_policies(
        limit=10,
    )
    for escalation_policy in escalation_policies.result:
        print("Escalation policy: {}\n".format(json.dumps(escalation_policy.dict(), indent=2)))

    if len(escalation_policies.result) > 0:
        oncall = tenant.synqly_engine_client.ticketing.list_on_call(
            escalation_policy_id=escalation_policies.result[0].id
        )
        for agent in oncall.result:
            print("On-call Agent for escalation policy {}: {}\n".format(escalation_policies.result[0].id, json.dumps(agent.dict(), indent=2)))



def main() -> None:
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    pagerduty_url = args.pagerduty_url
    pagerduty_token = args.pagerduty_token
    service_id = args.service_id
    creator_email = args.creator_email

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

    # Configure a PagerDuty integration for incident response
    print("Using PagerDuty as the ticketing provider for incident response\n")
    provider_config = pagerduty_provider_config(pagerduty_url, pagerduty_token)

    try:
        app.configure_integration(TENANT_NAME, provider_config)
    except Exception as e:
        print("Error configuring provider integration for tenant {}: ".format(TENANT_NAME) + str(e))
        clean_example(app, synqly_org_token)
        raise e

    try:
        incident_response_actions(app.tenants[TENANT_NAME])
    except Exception as e:
        print("Error running incident response actions: " + str(e))
        clean_example(app, synqly_org_token)
        raise e

    if service_id != "" and creator_email != "":
        try:
            ticketing_actions(app.tenants[TENANT_NAME], service_id, creator_email)
        except Exception as e:
            print("Error running ticketing actions: " + str(e))
            clean_example(app, synqly_org_token)
            raise e

    clean_example(app, synqly_org_token)


try:
    main()
except Exception as e:
    print("Error: " + str(e))
    sys.exit(1)
