"""
Synqly Python SDK Notifications Example

This example demonstrates how to use the Synqly Python SDK to create a
Notifications Integration for a tenant.
"""

# Standard imports
import time
import sys
import argparse
from pathlib import Path

# Add the root directory to the system path so that we can import common
# Application logic.
current_script = Path(__file__).resolve()
root = current_script.parents[1]
sys.path.append(str(root))

from shared import utils

# Synqly Python SDK imports
import engine
import management as mgmt


def parse_args():
    """
    Parses command line arguments for this example.
    """
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK Notifications Connector Example"
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
        "--slack-channel",
        dest="slack_channel",
        type=str,
        required=True,
        default="",
        help="ID of the Slack channel to send messages to",
    )
    parser.add_argument(
        "--slack-token",
        dest="slack_token",
        type=str,
        required=True,
        default="",
        help="",
    )
    args = parser.parse_args()
    return args


def slack_provider_config(slack_channel: str, slack_token: str):
    return mgmt.ProviderConfig_NotificationsSlack(
        type="notifications_slack",
        channel=slack_channel,
        credential=mgmt.SlackCredential_Token(
            type="token",
            secret=slack_token,
        )
    )


def notify(tenant: utils.Tenant):
    # Send a notification
    print("\nSending notification")
    send_response = tenant.synqly_engine_client.notifications.create_notification(
        request=engine.CreateNotificationRequest(
            name="Hello World",
            description="Hello World!",
            created_at="2021-01-01T00:00:00Z",
            updated_at="2021-01-01T00:00:00Z",
            id="123",
            priority=engine.Priority.HIGH,
            project="project",
            status="status",
            summary="summary",
            issue_type="issue_type",
            creator="creator",
            assignee="assignee",
            contact="contact",
            tags=["tag1", "tag2"],
            reference="reference",
            notification_status=engine.NotificationStatus.OPEN,
        )
    )
    print("Sent notification: {}".format(send_response.result.id))


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token

    # Initialize an empty application
    app = utils.App("notifications")

    # Initialize tenants within our Application
    try:
        app.new_tenant(synqly_org_token, "Notifier Co")
        print("Tenant Notifier Co created")
    except Exception as e:
        print("Error creating Notifier Co:" + str(e))
        app._cleanup_handler()
        raise e

    try:
        app.configure_integration(
            "Notifier Co",
            slack_provider_config(args.slack_channel, args.slack_token),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        raise e

    # Send a notification
    try:
        notify(app.tenants["Notifier Co"])
    except Exception as e:
        print("Error sending notification: " + str(e))

    app._cleanup_handler()


main()
