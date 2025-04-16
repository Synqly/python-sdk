
# Synqly Bridge Setup and Testing

This repository contains scripts for setting up and testing a Synqly Bridge with a Splunk integration.

## Prerequisites

- Python 3.9+ with requests and the Synqly SDK installed
- Docker
- Synqly organization token
- Splunk HEC URL and token

## Scripts

### 1. Create Synqly Bridge (`create_synqly_bridge.py`)

This script creates a Synqly Bridge group and a Splunk integration configured to receive events from the bridge.

#### Usage

```bash
python create_synqly_bridge.py \
    --synqly-org-token $SYNQLY_ORG_TOKEN \
    --synqly-account your-account-name \
    --bridge-name my-bridge \
    --splunk-url $SPLUNK_URL \
    --splunk-token $SPLUNK_HEC_TOKEN \
    --integration-name my-bridge-integration
```

Run the script with `--help` to see all documentation for the available options:

```bash
python create_synqly_bridge.py --help
```

The script will:

1. Create a Synqly Bridge group
2. Save the bridge credentials to a file (<bridge_name>.creds)
3. Create a Splunk integration if splunk parameters are provided
4. Print a Docker command to start the bridge container

### 2. Start the Bridge Container

After running the first script, start the bridge container using the Docker command provided.
You can add the flag `--level -1` to the command to see trace-level logging.

### 3. Send Test Events

Once the bridge is running, use the `send_requests.py` script to send test events:

```bash
./examples/bridge/send_requests.py \
  --synqly-org-token YOUR_SYNQLY_ORG_TOKEN \
  --synqly-account YOUR_ACCOUNT_ID \
  --integration-name my-bridge-integration
```

## Security Notes

- Treat the Bridge credentials securely as they contain secrets
- Bridge credentials should be rotated periodically
- The Bridge credential can only be used to receive integration requests for the specific Bridge ID

## References

- [Synqly Bridge Documentation](https://docs.synqly.com/bridge/agent-setup)
- [Synqly Bridge API](https://docs.synqly.com/api-reference/management/bridges)
- [Synqly Python SDK](https://github.com/Synqly/python-sdk)
