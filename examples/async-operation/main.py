"""
Synqly Python SDK - Async Demo Example
"""

import os
import time
import threading

from synqly import engine
from synqly.engine.client import SynqlyEngine
from synqly import management as mgmt
from synqly.management.client import SynqlyManagement

mgmt_url = "https://api.synqly.com"
engine_url = "https://api.synqly.com"

operation_id = "appsec_query_findings"

def fetch_findings(engine_client: SynqlyEngine, account: mgmt.Account) -> None:
    operation = engine_client.operations.create(
        request=engine.CreateOperationRequest(
            operation=operation_id,
            input=engine.OperationInput(
                filter=[],
            ),
        )
    )
    print(f"Started pulling findings for account {account.name}. Operation details: {operation.result.operation.dict()}")

    id = operation.result.operation.id
    status = operation.result.operation.status
    while status != engine.OperationStatus.COMPLETE:
        op = engine_client.operations.get(id)
        if op.result.errors:
            print(f"Operation failed with errors: {op.result.errors}")
            break
        status = op.result.status
        print(f"account: ({account.name}:{account.id}) status: {status}")
        time.sleep(10)


def main():
    org_token = os.getenv("SYNQLY_ORG_TOKEN")
    mgmt_client = SynqlyManagement(
        base_url=mgmt_url,
        token=org_token,
    )

    connector_category = operation_id.split("_")[0]

    # get all configured integrations for the connector category
    integrations = mgmt_client.integrations.list(
        filter=["category[eq]" + connector_category],
        expand=["account"],
    )
    print(f"Found {len(integrations.result)} integrations")
    for integration in integrations.result:
        print(f"Integration: {integration.name} of type {integration.provider_config.type} in account {integration.account.name}")

    threads: list[threading.Thread] = []
    for integration in integrations.result:
        token = mgmt_client.tokens.create_integration_token(
            account_id=integration.account.id,
            integration_id=integration.id,
            request=mgmt.CreateIntegrationTokenRequest(
                token_ttl="1h",
            )
        )
        engine_client = SynqlyEngine(
            base_url=engine_url,
            token=token.result.secret
        )

        # Create and start a new thread for each save_findings call
        thread = threading.Thread(
            target=fetch_findings,
            args=(engine_client, integration.account)
        )
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All operations completed")

if __name__ == "__main__":
    main()
