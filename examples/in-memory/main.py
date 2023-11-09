import os

from synqly_management import SynqlyManagement
from synqly_management import CreateAccountRequest

SYNQLY_ORG_ID = os.getenv('SYNQLY_ORG_ID')
SYNQLY_ORG_TOKEN = os.getenv('SYNQLY_ORG_TOKEN')

class App:
    def __init__(self):
        self.tenants = []
    
    # Add a new tenant to the app's tenant pool
    def new_tenant(self, tenant_id):
        # Make sure the tenant doesn't already exist
        for tenant in self.tenants:
            if tenant.id == id:
                raise Exception("Duplicate tenant id: " + id)
            
        # Create a Synqly Account for the new tenant
        synqly_management_client = SynqlyManagement(token=SYNQLY_ORG_TOKEN)

        account_request = CreateAccountRequest(name=tenant_id)
        synqly_management_client.accounts.create_account(account_request)
            
    def configure_event_logging(tenant_id):
        # Find the tenant
        tenant = None
        for t in self.tenants:
            if t.id == tenant_id:
                tenant = t
                break
        
        if tenant is None:
            raise Exception(tenant_id + " not found")
        
        # Create a new event logger for the tenant
        tenant.synqly_event_logger = SynqlyEventLogger(tenant.synqly_account_id, tenant.synqly_management_client)


        # credential, err := tenant.SynqlyClient.Credentials.CreateCredential(ctx, tenant.SynqlyAccountId, &mgmt.CreateCredentialRequest{
		# Name: "Inmem Login",
        #     Config: mgmt.NewCredentialConfigFromToken(&mgmt.TokenCredential{
        #         Secret: "in-mem-sample-cred",
        #     }),
        # })
        # if err != nil {
        #     return err
        # }

class Tenant:
    def __init__(self, synqly_account_id, synqly_management_client, synqly_event_logger):
        self.id = id
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

    app.new_tenant("Tenant ABC")
    print("Tenant ABC created")

    app.new_tenant("Tenant XYZ")
    print ("Tenant XYZ created")

    app.configure_event_logging("Tenant ABC")

main()