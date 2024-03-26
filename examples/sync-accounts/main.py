import argparse
import json
from typing import Dict

import management as mgmt
from management.client import SynqlyManagement
from engine.client import SynqlyEngine


def parse_args() -> dict:
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
        "--tenants-file-path",
        dest="tenants_file_path",
        type=str,
        required=True,
        default="",
        help="Path to the file containing the list of tenants to sync",
    )
    args = parser.parse_args()
    return args


def tenable_provider_config(token: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_VulnerabilitiesTenableCloud(
        type="vulnerabilities_tenable_cloud",
        credential=mgmt.TenableCloudCredential_Token(
            type="token",
            secret=token,
        ),
    )


"""
Input: json file with
[
    {
        "tenant_name": "your-customer",
        "tenable_access_key": "accessKey=value;secretKey=secret-value"
    },
    {
        "tenant_name": "another-customer",
        "tenable_access_key": "tenable_access_key"
    }
]
"""
def sync_tenants(client: SynqlyManagement, filename: str) -> None:
    to_sync_accounts = json.load(open(filename, "r"))

    for customer in to_sync_accounts:
        synqly_account = client.accounts.list(filter="name[eq]"+customer["tenant_name"]).result
        if len(synqly_account) == 0:
            print("Creating account for {}".format(customer["tenant_name"]))
            client.accounts.create(request=mgmt.CreateAccountRequest(name=customer["tenant_name"]))
        else:
            print("Account for {} already exists".format(customer["tenant_name"]))

    ensure_tenable_configured(client, to_sync_accounts)


def ensure_tenable_configured(client: SynqlyManagement, to_sync_accounts: Dict[str, any]) -> None:
    for customer in to_sync_accounts:
        synqly_account = client.accounts.list(filter="name[eq]"+customer["tenant_name"]).result[0]
        integrations = client.integrations.list_account(
            account_id=synqly_account.id,
            filter="name[eq]tenable",
        ).result
        if len(integrations) > 0:
            print("Tenable integration already exists for {}".format(customer["tenant_name"]))
            continue

        client.integrations.create(
            account_id=synqly_account.id,
            request=mgmt.CreateIntegrationRequest(
                name="tenable",
                provider_config=tenable_provider_config(customer["tenable_access_key"]),
            )
        )
        print("Tenable integration created for {}".format(customer["tenant_name"]))

def query_tenable(client: SynqlyManagement, tenant_name: str) -> None:
    integrations = client.integrations.list_account(
        account_id=client.accounts.list(filter="name[eq]"+tenant_name).result[0].id,
        filter="name[eq]tenable",
    ).result
    if len(integrations) == 0:
        print("No Tenable integration found for {}".format(tenant_name))
        return

    integration = integrations[0]

    # reset the token for this integration and setup an engine SDK client
    response = client.tokens.reset(
        owner_id=integration.id,
        refresh_token_id=integration.refresh_token_id,
    )
    secret = response.result.primary.access.secret
    engine_client = SynqlyEngine(token=secret)

    findings = engine_client.vulnerabilities.query_findings(
        filter=[
            "severity[in]Critical,High",
            "finding.last_seen_time[gte]2024-01-01T00:00:00Z",
        ]
    )
    print("Found security {} findings".format(len(findings.result)))


def main() -> None:
    args = parse_args()
    client = SynqlyManagement(token=args.synqly_org_token)

    sync_tenants(client, args.tenants_file_path)

    query_tenable(client, "your-customer")


if __name__ == '__main__':
    main()
