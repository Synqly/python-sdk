# SIEM Query Push Example

This sample demonstrates how to use the Synqly Python SDK to query security events from OpenSearch. The script connects to your Synqly organization, creates an integration with OpenSearch using your credentials, and executes a query to retrieve security events.

## Prerequisites

- A [Synqly](https://synqly.com) `Organization`
- Your Synqly Organization API Token
- Python 3
- An OpenSearch instance with security events
- OpenSearch credentials (username/password)

## Setup and Run

All commands are run from the root of this directory.

1. Install the Synqly Python SDK and its dependencies:

   ```bash
   poetry update
   ```

2. Run the script with the required parameters:

   ```bash
   poetry run python main.py \
     --synqly-org-token YOUR_SYNQLY_ORG_TOKEN \
     --opensearch-url https://your-opensearch-instance.example.com \
     --opensearch-username admin \
     --opensearch-password your_secure_password \
     --opensearch-index security-events
   ```

## Command Line Arguments

The script accepts the following command line arguments:

- `--synqly-org-token`: Your Synqly Organization API token for authentication
- `--opensearch-url`: URL of your OpenSearch instance
- `--opensearch-username`: Username for OpenSearch basic authentication
- `--opensearch-password`: Password for OpenSearch basic authentication
- `--opensearch-index`: Index name in OpenSearch containing the security events

## How It Works

The script:

1. Creates a Synqly account if it doesn't exist
2. Creates or updates an OpenSearch integration with your provided credentials
3. Generates a session token for the integration
4. Uses the Synqly Engine API to query events from OpenSearch
5. Prints the query results

## Local Development

While the files under `/src` are auto-generated, it can sometimes be useful to install a local copy of the SDK in order to debug issues such as type mismatches. The following command will install the local version of `SynqlyPythonClient`, overriding the upstream repository.

```bash
cd ~/python-sdk
pip install -e .
```
