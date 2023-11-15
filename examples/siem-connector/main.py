import os
import time
import signal

import engine
import engine.client as engineClient
import management as mgmt
from management.client import SynqlyManagement

SYNQLY_ORG_ID = os.getenv('SYNQLY_ORG_ID')
SYNQLY_ORG_TOKEN = os.getenv('SYNQLY_ORG_TOKEN')
SPLUNK_URL = os.getenv('SPLUNK_URL')
SPLUNK_HEC_TOKEN = os.getenv('SPLUNK_HEC_TOKEN')

class App:
    def __init__(self):
        self.tenants = []
        # Initialize signal handlers to intercept Ctrl-C and perform cleanup
        signal.signal( signal.SIGINT, lambda signal, frame: self._cleanup_handler() )
        signal.signal( signal.SIGTERM, lambda signal, frame: self._cleanup_handler() )
        self.terminated = False

    def _cleanup_handler( self ):
        print("Cleaning up...")
        for tenant in self.tenants:
            # Delete the Synqly Account
            tenant.synqly_management_client.accounts.delete_account(tenant.synqly_account_id)
            print("Cleaned up Account " + tenant.synqly_account_id)
        self.terminated = True
    
    # Add a new tenant to the app's tenant pool
    def new_tenant(self, new_tenant_name):
        # Make sure the tenant doesn't already exist
        for tenant in self.tenants:
            if tenant.synqly_account_id == new_tenant_name:
                raise Exception("Duplicate tenant id: " + id)
            
        # Create a Synqly Account for the new tenant
        management_client = SynqlyManagement(token=SYNQLY_ORG_TOKEN)

        account_request = mgmt.CreateAccountRequest(name=new_tenant_name)
        account_response = management_client.accounts.create_account(request=account_request)
        account_id = account_response.result.account.id

        # Add the new tenant to the tenant pool. The Event Logger client will be
        # initialized in configure_event_logging, so leave it as None for now.
        self.tenants.append(Tenant(
            tenant_name=new_tenant_name,
            synqly_account_id=account_id, 
            synqly_management_client=management_client, 
            synqly_event_logger=None))
            
    def configure_event_logging(self, tenant_name, siem_provider_type, siem_provider_token):
        # Locate the tenant in our App's tenant pool
        tenant = None
        for t in self.tenants:
            print ("Found synqly account: "+t.tenant_name)
            if t.tenant_name == tenant_name:
                tenant = t
                break
        
        if tenant is None:
            raise Exception(tenant_name + " not found")
        
        # If a Token is not provided, set a default value to pass SDK type checks
        if siem_provider_token is None:
            siem_provider_token = "No Auth Needed"

        # We need to save the Provider credentials in Synqly before configuring the Integration
	    # We will use the Synqly Client we created for the tenant to do this
        credential = tenant.synqly_management_client.credentials.create_credential(
            account_id = tenant.synqly_account_id,
            request = mgmt.CreateCredentialRequest(
                name = "{} authentication token".format(siem_provider_type),
                config = mgmt.CredentialConfig_Token(
                    secret = siem_provider_token,
                    type="token"
                )
            )
        )
        print ("Credential response "+ str(credential))

        print("Created credential: " + credential.result.id)
        # Generate Provider configuration based on which provider type was selected.
        # A Provider configuration object references a Credential object, and acts
        # as the basis for initializing an Integration.
        provider_config = None
        if siem_provider_type == "splunk":
            provider_config = self.splunk_config(SPLUNK_URL, credential.result.id)
        elif siem_provider_type == "inmem":
            provider_config = self.in_mem_config(credential.result.id)
        else:
            raise Exception("Invalid SIEM provider type: " + siem_provider_type)

        # Create a Synqly SIEM Integration for the tenant
        integrationReq = mgmt.CreateIntegrationRequest(
            name = "Background Event Logger",
            category = "siem",
            provider_type = siem_provider_type,
            provider_config = provider_config,
        )
        integration = tenant.synqly_management_client.integrations.create_integration(
            account_id = tenant.synqly_account_id,
            request = integrationReq)

        print("Created integration: " + str(integration))

        # Create an Event Logger for the tenant. The Event Logger is essentially
        # just a persistent engine Client that's configured to send data to a 
        # specific Synqly Integration.
        tenant.synqly_event_logger = engineClient.SynqlyEngine(
            token = integration.result.token.access.secret,
        )

    # Return Synqly Provider configuration for a Splunk provider
    def splunk_config(self, splunk_url, credential_id):
        return mgmt.ProviderConfig_Siem(
            type = "siem",
            url = splunk_url,
            credential_id = credential_id,
            config = mgmt.SiemProviderTypeConfig_Splunk(
                type="splunk",
                # Do not verify the Splunk server's TLS certificate. This
                # is not recommended for production use; however, it is set
                # here because Splunk HEC endpoints use self-signed
                # "SplunkServerDefaultCert" certificates by default.
                skip_tls_verify = True,
            )
        )
    
    # Return Synqly Provider configuration for an in-memory mock SIEM. Intended for
    # testing without the need for an external provider.
    def in_mem_config(self, credential_id):
        return mgmt.ProviderConfig_Siem(
            url = None,
            credential_id = "not-used",
            type = "siem"
        )

    def background_job(self):
        while not self.terminated:
            for tenant in self.tenants:
                print("Doing some work for tenant %s".format(tenant.tenant_name))

                new_event = create_sample_event()

                if tenant.synqly_event_logger is not None:

                    continue
                # Send an event to the tenant's Event Logger
                tenant.synqly_event_logger.send_event(
                    event_type = "background-job",
                    event = {
                        "message": "Hello from " + tenant.tenant_name,
                    }
                )
                print("Sent event to " + tenant.tenant_name)
            time.sleep(1)
            pass
    
def create_sample_event():
    # Currently uses hard-coded numbers to represent OCSF Enums. We aim to add
    # lexicographic names for these values in the future to make OCSF objects
    # easier to work with.
    return engine.Event_ScheduledJobActivity(
        # OCSF Activity_Update
        activity_id=2,
        # OCSF CategoryUID: 1 - SystemActivity
        category_uid=1,
        # OCSF ClassUID: 1006 - ScheduledJobActivity:
        class_uid = 1006,

        cloud = None,

        disposition_id = "Other",
        # OCSF DeviceType_Server
        device = {
            "type_id": 1,
        },
        # OCSF scheduledJobActivity.Job
        job = {
            # OCSF scheduledJobActivity.File
            "file": {
                "name": "main.py",
                "type_id":  1,
            },
            "name": "Background Job",
        },
        # OCSF scheduledJobActivity.Metadata
        metadata = {
            # OCSF scheduledJobActivity.Product
            "product": {
                "vendor_name": "Synqly Python SDK",
            },
            "version": "1.0.0",
        },
        time = time.time(),
        # OCSF Severity_Informational
        severity_id=1,
        # OCSF Type_ScheduledJobActivity_Update
        type_uid = 100602,
    )

class Tenant:
    def __init__(self, tenant_name, synqly_account_id, synqly_management_client, synqly_event_logger):
        self.tenant_name = tenant_name
        self.synqly_account_id = synqly_account_id
        self.synqly_management_client = synqly_management_client
        self.synqly_event_logger = synqly_event_logger

def main():
    # Environment variables for connecting to Synqly
    if "SYNQLY_ORG_ID" not in os.environ or "SYNQLY_ORG_TOKEN" not in os.environ:
        print("SYNQLY_ORG_ID and SYNQLY_ORG_TOKEN environment variables must be set")
        return
    
    if SYNQLY_ORG_ID == "" or SYNQLY_ORG_TOKEN == "":
        print("SYNQLY_ORG_ID and SYNQLY_ORG_TOKEN environment variables must be set to non-empty strings")
        return
    
    app = App()

    try:
        app.new_tenant("Tenant ABC")
        print("Tenant ABC created")
    except Exception as e:
        print("Error creating Tenant ABC:" + str(e))
        app._cleanup_handler()
        
    try:
        app.new_tenant("Tenant XYZ")
        print ("Tenant XYZ created")
    except Exception as e:
        print("Error creating Tenant XYZ:" + str(e))
        app._cleanup_handler()

    try:
        app.configure_event_logging("Tenant ABC", "splunk", SPLUNK_HEC_TOKEN)
    except Exception as e:
        print("Error configuring event logging for Tenant ABC: " + str(e))
        app._cleanup_handler()

    app.background_job()

main()