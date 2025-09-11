#!/usr/bin/env python3
import argparse
import time
import requests

from synqly.management import (
    CreateIntegrationTokenRequest,
)
from synqly.management.client import SynqlyManagement


def parse_args():
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
        "--integration-name",
        dest="integration_name",
        type=str,
        default="",
        help="Name for the integration (default: <bridge_name>-integration)",
    )
    return parser.parse_args()



def send_event(integration_token):
    """Send a test event to exercise the bridge."""

    url = "https://api.synqly.com/v1/siem/events"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {integration_token}"
    }
    data = [
        {
          "class_name": "Detection Finding",
          "activity_id": 1,
          "category_uid": 2,
          "class_uid": 2004,
          "type_uid": 200401,
          "type_name": "Detection Finding: Create",
          "message": "Malware detected on endpoint",
          "severity_id": 4,
          "severity": "High",
          "time": int(time.time() * 1000),
          "timezone_offset": 0,
          "actor": {
            "process": {
              "pid": 1234,
              "name": "suspicious.exe"
            }
          },
          "src_endpoint": {
            "hostname": "infected-workstation",
            "ip": "10.0.3.15",
            "name": "user-laptop-abc",
            "os": {
              "name": "Windows",
              "version": "10",
              "platform": "windows"
            },
            "mac": "aa:bb:cc:11:22:33"
          },
          "metadata": {
            "product": {
              "name": "Endpoint Protection",
              "vendor_name": "Security Corp",
              "version": "5.3.1"
            },
            "version": "1.3.0",
            "log_provider": "edr-service"
          },
          "disposition_id": 2,
          "disposition": "Blocked",
          "finding_info": {
            "analytic": {
              "name": "Malware Signature Detection",
              "uid": "sig-12345",
              "rule_id": "rule-6789",
              "rule_name": "Known Ransomware",
              "type_id": 1
            },
            "created_time": int(time.time() * 1000),
            "desc": "Detected known ransomware signature with high confidence",
            "first_seen_time": int(time.time() * 1000),
            "last_seen_time": int(time.time() * 1000),
            "title": "Ransomware Detection",
            "uid": "finding-12345"
          },
          "threat_info": {
            "category_id": 3,
            "category": "Malware",
            "name": "Ransomware.Cryptolocker",
            "type_id": 5,
            "type": "Ransomware"
          },
          "data_sources": [
            {
              "category": "File",
              "category_id": 2,
              "name": "File Creation Event",
              "source_id": 4,
              "source": "File System"
            },
            {
              "category": "Process",
              "category_id": 1,
              "name": "Process Creation Event",
              "source_id": 1,
              "source": "Process Monitor"
            }
          ],
          "status_id": 1,
          "status": "New"
        }
    ]

    response = requests.post(url, headers=headers, json=data)
    if response.status_code <= 300:
        print("Successfully sent test event")
    else:
        print(f"Failed to send test event: {response.status_code} {response.text}")


def main():
    args = parse_args()

    # Initialize Synqly Management client
    client = SynqlyManagement(token=args.synqly_org_token)

    # Send a test event if requested
    if not args.integration_name:
        print("No integration name provided, please provide an integration name to send a test event")
        return

    # Create a session token for the integration
    token = client.tokens.create_integration_token(
        account_id=args.synqly_account,
        integration_id=args.integration_name,
        token_ttl="1m",
    )
    print("Created a session token for the integration")

    print("Sending a test event...")
    send_event(token.result.secret)

    return


if __name__ == "__main__":
    main()