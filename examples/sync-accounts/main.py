import argparse
import json
from typing import Dict

from synqly import engine
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement
from synqly.engine.client import SynqlyEngine


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
    parser.add_argument(
        "--sentinelone-file-path",
        dest="sentinelone_file_path",
        type=str,
        required=True,
        default="",
        help="Path to the file containing sentinelone configuration",
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


def sentinelone_provider_config(
    sentinelone_url: str, sentinelone_token: str
) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_EdrSentinelone(
        type="edr_sentinelone",
        credential=mgmt.SentinelOneCredential_Token(
            type="token", secret=sentinelone_token
        ),
        url=sentinelone_url,
    )


"""
Input:

Tenants json file with
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

SentinelOne json file with
{
    "sentinelone": {
        "url": "https://<sentinelone-instance>.sentinelone.net",
        "api_token": "sentinelone_api_token"
    }
}
"""


def sync_tenants(
    client: SynqlyManagement, tenants_filename: str, sentinelone_filename: str
) -> None:
    to_sync_accounts = json.load(open(tenants_filename, "r"))
    sentinelone_config = json.load(open(sentinelone_filename, "r"))

    for customer in to_sync_accounts:
        synqly_account = client.accounts.list(
            filter="name[eq]" + customer["tenant_name"]
        ).result
        if len(synqly_account) == 0:
            print("Creating account for {}".format(customer["tenant_name"]))
            client.accounts.create(
                request=mgmt.CreateAccountRequest(name=customer["tenant_name"])
            )
        else:
            print("Account for {} already exists".format(customer["tenant_name"]))

    ensure_tenable_configured(client, to_sync_accounts)
    ensure_sentinelone_configured(client, sentinelone_config["sentinelone"])


def ensure_tenable_configured(
    client: SynqlyManagement, to_sync_accounts: Dict[str, any]
) -> None:
    for customer in to_sync_accounts:
        synqly_account = client.accounts.list(
            filter="name[eq]" + customer["tenant_name"]
        ).result[0]
        integrations = client.integrations.list_account(
            account_id=synqly_account.id,
            filter="name[eq]tenable",
        ).result
        if len(integrations) > 0:
            print(
                "Tenable integration already exists for {}".format(
                    customer["tenant_name"]
                )
            )
            continue

        client.integrations.create(
            account_id=synqly_account.id,
            request=mgmt.CreateIntegrationRequest(
                name="tenable",
                provider_config=tenable_provider_config(customer["tenable_access_key"]),
            ),
        )
        print("Tenable integration created for {}".format(customer["tenant_name"]))


def ensure_sentinelone_configured(
    client: SynqlyManagement, sentinelone_config: Dict[str, any]
) -> None:

    account_id = ensure_sentinelone_account(client, "sentinelone-account")

    integrations = client.integrations.list_account(
        account_id=account_id,
        filter="name[eq]sentinelone-integration",
    ).result
    if len(integrations) > 0:
        print("SentinelOne integration already exists")
        return

    client.integrations.create(
        account_id=account_id,
        request=mgmt.CreateIntegrationRequest(
            name="sentinelone-integration",
            provider_config=sentinelone_provider_config(
                sentinelone_config["url"], sentinelone_config["api_token"]
            ),
        ),
    )
    print("SentinelOne integration created")


def ensure_sentinelone_account(
    client: SynqlyManagement, sentinelone_account_name: str
) -> str:
    accounts = client.accounts.list(filter="name[eq]" + sentinelone_account_name).result
    if len(accounts) > 0:
        print("SentinelOne account already exists")
        return accounts[0].id

    account_resp = client.accounts.create(
        request=mgmt.CreateAccountRequest(name=sentinelone_account_name)
    )
    return account_resp.result.account.id


def query_tenable(client: SynqlyManagement, tenant_name: str) -> None:
    integrations = client.integrations.list_account(
        account_id=client.accounts.list(filter="name[eq]" + tenant_name).result[0].id,
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
    print("Found {} security findings in Tenable".format(len(findings.result)))


def query_sentinelone(client: SynqlyManagement, sentinelone_account_name: str) -> None:
    integrations = client.integrations.list_account(
        account_id=client.accounts.list(filter="name[eq]sentinelone-account")
        .result[0]
        .id,
        filter="name[eq]sentinelone-integration",
    ).result
    if len(integrations) == 0:
        print("No SentinelOne integration found")
        return

    integration = integrations[0]

    # reset the token for this integration and setup an engine SDK client
    response = client.tokens.reset(
        owner_id=integration.id,
        refresh_token_id=integration.refresh_token_id,
    )
    secret = response.result.primary.access.secret
    engine_client = SynqlyEngine(token=secret)

    currentCursor = ""
    application_response = engine_client.edr.query_applications(cursor=currentCursor)
    first_application = application_response.result[0]
    print("Found SentinelOne application: {}".format(first_application.product.name))
    sentinelone_customer_lookup(engine_client, first_application)


def sentinelone_customer_lookup(
    engine_client: SynqlyEngine, application: engine.Application
) -> None:
    endpointResponse = engine_client.edr.query_endpoints(
        filter="device.instance_uid[eq]" + application.device.uid,
    )
    print(
        "{} is installed on a {} device".format(
            application.product.name, endpointResponse.result[0].device.org.ou_name
        )
    )


def main() -> None:
    args = parse_args()
    client = SynqlyManagement(token=args.synqly_org_token)

    sync_tenants(client, args.tenants_file_path, args.sentinelone_file_path)

    query_tenable(client, "your-customer")

    query_sentinelone(client, "sentinelone-account")


if __name__ == "__main__":
    main()
