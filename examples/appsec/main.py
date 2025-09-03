import sys
import argparse
import configparser
import pprint
from pathlib import Path

# Synqly Python SDK imports
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement
from synqly import engine
from synqly.engine.client import SynqlyEngine

TENANT_NAME = "AppSec Tenant"
BASE_URL = "https://api.synqly.com"

def parse_args():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK AppSec Connector Example"
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
        "--config",
        dest="config_path",
        default="config.ini",
        type=str,
        required=True,
        help="Path to INI config file with AppSec provider settings.",
    )
    return parser.parse_args()


def oauth_client_credential_config(client_id: str, client_secret: str) -> mgmt.CredentialConfig_OAuthClient:
    return mgmt.CredentialConfig_OAuthClient(
        type="o_auth_client",
        client_id=client_id,
        client_secret=client_secret,
    )


def appscan_provider_config(url: str, client_id: str, client_secret: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_AppsecHclAppscanOnCloud(
        type="appsec_hcl_appscan_on_cloud",
        credential=mgmt.HclAppScanOnCloudCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        url=url,
    )


def opentext_provider_config(url: str, client_id: str, client_secret: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_AppsecOpentextCoreApplicationSecurity(
        type="appsec_opentext_core_application_security",
        credential=mgmt.OpenTextCoreApplicationSecurityCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        url=url,
    )


def demo_appsec(session_token: str, base_url: str):
    engine_client = SynqlyEngine(
        base_url=base_url,
        token=session_token,
    )

    response = engine_client.appsec.query_applications()
    results_page = response.result
    if results_page is None:
        print("Unable to retrieve applications")
        return

    for app_item in results_page:
        print(f"\nApplication: {app_item.name}")
        pprint.pp(app_item)

    # Query findings for first application (if any)
    if len(results_page) > 0:
        print(f"\nFindings for application: {results_page[0].id}")
        app_findings_resp = engine_client.appsec.query_application_findings(
            application_id=results_page[0].id
        )
        if app_findings_resp.result is None:
            print("Unable to retrieve application findings")
            return
        for f in app_findings_resp.result[:5]:
            pprint.pp(f)

    resp = engine_client.appsec.query_findings()
    if resp.result is None:
        print("Unable to retrieve combined findings")
        return
    for finding_result in resp.result[:5]:
        pprint.pp(finding_result)


def load_config(path: str) -> tuple[str, dict]:
    cfg = configparser.ConfigParser()
    with open(path, "r") as f:
        cfg.read_file(f)

    base_url = cfg.get("general", "base_url", fallback=BASE_URL).strip()

    providers: dict[str, dict] = {}

    if cfg.has_section("appsec_hcl_appscan_on_cloud"):
        section = cfg["appsec_hcl_appscan_on_cloud"]
        url = section.get("url", "").strip()
        client_id = section.get("client_id", "").strip()
        client_secret = section.get("client_secret", "").strip()
        if url and client_id and client_secret:
            providers["appsec_hcl_appscan_on_cloud"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
            }

    if cfg.has_section("appsec_opentext_core_application_security"):
        section = cfg["appsec_opentext_core_application_security"]
        url = section.get("url", "").strip()
        client_id = section.get("client_id", "").strip()
        client_secret = section.get("client_secret", "").strip()
        if url and client_id and client_secret:
            providers["appsec_opentext_core_application_security"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
            }

    return base_url, providers


def main():
    # Parse command line arguments
    args = parse_args()

    synqly_org_token = args.synqly_org_token
    config_path = args.config_path

    base_url, providers = load_config(config_path)

    if len(providers) == 0:
        print("No AppSec providers configured with complete credentials in the config file.")
        sys.exit(1)

    mgmt_client = SynqlyManagement(
        base_url=base_url,
        token=synqly_org_token,
    )

    # create an account
    account_response = mgmt_client.accounts.create(request=mgmt.CreateAccountRequest(fullname="AppSec Example"))
    account_id = account_response.result.account.id

    integration_ids: list[str] = []

    try:
        # Configure integrations for all configured providers
        for provider_name, cfg in providers.items():
            if provider_name == "appsec_hcl_appscan_on_cloud":
                provider_cfg = appscan_provider_config(
                    cfg["url"], cfg["client_id"], cfg["client_secret"]
                )
            elif provider_name == "appsec_opentext_core_application_security":
                provider_cfg = opentext_provider_config(
                    cfg["url"], cfg["client_id"], cfg["client_secret"]
                )
            else:
                continue

            integration_response = mgmt_client.integrations.create(
                account_id=account_id,
                request=mgmt.CreateIntegrationRequest(
                    fullname=f"AppSec Example - {provider_name}",
                    provider_config=provider_cfg,
                ),
            )
            integration_id = integration_response.result.integration.id
            integration_ids.append(integration_id)

            # create a session token for the integration
            session_token_response = mgmt_client.tokens.create_integration_token(
                account_id=account_id,
                integration_id=integration_id,
                request=mgmt.CreateIntegrationTokenRequest(token_ttl="10m"),
            )
            session_token = session_token_response.result.secret

            # Demonstrate AppSec API calls for this provider
            print(f"\n=== Demo for {provider_name} ===")
            demo_appsec(session_token, base_url)

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
