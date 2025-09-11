#!/usr/bin/env python3
import argparse
import json
import os

import requests

import synqly.management
from synqly.management.client import SynqlyManagement


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create Synqly Bridge group and integration"
    )
    parser.add_argument(
        "--synqly-org-token",
        dest="synqly_org_token",
        type=str,
        required=True,
        help="Organization token for authenticating with Synqly",
    )
    parser.add_argument(
        "--synqly-account",
        dest="synqly_account",
        type=str,
        required=True,
        help="Account name or ID",
    )
    parser.add_argument(
        "--bridge-name",
        dest="bridge_name",
        type=str,
        required=False,
        help="Name for the bridge",
    )
    parser.add_argument(
        "--labels",
        dest="labels",
        type=str,
        nargs="+",
        default=["test"],
        help="Labels for the bridge (default: test)",
    )
    parser.add_argument(
        "--splunk-url",
        dest="splunk_url",
        type=str,
        help="Splunk HEC URL for integration (e.g., https://10.200.21.55:8088)",
    )
    parser.add_argument(
        "--splunk-token",
        dest="splunk_token",
        type=str,
        help="Splunk HEC token for integration",
    )
    parser.add_argument(
        "--integration-name",
        dest="integration_name",
        type=str,
        default="",
        help="Name for the integration (default: <bridge_name>-integration)",
    )
    parser.add_argument(
        "--exercise-bridge",
        dest="exercise_bridge",
        action="store_true",
        help="Send a test event to exercise the bridge",
    )
    return parser.parse_args()


def create_bridge(client: SynqlyManagement, account_id: str, bridge_name: str, labels: list[str]) -> synqly.management.CreateBridgeResponseResult:
    """Create a Synqly Bridge group and return the response."""
    request = synqly.management.CreateBridgeRequest(name=bridge_name, labels=labels)
    try:
        client.bridges.get(account_id=account_id, bridge_id=bridge_name)
    except synqly.management.NotFoundError as e:
        print(f"Bridge {bridge_name} does not exist, creating new bridge")
    else:
        print(f"Bridge {bridge_name} already exists, deleting existing bridge")
        client.bridges.delete(account_id=account_id, bridge_id=bridge_name)

    response = client.bridges.create(account_id=account_id, name=bridge_name, labels=labels)
    return response.result


def save_bridge_credentials(bridge_credential: str, bridge_name: str) -> str:
    """Save bridge credentials to a file."""
    creds_file = f"{bridge_name}.creds"
    bridge_credential = bridge_credential.replace("\\n", "\n")
    with open(creds_file, "w") as f:
        f.write(bridge_credential)
    print(f"Bridge credentials saved to {creds_file}")
    return creds_file


def create_integration(client: SynqlyManagement, account_id: str, integration_name: str, bridge_labels: list[str], splunk_url: str, splunk_token: str) -> synqly.management.CreateIntegrationResponse:
    """Create a Synqly Integration that uses the bridge."""
    # Create a bridge selector that points to our bridge
    bridge_selector = synqly.management.BridgeSelector_Labels(type="labels", value=bridge_labels)

    # Create Splunk provider configuration
    provider_config = synqly.management.ProviderConfig_SiemSplunk(
        type="siem_splunk",
        hec_url=splunk_url,
        hec_credential=synqly.management.SplunkHecToken_Token(
            type="token",
            secret=splunk_token
        ),
        skip_tls_verify=True
    )

    # Create the integration
    try:
        response = client.integrations.create(
            account_id=account_id,
            name=integration_name,
            provider_config=provider_config,
            bridge_selector=bridge_selector
        )
    except synqly.management.ConflictError:
        print(f"Integration {integration_name} already exists, updating existing integration")
        existing_integration = client.integrations.get(account_id=account_id, integration_id=integration_name)
        updated_integration = existing_integration.result.copy(
            update={
                "provider_config": provider_config,
                "bridge_selector": bridge_selector
            }
        )
        response = client.integrations.update(account_id=account_id, integration_id=integration_name, **updated_integration.dict())
        print(f"Integration {integration_name} updated\n")

    return response.result


def main():
    args = parse_args()

    # Initialize Synqly Management client
    client = SynqlyManagement(token=args.synqly_org_token)

    # Create a Synqly Bridge group
    print(f"Creating Synqly Bridge group: {args.bridge_name}")
    bridge_response = create_bridge(client, args.synqly_account, args.bridge_name, args.labels)

    # Extract bridge ID and credentials
    bridge_id = bridge_response.bridge.id
    bridge_credential = bridge_response.credential

    print(f"Bridge created with ID: {bridge_id} and labels: {args.labels}")

    # Save bridge credentials to a file
    save_bridge_credentials(bridge_credential, args.bridge_name)

    # Create integration if Splunk details are provided
    if args.splunk_url and args.splunk_token:
        integration_name = args.integration_name or f"{args.bridge_name}-integration"
        print(f"Creating integration: {integration_name}")

        try:
            create_integration(
                client,
                args.synqly_account,
                integration_name,
                args.labels,
                args.splunk_url,
                args.splunk_token
            )
        except synqly.management.ConflictError as e:
            print(f"Integration {integration_name} already exists, using existing integration")

        # Print docker run command
        print("\nRun the following command to start the bridge container:")
        print(f"docker run -v $(pwd):/creds quay.io/synqly/bridge --bridge-creds=/creds/{args.bridge_name}.creds --bridge-id={bridge_id} --bridge-server-address=tls://bridge.synqly.com:4222 --allow-address={args.splunk_url.split('//')[1].split('/')[0]}")

    print("\nBridge Security Note:")
    print("Treat the BridgeGroup credential securely as it contains a secret.")
    print("The BridgeGroup credential needs to be rotated periodically.")
    print("The BridgeGroup credential can only be used to receive integration requests for the specific BridgeGroup.Id")


if __name__ == "__main__":
    main()
