"""
Synqly Python SDK - Assets Example

This example demonstrates how to use Synqly Python SDK to create an Assets Integration for a tenant.
"""

# Standard imports
import sys
import argparse
import configparser
import httpx
import time
from datetime import datetime, timedelta, timezone
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

TENANT_SERVICENOW_NAME = "Tenant ServiceNow"

def clean_async(account_id: str, async_mgmt: SynqlyManagement, tenant: utils.Tenant):
    if tenant != None:
        try:
            list_webhooks_response = tenant.synqly_management_client.organization_webhooks.list()

            for webhook in list_webhooks_response.result:
                try:
                    tenant.synqly_management_client.organization_webhooks.delete(
                        webhook_id = webhook.id
                    )
                    print("Cleaned up async integration webhook for account {}".format(tenant.synqly_account_id))
                except Exception as e:
                    print("there was an error deleting async integration webhook for account {}".format(tenant.synqly_account_id))
        except Exception as e:
            print("there was an error listing the current webhooks for tenant {}".format(tenant.tenant_name))

    if account_id != "" and async_mgmt != None:
        try:
            integrations_response = async_mgmt.integrations.list_account(
                account_id = account_id,
                filter=["name[eq]synqly-operation-events"]
            )

            for integration in integrations_response.result:
                try:
                    async_mgmt.integrations.delete(
                        account_id = account_id,
                        integration_id = integration.id
                    )
                    print("Cleaned up async integration for account {}".format(account_id))
                except Exception as e:
                    print("error deleting synqly async integration: {}".format(str(e)))
        except Exception as e:
            print("there was an error listing the current account integrations")

def clean_example(app: utils.App, app_config: any, async_mgmt: SynqlyManagement, synqly_async_integration_token: any):
    async_account_id = None
    async_tenant = None

    # Async Clean
    if app != None:
        for tenant_name in app.tenants:
            async_tenant = app.tenants[tenant_name]
            break

    if synqly_async_integration_token != None:
        async_account_id = synqly_async_integration_token.account_id

    clean_async(async_account_id, async_mgmt, async_tenant)

    # Main Clean
    if app != None and len(app.tenants) > 0:
        app._cleanup_handler()
    elif app_config != None and app_config.synqly_org_token != None:
        transport = httpx.HTTPTransport(retries=3)
        management_client = SynqlyManagement(
            token=app_config.synqly_org_token,
            httpx_client=httpx.Client(transport=transport),
        )

        available_accounts = management_client.accounts.list()
        
        for account in available_accounts.result:
            if account.fullname == TENANT_SERVICENOW_NAME:
                try:
                    management_client.accounts.delete(account.id)
                    print("Cleaned up account '{}'".format(account.id))
                except Exception as e:
                    print("Error deleting account '{}': {}".format(account.name, str(e)))

def configure_provider(app: utils.App, app_config: any):
    if app_config.servicenow_url != None and app_config.servicenow_username != None and app_config.servicenow_secret != None:
        # Create Tenant
        try:
            app.new_tenant(app_config.synqly_org_token, TENANT_SERVICENOW_NAME)
            print("Tenant '{}' created".format(TENANT_SERVICENOW_NAME))
        except Exception as e:
            print("Error creating tenant '{}': {}".format(TENANT_SERVICENOW_NAME, str(e)))
            raise e

        # Create Integration
        try:
            app.configure_integration(
                TENANT_SERVICENOW_NAME,
                provider_config_servicenow(app_config.servicenow_secret, app_config.servicenow_url, app_config.servicenow_username)
            )
            print("Integration configured for tenant '{}'".format(TENANT_SERVICENOW_NAME))
        except Exception as e:
            print("Error creating integration for tenant '{}': {}".format(TENANT_SERVICENOW_NAME, str(e)))

def do_example(tenant: utils.Tenant, webhook_url: str):
    # Configure Response WebHook
    try:
        if webhook_url != None and webhook_url != "":
            tenant.synqly_management_client.organization_webhooks.create(
                request = mgmt.CreateOrganizationWebhookRequest(
                    name="test-webhook-for-async-operation",
                    filters=[
                        mgmt.WebhookFilter.OPERATION_COMPLETE
                    ],
                    secret=mgmt.OrganizationWebhookSecret(
                        value="test1"
                    ),
                    url=webhook_url
                )
            )

        print("Async operation WebHook created successfully...")
    except Exception as e:
        print("error creating async operation WebHook: {}".format(str(e)))
        return

    try:
        # Schedule Operation
        schedule_seconds = 15
        schedule_time= datetime.now() + timedelta(seconds=schedule_seconds)
        scheduled_operation_response = tenant.synqly_engine_client.operations.create(
            request=engine.CreateOperationRequest(
                input=engine.OperationInput(
                    limit=123
                ),
                operation="assets_query_devices",
                # schedule=engine.OperationSchedule( # Not working, commented while fixed...
                #     run_at=schedule_time
                # )
            )
        )

        print("Async operation '{}' scheduled successfully...".format(scheduled_operation_response.result.operation.id))
    except Exception as e:
        print("error scheduling async operation: {}".format(str(e)))
        return

    # Check Operation Status
    try:
        operation_status_response = tenant.synqly_engine_client.operations.get(
            operation_id=scheduled_operation_response.result.operation.id
        )

        print("Async operation status: {}".format(operation_status_response.result.status))
        print("Waiting '{}' seconds for the execution...".format(schedule_seconds+5))
        time.sleep(schedule_seconds + 5)
    except Exception as e:
        print("error checking async operation status: {}".format(str(e)))
        return

def init_async_configuration(app_config: any):
    if app_config.general_webhook_url == None or app_config.crowdstrike_sink_hec_secret == None or app_config.crowdstrike_sink_hec_url == None:
        return None, None, None
    
    # Create Synqly Integration Token
    try:
        transport = httpx.HTTPTransport(retries=3)
        management_client = SynqlyManagement(
            token=app_config.synqly_org_token,
            httpx_client=httpx.Client(transport=transport),
        )

        synqly_integration_token_response = management_client.tokens.create_synqly_integrations_token(
            request = mgmt.CreateSynqlyIntegrationsTokenRequest(
                token_ttl = "10m"
            )
        )

        synqly_integration_token = synqly_integration_token_response.result

        print("Synqly integration token created successfully...")
    except Exception as e:
        return None, None, "error creating Synqly integration token: {}".format(str(e))
    
    # Create Sink Integration
    try:
        async_mgmt_client = SynqlyManagement(
            base_url="https://api.synqly.com",
            token=synqly_integration_token.token.primary.access.secret
        )

        eventName = "synqly-operation-events"

        # Integration Points
        integration_point_list_response = async_mgmt_client.integration_points.list(
            filter=["name[eq]" + eventName]
        )

        if len(integration_point_list_response.result) == 0:
            raise Exception("Integration point '{}' not found".format(eventName))

        integration_point_response = async_mgmt_client.integration_points.get(
            integration_point_id = eventName
        )

        # Create Sink Integration
        integration_req = mgmt.CreateIntegrationRequest(
            name = eventName,
            integration_point_id = integration_point_response.result.id,
            provider_config = mgmt.ProviderConfig_SinkCrowdstrikeHec(
                type="sink_crowdstrike_hec",
                credential=mgmt.CrowdstrikeHecCredential_Token(
                    secret=app_config.crowdstrike_sink_hec_secret,
                    type="token"
                ),
                url=app_config.crowdstrike_sink_hec_url
            )
        )

        integration_resp = async_mgmt_client.integrations.create(
            account_id = synqly_integration_token.account_id,
            request = integration_req
        )

        print("Synqly sink integration '{}' created successfully...".format(integration_resp.result.integration.id))
    except Exception as e:
        return synqly_integration_token, async_mgmt_client, "error creating sink integration: {}".format(str(e))

    return synqly_integration_token, async_mgmt_client, None

def load_configuration():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK Assets Connector Example"
    )
    
    parser.add_argument(
        "--use_config_file",
        dest="use_config_file",
        type=bool,
        required=False,
        default=False,
        help="Define if the example configuration variables are going to be loaded from ini file or run flags"
    )

    parser.add_argument("--crowdstrike_sink_hec_secret", dest="crowdstrike_sink_hec_secret", type=str, required=False)
    parser.add_argument("--crowdstrike_sink_hec_url", dest="crowdstrike_sink_hec_url", type=str, required=False)
    parser.add_argument("--general_webhook_url", dest="general_webhook_url", type=str, required=False)
    parser.add_argument(
        "--synqly_org_token", dest="synqly_org_token", type=str, required=False,
        help="Token for authenticating with a Synqly Organization. For more information, see https://docs.synqly.com/reference/api-authentication.",
    )
    parser.add_argument("--servicenow_secret", dest="servicenow_secret", type=str, required=False)
    parser.add_argument("--servicenow_username", dest="servicenow_username", type=str, required=False)
    parser.add_argument("--servicenow_url", dest="servicenow_url", type=str, required=False)

    args = parser.parse_args()

    if args.use_config_file:
        config = configparser.ConfigParser()
        config.read("./config.ini")

        args.crowdstrike_sink_hec_secret = config.get('crowdstrike', 'sink_hec_secret', fallback=None)
        args.crowdstrike_sink_hec_url = config.get('crowdstrike', 'sink_hec_url', fallback=None)
        args.general_webhook_url = config.get('general', 'webhook_url', fallback=None)
        args.synqly_org_token = config.get('synqly', 'org_token', fallback=None)
        args.servicenow_secret = config.get('servicenow', 'secret', fallback=None)
        args.servicenow_username = config.get('servicenow', 'username', fallback=None)
        args.servicenow_url = config.get('servicenow', 'url', fallback=None)
    
    if args.synqly_org_token == None:
        return None, "Please provide a Synqly Organization Token"

    return args, None

def provider_config_servicenow(secret, url, username: str):
    return mgmt.ProviderConfig_AssetsServicenow(
        type="assets_servicenow",
        credential=mgmt.ServiceNowCredential_Basic(
                secret=secret,
                type="basic",
                username=username
            ),
        url=url
    )

def main():
    # Load Configuration
    app_config, err = load_configuration()
    if err != None:
        print("There was an error loading the configuration: {}".format(err))
        return
    
    synqly_async_integration_token, async_mgmt_client, err = init_async_configuration(app_config)
    if err != None:
        print("There was an error loading the async configurations: {}".format(err))

        if synqly_async_integration_token != None and async_mgmt_client != None:
            clean_example(None, app_config, async_mgmt_client, synqly_async_integration_token)
            print("Async example data cleared, try again...")
        return

    # Initialize an empty application to store tenants
    app = utils.App(connector_type="asset")

    # Configure providers depending on the provided credentials
    try:
        configure_provider(app, app_config)
    except Exception as e:
        print("Error configuring providers:" + str(e))
        clean_example(app, app_config, async_mgmt_client, synqly_async_integration_token)
        return

    # Execute async operations example for a single tenant
    if synqly_async_integration_token != None and async_mgmt_client != None and app_config.general_webhook_url != None:
        for tenant_name  in app.tenants:
            do_example(app.tenants[tenant_name], app_config.general_webhook_url)
            break
    else:
        print("Skipping async example, missing configurations...")

    # Clean up Synqly Accounts and Integrations
    clean_example(app, app_config, async_mgmt_client, synqly_async_integration_token)

try:
    main()
except:
    sys.exit(1)
