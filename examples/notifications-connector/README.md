# Notifications Connector Example

This example demonstrates how to use the Notifications Connector to send a notification to Slack.

## Prerequisites

- Synqly Organization Access Token
- Slack account and a Slack workspace

## Setup

You will need to create a Slack app and install it to your workspace. To do this, follow the steps below:

1. Browse to https://api.slack.com/apps
1. Click on Create New App button
1. Select From Scratch
1. Give your app a name and select the workspace you want to install it to. Click Create App.
1. In the "Add features and functionality" section, click on "Bots".
1. Scroll down to the Scopes section, and pick channels:read and chat:write from the drop-down menu.
1. Scroll back to the top of this page and look for the button that says Install to Workspace under the "OAuth Tokens for Your Workspace" section. Click this button and follow the instructions to install the app to your workspace.
1. On the OAuth & Permissions page you're brought back to, you should now see an OAuth access token available under the heading "Bot User OAuth Token". The token should start with `xoxb`. Copy this token and save it for later.

Your Slack app is now installed to your workspace and you have an OAuth token that you can use to send messages to Slack.

Before it can send message to a Slack channel; however, it must be invited to that channel. You can do this by typing `/invite @your-app-name` in the channel you want to invite it to.

## Running the Example

```
python3 main.py \
    --synqly-org-token $SYNQLY_ORG_TOKEN \
    --slack-channel "#channel-name" \
    --slack-token "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx"
```
