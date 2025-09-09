#!/usr/bin/env python3
"""
Complete example demonstrating Synqly Organization Webhook functionality.

This script:
1. Sets up a local HTTP server to receive webhooks
2. Uses ngrok to create a public tunnel for webhook delivery
3. Creates an organization webhook configured for account creation events
4. Creates a test account to trigger the webhook
5. Verifies that the webhook was received and processed correctly
6. Cleans up resources

Prerequisites:
- SYNQLY_ORG_TOKEN environment variable set
- ngrok installed and authenticated (ngrok authtoken <token>)
- Flask installed (pip install flask)
- pyngrok installed (pip install pyngrok)

Usage:
export SYNQLY_ORG_TOKEN="your-token-here"
python webhook_example.py
"""

import sys
import os
import threading
import time
import json
import hmac
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from flask import Flask, request, jsonify
import typing

# Add the src directory to the Python path so we can import the local synqly package
# Go up two levels from this directory to reach the python-sdk root.
# For production use, you should use the synqly package from PyPI.
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))

# Suppress syntax warnings for OCSF files (they contain regex patterns that trigger warnings)
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="synqly.management.*")

# Import the Synqly SDK components
import synqly.management as mgmt
from synqly.management.client import SynqlyManagement
from synqly.management.environment import SynqlyManagementEnvironment


# Webhook storage
received_webhooks: typing.List[mgmt.OrganizationWebhookPayload] = []
webhook_secret = None


def validate_webhook_signature(payload_body, signature_header, integrator_key):
    """
    Validate a webhook signature from Synqly

    Args:
        payload_body (bytes): Raw request body
        signature_header (str): Value from Synqly-Signature header
        integrator_key (str): Your webhook secret (Integrator Key)

    Returns:
        bool: True if signature is valid, False otherwise
    """
    # Remove 'sha256=' prefix if present
    received_signature = signature_header.replace('sha256=', '')

    # Generate expected signature
    expected_signature = hmac.new(
        integrator_key.encode('utf-8'),
        payload_body,
        hashlib.sha256
    ).hexdigest()

    # Use timing-safe comparison
    return hmac.compare_digest(received_signature, expected_signature)


def create_flask_app():
    """Create and configure Flask application for webhook reception."""
    app = Flask(__name__)

    @app.route('/webhooks', methods=['POST'])
    def webhook_handler():
        """Handle incoming webhook requests."""
        try:
            # Get the raw request data
            payload = request.get_data()
            signature = request.headers.get('X-Synqly-Signature')

            if not validate_webhook_signature(payload, signature, webhook_secret):
                print("❌ Webhook signature verification failed")
                return jsonify({"error": "Invalid signature"}), 401

            # Parse JSON payload
            data = json.loads(payload.decode())
            try:
                # Pydantic v2
                webhook_payload = mgmt.OrganizationWebhookPayload.model_validate(data)
            except Exception as e:
                # Pydantic v1
                webhook_payload = mgmt.OrganizationWebhookPayload.parse_obj(data)

            received_webhooks.append(webhook_payload)

            print("✅ Webhook received and validated")
            print(f"   Payload: {json.dumps(data, indent=4)}")

            return jsonify({"status": "received"}), 200

        except json.JSONDecodeError:
            print("❌ Error parsing webhook JSON payload")
            return jsonify({"error": "Invalid JSON payload"}), 400
        except Exception as e:
            print(f"❌ Error processing webhook: {e}")
            return jsonify({"error": str(e)}), 500

    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint."""
        return jsonify({
            "status": "healthy",
            "webhooks_received": len(received_webhooks)
        }), 200

    return app

# Setup ngrok tunnel to expose the local webhook server to the internet.
def setup_ngrok(port=6000):
    """Setup ngrok tunnel and return the public URL."""
    try:
        from pyngrok import ngrok

        # Kill any existing tunnels
        ngrok.kill()

        # Start ngrok tunnel
        tunnel = ngrok.connect(port, bind_tls=True)
        public_url = tunnel.public_url

        print("✅ Ngrok tunnel established!")
        print(f"   Local:  http://localhost:{port}")
        print(f"   Public: {public_url}")
        print(f"   Webhook endpoint: {public_url}/webhooks")

        return public_url

    except ImportError:
        print("❌ pyngrok not installed. Please install with: pip install pyngrok")
        print("   Alternative: Start ngrok manually with: ngrok http {port}")
        return f"http://localhost:{port}"
    except Exception as e:
        print(f"❌ Error setting up ngrok: {e}")
        return f"http://localhost:{port}"


# Generate a secure webhook secret
def generate_webhook_secret():
    """Generate a secure webhook secret."""
    import secrets
    return secrets.token_hex(32)


def main():
    """Main function demonstrating organization webhook functionality."""
    global webhook_secret

    print("🚀 Starting Synqly Organization Webhook Demo")
    print("=" * 50)

    # Check for required environment variables
    token = os.getenv("SYNQLY_ORG_TOKEN")
    if not token:
        print("❌ SYNQLY_ORG_TOKEN environment variable not set")
        print("   Please set it with: export SYNQLY_ORG_TOKEN='your-token-here'")
        sys.exit(1)

    try:
        # Initialize Synqly management client
        print("🔗 Initializing Synqly client...")
        mgmt_client = SynqlyManagement(
            token=token,
            environment=SynqlyManagementEnvironment.SYNQLY,
        )
        print("✅ Synqly client initialized")

        # Setup local HTTP server to receive webhooks
        print("\n📡 Setting up local webhook server...")
        app = create_flask_app()
        port = 6000

        # Start Flask server in background thread
        def run_server():
            app.run(host='0.0.0.0', port=port, debug=False)

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        time.sleep(2)  # Give server time to start
        print(f"✅ Local server running on http://localhost:{port}")

        # Setup ngrok tunnel so we have a public URL to receive webhooks
        print("\n🌐 Setting up ngrok tunnel...")
        public_url = setup_ngrok(port)

        # Create organization webhook
        print("\n🔧 Setting up organization webhook...")
        webhook_secret = generate_webhook_secret()

        # In case the webhook already exists, delete it
        try:
            mgmt_client.organization_webhooks.delete(webhook_id="demo-webhook")
        except mgmt.NotFoundError:
            pass

        # Create new webhook for account creation events
        print("🆕 Creating new webhook...")
        webhook_config = mgmt_client.organization_webhooks.create(
            request=mgmt.CreateOrganizationWebhookRequest(
            name="demo-webhook",
            fullname="Demo Webhook for Account Creation",
            environment="test",
            filters=["account_create"],
            url=f"{public_url}/webhooks",
            secret=mgmt.OrganizationWebhookSecret(
                value=webhook_secret,
                    expires=datetime.now() + timedelta(days=30)  # Expire in 30 days
                )
            )
        )
        webhook_id = webhook_config.result.id
        print(f"✅ Created new webhook: {webhook_id}")
        print(f"   Secret: {webhook_secret[:10]}...")
        print(f"   URL: {public_url}/webhooks")

        # Create test account to trigger webhook
        print("\n👤 Creating test account to trigger webhook...")
        test_account_name = f"~test-account-{int(time.time())}"

        account_response = mgmt_client.accounts.create(
            request=mgmt.CreateAccountRequest(
                name=test_account_name,
                environment="test",
            )
        )
        account_id = account_response.result.account.id
        print(f"✅ Created test account: {test_account_name} ({account_id})")

        # Wait for webhook to be received
        print("\n⏳ Waiting for webhook to be received...")
        timeout = 30  # 30 seconds timeout
        start_time = time.time()

        while time.time() - start_time < timeout:
            if received_webhooks:
                webhook = received_webhooks[0]
                print("✅ Webhook received!")
                print(f"   Event Type: {webhook.event}")
                print(f"   Account name: {webhook.account.name}")

                # Verify this is an account creation event for our test account
                if (webhook.event == 'account_create' and webhook.account.id == account_id):
                    print("✅ Webhook verification successful - received expected account creation event!")
                    break
                else:
                    print(f"⚠️  Received webhook event '{webhook.event}' doesn't match expected 'account_create' event")

            time.sleep(1)

        if not received_webhooks:
            print("❌ Timeout waiting for webhook")
            print("   This might be normal if webhooks are delayed or filtered")

        # List webhooks to verify our webhook exists
        print("\n📋 Listing organization webhooks...")
        webhooks_response = mgmt_client.organization_webhooks.list()
        print(f"✅ Found {len(webhooks_response.result)} webhooks")

        for webhook in webhooks_response.result:
            if webhook.id == webhook_id:
                print(f"   ✅ Our webhook: {webhook.name} ({webhook.id})")
                break

        # Cleanup
        print("\n🧹 Cleaning up resources...")

        # Delete test account
        try:
            mgmt_client.accounts.delete(account_id)
            print(f"✅ Deleted test account: {account_id}")
        except Exception as e:
            print(f"⚠️  Could not delete test account: {e}")

        # Delete webhook
        try:
            mgmt_client.organization_webhooks.delete(webhook_id)
            print(f"✅ Deleted webhook: {webhook_id}")
        except Exception as e:
            print(f"⚠️  Could not delete webhook: {e}")

        # Stop ngrok
        try:
            from pyngrok import ngrok
            ngrok.kill()
            print("✅ Stopped ngrok tunnel")
        except:
            pass

        print("\n🎉 Demo completed successfully!")

        # Summary
        print("\n📊 Summary:")
        print(f"   Webhooks received: {len(received_webhooks)}")
        print(f"   Test account created: {test_account_name}")
        print(f"   Webhook URL: {public_url}/webhooks")

        if received_webhooks:
            webhook = received_webhooks[0]
            print(f"   ✅ Webhook functionality verified! Received {webhook.event.replace('_', ' ')} event")
            if webhook.account:
                print(f"   Account: {webhook.account.name} ({webhook.account.id})")
            print(f"   Nonce: {webhook.nonce}")
        else:
            print("   ⚠️  Webhook not received within timeout period")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
