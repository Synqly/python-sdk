"""
Synqly Python SDK Vulnerabilities Example

This example demonstrates how to use the Synqly Python SDK to create a
Vulnerabilities Integration for a tenant.
"""

# Standard imports
import time
import sys
import argparse
import httpx
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
from synqly.management.client import SynqlyManagement

TENANT_NAME = "Tenant XYZ"

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
        description="Synqly Python SDK Vulnerabilities Connector Example"
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
        "--tenable-token",
        dest="tenable_token",
        type=str,
        required=True,
        default="",
        help="Token for authenticating with Tenable cloud.",
    )
    args = parser.parse_args()
    return args


def tenable_credential_config(tenable_token):
    """
    Helper method to construct an AWS CredentialConfig object.
    """
    return mgmt.CredentialConfig_Token(type="token", secret=tenable_token)


def tenable_provider_config(credential_id):
    return mgmt.ProviderConfig_VulnerabilitiesTenableCloud(
        type="vulnerabilities_tenable_cloud",
        credential=mgmt.TenableCloudCredential_TokenId(
            type="token_id",
            value=credential_id,
        ),
    )


def background_job(app):
    """
    Simulates a background process performing work on behalf of tenants.
    Iterates through all tenants and, for any tenant with a Synqly Engine
    Client defined, queries for security findings.
    """
    # Iterate through each tenant and send an event to their Event Logger
    for tenant in app.tenants.values():
        # Skip tenants that don't have a Synqly Engine Client initialized
        if tenant.synqly_engine_client is None:
            continue

        findings = (
            tenant.synqly_engine_client.vulnerabilities.query_findings(
                filter=[
                    "severity[in]Critical,High,Medium",
                    "finding.last_seen_time[gte]2024-01-05T00:00:00Z",
                ]
            )
        )
        print("Found security {} findings".format(len(findings.result)))
        for finding in findings.result:
            print(finding)


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    tenable_token = args.tenable_token

    # Initialize an empty application to store simulated tenants
    app = utils.App("vulnerabilities")

    # Initialize tenants within the Application
    try:
        app.new_tenant(synqly_org_token, TENANT_NAME)
        print("{} created".format(TENANT_NAME))
    except Exception as e:
        print("Error creating {}: {}".format(TENANT_NAME, str(e)))
        clean_example(app, synqly_org_token)
        raise e

    # Placeholder variable for the IDs of the Credential we will create
    xyz_credential_id = ""

    # Create a Synqly Credential for each tenant.
    try:
        xyz_credential_id = app.create_credential(
            TENANT_NAME,
            "tenable",
            tenable_credential_config(tenable_token),
        )
    except Exception as e:
        print("Error creating Credential for {}: {}".format(TENANT_NAME, str(e)))
        clean_example(app, synqly_org_token)
        raise e

    # Configure a Tenable Integration for Tenant XYZ
    try:
        app.configure_integration(
            TENANT_NAME,
            tenable_provider_config(xyz_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for {}: {}".format(TENANT_NAME, str(e)))
        clean_example(app, synqly_org_token)
        raise e

    # Start a background job to query for security findings
    try:
        background_job(app)
    except Exception as e:
        print("Error running background job: " + str(e))
        clean_example(app, synqly_org_token)
        raise e

    clean_example(app, synqly_org_token)


try:
    main()
except:
    sys.exit(1)
