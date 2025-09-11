import sys
import argparse
import configparser
import pprint
from pathlib import Path
from typing import Optional, Tuple, Dict

# Synqly Python SDK imports
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement
from synqly.engine.client import SynqlyEngine

TENANT_NAME = "EDR Tenant"
BASE_URL = "https://api.synqly.com"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK EDR Connector Example"
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
        help="Path to INI config file with EDR provider settings.",
    )
    return parser.parse_args()


def provider_config_crowdstrike(url: Optional[str], client_id: str, client_secret: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_EdrCrowdstrike(
        type="edr_crowdstrike",
        credential=mgmt.CrowdStrikeCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        url=url,
    )


def provider_config_sentinelone(url: Optional[str], token: str, xdr_url: Optional[str], xdr_token: Optional[str]) -> mgmt.ProviderConfig:

    edr_events_credential = None
    if xdr_url and xdr_token:
        edr_events_credential = mgmt.SentinelOneEdrEventsCredential_Token(
            type="token",
            secret=xdr_token
        )

    return mgmt.ProviderConfig_EdrSentinelone(
        type="edr_sentinelone",
         credential=mgmt.SentinelOneCredential_Token(
            type="token", secret=token),
        url=url,
        edr_events_url=xdr_url,
        edr_events_credential=edr_events_credential,
    )

def provider_config_defender(url: Optional[str], client_id: str, client_secret: str, tenant_id: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_EdrDefender(
        type="edr_defender",
        credential=mgmt.DefenderCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        tenant_id=tenant_id,
        url=url,
    )

def provider_config_sophos(url: Optional[str], client_id: str, client_secret: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_EdrSophos(
        type="edr_sophos",
        credential=mgmt.SophosCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        url=url,
    )

def provider_config_malwarebytes(url: Optional[str], client_id: str, client_secret: str, account_id: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_EdrMalwarebytes(
        type="edr_malwarebytes",
        credential=mgmt.MalwarebytesCredential_OAuthClient(
            type="o_auth_client",
            client_id=client_id,
            client_secret=client_secret,
        ),
        account_identifier=account_id,
        url=url,
    )

def provider_config_tanium(url: Optional[str], token: str) -> mgmt.ProviderConfig:
    return mgmt.ProviderConfig_EdrTanium(
        type="edr_tanium",
        credential=mgmt.TaniumCloudCredential_Token(
            type="token", secret=token),
        url=url,
    )

def load_config(path: str) -> Tuple[str, Dict]:
    cfg = configparser.ConfigParser()
    with open(path, "r") as f:
        cfg.read_file(f)

    base_url = cfg.get("general", "base_url", fallback=BASE_URL).strip()

    providers: Dict[str, Dict] = {}

    if cfg.has_section("edr_crowdstrike"):
        s = cfg["edr_crowdstrike"]
        url = s.get("url", "").strip() or None
        client_id = s.get("client_id", "").strip()
        client_secret = s.get("client_secret", "").strip()
        if client_id and client_secret:
            providers["edr_crowdstrike"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
            }

    if cfg.has_section("edr_sentinelone"):
        s = cfg["edr_sentinelone"]
        url = s.get("url", "").strip() or None
        token = s.get("token", "").strip()
        xdr_url = s.get("xdr_url", "").strip()
        xdr_token = s.get("xdr_token", "").strip()

        if token and xdr_url and xdr_token:
            providers["edr_sentinelone"] = {
                "url": url,
                "token": token,
                "xdr_url": xdr_url,
                "xdr_token": xdr_token,
            }
    if cfg.has_section("edr_defender"):
        s = cfg["edr_defender"]
        url = s.get("url", "").strip() or None
        client_id = s.get("client_id", "").strip()
        client_secret = s.get("client_secret", "").strip()
        tenant_id = s.get("tenant_id", "").strip()
        if client_id and client_secret and tenant_id:
            providers["edr_defender"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
                "tenant_id": tenant_id,
            }
    if cfg.has_section("edr_sophos"):
        s = cfg["edr_sophos"]
        url = s.get("url", "").strip() or None
        client_id = s.get("client_id", "").strip()
        client_secret = s.get("client_secret", "").strip()
        if client_id and client_secret:
            providers["edr_sophos"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
            }
    if cfg.has_section("edr_malwarebytes"):
        s = cfg["edr_malwarebytes"]
        url = s.get("url", "").strip() or None
        client_id = s.get("client_id", "").strip()
        client_secret = s.get("client_secret", "").strip()
        account_id = s.get("account_id", "").strip()
        if client_id and client_secret and account_id:
            providers["edr_malwarebytes"] = {
                "url": url,
                "client_id": client_id,
                "client_secret": client_secret,
                "account_id": account_id,
            }
    if cfg.has_section("edr_tanium"):
        s = cfg["edr_tanium"]
        url = s.get("url", "").strip() or None
        token = s.get("token", "").strip()
        if token:
            providers["edr_tanium"] = {
                "url": url,
                "token": token,
            }

    return base_url, providers


def demo_edr(session_token: str, base_url: str):
    engine_client = SynqlyEngine(
        base_url=base_url,
        token=session_token,
    )

    # Query Applications
    response = engine_client.edr.query_applications(
        limit=1,
    )
    results_page = response.result
    if results_page is None:
        print("Unable to retrieve applications")
        return

    print(f"Applications results: {len(results_page)}")
    for application in results_page:
        pprint.pp(application)

    # Query Edr Threats
    findings_resp = engine_client.edr.query_threatevents(limit=1, include_raw_data=True)
    if findings_resp.result is None:
        print("Unable to retrieve threats")
        return

    print(f"\nThreats: {len(findings_resp.result)}")
    for threat in findings_resp.result:
        pprint.pp(threat)

    # Query Edr Alerts
    alerts_resp = engine_client.edr.query_alerts(
        limit=1,
    )
    if alerts_resp.result is None:
        print("Unable to retrieve alerts")
        return

    print(f"\nAlerts: {len(alerts_resp.result)}")
    for alert in alerts_resp.result:
        pprint.pp(alert)


    # Query Edr Endpoints
    endpoints_resp = engine_client.edr.query_endpoints(limit=1)
    if endpoints_resp.result is None:
        print("Unable to retrieve endpoints")
        return

    print(f"\nEndpoints: {len(endpoints_resp.result)}")
    for endpoint in endpoints_resp.result:
        pprint.pp(endpoint)
        device_id = endpoint.device.uid
        print(f"\nGet Endpoint: {device_id}")
        device_resp = engine_client.edr.get_endpoint(id=device_id)
        pprint.pp(device_resp)
        print(f"\n")

def main():
    args = parse_args()

    synqly_org_token = args.synqly_org_token
    config_path = args.config_path

    base_url, providers = load_config(config_path)

    if len(providers) == 0:
        print("No EDR providers configured with complete credentials in the config file.")
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

            if provider_name == "edr_crowdstrike":
                provider_cfg = provider_config_crowdstrike(
                    cfg["url"], cfg["client_id"], cfg["client_secret"]
                )
            elif provider_name == "edr_sentinelone":
                provider_cfg = provider_config_sentinelone(
                    cfg["url"], cfg["token"], cfg["xdr_url"], cfg["xdr_token"]
                )
            elif provider_name == "edr_defender":
                provider_cfg = provider_config_defender(
                    cfg["url"], cfg["client_id"], cfg["client_secret"], cfg["tenant_id"]
                )
            elif provider_name == "edr_sophos":
                provider_cfg = provider_config_sophos(
                    cfg["url"], cfg["client_id"], cfg["client_secret"]
                )
            elif provider_name == "edr_malwarebytes":
                provider_cfg = provider_config_malwarebytes(
                    cfg["url"], cfg["client_id"], cfg["client_secret"], cfg["account_id"]
                )
            elif provider_name == "edr_tanium":
                provider_cfg = provider_config_tanium(
                    cfg["url"], cfg["token"]
                )
            else:
                continue

            integration_response = mgmt_client.integrations.create(
                account_id=account_id,
                fullname=f"Edr Connector Example - {provider_name}",
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
            demo_edr(session_token, base_url)

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
