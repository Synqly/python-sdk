import sys
import argparse
import configparser
import pprint
from pathlib import Path

# Synqly Python SDK imports
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement
from synqly.engine.client import SynqlyEngine

TENANT_NAME = "Cloud Security Tenant"
BASE_URL = "https://api.synqly.com"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK Cloud Security Example"
    )
    parser.add_argument(
        "--synqly-org-token",
        dest="synqly_org_token",
        type=str,
        required=True,
        default="",
        help="Token for authenticating with a Synqly Organization. See https://docs.synqly.com/reference/api-authentication.",
    )
    parser.add_argument(
        "--config",
        dest="config_path",
        default="config.ini",
        type=str,
        required=True,
        help="Path to INI config file with Cloud Security provider settings.",
    )
    return parser.parse_args()


def provider_config_crowdstrike(url: str | None, client_id: str, client_secret: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_CloudsecurityCrowdstrike(
        type="cloudsecurity_crowdstrike",
        credential=mgmt.CrowdStrikeCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        url=url,
    )


def provider_config_defender(url: str | None, client_id: str, client_secret: str, subscription_id: str, tenant_id: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_CloudsecurityDefender(
        type="cloudsecurity_defender",
        credential=mgmt.DefenderCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        subscription_id=subscription_id,
        tenant_id=tenant_id,
        url=url,
    )


def load_config(path: str) -> tuple[str, dict]:
    cfg = configparser.ConfigParser()
    with open(path, "r") as f:
        cfg.read_file(f)

    base_url = cfg.get("general", "base_url", fallback=BASE_URL).strip()

    providers: dict[str, dict] = {}

    if cfg.has_section("cloudsecurity_crowdstrike"):
        s = cfg["cloudsecurity_crowdstrike"]
        url = s.get("url", "").strip() or None
        client_id = s.get("client_id", "").strip()
        client_secret = s.get("client_secret", "").strip()
        if client_id and client_secret:
            providers["cloudsecurity_crowdstrike"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
            }

    if cfg.has_section("cloudsecurity_defender"):
        s = cfg["cloudsecurity_defender"]
        url = s.get("url", "").strip() or None
        client_id = s.get("client_id", "").strip()
        client_secret = s.get("client_secret", "").strip()
        subscription_id = s.get("subscription_id", "").strip()
        tenant_id = s.get("tenant_id", "").strip()
        if client_id and client_secret and subscription_id and tenant_id:
            providers["cloudsecurity_defender"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
                "subscription_id": subscription_id,
                "tenant_id": tenant_id,
            }

    return base_url, providers


def demo_cloudsecurity(session_token: str, base_url: str):
    engine_client = SynqlyEngine(
        base_url=base_url,
        token=session_token,
    )

    response = engine_client.cloudsecurity.query_cloud_resource_inventory()
    results_page = response.result
    if results_page is None:
        print("Unable to retrieve cloud resource inventory")
        return

    print(f"Cloud resource inventory results: {len(results_page)}")
    for resource_item in results_page[:5]:  # Show first 5 items
        pprint.pp(resource_item)

    # Query compliance findings
    findings_resp = engine_client.cloudsecurity.query_compliance_findings()
    if findings_resp.result is None:
        print("Unable to retrieve compliance findings")
        return

    print(f"\nCompliance findings: {len(findings_resp.result)}")
    for finding in findings_resp.result[:5]:  # Show first 5 findings
        pprint.pp(finding)

    ioms_resp = engine_client.cloudsecurity.query_ioms(
        limit=5,
    )
    if ioms_resp.result is None:
        print("Unable to retrieve IOMs")
        return

    print(f"\nIOMs: {len(ioms_resp.result)}")
    for iom in ioms_resp.result:
        pprint.pp(iom)


def main():
    args = parse_args()

    synqly_org_token = args.synqly_org_token
    config_path = args.config_path

    base_url, providers = load_config(config_path)

    if len(providers) == 0:
        print("No Cloud Security providers configured with complete credentials in the config file.")
        sys.exit(1)

    mgmt_client = SynqlyManagement(
        base_url=base_url,
        token=synqly_org_token,
    )

    # create an account
    account_response = mgmt_client.accounts.create(fullname=TENANT_NAME)
    account_id = account_response.result.account.id

    integration_ids: list[str] = []

    try:
        # Configure integrations for all configured providers
        for provider_name, cfg in providers.items():
            if provider_name == "cloudsecurity_crowdstrike":
                provider_cfg = provider_config_crowdstrike(
                    cfg["url"], cfg["client_id"], cfg["client_secret"]
                )
            elif provider_name == "cloudsecurity_defender":
                provider_cfg = provider_config_defender(
                    cfg["url"], cfg["client_id"], cfg["client_secret"], cfg["subscription_id"], cfg["tenant_id"]
                )
            else:
                continue

            integration_response = mgmt_client.integrations.create(
                account_id=account_id,
                fullname=f"CloudSecurity Example - {provider_name}",
                provider_config=provider_cfg,
            )
            integration_id = integration_response.result.integration.id
            integration_ids.append(integration_id)

            # create a session token for the integration
            session_token_response = mgmt_client.tokens.create_integration_token(
                account_id=account_id,
                integration_id=integration_id,
                token_ttl="10m",
            )
            session_token = session_token_response.result.secret

            print(f"\n=== Demo for {provider_name} ===")
            demo_cloudsecurity(session_token, base_url)

    except Exception as e:
        print("Error configuring provider integration or running demo: " + str(e))
    finally:
        # Cleanup
        for iid in integration_ids:
            try:
                mgmt_client.integrations.delete(account_id=account_id, integration_id=iid)
            except Exception as ce:
                print(f"Cleanup error (integration {iid}): {ce}")
        try:
            mgmt_client.accounts.delete(account_id=account_id)
        except Exception as ce:
            print(f"Cleanup error (account {account_id}): {ce}")


try:
    main()
except:
    sys.exit(1)
