# Synqly Organization Webhook Demo

This directory contains a complete example demonstrating how to use Synqly's organization webhook feature.

## Overview

This example demonstrates how to use Synqly's organization webhook feature to receive real-time notifications about events in your Synqly organization. The example will create a webhook for account creation events and create a test account to trigger the webhook.

It shows how to validate the webhook signature and verify the webhook was received and processed correctly.

## Prerequisites

1. Synqly Organization Token
   You need a valid Synqly organization token with administrator permissions:

    ```bash
    export SYNQLY_ORG_TOKEN="{YOUR_SYNQLY_ORG_TOKEN}"
    ```

2. Python Dependencies
   Create a virtual environment and install the required packages:

    ```bash
    make setup
    ```

3. ngrok Setup
   ngrok is used to create a public tunnel to your local webhook server.

   Install ngrok:

   ```bash
   # macOS with Homebrew
   brew install ngrok/ngrok/ngrok
   ```

   ```bash
   # Or download from https://ngrok.com/download
   ```

   Authenticate ngrok:

   ```bash
   ngrok config add-authtoken {YOUR_NGROK_AUTH_TOKEN}
   ```

   Get your auth token from https://dashboard.ngrok.com/get-started/your-authtoken

## Quick Start

```bash
# Setup and run
make setup
export SYNQLY_ORG_TOKEN="{YOUR_SYNQLY_ORG_TOKEN}"
ngrok config add-authtoken {YOUR_NGROK_AUTH_TOKEN}
make run
```

## What It Does

1. Sets up a local Flask server to receive webhooks
2. Creates an ngrok tunnel for public access
3. Creates an organization webhook for account creation events
4. Creates a test account to trigger the webhook
5. Verifies webhook receipt and signature validation
6. Cleans up all resources
