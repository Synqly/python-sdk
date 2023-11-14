import os
import sys
import signal

import engine.client as engineClient
import management as mgmt
from management.client import SynqlyManagement


from management import CreateAccountRequest

SYNQLY_ORG_ID = os.getenv('SYNQLY_ORG_ID')
SYNQLY_ORG_TOKEN = os.getenv('SYNQLY_ORG_TOKEN')

class App:
    def __init__(self):
        self.tenants = []
        # Initialize signal handlers to intercept Ctrl-C and perform cleanup
        signal.signal( signal.SIGINT, lambda signal, frame: self._signal_handler() )
        signal.signal( signal.SIGTERM, lambda signal, frame: self._signal_handler() )
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
        print ("Credential response "+str(credential))

        print("Created credential: " + credential.result.credential.id)
        # Generate Provider configuration based on which provider type was selected.
        # A Provider configuration object references a Credential object, and acts
        # as the basis for initializing an Integration.
        provider_config
        if siem_provider_type == "splunk":
            provider_config = self.splunk_config(siem_provider_token, credential.id)
        elif siem_provider_type == "inmem":
            provider_config = self.in_mem_config(credential.id)
        else:
            raise Exception("Invalid SIEM provider type: " + siem_provider_type)

        # Create a Synqly SIEM Integration for the tenant
        integration = tenant.synqly_management_client.integrations.create_integration(
            name = "Background Event Logger",
            category = "siem",
            provider_type = siem_provider_type,
            provider_config = provider_config,
        )

        # Create an Event Logger for the tenant. The Event Logger is essentially
        # just a persistent engine Client that's configured to send data to a 
        # specific Synqly Integration.
        tenant.synqly_event_logger = engineClient.SynqlyEngine(
            token = integration.result.token.access.secret,
        )

    # Return Synqly Provider configuration for a Splunk provider
    def splunk_config(self, splunk_url, credential_id):
        return mgmt.ProviderConfig_Siem(
            mgmt.SiemConfig(
                url = splunk_url,
                credential_id = credential_id,
                config = mgmt.SiemProviderTypeConfig_Splunk(
                    config = mgmt.SplunkConfig(
                        # Do not verify the Splunk server's TLS certificate. This
                        # is not recommended for production use; however, it is set
                        # here because Splunk HEC endpoints use self-signed
                        # "SplunkServerDefaultCert" certificates by default.
                        skip_tls_verify = True,
                    )
                )
            )
        )
    
    # Return Synqly Provider configuration for an in-memory mock SIEM. Intended for
    # testing without the need for an external provider.
    def in_mem_config(self):
        return mgmt.ProviderConfig_Siem(
            url = None,
            credential_id = "not used for in memory provider",
        )

    def background_job(self):
        while not self.terminated:
            print("Hi")
            pass
    

class Tenant:
    def __init__(self, tenant_name, synqly_account_id, synqly_management_client, synqly_event_logger):
        self.tenant_name = tenant_name
        self.synqly_account_id = synqly_account_id
        self.synqly_management_client = synqly_management_client
        self.synqly_event_logger = synqly_event_logger

def main():
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
        app.configure_event_logging("Tenant ABC", "inmem", None)
    except Exception as e:
        print("Error configuring event logging for Tenant ABC: " + str(e))
        app._cleanup_handler()

    app.background_job()

main()