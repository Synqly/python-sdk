"""
Synqly Python SDK - Identity Example

This example demonstrates how to use Synqly Python SDK to create an Identity Integration for a tenant.
"""

import sys
import argparse
import configparser
import httpx
from pathlib import Path

# Add the root directory to the system path so that we can import "shared".
# "shared" contains common Application logic used throughout the SDK examples.
current_script = Path(__file__).resolve()
root = current_script.parents[1]
sys.path.append(str(root))

from shared import utils

# Synqly Python SDK imports
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement

TENANT_GOOGLE_NAME = "Tenant Google"
TENANT_OKTA_NAME = "Tenant Okta"
TENANT_PINGONE_NAME = "Tenant PingOne"

def clean_example(app: utils.App, app_config: any):
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
            if account.fullname == TENANT_GOOGLE_NAME or account.fullname == TENANT_OKTA_NAME or account.fullname == TENANT_PINGONE_NAME:
                try:
                    management_client.accounts.delete(account.id)
                    print("Cleaned up account '{}'".format(account.id))
                except Exception as e:
                    print("Error deleting account '{}': {}".format(account.name, str(e)))

def configure_provider(app: utils.App, tenant_name, synqly_org_token: str, provider_config: any):
    # Create Tenant
    try:
        app.new_tenant(synqly_org_token, tenant_name)
        print("Tenant '{}' created".format(tenant_name))
    except Exception as e:
        print("Error creating tenant '{}': {}".format(tenant_name, str(e)))
        return

    # Create Integration
    try:
        app.configure_integration(
            tenant_name,
            provider_config
        )
        print("Integration configured for tenant '{}'".format(tenant_name))
    except Exception as e:
        print("Error creating integration for tenant '{}': {}".format(tenant_name, str(e)))

def configure_providers(app: utils.App, app_config: any):
    # Check Google
    if app_config.google_client_email != None and app_config.google_client_id != None and app_config.google_delegate != None and app_config.google_secret != None and app_config.google_token_url != None:
        configure_provider(app, TENANT_GOOGLE_NAME, app_config.synqly_org_token, provider_config_google(app_config.google_client_email, app_config.google_client_id, app_config.google_delegate, app_config.google_secret, app_config.google_token_url))

    # Check Okta
    if app_config.okta_client_id != None and app_config.okta_token != None and app_config.okta_url != None:
        configure_provider(app, TENANT_OKTA_NAME, app_config.synqly_org_token, provider_config_okta(app_config.okta_client_id, app_config.okta_token, app_config.okta_url))
    
    # Check PingOne
    if app_config.pingone_auth_url != None and app_config.pingone_client_id != None and app_config.pingone_environment_id != None and app_config.pingone_secret != None and app_config.pingone_url != None:
        configure_provider(app, TENANT_PINGONE_NAME, app_config.synqly_org_token, provider_config_pingone(app_config.pingone_auth_url, app_config.pingone_client_id, app_config.pingone_environment_id, app_config.pingone_secret, app_config.pingone_url))

def do_example(tenant: utils.Tenant, tests_email: str):
    try:
        # Query Groups
        groups_response = tenant.synqly_engine_client.identity.query_groups()
        groups = groups_response.result

        groups_result = ""
        for group in groups:
            groups_result += "\n    - {}".format(group.entity.group.name)

        print("'{}' groups: {}".format(tenant.tenant_name, groups_result))
    except Exception as e:
        print("Error querying groups for tenant '{}': {}".format(tenant.tenant_name, str(e)))

    try:
        # Query Users
        users_response = tenant.synqly_engine_client.identity.query_users(
            filter=["entity.user.email_addr[eq]" + tests_email]
        )
        users = users_response.result

        if len(users) == 0:
            print("User with email '{}' not found".format(tests_email))
            return
        
        user = users[0]
        print("'{}' user '{}' found!".format(tenant.tenant_name, tests_email))
    except Exception as e:
        print("Error querying users for tenant '{}': {}".format(tenant.tenant_name, str(e)))
        return

    try:
        # Force user password reset
        tenant.synqly_engine_client.identity.force_user_password_reset(
            user_id = user.entity.uid
        )

        print("'{}' tenant, user '{}' password reset successfully...".format(tenant.tenant_name, tests_email))
    except Exception as e:
        print("There was an error resetting user '{}' password, for tenant '{}': {}".format(tests_email, tenant.tenant_name, str(e)))

    try:
        # Disable user
        tenant.synqly_engine_client.identity.disable_user(
            user_id = user.entity.uid
        )

        print("'{}' tenant, user '{}' disabled".format(tenant.tenant_name, tests_email))
    except Exception as e:
        print("There was an error disabling the user '{}' for tenant '{}': {}".format(tests_email, tenant.tenant_name, str(e)))

    try:
        # Enable user
        tenant.synqly_engine_client.identity.enable_user(
            user_id = user.entity.uid
        )

        print("'{}' tenant, user '{}' enabled".format(tenant.tenant_name, tests_email))
    except Exception as e:
        print("There was an error disabling the user '{}' for tenant '{}': {}".format(tests_email, tenant.tenant_name, str(e)))

def load_configuration():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK IAM Connector Example"
    )
    
    parser.add_argument(
        "--use_config_file",
        dest="use_config_file",
        type=bool,
        required=False,
        default=False,
        help="Define if the example configuration variables are going to be loaded from ini file or run flags"
    )

    parser.add_argument(
        "--general_tests_email", dest="general_tests_email", type=str, required=False,
        help="Email to be used on the tests, this email should be a dummy one, tests like 'force user password reset' are executed...",
    )
    parser.add_argument("--google_client_email", dest="google_client_email", type=str, required=False)
    parser.add_argument("--google_client_id", dest="google_client_id", type=str, required=False)
    parser.add_argument("--google_delegate", dest="google_delegate", type=str, required=False)
    parser.add_argument("--google_secret", dest="google_secret", type=str, required=False)
    parser.add_argument("--google_token_url", dest="google_token_url", type=str, required=False)
    parser.add_argument("--okta_client_id", dest="okta_client_id", type=str, required=False)
    parser.add_argument("--okta_token", dest="okta_token", type=str, required=False)
    parser.add_argument("--okta_url", dest="okta_url", type=str, required=False)
    parser.add_argument("--pingone_auth_url", dest="pingone_auth_url", type=str, required=False)
    parser.add_argument("--pingone_client_id", dest="pingone_client_id", type=str, required=False)
    parser.add_argument("--pingone_environment_id", dest="pingone_environment_id", type=str, required=False)
    parser.add_argument("--pingone_secret", dest="pingone_secret", type=str, required=False)
    parser.add_argument("--pingone_url", dest="pingone_url", type=str, required=False)
    parser.add_argument(
        "--synqly_org_token", dest="synqly_org_token", type=str, required=False,
        help="Token for authenticating with a Synqly Organization. For more information, see https://docs.synqly.com/reference/api-authentication.",
    )

    args = parser.parse_args()

    if args.use_config_file:
        config = configparser.ConfigParser()
        config.read("./examples/iam-connector/config.ini")

        args.general_tests_email = config.get('general', 'tests_email', fallback=None)
        args.google_client_email = config.get('google', 'client_email', fallback=None)
        args.google_client_id = config.get('google', 'client_id', fallback=None)
        args.google_delegate = config.get('google', 'delegate', fallback=None)
        args.google_secret = config.get('google', 'secret', fallback=None)
        args.google_token_url = config.get('google', 'token_url', fallback=None)
        args.okta_client_id = config.get('okta', 'client_id', fallback=None)
        args.okta_token = config.get('okta', 'token', fallback=None)
        args.okta_url = config.get('okta', 'url', fallback=None)
        args.pingone_auth_url = config.get('pingone', 'auth_url', fallback=None)
        args.pingone_client_id = config.get('pingone', 'client_id', fallback=None)
        args.pingone_environment_id = config.get('pingone', 'environment_id', fallback=None)
        args.pingone_secret = config.get('pingone', 'secret', fallback=None)
        args.pingone_url = config.get('pingone', 'url', fallback=None)
        args.synqly_org_token = config.get('synqly', 'org_token', fallback=None)
    
    if args.synqly_org_token == None:
        return None, "Please provide a Synqly Organization Token"
    
    if args.general_tests_email == None:
        return None, "Please provide an email to be used on tests"

    return args, None

def provider_config_google(client_email, client_id, delegate, secret, token_url: str):
    return mgmt.ProviderConfig_IdentityGoogle(
        client_email=client_email,
        delegate = delegate,
        type="identity_google",
        credential=mgmt.GoogleCredential_OAuthClient(
            client_id=client_id,
            client_secret=secret,
            token_url=token_url,
            type="o_auth_client"
        )
    )

def provider_config_okta(client_id, token, url: str):
    return mgmt.ProviderConfig_IdentityOkta(
        credential=mgmt.OktaCredential_OAuthClient(
            client_id=client_id,
            client_secret=token,
            type="o_auth_client"
        ),
        type="identity_okta",
        url=url
    )

def provider_config_pingone(auth_url, client_id, environment_id, secret, url):
    return mgmt.ProviderConfig_IdentityPingone(
        auth_url=auth_url,
        client_id=client_id,
        credential=mgmt.PingOneCredential_Token(
            secret=secret,
            type="token"
        ),
        organization_id=environment_id,
        type="identity_pingone",
        url=url
    )

def main():
    # Load Configuration
    app_config, err = load_configuration()
    if err != None:
        print("There was an error loading the configuration: {}".format(err))
        return

    # Initialize an empty application to store tenants
    app = utils.App(connector_type="identity")

    # Configure providers depending on the provided credentials
    try:
        configure_providers(app, app_config)
    except Exception as e:
        print("Error configuring providers:" + str(e))
        clean_example(app, app_config)
        return

    # Execute example for each tenant
    for tenant_name  in app.tenants:
        do_example(app.tenants[tenant_name], app_config.general_tests_email)

    # Clean up Synqly Accounts and Integrations
    clean_example(app, app_config)

try:
    main()
except:
    sys.exit(1)
