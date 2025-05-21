import sys
import time
import argparse
from pathlib import Path

# Synqly Python SDK imports
from synqly import engine
from synqly.engine.client import SynqlyEngine
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK SIEM Connector Example"
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
        "--opensearch-url",
        dest="opensearch_url",
        type=str,
        required=True,
        default="",
        help="URL of target OpenSearch endpoint, example: 'https://opensearch.synqly.com'",
    )
    parser.add_argument(
        "--opensearch-username",
        dest="opensearch_username",
        type=str,
        required=True,
        default="",
        help="Username for OpenSearch basic authentication",
    )
    parser.add_argument(
        "--opensearch-password",
        dest="opensearch_password",
        type=str,
        required=True,
        default="",
        help="Password for OpenSearch basic authentication",
    )
    parser.add_argument(
        "--opensearch-index",
        dest="opensearch_index",
        type=str,
        required=True,
        default="",
        help="Index name in OpenSearch to write data to",
    )
    return parser.parse_args()


def opensearch_config(opensearch_url, username, password, index):
    return mgmt.ProviderConfig_SiemOpensearch(
        type="siem_opensearch",
        index=index,
        url=opensearch_url,
        skip_tls_verify=True,
        credential=mgmt.OpenSearchCredential_Basic(
            type="basic",
            username=username,
            secret=password
        )
    )


def create_or_update_account_and_integration(client: SynqlyManagement, account_name: str, integration_name: str, opensearch_url: str, opensearch_username: str, opensearch_password: str, opensearch_index: str, mapping_id: str):
    # Create an account if it doesn't exist
    try:
        client.accounts.get(account_id=account_name)
    except mgmt.NotFoundError:
        print(f"Account {account_name} not found, creating it")
        client.accounts.create(
            request=mgmt.CreateAccountRequest(
                name=account_name,
                labels=["demo"],
                description="Synqly OpenSearch Example",
                environment=mgmt.Environment.PROD
            )
        )
    else:
        print(f"Using existing account {account_name}")

    # Create the integration request
    request = mgmt.CreateIntegrationRequest(
        name=integration_name,
        provider_config=opensearch_config(opensearch_url, opensearch_username, opensearch_password, opensearch_index),
        mappings=[
            mgmt.MappingChain(
                mappings=[mapping_id],
                operation_ids=['siem_query_events'],
            )
        ],
    )

    # Create the integration
    try:
        response = client.integrations.create(account_id=account_name, request=request)
    except mgmt.ConflictError:
        print(f"Integration {integration_name} already exists, updating existing integration")
        existing_integration = client.integrations.get(account_id=account_name, integration_id=integration_name)
        updated_integration = existing_integration.result.copy(
            update={
                "provider_config": opensearch_config(opensearch_url, opensearch_username, opensearch_password, opensearch_index),
                "mappings": [
                    mgmt.MappingChain(
                        mappings=[mapping_id],
                        operation_ids=['siem_query_events'],
                    )
                ]
            }
        )
        response = client.integrations.update(
            account_id=account_name,
            integration_id=integration_name,
            request=updated_integration
        )
        print(f"Integration {integration_name} updated\n")


def session_token_for_integration(client: SynqlyManagement, account_name: str, integration_name: str) -> str:
    response = client.tokens.create_integration_token(
        account_id=account_name,
        integration_id=integration_name,
        request=mgmt.CreateIntegrationTokenRequest(
            ttl="10m"
        )
    )
    return response.result.secret


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    opensearch_url = args.opensearch_url
    opensearch_username = args.opensearch_username
    opensearch_password = args.opensearch_password
    opensearch_index = args.opensearch_index

    # Initialize Synqly Management client
    client = SynqlyManagement(token=synqly_org_token)

    account_name = "synqly-opensearch-example"
    integration_name = "opensearch-integration"

    mapping_id = "INSERT_MAPPING_ID_HERE"

    create_or_update_account_and_integration(client, account_name, integration_name, opensearch_url, opensearch_username, opensearch_password, opensearch_index, mapping_id)
    session_token = session_token_for_integration(client, account_name, integration_name)

    # Initialize Synqly Engine client
    engine_client = SynqlyEngine(token=session_token)

    # query events from OpenSearch
    response = engine_client.siem.query_events(
        filter="time[gte]2025-05-20T00:00:00.000Z"
    )
    print(response.result)


try:
    main()
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")
    sys.exit(1)
