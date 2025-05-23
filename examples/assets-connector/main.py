"""
Synqly Python SDK - Assets Example

This example demonstrates how to use Synqly Python SDK to create an Assets Integration for a tenant.
"""

# Standard imports
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
from synqly import engine
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement

TENANT_ARMIS_NAME = "Tenant Armis Centrix"
TENANT_NOZOMI_NAME = "Tenant Nozomi Vantage"
TENANT_SERVICENOW_NAME = "Tenant ServiceNow"

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
            if account.fullname == TENANT_ARMIS_NAME or account.fullname == TENANT_NOZOMI_NAME or account.fullname == TENANT_SERVICENOW_NAME:
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
        raise e

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
    # Check Armis
    if app_config.armis_token != None and app_config.armis_url != None:
        configure_provider(app, TENANT_ARMIS_NAME, app_config.synqly_org_token, provider_config_armis(app_config.armis_token, app_config.armis_url))

    # Check Nozomi
    if app_config.nozomi_url != None and app_config.nozomi_username != None and app_config.nozomi_secret != None:
        configure_provider(app, TENANT_NOZOMI_NAME, app_config.synqly_org_token, provider_config_nozomi(app_config.nozomi_secret, app_config.nozomi_url, app_config.nozomi_username))

    # Check ServiceNow
    if app_config.servicenow_url != None and app_config.servicenow_username != None and app_config.servicenow_secret != None:
        configure_provider(app, TENANT_SERVICENOW_NAME, app_config.synqly_org_token, provider_config_servicenow(app_config.servicenow_secret, app_config.servicenow_url, app_config.servicenow_username))

def do_example(tenant: utils.Tenant):
    device: engine.Device

    # Query Devices
    try:
        devices_response = tenant.synqly_engine_client.assets.query_devices(
            limit=123
        )
        devices = devices_response.result
        
        if len(devices) > 0:
            device = devices[0]

        print("Query devices from '{}': {}".format(tenant.tenant_name, len(devices)))
    except Exception as e:
        print("Error querying devices for tenant '{}': {}".format(tenant.tenant_name, str(e)))
    
    # Create Device
    try:
        # Not working, disabled while fixed...
        if False and tenant.tenant_name == TENANT_SERVICENOW_NAME:
            if device == None or device.device == None or device.device.name == "":
                print("Skipping 'Create Device' example for Tenant '{}': There where no previous devices to generate a copy from".format(tenant.tenant_name))
            
            new_device = engine.Device(
                activity_id=device.activity_id,
                category_uid=device.category_uid,
                class_uid=device.class_uid,
                device={
                    "name": "{}-copy".format(device.device.name),
                    "uid": "{}-copy".format(device.device.uid),
                    "type_id": device.device.type_id
                },
                metadata={
                    "product": {
                        "vendor_name": device.metadata.product.vendor_name
                    },
                    "version": device.metadata.version
                },
                severity_id=device.severity_id,
                time=device.time,
                type_uid=device.type_uid
            )
            
            create_asset_response = tenant.synqly_engine_client.assets.create_asset(
                request=engine.CreateDeviceRequest(device=new_device)
            )

            print("Asset '{}' created for tenant '{}': {}".format(device.device.name, tenant.tenant_name), create_asset_response)
        else:
            print("Skipping 'Create Device' example for Tenant '{}': Not supported".format(tenant.tenant_name))
    except Exception as e:
        print("Error creating a device for tenant '{}': {}".format(tenant.tenant_name, str(e)))

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

    parser.add_argument(
        "--synqly_org_token", dest="synqly_org_token", type=str, required=False,
        help="Token for authenticating with a Synqly Organization. For more information, see https://docs.synqly.com/reference/api-authentication.",
    )
    parser.add_argument("--armis_token", dest="armis_token", type=str, required=False)
    parser.add_argument("--armis_url", dest="armis_url", type=str, required=False)
    parser.add_argument("--nozomi_secret", dest="nozomi_secret", type=str, required=False)
    parser.add_argument("--nozomi_username", dest="nozomi_username", type=str, required=False)
    parser.add_argument("--nozomi_url", dest="nozomi_url", type=str, required=False)
    parser.add_argument("--servicenow_secret", dest="servicenow_secret", type=str, required=False)
    parser.add_argument("--servicenow_username", dest="servicenow_username", type=str, required=False)
    parser.add_argument("--servicenow_url", dest="servicenow_url", type=str, required=False)

    args = parser.parse_args()

    if args.use_config_file:
        config = configparser.ConfigParser()
        config.read("./config.ini")

        args.synqly_org_token = config.get('synqly', 'org_token', fallback=None)
        args.armis_token = config.get('armis', 'token', fallback=None)
        args.armis_url = config.get('armis', 'url', fallback=None)
        args.nozomi_secret = config.get('nozomi', 'secret', fallback=None)
        args.nozomi_username = config.get('nozomi', 'username', fallback=None)
        args.nozomi_url = config.get('nozomi', 'url', fallback=None)
        args.servicenow_secret = config.get('servicenow', 'secret', fallback=None)
        args.servicenow_username = config.get('servicenow', 'username', fallback=None)
        args.servicenow_url = config.get('servicenow', 'url', fallback=None)
    
    if args.synqly_org_token == None:
        return None, "Please provide a Synqly Organization Token"

    return args, None

def provider_config_armis(token, url: str):
    return mgmt.ProviderConfig_AssetsArmisCentrix(
        type="assets_armis_centrix",
        credential=mgmt.ArmisCredential_Token(
            secret=token,
            type="token"
        ),
        url=url
    )

def provider_config_nozomi_secret(secret, url, username: str):
    return mgmt.ProviderConfig_AssetsNozomiVantage(
        type="assets_nozomi_vantage",
        credential=mgmt.NozomiVantageCredential_Basic,
        url=url
    )

def provider_config_nozomi(secret, url, username: str):
    return mgmt.ProviderConfig_AssetsNozomiVantage(
        type="assets_nozomi_vantage",
        credential=mgmt.NozomiVantageCredential_Basic(
            secret=secret,
            type="basic",
            username=username
        ),
        url=url
    )

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

    # Initialize an empty application to store tenants
    app = utils.App(connector_type="asset")

    # Configure providers depending on the provided credentials
    try:
        configure_providers(app, app_config)
    except Exception as e:
        print("Error configuring providers:" + str(e))
        clean_example(app, app_config)
        return

    # Execute example for each tenant
    for tenant_name  in app.tenants:
        do_example(app.tenants[tenant_name])

    # Clean up Synqly Accounts and Integrations
    clean_example(app, app_config)

try:
    main()
except:
    sys.exit(1)
