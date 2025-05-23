# Assets Connector Example

This example demonstrates how to use the Assets Connector to query and create devices.

## Prerequisites

- Synqly Organization Access Token
- At least one of the next provider accounts and credentials:
    - Armis Centrix
    - Nozomi Vantage
    - ServiceNow

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
    --armis_token ... \
    --armis_url ... \
    --nozomi_secret ... \
    --nozomi_username ... \
    --nozomi_url ... \
    --servicenow_secret ... \
    --servicenow_username ... \
    --servicenow_url ...
```
