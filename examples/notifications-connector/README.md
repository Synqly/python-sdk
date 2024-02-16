# Notifications Connector Example

This example demonstrates how to use the Notifications Connector to send a notification to Slack.

## Prerequisites

- Synqly Organization Access Token
- Slack account and a Slack workspace

## Setup

You will need to create a Slack app and install it to your workspace. To do this, follow the steps below:

1. Browse to https://api.slack.com/apps
1. Click on Create New App button
1. Choose an app name
1. Give the app permission to send messages to your workspace and install it
    1. Open the settings for your app from the App Management page.
    1. In the navigation menu, select OAuth & Permissions.
    1. Scroll down to the Scopes section, and pick channels:read and chat:write from the drop-down menu.
    1. Click Save changes.
    1. Scroll back to the top of this page and look for the button that says Install App to Workspace
1. On the OAuth & Permissions page you're brought back to, you should now see an OAuth access token available. The token should start with `xoxb`. Copy this token and save it for later.

## Running the Example

```
python3 python/notifications-connector/main.py \
                --synqly-org-token $SYNQLY_ORG_TOKEN \
                --slack-channel "#channle-name" \
                --slack-token "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx"
```
