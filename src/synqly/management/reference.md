# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">list</a>(...) -> ListAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Account` objects. For more information on
Organizations and Accounts, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.accounts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Account` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Account` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[bool]` — Return total number of accounts in the system, respecting all applied filters. This is expensive, use sparingly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">get</a>(...) -> GetAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Account` object matching `{accountId}`. For more information on
Organizations and Accounts, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.accounts.get(
    account_id="accountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">create</a>(...) -> CreateAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Account` object. For more information on Organizations and
Accounts, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.accounts.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateAccountRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">update</a>(...) -> UpdateAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Account` object matching `{accountId}`. For more information on
Organizations and Accounts, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.organization_base import Environment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.accounts.update(
    account_id="accountId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    fullname="fullname",
    organization_id="organization_id",
    environment=Environment.TEST,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateAccountRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">patch</a>(...) -> PatchAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `Account` object matching `{accountId}`. For more information on
Organizations and Accounts, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.accounts.patch(
    account_id="accountId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the `Account` matching `{accountId}`. Deleting an `Account` also deletea
all `Tokens` and `Credentials` belonging to the `Account`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.accounts.delete(
    account_id="accountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Audit
<details><summary><code>client.audit.<a href="src/synqly/audit/client.py">list</a>(...) -> ListAuditEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all Synqly `Audit` events for the `Organization`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.audit.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Audit` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Audit` objects starting after this `created_at`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order defaults to created_at[asc] and can changed to descending order by specifying created_at[desc].
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">logon</a>(...) -> LogonResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates a new session for the given member in specified Synqly organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.logon(
    organization_id="organizationId",
    name="name",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LogonRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">change_password</a>(...) -> ChangePasswordResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change member password.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.change_password(
    old_secret="old_secret",
    new_secret="new_secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ChangePasswordRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">logoff</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminates the session identified by the given logon token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.logoff()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">create_sso</a>(...) -> CreateSsoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure an identity provider for Single Sign-On (SSO) with the organization.
Returns the created resource with its assigned SSO configuration ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.auth import CreateSsoConfiguration_Oidc

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.create_sso(
    fullname="fullname",
    config=CreateSsoConfiguration_Oidc(
        issuer_url="issuer_url",
        client_id="client_id",
        client_secret="client_secret",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateSsoRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">list_sso</a>() -> ListSsoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all Single Sign-On (SSO) configurations for the organization.
Client secrets are not included.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.list_sso()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">get_sso</a>(...) -> GetSsoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific Single Sign-On (SSO) configuration. Client
secrets are not included.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.get_sso(
    sso_id="ssoId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sso_id:** `SsoConfigurationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">get_sso_metadata</a>() -> GetSsoMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns configuration that must be used when configuring Identity
Providers, such as the OIDC redirect URI or SAML ACS URL and SP
entity ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.get_sso_metadata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">update_sso</a>(...) -> UpdateSsoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the SSO configuration by ID. This is a full replacement of the
configuration. The `updated_at` field is used for optimistic locking
to prevent concurrent updates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.auth import UpdateSsoConfiguration_Oidc

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.update_sso(
    sso_id="ssoId",
    fullname="fullname",
    config=UpdateSsoConfiguration_Oidc(
        issuer_url="issuer_url",
        client_id="client_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sso_id:** `SsoConfigurationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSsoRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">delete_sso</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a specific Single Sign-On (SSO) configuration. This may disable signing on
with the identity provider defined in the configuration, and can result in members
linked to that identity provider no longer being able to access the Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.auth.delete_sso(
    sso_id="ssoId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sso_id:** `SsoConfigurationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Billing
<details><summary><code>client.billing.<a href="src/synqly/billing/client.py">list</a>(...) -> ListBillingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of billing reports. Use a RootOrganization token for multiple organizations. For more information on Organizations and Billings, refer to our [Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.billing.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of billing reports to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return billing reports starting after this `organization_id`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `organization_id`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `organization_id[desc]` will sort the results by `organization_id` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing.<a href="src/synqly/billing/client.py">get</a>(...) -> GetBillingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the billing reports matching `{organizationId} and {month}`. For more information on
Organizations and Billings, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.billing import BillingMonth

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.billing.get(
    organization_id="organizationId",
    month=BillingMonth.PARTIAL,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**month:** `BillingMonth` — Specify month for a previously generated monthly report or 'partial' to generate the current month-to-date partial billing report.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bridges
<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">list</a>(...) -> ListBridgesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Bridge Group` objects that match the query params.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.list(
    account_id="accountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Bridge` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Bridge` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">get</a>(...) -> GetBridgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Bridge Group object matching `{bridgeId}`. For more information on Bridges, refer to the
[Bridge Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.get(
    account_id="accountId",
    bridge_id="bridgeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**bridge_id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">get_status</a>(...) -> GetBridgeStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status and local configuration of running Bridges Agents in the Bridge Group `{bridgeId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.get_status(
    account_id="accountId",
    bridge_id="bridgeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**bridge_id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">create</a>(...) -> CreateBridgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Bridge Group` with a unique identifier and authentication
credentials. This allows for Bridge Agents to connect to Synqly. For
more information on Bridges, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.create(
    account_id="accountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateBridgeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">update</a>(...) -> UpdateBridgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Bridge Group` object matching `{bridgeId}`. For more information on Bridges, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.update(
    account_id="accountId",
    bridge_id="bridgeId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    fullname="fullname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**bridge_id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateBridgeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">patch</a>(...) -> PatchBridgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `Bridge Group` object matching `{bridgeId}`. For more information on Bridges, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.patch(
    account_id="accountId",
    bridge_id="bridgeId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**bridge_id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the `Bridge Group` matching `{bridgeId}`. Deleting an `Bridge Group` also deletea
all `Tokens` and `Credentials` belonging to the `Bridge Group`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.bridges.delete(
    account_id="accountId",
    bridge_id="bridgeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**bridge_id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Capabilities
<details><summary><code>client.capabilities.<a href="src/synqly/capabilities/client.py">list_connectors</a>(...) -> ListConnectorsCapabilitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Connectors`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.capabilities.list_connectors()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expand:** `typing.Optional[typing.Union[ListConnectorCapabilitiesExpandOptions, typing.Sequence[ListConnectorCapabilitiesExpandOptions]]]` 

Expand the capabilities result fields that are otherwise
omitted or returned as references to OpenAPI spec components.
NOTE: This can yield very big response objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.capabilities.<a href="src/synqly/capabilities/client.py">list_providers</a>(...) -> ListProvidersCapabilitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all Provider capabilities and their configurations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.capabilities.list_providers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**expand:** `typing.Optional[typing.Union[ListProviderCapabilitiesExpandOptions, typing.Sequence[ListProviderCapabilitiesExpandOptions]]]` 

Expand the capabilities result fields that are otherwise
omitted or returned as references to OpenAPI spec components.
NOTE: This can yield very big response objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.capabilities.<a href="src/synqly/capabilities/client.py">get_provider</a>(...) -> ProviderCapabilitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the capabilities and configurations for a specific Provider type
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.providers_generated import ProviderConfigId

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.capabilities.get_provider(
    provider_id=ProviderConfigId.APPSEC_AMAZON_INSPECTOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_id:** `ProviderConfigId` 
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Union[GetProviderCapabilitiesExpandOptions, typing.Sequence[GetProviderCapabilitiesExpandOptions]]]` 

Expand the capabilities result fields that are otherwise
omitted or returned as references to OpenAPI spec components.
NOTE: This can yield very big response objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credentials
<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">list</a>(...) -> ListCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Credential` objects belonging to the `Account`, `Integration`, or `IntegrationPoint`, or `OrganizationWebhook` matching
`{ownerId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.list(
    owner_id="ownerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Credential` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Credential` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">get</a>(...) -> GetCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Credential` object matching `{credentialId}` where the
`Credential` belongs to the `Account`, `Integration`, `IntegrationPoint` or `OrganizationWebhook` matching `{ownerId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.get(
    owner_id="ownerId",
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `CredentialId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">lookup</a>(...) -> LookupCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Credential` object matching `{credentialId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.lookup(
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `CredentialId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">create</a>(...) -> CreateCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Credential` object in the `Account`, `IntegrationPoint`, or `OrganizationWebhook` matching matching
`{ownerId}`. A `Credential` may only by used by a single `Account`, `Integration`, `IntegrationPoint` or `OrganizationWebhook`;
however, `Credential` objects can be shared by multiple `Integrations` within an `Account`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.create(
    owner_id="ownerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateCredentialRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">update</a>(...) -> UpdateCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Credential` object matching `{credentialId}`, where the
`Credential` belongs to the `Account`, `Integration`, `IntegrationPoint` or `OrganizationWebhook` matching `{ownerId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.credentials import OwnerType, ManagedType

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.update(
    owner_id="ownerId",
    credential_id="credentialId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    owner_type=OwnerType.ACCOUNT,
    fullname="fullname",
    managed=ManagedType.MANAGED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `CredentialId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateCredentialRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">patch</a>(...) -> PatchCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `Credential` object matching `{credentialId}`, where the
`Credential` belongs to the `Account`, `Integration`, `IntegrationPoint` or `OrganizationWebhook` matching `{ownerId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.patch(
    owner_id="ownerId",
    credential_id="credentialId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `CredentialId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the `Credential` object matching `{credentialId}`, where the
`Credential` belongs to the `Account`, `Integration`, `IntegrationPoint` or `OrganizationWebhook` matching `{ownerId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.credentials.delete(
    owner_id="ownerId",
    credential_id="credentialId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `CredentialId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customs
<details><summary><code>client.customs.<a href="src/synqly/customs/client.py">list</a>(...) -> ListCustomsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Custom` provider objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.customs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of custom provider objects to return in this page. Defaults to 100. Items listed will not include the `data` field.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return custom provider objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[bool]` — Return total number of custom providers in the system, respecting all applied filters. This is expensive, use sparingly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customs.<a href="src/synqly/customs/client.py">get</a>(...) -> GetCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Custom` provider object matching `{customId}`. This response will include the full `data` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.customs.get(
    custom_id="customId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_id:** `CustomId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customs.<a href="src/synqly/customs/client.py">create</a>(...) -> CreateCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an custom provider object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.customs.create(
    data="data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateCustomRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customs.<a href="src/synqly/customs/client.py">update</a>(...) -> UpdateCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the custom provider object matching `{customId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.customs.update(
    custom_id="customId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    fullname="fullname",
    organization_id="organization_id",
    data="data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_id:** `CustomId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateCustomRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customs.<a href="src/synqly/customs/client.py">patch</a>(...) -> PatchCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the custom provider object matching `{customId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.customs.patch(
    custom_id="customId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_id:** `CustomId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customs.<a href="src/synqly/customs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the custom provider object matching `{customId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.customs.delete(
    custom_id="customId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_id:** `CustomId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IntegrationPoints
<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">list</a>(...) -> ListIntegrationPointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `IntegrationPoint` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integration_points.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `IntegrationPoint` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `IntegrationPoint` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[bool]` — Return total number of integration points in the system, respecting all applied filters. This is expensive, use sparingly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">get</a>(...) -> GetIntegrationPointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `IntegrationPoint` object matching `{integrationPointId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integration_points.get(
    integration_point_id="integrationPointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**integration_point_id:** `IntegrationPointId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">create</a>(...) -> CreateIntegrationPointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a `IntegrationPoint` object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.capabilities_base import CategoryId
from synqly.integration_points import IntegrationEnvironments

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integration_points.create(
    connector=CategoryId.APPSEC,
    environments=IntegrationEnvironments(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateIntegrationPointRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">update</a>(...) -> UpdateIntegrationPointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `IntegrationPoint` object matching `{integrationPointId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.capabilities_base import CategoryId
from synqly.integration_points import IntegrationEnvironments

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integration_points.update(
    integration_point_id="integrationPointId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    connector=CategoryId.APPSEC,
    environments=IntegrationEnvironments(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**integration_point_id:** `IntegrationPointId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateIntegrationPointRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">patch</a>(...) -> PatchIntegrationPointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `IntegrationPoint` object matching `{integrationPointId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integration_points.patch(
    integration_point_id="integrationPointId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**integration_point_id:** `IntegrationPointId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the `IntegrationPoint` object matching `{integrationPointId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integration_points.delete(
    integration_point_id="integrationPointId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**integration_point_id:** `IntegrationPointId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations
<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">list</a>(...) -> ListIntegrationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Integration` objects that match the query params.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Integration` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Integration` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Union[ListIntegrationOptions, typing.Sequence[ListIntegrationOptions]]]` — Expand the integration result with the related integration point and/or account information.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[bool]` — Return total number of all integrations in the system, respecting all applied filters. This is expensive, use sparingly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">list_account</a>(...) -> ListAccountIntegrationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Integration` objects belonging to the
`Account` matching `{accountId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.list_account(
    account_id="accountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Integration` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Integration` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Union[ListIntegrationOptions, typing.Sequence[ListIntegrationOptions]]]` — Expand the integration result with the related integration point and/or account information.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[bool]` — Return total number of integrations for a particular account. This is expensive, use sparingly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">get</a>(...) -> GetIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Integration` object matching `{integrationId}` where
the `Integration` belongs to the `Account` matching `{accountId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.get(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">create</a>(...) -> CreateIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Integration` object belonging to the `Account` matching
`{accountId}`. Configures the `Integration` with the Provider specified
in the request. Returns an `Integration` token for use with `Integration` APIs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.providers_generated import ProviderConfig_AppsecAmazonInspector, AwsProviderCredential_Aws, AwsRegion

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.create(
    account_id="accountId",
    provider_config=ProviderConfig_AppsecAmazonInspector(
        credential=AwsProviderCredential_Aws(
            access_key_id="access_key_id",
            secret_access_key="secret_access_key",
        ),
        region=AwsRegion.US_EAST_1,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateIntegrationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">verify</a>(...) -> VerifyIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies an ephemeral `Integration` and provider configuration and tests the authentication and provider connectivity.
The provider config credential IDs can utilize persistent IDs or use "#/n" reference IDs;
where (n) is the zero based offset in the optional credentials list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.integrations import CreateIntegrationRequest
from synqly.providers_generated import ProviderConfig_AppsecAmazonInspector, AwsProviderCredential_Aws, AwsRegion

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.verify(
    account_id="accountId",
    integration=CreateIntegrationRequest(
        provider_config=ProviderConfig_AppsecAmazonInspector(
            credential=AwsProviderCredential_Aws(
                access_key_id="access_key_id",
                secret_access_key="secret_access_key",
            ),
            region=AwsRegion.US_EAST_1,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `VerifyIntegrationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">verify_existing</a>(...) -> VerifyIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies the `Integration` matching `{integrationId}` and tests authentication
and provider connectivity.

When called without a request body, the stored integration configuration is
verified. When a request body is provided, it uses the same shape as the
Update Integration API; the integration is verified as if that update were
applied, without persisting changes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.verify_existing(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[UpdateIntegrationRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">update</a>(...) -> UpdateIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Integration` object matching `{integrationId}`, where the
`Integration` belongs to the `Account` matching `{accountId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.capabilities_base import CategoryId
from synqly.providers_generated import ProviderConfig_AppsecAmazonInspector, AwsProviderCredential_Aws, AwsRegion

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.update(
    account_id_="accountId",
    integration_id="integrationId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    fullname="fullname",
    refresh_token_id="refresh_token_id",
    account_id="account_id",
    category=CategoryId.APPSEC,
    provider_config=ProviderConfig_AppsecAmazonInspector(
        credential=AwsProviderCredential_Aws(
            access_key_id="access_key_id",
            secret_access_key="secret_access_key",
        ),
        region=AwsRegion.US_EAST_1,
    ),
    provider_fullname="provider_fullname",
    provider_type="provider_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateIntegrationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">patch</a>(...) -> PatchIntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `Integration` object matching `{integrationId}`, where the
`Integration` belongs to the `Account` matching `{accountId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.patch(
    account_id="accountId",
    integration_id="integrationId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the `Integration` object matching `{integrationId}, where the
`Integration` belongs to the `Account` matching `{accountId}`. Deleting
an `Integration` also deletes any tokens that belong to it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.integrations.delete(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mappings
<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">list</a>(...) -> ListMappingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Mapping` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of mapping objects to return in this page. Defaults to 100. Items listed will not include the `data` field.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return mapping objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[bool]` — Return total number of mappings in the system, respecting all applied filters. This is expensive, use sparingly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">get</a>(...) -> GetMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Mapping` object matching `{mappingId}`. This response will include the full `data` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.get(
    mapping_id="mappingId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mapping_id:** `MappingId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">create</a>(...) -> CreateMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an mapping object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.create(
    data="data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMappingRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">update</a>(...) -> UpdateMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the mapping object matching `{mappingId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.update(
    mapping_id="mappingId",
    id="id",
    fullname="fullname",
    organization_id="organization_id",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    data="data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mapping_id:** `MappingId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateMappingRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">patch</a>(...) -> PatchMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the mapping object matching `{mappingId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.patch(
    mapping_id="mappingId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mapping_id:** `MappingId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the mapping object matching `{mappingId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.delete(
    mapping_id="mappingId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mapping_id:** `MappingId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">apply</a>(...) -> ApplyMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a list of mapping transforms against the JSON input.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.mappings.apply(
    mappings=[
        "mappings",
        "mappings"
    ],
    data={
        "data": {"key": "value"}
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ApplyMappingRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the input in the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Members
<details><summary><code>client.members.<a href="src/synqly/members/client.py">list</a>(...) -> ListMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all members
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.members.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Member` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Member` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.members.<a href="src/synqly/members/client.py">get</a>(...) -> GetMemberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a Member by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.members.get(
    member_id="memberId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.members.<a href="src/synqly/members/client.py">create</a>(...) -> CreateMemberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new member for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.members.create(
    name="name",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMemberRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.members.<a href="src/synqly/members/client.py">update</a>(...) -> UpdateMemberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Member by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.member_base import State, MemberType

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.members.update(
    member_id="memberId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    state=State.DISABLED,
    last_logon=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    fullname="fullname",
    ttl="ttl",
    token_ttl="token_ttl",
    expires=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    pin_expires=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    role_binding=[
        "role_binding",
        "role_binding"
    ],
    type=MemberType.PERSONAL,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateMemberRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.members.<a href="src/synqly/members/client.py">patch</a>(...) -> PatchMemberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Member by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.members.patch(
    member_id="memberId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.members.<a href="src/synqly/members/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Member by ID. Also deletes all Tokens for the Member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.members.delete(
    member_id="memberId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**member_id:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Meta
<details><summary><code>client.meta.<a href="src/synqly/meta/client.py">management_openapi_spec</a>() -> GetOpenApiSpecResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the OpenAPI spec for the Management API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.meta.management_openapi_spec()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.meta.<a href="src/synqly/meta/client.py">engine_openapi_spec</a>() -> GetOpenApiSpecResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the OpenAPI spec for the Engine APIs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.meta.engine_openapi_spec()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Operations
<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">list</a>(...) -> ListOperationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Asynchronous Operations` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.operations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Asynchronous Operations` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Asynchronous Operations` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `id`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field id. For example, `id[desc]` will sort the results by `id` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">list_execution_history</a>(...) -> ListExecutionHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the execution history for all operations.
History is stored for the configured retention period (default 4 weeks).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.operations.list_execution_history()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter operation execution history by this query.
Available filters:
- `id[eq]` - Filter by specific operation ID
- `integration_id[eq]` - Filter by specific integration ID
- `account_id[eq]` - Filter by specific account ID
- `execution_id[eq]` - Filter by specific execution ID
- `started_at[gte]` - Filter executions started at or after a specific datetime (RFC3339 format)
- `started_at[lte]` - Filter executions started at or before a specific datetime (RFC3339 format)
- `started_at[gt]` - Filter executions started after a specific datetime
- `started_at[lt]` - Filter executions started before a specific datetime
- `operation_id[eq]` - Filter by operation name (e.g., "assets_query_devices")
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `started_at[desc]`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field id. For example, `started_at[asc]` will sort the results by `started_at` in ascending order.
The ordering defaults to `desc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return (default 100, max 500)
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return execution history starting after this cursor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrganizationWebhooks
<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">list</a>(...) -> ListOrganizationWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List webhooks for the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization_webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Webhook` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Webhook` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">get</a>(...) -> GetOrganizationWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Webhook` object matching `{webhookId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization_webhooks.get(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">create</a>(...) -> CreateOrganizationWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook for the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.organization_webhook_base import WebhookFilter
from synqly.organization_webhooks import OrganizationWebhookSecret

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization_webhooks.create(
    filters=[
        WebhookFilter.ALL,
        WebhookFilter.ALL
    ],
    url="url",
    secret=OrganizationWebhookSecret(
        value="value",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateOrganizationWebhookRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">update</a>(...) -> UpdateOrganizationWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Webhook` object matching `{webhookId}`. For more information on
Organizations and Webhooks, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.organization_base import Environment
from synqly.organization_webhook_base import WebhookFilter

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization_webhooks.update(
    webhook_id="webhookId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    fullname="fullname",
    environment=Environment.TEST,
    filters=[
        WebhookFilter.ALL,
        WebhookFilter.ALL
    ],
    url="url",
    credential_id="credential_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateOrganizationWebhookRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">patch</a>(...) -> PatchOrganizationWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `Webhook` object matching `{webhookId}`. For more information on
Organizations and Webhooks, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization_webhooks.patch(
    webhook_id="webhookId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook for the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization_webhooks.delete(
    webhook_id="webhookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization
<details><summary><code>client.organization.<a href="src/synqly/organization/client.py">get</a>() -> GetOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/synqly/organization/client.py">update</a>(...) -> UpdateOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.organization_base import OrganizationType

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization.update(
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    refresh_token_id="refresh_token_id",
    organization_type=OrganizationType.ROOT,
    fullname="fullname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateOrganizationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/synqly/organization/client.py">patch</a>(...) -> PatchOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patch Organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.organization.patch(
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissionset
<details><summary><code>client.permissionset.<a href="src/synqly/permissionset/client.py">list</a>() -> ListPermissionSetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `PermissionSets` objects that match the query params.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.permissionset.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissionset.<a href="src/synqly/permissionset/client.py">get</a>(...) -> GetPermissionSetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `PermissionSet` object matching `{permissionsetId}`. For more information on PermissionSets, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.permissionset_base import Permissions

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.permissionset.get(
    permissionset_id=Permissions.ADMINISTRATOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**permissionset_id:** `Permissions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">list</a>(...) -> ListRolesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `Roles` objects that match the query params.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.roles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Role` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Role` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">get</a>(...) -> GetRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Role` object matching `{roleId}`. For more information on Roles, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.roles.get(
    role_id="roleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">create</a>(...) -> CreateRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Role` object. For more information on Roles, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.permissionset_base import Permissions

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.roles.create(
    permission_set=Permissions.ADMINISTRATOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateRoleRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">update</a>(...) -> UpdateRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Role` object matching `{roleId}`. For more information on Roles, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
import datetime
from synqly.permissionset_base import Permissions

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.roles.update(
    role_id="roleId",
    name="name",
    created_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    updated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    id="id",
    fullname="fullname",
    permission_set=Permissions.ADMINISTRATOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateRoleRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">patch</a>(...) -> PatchRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches the `Role` object matching `{roleId}`. For more information on Roles, refer to our
[Synqly Overview](https://docs.synqly.com/docs/synqly-overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.roles.patch(
    role_id="roleId",
    request=[
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        ),
        PatchOperation(
            op=PatchOp.ADD,
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the `Role` matching `{roleId}`. Deleting an `Role` also deletea
all `Tokens` and `Credentials` belonging to the `Role`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.roles.delete(
    role_id="roleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Status
<details><summary><code>client.status.<a href="src/synqly/status/client.py">list</a>(...) -> ListStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all matching `Status` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.status.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Status` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Status` objects starting after this `account_id,integration_id`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `account_id,integration_id`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Union[ListStatusOptions, typing.Sequence[ListStatusOptions]]]` — Expand the status result with the related integration and/or account information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status.<a href="src/synqly/status/client.py">get</a>(...) -> GetStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the integration `Status` object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.status.get(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status.<a href="src/synqly/status/client.py">reset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets the integration `Status` object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.status.reset(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status.<a href="src/synqly/status/client.py">list_events</a>(...) -> ListStatusEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns integration `Status` object list of `StatusEvent` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.status.list_events(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `StatusEvent` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `StatusEvent` objects starting after this `created_at`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order defaults to created_at[asc] and can changed to descending order by specifying created_at[desc].
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status.<a href="src/synqly/status/client.py">get_timeseries</a>() -> GetStatusTimeseries</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns organization last hour usage timeseries.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.status.get_timeseries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status.<a href="src/synqly/status/client.py">get_integration_timeseries</a>(...) -> GetIntegrationTimeseries</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns organization last hour usage timeseries.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.status.get_integration_timeseries(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[str]` — [hour] provide most recent 24 hour timeseries. default: hour
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SubOrgs
<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">list</a>() -> ListOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all organizations
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.sub_orgs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">get</a>(...) -> GetOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an Organization by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.sub_orgs.get(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">create</a>(...) -> CreateOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.sub_orgs.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateOrganizationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Organization by ID. Also deletes
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.sub_orgs.delete(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tokens
<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_token</a>(...) -> CreateTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an adhoc organization token restricted to specified resources and permission set.
Tokens can only be reduced in scope, never expanded.
Permissions are inherited from the token used to call this API.
Permissions assigned to the new token will not be persisted, this is not a way to create roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.role_base import Resources
from synqly.permissionset_base import Permissions

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.create_token(
    resources=Resources(),
    permission_set=Permissions.ADMINISTRATOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateTokenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_mcp_token</a>(...) -> CreateMcpTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a token for MCP authentication. This token is soley for MCP authentication and cannot
authenticate with any other API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment
from synqly.tokens import McpTokenScope_Management

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.create_mcp_token(
    scope=McpTokenScope_Management(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMcpTokenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_integration_token</a>(...) -> CreateIntegrationTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an adhoc integration token restricted to a single integration. The token used to call
this API must have the necessary permissions to create tokens and have access to the account
and integration IDs. Permissions may not be escalated, so any operation that the invocation
token does not have access to cannot be granted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.create_integration_token(
    account_id="accountId",
    integration_id="integrationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateIntegrationTokenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_synqly_integrations_token</a>(...) -> CreateSynqlyIntegrationsTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a token for managing Synqly-specific integrations. This token can be used with the integration APIs to manage
integrations for Synqly-specific integrations, such as status events exports and async operations. See the
[Synqly Integrations](https://docs.synqly.com/guides/synqly-integrations) documentation for more information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.create_synqly_integrations_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateSynqlyIntegrationsTokenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the Refresh Token with id `{id}`. This immediately
invalidates both the primary and secondary token pairs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.delete(
    refresh_token_id="refreshTokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refresh_token_id:** `TokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">list</a>(...) -> ListTokensResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all `RefreshToken` objects belonging to the Authorization Bearer
token. For more infromation on Tokens, refer to
[Authentication](/api-reference/authentication).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Token` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**start_after:** `typing.Optional[str]` — Return `Token` objects starting after this `name`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/getting-started/management-api-filtering). Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">get</a>(...) -> GetTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `RefreshToken` object matching `{tokenId}`. For more information on
Tokens, refer to
[Authentication](/api-reference/authentication).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.get(
    refresh_token_id="refreshTokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refresh_token_id:** `TokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">reset</a>(...) -> ResetTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API can be used to reset `Organization` or `Integration` `RefreshTokens`.
Resets the specified `RefreshToken` and expiration time, removes the secondary, and resets access and refresh tokens for the
`RefreshToken` object matching `{ownerId}/{refreshTokenId}` where `ownerId` is an `organizationId` or `integrationId`.
An `Organization` token with `administrator` permissions can be used to perform this operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.reset(
    owner_id="ownerId",
    refresh_token_id="refreshTokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token_id:** `TokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">rotate</a>(...) -> RotateTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API can be used to rotate an `Organization` or `Integration` `RefreshTokens`.
Rotate deletes the existing `Secondary` TokenPair, moves the `Primary` TokenPair to the `Secondary` TokenPair and creates a new `Primary` TokenPair for the
`RefreshToken` object matching `{ownerId}/{refreshTokenId}` where `ownerId` is an `organizationId` or `integrationId`.
An `Organization` token with `administrator` permissions can be used to perform this operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.rotate(
    owner_id="ownerId",
    refresh_token_id="refreshTokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token_id:** `TokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">refresh</a>(...) -> RefreshTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new primary `TokenPair` object, setting the secondary `TokenPair`
to the previous primary value. Call `/v1/removeSecondaryToken` to remove
this secondary backup once the new primary `TokenPair` has been deployed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.refresh(
    refresh_token_id="refreshTokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refresh_token_id:** `TokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">remove_secondary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the secondary `TokenPair` for the `RefreshToken` object
matching `{refreshTokenId}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly import SynqlyManagement
from synqly.environment import SynqlyManagementEnvironment

client = SynqlyManagement(
    token="<token>",
    environment=SynqlyManagementEnvironment.SYNQLY,
)

client.tokens.remove_secondary(
    refresh_token_id="refreshTokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refresh_token_id:** `TokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

