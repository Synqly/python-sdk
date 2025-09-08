# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.accounts.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
    total=True,
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.accounts.get(
    account_id="string",
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

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">create</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.accounts.create(
    name="string",
    fullname="string",
    environment="test",
    labels=["string"],
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

**name:** `typing.Optional[str]` — Unique short name for this Account (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to AccountId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Account, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[Environment]` — Environment this account runs in. Defaults to `prod` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — User defined labels that apply to this account. These values can be used in role bindings to limit the scope of permissions.
    
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

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.accounts.update(
    account_id="string",
    id="string",
    fullname="string",
    organization_id="string",
    environment="test",
    labels=["string"],
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Human friendly display name for this account.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `OrganizationId` — Organization that manages this Account.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `Environment` — Environment this account runs in.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — User defined labels that apply to this account. These values can be used in role bindings to limit the scope of permissions.
    
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

<details><summary><code>client.accounts.<a href="src/synqly/accounts/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.accounts.patch(
    account_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.accounts.delete(
    account_id="string",
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
<details><summary><code>client.audit.<a href="src/synqly/audit/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.audit.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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
<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">logon</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.auth.logon(
    organization_id="string",
    name="string",
    secret="string",
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

**name:** `str` — Email address identifying the member to initiate a session for.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — Password of the member to initiate a session for.
    
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

<details><summary><code>client.auth.<a href="src/synqly/auth/client.py">change_password</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.auth.change_password(
    old_secret="string",
    new_secret="string",
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

**old_secret:** `str` — Old member secret
    
</dd>
</dl>

<dl>
<dd>

**new_secret:** `str` — New member secret
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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

## Bridges
<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.list(
    account_id="string",
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.get(
    account_id="string",
    bridge_id="string",
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

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">get_status</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.get_status(
    account_id="string",
    bridge_id="string",
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

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">create</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.create(
    account_id="string",
    name="string",
    fullname="string",
    description="string",
    labels=["string"],
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

**name:** `typing.Optional[str]` — Unique short name for this Bridge (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to BridgeGroupId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Bridge, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the resources included in the bridge and permissions granted on those resources. Includes details of when to use this bridge along with the intended personas.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Bridge selection labels
    
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

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.update(
    account_id="string",
    bridge_id="string",
    id="string",
    fullname="string",
    description="string",
    labels=[],
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**bridge_id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `BridgeGroupId` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Full name of bridge
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the resources included in the bridge and permissions granted on those resources. Includes details of when to use this bridge along with the intended personas.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Labels applied to Bridges within the group. These labels can be used by integrations to select the groups of bridges capable of handling requests to the integration.
    
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

<details><summary><code>client.bridges.<a href="src/synqly/bridges/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.patch(
    account_id="string",
    bridge_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.bridges.delete(
    account_id="string",
    bridge_id="string",
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
<details><summary><code>client.capabilities.<a href="src/synqly/capabilities/client.py">list_connectors</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.capabilities.list_connectors(
    expand="providers",
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

**expand:** `typing.Optional[
    typing.Union[
        ListConnectorCapabilitiesExpandOptions,
        typing.Sequence[ListConnectorCapabilitiesExpandOptions],
    ]
]` 

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

<details><summary><code>client.capabilities.<a href="src/synqly/capabilities/client.py">list_providers</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.capabilities.list_providers(
    expand="connector",
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

**expand:** `typing.Optional[
    typing.Union[
        ListProviderCapabilitiesExpandOptions,
        typing.Sequence[ListProviderCapabilitiesExpandOptions],
    ]
]` 

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

<details><summary><code>client.capabilities.<a href="src/synqly/capabilities/client.py">get_provider</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.capabilities.get_provider(
    provider_id="appsec_hcl_appscan_on_cloud",
    expand="connector",
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

**expand:** `typing.Optional[
    typing.Union[
        GetProviderCapabilitiesExpandOptions,
        typing.Sequence[GetProviderCapabilitiesExpandOptions],
    ]
]` 

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
<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.list(
    owner_id="string",
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.get(
    owner_id="string",
    credential_id="string",
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

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">lookup</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.lookup(
    credential_id="string",
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

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">create</a>(...)</code></summary>
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
import datetime

from synqly import CredentialConfig_Aws
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.create(
    owner_id="string",
    name="string",
    fullname="string",
    config=CredentialConfig_Aws(
        access_key_id="string",
        secret_access_key="string",
        session="string",
    ),
    owner_type="account",
    expires=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**owner_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique short name for this Credential (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to CredentialId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Credential, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[CredentialConfig]` — Credential configuration
    
</dd>
</dl>

<dl>
<dd>

**owner_type:** `typing.Optional[OwnerType]` — One of `account` or `integration_point`; defaults to `account` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**expires:** `typing.Optional[dt.datetime]` — Time when this credential expires and can no longer be used again.
    
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

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly import CredentialConfig_Aws
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.update(
    owner_id="string",
    credential_id="string",
    id="string",
    account_id="string",
    integration_id="string",
    integration_point_id="string",
    organization_webhook_id="string",
    owner_type="account",
    fullname="string",
    config=CredentialConfig_Aws(),
    expires=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    managed="Managed",
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**id:** `CredentialId` 
    
</dd>
</dl>

<dl>
<dd>

**owner_type:** `OwnerType` — One of `account` or `integration_point`.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Human friendly display name for this Credential
    
</dd>
</dl>

<dl>
<dd>

**managed:** `ManagedType` — Field is set by the management process. Determines lifecycle and ownership of the credential.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[AccountId]` — Account that manages this credential.
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `typing.Optional[IntegrationId]` — Integration associated with this credential.
    
</dd>
</dl>

<dl>
<dd>

**integration_point_id:** `typing.Optional[IntegrationPointId]` — Integration Point associated with this credential.
    
</dd>
</dl>

<dl>
<dd>

**organization_webhook_id:** `typing.Optional[WebhookId]` — Organization Webhook associated with this credential.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[CredentialConfig]` — Credential configuration
    
</dd>
</dl>

<dl>
<dd>

**expires:** `typing.Optional[dt.datetime]` — Time when this credential expires and can no longer be used again.
    
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

<details><summary><code>client.credentials.<a href="src/synqly/credentials/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.patch(
    owner_id="string",
    credential_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.credentials.delete(
    owner_id="string",
    credential_id="string",
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

## IntegrationPoints
<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integration_points.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
    total=True,
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integration_points.get(
    integration_point_id="string",
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

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">create</a>(...)</code></summary>
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
from synqly import (
    AdditionalMappingTemplate,
    IntegrationEnvironments,
    MappingChainTemplate,
)
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integration_points.create(
    name="string",
    fullname="string",
    description="string",
    connector="appsec",
    environments=IntegrationEnvironments(),
    mappings=[
        MappingChainTemplate(
            providers=["appsec_hcl_appscan_on_cloud"],
            mappings=["string"],
            operation_ids=["string"],
        )
    ],
    additional_mappings=[
        AdditionalMappingTemplate(
            providers=["appsec_hcl_appscan_on_cloud"],
            mapping_type="recommended",
            resource="alerts",
            actions=["query"],
            source="string",
            destination="string",
            literal=True,
            data_type="string",
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

**connector:** `CategoryId` — Connector to use for the Integration Point.
    
</dd>
</dl>

<dl>
<dd>

**environments:** `IntegrationEnvironments` — Selects providers to use for account environments.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique short name for this Integration Point (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to IntegrationPointId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Name of integration point, will be shown to end-users in the Connect UI. Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the Integration Point. Will not be displayed to end-users of Connect UI.
    
</dd>
</dl>

<dl>
<dd>

**mappings:** `typing.Optional[typing.Sequence[MappingChainTemplate]]` — A list of mapping chains to apply to integrations using this integration point. Each mapping chain is a list of mappings to apply to the integration in the order they should be applied. Mappings are applied by operation ID. If an integration is created that declares its own mappings for an operation, they will override this list of mappings. Leave this empty to use the default default mappings.
    
</dd>
</dl>

<dl>
<dd>

**additional_mappings:** `typing.Optional[typing.Sequence[AdditionalMappingTemplate]]` — Additional data mappings for integrations added to this integration point. This allows for custom data to be mapped to the custom_fields portion of the response.
    
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

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly import IntegrationEnvironments
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integration_points.update(
    integration_point_id="string",
    id="string",
    connector="appsec",
    environments=IntegrationEnvironments(),
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**integration_point_id:** `IntegrationPointId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `IntegrationPointId` 
    
</dd>
</dl>

<dl>
<dd>

**connector:** `CategoryId` — Connector to use for the Integration Point.
    
</dd>
</dl>

<dl>
<dd>

**environments:** `IntegrationEnvironments` — Selects providers to use for account environments.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Name of integration point, will be shown to end-users in the Connect UI.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the Integration Point. Will not be displayed to end-users of Connect UI.
    
</dd>
</dl>

<dl>
<dd>

**mappings:** `typing.Optional[typing.Sequence[MappingChainTemplate]]` — A list of mapping chains to apply to integrations using this integration point. Each mapping chain is a list of mappings to apply to the integration in the order they should be applied. Mappings are applied by operation ID. If an integration is created that declares its own mappings for an operation, they will override this list of mappings. Leave this empty to use the default default mappings.
    
</dd>
</dl>

<dl>
<dd>

**additional_mappings:** `typing.Optional[typing.Sequence[AdditionalMappingTemplate]]` — Additional data mappings for integrations added to this integration point. This allows for custom data to be mapped to the custom_fields portion of the response.
    
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

<details><summary><code>client.integration_points.<a href="src/synqly/integration_points/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integration_points.patch(
    integration_point_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integration_points.delete(
    integration_point_id="string",
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
<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
    expand="account",
    total=True,
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        ListIntegrationOptions, typing.Sequence[ListIntegrationOptions]
    ]
]` — Expand the integration result with the related integration point and/or account information.
    
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

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">list_account</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.list_account(
    account_id="string",
    limit=1,
    start_after="string",
    order="string",
    filter="string",
    expand="account",
    total=True,
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        ListIntegrationOptions, typing.Sequence[ListIntegrationOptions]
    ]
]` — Expand the integration result with the related integration point and/or account information.
    
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

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.get(
    account_id="string",
    integration_id="string",
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

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">create</a>(...)</code></summary>
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
from synqly import (
    AdditionalMapping,
    BridgeSelector_Id,
    MappingChain,
    ProviderConfig_AppsecHclAppscanOnCloud,
    WebhookConfig,
)
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.create(
    account_id="string",
    name="string",
    fullname="string",
    provider_config=ProviderConfig_AppsecHclAppscanOnCloud(),
    integration_point_id="string",
    bridge_selector=BridgeSelector_Id(value="string"),
    webhook_config=WebhookConfig(
        items=[],
    ),
    mappings=[
        MappingChain(
            mappings=["string"],
            operation_ids=["string"],
        )
    ],
    additional_mappings=[
        AdditionalMapping(
            resource="alerts",
            actions=["query"],
            source="string",
            destination="string",
            literal=True,
            data_type="string",
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

**provider_config:** `ProviderConfig` — Provider configuration for this Integration.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique short name for this Integrations (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to IntegrationId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Integrations, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**integration_point_id:** `typing.Optional[IntegrationPointId]` — Integration Point associated with this integration.
    
</dd>
</dl>

<dl>
<dd>

**bridge_selector:** `typing.Optional[BridgeSelector]` — Use a Bridge to connect to the provider.
    
</dd>
</dl>

<dl>
<dd>

**webhook_config:** `typing.Optional[WebhookConfig]` — Web hook config for this integration
    
</dd>
</dl>

<dl>
<dd>

**mappings:** `typing.Optional[typing.Sequence[MappingChain]]` — A list of mapping chains to apply to the integration. Each mapping chain is a list of mappings to apply to the integration in the order they should be applied. Mappings are applied by operation ID. Leave this empty to use the default default mappings.
    
</dd>
</dl>

<dl>
<dd>

**additional_mappings:** `typing.Optional[typing.Sequence[AdditionalMapping]]` — Additional data mappings for this integration. This allows for custom data to be mapped to the custom_fields portion of the response.
    
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

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">verify</a>(...)</code></summary>
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
from synqly import (
    AdditionalMapping,
    BridgeSelector_Id,
    CreateIntegrationRequest,
    MappingChain,
    ProviderConfig_AppsecHclAppscanOnCloud,
    WebhookConfig,
)
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.verify(
    account_id="string",
    integration=CreateIntegrationRequest(
        name="string",
        fullname="string",
        provider_config=ProviderConfig_AppsecHclAppscanOnCloud(),
        integration_point_id="string",
        bridge_selector=BridgeSelector_Id(value="string"),
        webhook_config=WebhookConfig(
            items=[],
        ),
        mappings=[
            MappingChain(
                mappings=["string"],
                operation_ids=["string"],
            )
        ],
        additional_mappings=[
            AdditionalMapping(
                resource="alerts",
                actions=["query"],
                source="string",
                destination="string",
                literal=True,
                data_type="string",
            )
        ],
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

**integration:** `CreateIntegrationRequest` 
    
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

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly import (
    Account,
    BridgeSelector_Id,
    IntegrationEnvironments,
    IntegrationPoint,
    ProviderConfig_AppsecHclAppscanOnCloud,
    WebhookConfig,
)
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.update(
    account_id_="string",
    integration_id="string",
    id="string",
    fullname="string",
    refresh_token_id="string",
    account_id="string",
    account=Account(
        id="string",
        fullname="string",
        organization_id="string",
        environment="test",
        labels=["string"],
        name="string",
        created_at=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
    ),
    category="appsec",
    provider_config=ProviderConfig_AppsecHclAppscanOnCloud(),
    provider_fullname="string",
    provider_type="string",
    integration_point_id="string",
    integration_point=IntegrationPoint(
        id="string",
        connector="appsec",
        environments=IntegrationEnvironments(),
        name="string",
        created_at=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
    ),
    bridge_selector=BridgeSelector_Id(value={"key": "value"}),
    webhook_config=WebhookConfig(
        items=[],
    ),
    mappings=[],
    additional_mappings=[],
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**account_id_:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `IntegrationId` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Human friendly display name for this integration.
    
</dd>
</dl>

<dl>
<dd>

**refresh_token_id:** `TokenId` — Integration refresh token id
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `AccountId` — Account associated with this integration. Use the expand=accounts parameter with the List and ListAccount APIs to expand the Account to the full object
    
</dd>
</dl>

<dl>
<dd>

**category:** `CategoryId` — Id of the Connector Category for this Integration.
    
</dd>
</dl>

<dl>
<dd>

**provider_config:** `ProviderConfig` — Provider configuration for this Integration.
    
</dd>
</dl>

<dl>
<dd>

**provider_fullname:** `str` — Human friendly display name for the provider.
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `str` — Type of the provider for this Integration.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[Account]` — When using the expand option on the List or ListAccount APIs, the full account object is included in the response
    
</dd>
</dl>

<dl>
<dd>

**integration_point_id:** `typing.Optional[IntegrationPointId]` — Integration Point associated with this integration. Use the expand=integration_points parameter with the List and ListAccount APIs to expand the Integration Point to the full object
    
</dd>
</dl>

<dl>
<dd>

**integration_point:** `typing.Optional[IntegrationPoint]` — When using the expand option on the List or ListAccount APIs, the full integration_point object is included in the response
    
</dd>
</dl>

<dl>
<dd>

**bridge_selector:** `typing.Optional[BridgeSelector]` — Use a Bridge to connect to the provider.
    
</dd>
</dl>

<dl>
<dd>

**webhook_config:** `typing.Optional[WebhookConfig]` — Webhook configuration for this integration. Some providers support webhooks, and will allow end users providers to send events to a server for new or updated data.
    
</dd>
</dl>

<dl>
<dd>

**mappings:** `typing.Optional[typing.Sequence[MappingChain]]` — A list of mapping chains to apply to the integration. Each mapping chain is a list of mappings to apply to the integration in the order they should be applied. Mappings are applied by operation ID. Leave this empty to use the default default mappings.
    
</dd>
</dl>

<dl>
<dd>

**additional_mappings:** `typing.Optional[typing.Sequence[AdditionalMapping]]` — Additional data mappings for this integration. This allows for custom data to be mapped to the custom_fields portion of the response.
    
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

<details><summary><code>client.integrations.<a href="src/synqly/integrations/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.patch(
    account_id="string",
    integration_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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

Deletes the `Integration` object matching `{integrationId}, where the `Integration`belongs to the`Account`matching`{accountId}`. Deleting an `Integration` also deletes any tokens that belong to it.
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.integrations.delete(
    account_id="string",
    integration_id="string",
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
<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
    total=True,
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.get(
    mapping_id="string",
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

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">create</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.create(
    name="string",
    fullname="string",
    data="string",
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

**data:** `str` — transform to apply.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique short name for this Mapping (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to MappingId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Mapping, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
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

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.update(
    mapping_id="string",
    data="string",
    id="string",
    fullname="string",
    organization_id="string",
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**mapping_id:** `MappingId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `str` — transform to apply.
    
</dd>
</dl>

<dl>
<dd>

**id:** `MappingId` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Human friendly display name for this mapping.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `OrganizationId` — Organization that manages this Mapping.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
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

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.patch(
    mapping_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.delete(
    mapping_id="string",
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

<details><summary><code>client.mappings.<a href="src/synqly/mappings/client.py">apply</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.mappings.apply(
    mappings=["string"],
    data={"string": {"key": "value"}},
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

**mappings:** `typing.Sequence[str]` — List of mappings to utilize. This can include custom mappings you have defined as well as Synqly built-in mappings.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, typing.Any]` — JSON input data to apply the mapping chain to.
    
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
<details><summary><code>client.members.<a href="src/synqly/members/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.members.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.members.<a href="src/synqly/members/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.members.get(
    member_id="string",
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

<details><summary><code>client.members.<a href="src/synqly/members/client.py">create</a>(...)</code></summary>
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
from synqly import MemberOptions
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.members.create(
    name="string",
    fullname="string",
    nickname="string",
    picture="string",
    secret="string",
    role_binding=["string"],
    options=MemberOptions(
        ttl="string",
        options=["disabled"],
        token_ttl="string",
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

**name:** `str` — Email name to use for this Member. Also used for duplicate detection and default sort order.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — Member secret used to logon. Must be at least 8 characters long and fewer than 72 characters. There are no restrictions on the characters used; however, the secret must be sufficiently complex. It cannot be a common word, previously leaked password, or easily guessed sequences like `qwerty` or `12345`.
    
</dd>
</dl>

<dl>
<dd>

**options:** `MemberOptions` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — User's full display name. Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — User's nickname
    
</dd>
</dl>

<dl>
<dd>

**picture:** `typing.Optional[str]` — Url of user's picture
    
</dd>
</dl>

<dl>
<dd>

**role_binding:** `typing.Optional[typing.Sequence[RoleName]]` — Roles granted to this member. Tokens inherit this access. Defaults to `member`.
    
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

<details><summary><code>client.members.<a href="src/synqly/members/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.members.update(
    member_id="string",
    id="string",
    state="disabled",
    last_logon=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    fullname="string",
    nickname="string",
    picture="string",
    ttl="string",
    token_ttl="string",
    expires=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    pin_expires=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    role_binding=["string"],
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**member_id:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `MemberId` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `State` 
    
</dd>
</dl>

<dl>
<dd>

**last_logon:** `dt.datetime` — Last logon time
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — User's full display name.
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**token_ttl:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**pin_expires:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**role_binding:** `typing.Sequence[RoleName]` — Roles granted to this member. Tokens inherit this access.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — User's nickname
    
</dd>
</dl>

<dl>
<dd>

**picture:** `typing.Optional[str]` — Url of user's picture
    
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

<details><summary><code>client.members.<a href="src/synqly/members/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.members.patch(
    member_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.members.delete(
    member_id="string",
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
<details><summary><code>client.meta.<a href="src/synqly/meta/client.py">management_openapi_spec</a>()</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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

<details><summary><code>client.meta.<a href="src/synqly/meta/client.py">engine_openapi_spec</a>()</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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
<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.operations.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

## OrganizationWebhooks
<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization_webhooks.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization_webhooks.get(
    webhook_id="string",
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

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">create</a>(...)</code></summary>
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
import datetime

from synqly import OrganizationWebhookSecret
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization_webhooks.create(
    name="string",
    fullname="string",
    environment="test",
    filters=["all"],
    url="string",
    secret=OrganizationWebhookSecret(
        value="string",
        expires=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
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

**filters:** `typing.Sequence[WebhookFilter]` — Specifies which Webhooks to send.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL that webhooks will be sent to.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `OrganizationWebhookSecret` — Secret used for signing webhooks. This value is used to verify the authenticity of the webhook payload.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human friendly slug for this webhook
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Fullname for this webhook
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[Environment]` — Environment that the webhook is configured for. Only events for accounts associated with this environment will trigger the webhook.
    
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

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization_webhooks.update(
    webhook_id="string",
    id="string",
    fullname="string",
    environment="test",
    filters=["all"],
    url="string",
    credential_id="string",
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Human friendly slug for this webhook
    
</dd>
</dl>

<dl>
<dd>

**environment:** `Environment` — Environment that the webhook is configured for. Only events associated with this environment will trigger the webhook.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Sequence[WebhookFilter]` — Specifies which Webhooks to send.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL that webhooks will be sent to
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `CredentialId` — Credential contain secret
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
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

<details><summary><code>client.organization_webhooks.<a href="src/synqly/organization_webhooks/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization_webhooks.patch(
    webhook_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization_webhooks.delete(
    webhook_id="string",
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
<details><summary><code>client.organization.<a href="src/synqly/organization/client.py">get</a>()</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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

<details><summary><code>client.organization.<a href="src/synqly/organization/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly import OrganizationOptions
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization.update(
    id="string",
    refresh_token_id="string",
    organization_type="root",
    fullname="string",
    contact="string",
    reply_to="string",
    picture="string",
    options=OrganizationOptions(
        invite_duration="string",
        forgot_duration="string",
        password_duration="string",
        minimum_password_length=1,
    ),
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token_id:** `TokenId` — Organization refresh token id
    
</dd>
</dl>

<dl>
<dd>

**organization_type:** `OrganizationType` — Organization type: root or standard
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Human friendly display name for this Organization
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[str]` — Organization email address
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Reply-to email address, used for SMTP emails. Defaults to no-reply@synqly.com
    
</dd>
</dl>

<dl>
<dd>

**picture:** `typing.Optional[str]` — Picture URL of the organization
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[OrganizationOptions]` — Organization options
    
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

<details><summary><code>client.organization.<a href="src/synqly/organization/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.organization.patch(
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
<details><summary><code>client.permissionset.<a href="src/synqly/permissionset/client.py">list</a>()</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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

<details><summary><code>client.permissionset.<a href="src/synqly/permissionset/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.permissionset.get(
    permissionset_id="administrator",
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
<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.roles.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.roles.get(
    role_id="string",
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

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">create</a>(...)</code></summary>
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
from synqly import Resources
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.roles.create(
    name="string",
    fullname="string",
    description="string",
    resources=Resources(),
    permission_set="administrator",
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

**permission_set:** `Permissions` — Permission set for this role.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique short name for this Role (lowercase [a-z0-9_-], can be used in URLs). Also used for case insensitive duplicate name detection and default sort order. Defaults to RoleId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Role, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the resources included in the role and permissions granted on those resources. Includes details of when to use this role along with the intended personas.
    
</dd>
</dl>

<dl>
<dd>

**resources:** `typing.Optional[Resources]` — Selects the resources the permission set applies to.
    
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

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">update</a>(...)</code></summary>
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
import datetime

from synqly import Resources
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.roles.update(
    role_id="string",
    id="string",
    fullname="string",
    description="string",
    resources=Resources(),
    permission_set="administrator",
    name="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `str` — Full name of role
    
</dd>
</dl>

<dl>
<dd>

**permission_set:** `Permissions` — Permission set for this role.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `dt.datetime` — Time object was originally created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `dt.datetime` — Last time object was updated
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the resources included in the role and permissions granted on those resources. Includes details of when to use this role along with the intended personas.
    
</dd>
</dl>

<dl>
<dd>

**resources:** `typing.Optional[Resources]` — Selects the resources the permission set applies to.
    
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

<details><summary><code>client.roles.<a href="src/synqly/roles/client.py">patch</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.roles.patch(
    role_id="string",
    request=[
        PatchOperation(
            op="add",
            path="string",
            from_="string",
            value={"key": "value"},
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

**request:** `typing.Sequence[PatchOperation]` 
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.roles.delete(
    role_id="string",
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
<details><summary><code>client.status.<a href="src/synqly/status/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.status.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
    expand="account",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[ListStatusOptions, typing.Sequence[ListStatusOptions]]
]` — Expand the status result with the related integration and/or account information.
    
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

<details><summary><code>client.status.<a href="src/synqly/status/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.status.get(
    account_id="string",
    integration_id="string",
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.status.reset(
    account_id="string",
    integration_id="string",
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

<details><summary><code>client.status.<a href="src/synqly/status/client.py">list_events</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.status.list_events(
    account_id="string",
    integration_id="string",
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.status.<a href="src/synqly/status/client.py">get_timeseries</a>()</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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

<details><summary><code>client.status.<a href="src/synqly/status/client.py">get_integration_timeseries</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.status.get_integration_timeseries(
    account_id="string",
    integration_id="string",
    interval="string",
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
<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">list</a>()</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
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

<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.sub_orgs.get(
    organization_id="string",
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

<details><summary><code>client.sub_orgs.<a href="src/synqly/sub_orgs/client.py">create</a>(...)</code></summary>
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
from synqly import CreateMemberRequest, MemberOptions
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.sub_orgs.create(
    name="string",
    fullname="string",
    contact="string",
    reply_to="string",
    picture="string",
    member=CreateMemberRequest(
        name="string",
        fullname="string",
        nickname="string",
        picture="string",
        secret="string",
        role_binding=["string"],
        options=MemberOptions(
            ttl="string",
            options=["disabled"],
            token_ttl="string",
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

**name:** `typing.Optional[str]` — Unique short name for this Organization (lowercase [a-z0-9_-], can be used in URLs). Used for case insensitive duplicate name detection and default sort order. Defaults to OrganizationId if both name and fullname are not specified.
    
</dd>
</dl>

<dl>
<dd>

**fullname:** `typing.Optional[str]` — Human friendly display name for this Organization, will auto-generate 'name' field (if 'name' is not specified). Defaults to the same value as the 'name' field if not specified.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[str]` — Organization email address
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[str]` — Reply-to email address, used for SMTP emails. Defaults to no-reply@synqly.com
    
</dd>
</dl>

<dl>
<dd>

**picture:** `typing.Optional[str]` — URL of the organization
    
</dd>
</dl>

<dl>
<dd>

**member:** `typing.Optional[CreateMemberRequest]` — Create organization member
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.sub_orgs.delete(
    organization_id="string",
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
<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_token</a>(...)</code></summary>
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
from synqly import Resources
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.create_token(
    name="string",
    resources=Resources(),
    permission_set="administrator",
    token_ttl="string",
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

**resources:** `Resources` — Limit access to supplied resources
    
</dd>
</dl>

<dl>
<dd>

**permission_set:** `Permissions` — Limit access to supplied permissions
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique name token. If not provided, defaults to generated newly created refresh token id.
    
</dd>
</dl>

<dl>
<dd>

**token_ttl:** `typing.Optional[str]` — Token time-to-live. If not provided, defaults to 24 hours. Use the format "1h", "1m", "1s" for hours, minutes, and seconds respectively, e.g., "24h" for 24 hours.
    
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

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_integration_token</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.create_integration_token(
    account_id="string",
    integration_id="string",
    name="string",
    token_ttl="string",
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

**name:** `typing.Optional[str]` — Unique name token. If not provided, defaults to generated newly created refresh token id.
    
</dd>
</dl>

<dl>
<dd>

**token_ttl:** `typing.Optional[str]` — Token time-to-live. If not provided, defaults to 10 minutes. Use the format "1h", "1m", "1s" for hours, minutes, and seconds respectively, e.g., "2h" for 2 hours.
    
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

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">create_synqly_integrations_token</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.create_synqly_integrations_token(
    token_ttl="string",
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

**token_ttl:** `typing.Optional[str]` — Token time-to-live. If not provided, defaults to 24 hours. Use the format "1h", "1m", "1s" for hours, minutes, and seconds respectively, e.g., "24h" for 24 hours.
    
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.delete(
    refresh_token_id="string",
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

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">list</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.list(
    limit=1,
    start_after="string",
    order="string",
    filter="string",
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

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
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

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.get(
    refresh_token_id="string",
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

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">reset</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.reset(
    owner_id="string",
    refresh_token_id="string",
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

<details><summary><code>client.tokens.<a href="src/synqly/tokens/client.py">refresh</a>(...)</code></summary>
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.refresh(
    refresh_token_id="string",
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
from synqly.client import SynqlyManagement

client = SynqlyManagement(
    token="YOUR_TOKEN",
)
client.tokens.remove_secondary(
    refresh_token_id="string",
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

