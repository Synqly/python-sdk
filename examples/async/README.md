# Async Example

This example demonstrates how to schedule an asynchronous operation and also configure a WebHook to get it's response. For this specific example we are going to schedule an 'Assets Query Devices' operation using ServiceNow provider.

## Prerequisites

- Synqly Organization Access Token
- One of the next provider accounts and credentials:
    - CrowdStrike sink
    - ServiceNow
- A WebHook url

_Note: The examples are going to be run for all the providers with available credentials._

## Running the Example
You have 2 options.

### Use config.ini
Go to `config.ini` file and fill the credentials of the examples you want to execute, then run:
```
python3 main.py --use_config_file true
```

### Use args
```
python3 main.py \
    --synqly_org_token $SYNQLY_ORG_TOKEN \
    --crowdstrike_sink_hec_secret ... \
    --crowdstrike_sink_hec_url ... \
    --general_webhook_url ... \
    --servicenow_secret ... \
    --servicenow_username ... \
    --servicenow_url ...
```
