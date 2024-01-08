import os
import sys
import argparse
from pathlib import Path

# Add the root directory to the system path so that we can import common
# Application logic.
current_script = Path(__file__).resolve()
root = current_script.parents[1]
sys.path.append(str(root))

from shared import utils

# Synqly Python SDK imports
import management as mgmt


def parse_args():
    """
    Parses command line arguments for this example.
    """
    parser = argparse.ArgumentParser(
        description="Synqly Python SDK Ticketing Connector Example"
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
        "--s3-bucket-name",
        dest="s3_bucket_name",
        type=str,
        required=True,
        default="",
        help="Name of target S3 bucket. The bucket must already exist.",
    )
    parser.add_argument(
        "--s3-bucket-region",
        dest="s3_bucket_region",
        type=str,
        required=True,
        default="",
        help="AWS region of target S3 bucket.",
    )
    parser.add_argument(
        "--s3-access-key-id",
        dest="s3_access_key_id",
        type=str,
        required=True,
        default="",
        help="AWS Access Key ID for an IAM Entity with permissions to read/write to the target S3 bucket.",
    )
    parser.add_argument(
        "--s3-secret-access-key",
        dest="s3_secret_access_key",
        type=str,
        required=True,
        default="",
        help="AWS Secret Access Key for an IAM Entity with permissions to read/write to the target S3 bucket.",
    )
    args = parser.parse_args()
    return args


def mock_credential_config():
    """
    Helper method to construct a mock CredentialConfig object.
    """
    return mgmt.CredentialConfig_Aws(
        type="aws", access_key_id="mock", secret_access_key="mock"
    )


def s3_credential_config(access_key_id, secret_access_key):
    """
    Helper method to construct an AWS CredentialConfig object.
    """
    return mgmt.CredentialConfig_Aws(
        type="aws", access_key_id=access_key_id, secret_access_key=secret_access_key
    )


def mock_provider_config(credential_id):
    return mgmt.ProviderConfig_Storage(
        type="storage",
        bucket="mock",
        region="mock",
        credential_id=credential_id,
    )


def s3_provider_config(bucket_name, bucket_region, credential_id):
    return mgmt.ProviderConfig_Storage(
        type="storage",
        bucket=bucket_name,
        region=bucket_region,
        credential_id=credential_id,
    )


def background_job(app):
    """
    Simulates a background process performing work on behalf of tenants.
    Iterates through all tenants and, for any tenant with a Synqly Engine
    Client defined, uploads an example file.
    """
    for tenant in app.tenants.values():
        # Skip tenants that don't have a Synqly Engine Client initialized
        if tenant.synqly_engine_client is None:
            continue

        upload_path = "upload_file.txt"

        print("\n{}: Uploading example file".format(tenant.tenant_name))
        example_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        example_file = open(os.path.join(example_dir, "upload_file.txt"))

        # Upload a file to the storage Provider
        upload_resp = tenant.synqly_engine_client.storage.upload_storage(
            path=upload_path,
            request=example_file.read(),
        )
        print("File uploaded to path: " + upload_path)

        print("\n{}: Downloading example file".format(tenant.tenant_name))
        download_resp = tenant.synqly_engine_client.storage.download_storage(
            path=upload_path
        )

        print("{}: Contents of downloaded file:".format(tenant.tenant_name))
        print(download_resp)


def main():
    # Parse command line arguments
    args = parse_args()
    synqly_org_token = args.synqly_org_token
    s3_bucket_name = args.s3_bucket_name
    s3_bucket_region = args.s3_bucket_region
    s3_access_key_id = args.s3_access_key_id
    s3_secret_access_key = args.s3_secret_access_key

    # Initialize an empty application to store tenants
    app = utils.App("storage")

    # Create tenants within the Application
    try:
        app.new_tenant(synqly_org_token, "Tenant ABC")
        print("\nTenant ABC created")
    except Exception as e:
        print("Error creating Tenant ABC:" + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e
    try:
        app.new_tenant(synqly_org_token, "Tenant XYZ")
        print("Tenant XYZ created")
    except Exception as e:
        print("Error creating Tenant XYZ:" + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e

    # Placeholder variables for the IDs of the Credentials we will create
    abc_credential_id = ""
    xyz_credential_id = ""

    # Create a Synqly Credential for each tenant.
    try:
        abc_credential_id = app.create_credential(
            "Tenant ABC", "mock_storage", mock_credential_config()
        )
    except Exception as e:
        print("Error creating Credential for Tenant ABC: " + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e
    try:
        xyz_credential_id = app.create_credential(
            "Tenant XYZ",
            "aws_s3",
            s3_credential_config(s3_access_key_id, s3_secret_access_key),
        )
    except Exception as e:
        print("Error creating Credential for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e

    # Configure a mock integration for tenant ABC and an S3 Integration for Tenant XYZ
    try:
        app.configure_integration(
            "Tenant ABC",
            "mock_storage",
            mock_provider_config(abc_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant ABC: " + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e
    try:
        app.configure_integration(
            "Tenant XYZ",
            "aws_s3",
            s3_provider_config(s3_bucket_name, s3_bucket_region, xyz_credential_id),
        )
    except Exception as e:
        print("Error configuring provider integration for Tenant XYZ: " + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e

    try:
        background_job(app)
    except Exception as e:
        print("Error running background job: " + str(e))
        app._cleanup_handler()
        # Pass the error up the call chain
        raise e

    # Clean up Synqly Accounts and Integrations
    app._cleanup_handler()


try:
    main()
except:
    sys.exit(1)
