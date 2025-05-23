# IAM Connector Example

This example demonstrates how to use the IAM Connector to query users, query groups, force user password reset, disable a user and enable a user.

## Prerequisites

- Synqly Organization Access Token
- One of the next provider accounts and credentials:
    - Google
    - Okta
    - PingOne
- You'll need a dummy email to be used for the operations. 

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
    --general_tests_email ... \
    --google_client_email ... \
    --google_client_id ... \
    --google_delegate ... \
    --google_secret ... \
    --google_token_url ... \
    --okta_client_id ... \
    --okta_token ... \
    --okta_url ... \
    --pingone_auth_url ... \
    --pingone_client_id ... \
    --pingone_environment_id ... \
    --pingone_secret ... \
    --pingone_url ... \
```
