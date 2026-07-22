# Reference
## Appsec
<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">query_applications</a>(...) -> AppSecQueryApplicationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of applications matching the query from a the token-linked application security integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.appsec.query_applications()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of applications to return. Defaults to 100 with a maximum of 5000. If a provider has a maximum limit lower than 5000, the provider's maximum limit will be used instead.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/appsec/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">query_application_findings</a>(...) -> AppSecQueryApplicationFindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of an application's findings matching `{applictionId}` and the query from a the token-linked application security integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.appsec.query_application_findings(
    application_id="applicationId",
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

**application_id:** `ApplicationId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of findings to return. Defaults to 100 with a maximum of 5000. If a provider has a maximum limit lower than 5000, the provider's maximum limit will be used instead.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/appsec/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">query_findings</a>(...) -> AppSecQueryFindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of each findings details combined with the application details for all applications in the token-linked application security integration. This API may perform multiple provider API calls per executation so can be slower to respond.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.appsec.query_findings()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of findings to return. Defaults to 100 with a maximum of 5000. If a provider has a maximum limit lower than 5000, the provider's maximum limit will be used instead.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/appsec/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">get_application_finding_details</a>(...) -> AppSecGetApplicationFindingDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of the finding matching `{findingId}` where the finding belongs to the application matching `{applicationId}` from the token-linked application security integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.appsec.get_application_finding_details(
    application_id="applicationId",
    finding_id="findingId",
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

**application_id:** `ApplicationId` 
    
</dd>
</dl>

<dl>
<dd>

**finding_id:** `FindingId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

## Assets
<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">query_devices</a>(...) -> QueryDevicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query devices from an asset inventory system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.assets.query_devices()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of finding reports to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/assets/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` 

Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order.
The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">create_asset</a>(...) -> CreateDeviceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Device` object in the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_3_0.inventoryinfo.classes import InventoryInfo
from synqly.ocsf.v_1_3_0.objects import Device, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.assets.create_asset(
    device=InventoryInfo(
        activity_id=1,
        category_uid=1,
        class_uid=1,
        device=Device(
            type_id=1,
        ),
        metadata=Metadata(
            product=Product(),
            version="version",
        ),
        severity_id=1,
        time=1,
        type_uid=1,
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

**request:** `CreateDeviceRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">create_devices</a>(...) -> CreateDevicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk create devices in an device inventory system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_3_0.inventoryinfo.classes import InventoryInfo
from synqly.ocsf.v_1_3_0.objects import Device, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.assets.create_devices(
    devices=[
        InventoryInfo(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            device=Device(
                type_id=1,
            ),
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
        ),
        InventoryInfo(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            device=Device(
                type_id=1,
            ),
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
        )
    ],
    source_name="source_name",
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

**request:** `CreateDevicesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">get_labels</a>(...) -> GetLabelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get labels from an asset inventory system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.assets.get_labels()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">query_software</a>(...) -> QuerySoftwareInventoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query software inventory records from an asset management system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.assets.query_software()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of software inventory records to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to the [Assets Filtering Guide](https://docs.synqly.com/guides/connectors/assets/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` 

Select a field to order the results by. Defaults to `package.name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `package.name[asc]` will sort the results by package name in ascending order.
The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">create_software</a>(...) -> CreateSoftwareInventoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a software inventory record in the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_8_0.softwareinventoryinfo.classes import SoftwareInfo
from synqly.ocsf.v_1_8_0.objects import Device, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.assets.create_software(
    software_inventory=SoftwareInfo(
        activity_id=1,
        category_uid=1,
        class_uid=1,
        device=Device(
            type_id=1,
        ),
        metadata=Metadata(
            product=Product(),
            version="version",
        ),
        severity_id=1,
        time=1,
        type_uid=1,
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

**request:** `CreateSoftwareInventoryRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Chat
<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_users</a>(...) -> ChatQueryUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of users in the connected workspace or tenant. Used to discover whose conversations can be queried.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_users()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of users to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/chat/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_user_conversations</a>(...) -> ChatQueryConversationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of conversations scoped to a specific user — DMs, group chats, or (for AI providers) synthesised sessions.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_user_conversations(
    user_id="userId",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of conversations to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_user_conversation_members</a>(...) -> ChatQueryConversationMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the members of a conversation scoped to a specific user. Required for providers where conversations are only addressable via the user (e.g. Teams DMs, Copilot AI sessions).
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_user_conversation_members(
    user_id="userId",
    conversation_id="conversationId",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of members to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_user_conversation_messages</a>(...) -> ChatQueryMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns messages from a conversation scoped to a specific user. Required for providers where conversations are only addressable via the user (e.g. Teams DMs, Copilot AI sessions).
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_user_conversation_messages(
    user_id="userId",
    conversation_id="conversationId",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of messages to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. Supported filter fields vary by provider. Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_conversations</a>(...) -> ChatQueryConversationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of conversations (channels or workspaces) not scoped to a specific user. Providers that can only enumerate conversations per-user return NotImplemented; use query_user_conversations instead.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_conversations()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of conversations to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_conversation_members</a>(...) -> ChatQueryConversationMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the members of a specific conversation. Use the user-scoped variant (query_user_conversation_members) for chats that only exist in a user's mailbox (e.g. Teams 1:1 chats).
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_conversation_members(
    conversation_id="conversationId",
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

**conversation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of members to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.chat.<a href="src/synqly/chat/client.py">query_conversation_messages</a>(...) -> ChatQueryMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns messages from a specific conversation. The conversationId must be obtained from query_conversations or query_user_conversations. Use the user-scoped variant (query_user_conversation_messages) for chats that only exist in a user's mailbox.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.chat.query_conversation_messages(
    conversation_id="conversationId",
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

**conversation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of messages to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. Supported filter fields vary by provider. Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

## Cloudsecurity
<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_events</a>(...) -> QueryEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of events that match the query from the cloud security provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.cloudsecurity.query_events()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/cloudsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_ioms</a>(...) -> QueryIomsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Indicators of Misconfiguration (IOM) findings that match the query from the cloud security provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.cloudsecurity.query_ioms()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of cloud resources to return. Defaults to 500.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/cloudsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the CloudSecurity in the response. Defaults to `false`.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_cloud_resource_inventory</a>(...) -> QueryCloudResourceInventoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of cloud resources that match the query from the cloud security provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.cloudsecurity.query_cloud_resource_inventory()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.  
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of cloud resources to return. Defaults to 500.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/cloudsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the CloudSecurity in the response. Defaults to `false`.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_compliance_findings</a>(...) -> QueryComplianceFindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of compliance findings matching the query from the cloud security provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.cloudsecurity.query_compliance_findings()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of compliance findings to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/cloudsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the CloudSecurity in the response. Defaults to `false`.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_threats</a>(...) -> QueryCloudSecurityThreatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of threat detections that match the query from the cloud security provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.cloudsecurity.query_threats()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of threats to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/cloudsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the CloudSecurity in the response. Defaults to `false`.
    
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

## Custom
<details><summary><code>client.custom.<a href="src/synqly/custom/client.py">query</a>(...) -> QueryCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries operation
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_id_generated import OperationId

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.custom.query(
    operation=OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS,
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

**operation:** `OperationId` — what `operation` to query
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `operation` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data in the response. Defaults to `false`.
    
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

<details><summary><code>client.custom.<a href="src/synqly/custom/client.py">get</a>(...) -> GetCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an Topic by ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_id_generated import OperationId

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.custom.get(
    operation=OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS,
    id="id",
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

**operation:** `OperationId` — what `operation` to query
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — ID of the `operation` to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data in the response. Defaults to `false`.
    
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

<details><summary><code>client.custom.<a href="src/synqly/custom/client.py">patch</a>(...) -> GetCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an `operation` by ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_id_generated import OperationId
from synqly.common import PatchOperation, PatchOp

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.custom.patch(
    operation=OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS,
    id="id",
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

**operation:** `OperationId` — what `operation` to query
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — ID of the `operation` to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchCustomRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.custom.<a href="src/synqly/custom/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the object matching `id` for the operation matching `operation`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_id_generated import OperationId

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.custom.delete(
    operation=OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS,
    id="id",
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

**operation:** `OperationId` — what `operation` to delete.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — ID of the `operation` to delete.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.custom.<a href="src/synqly/custom/client.py">post</a>(...) -> CreateCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes an `operation` object to the Custom provider configured with the token used for authentication.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_id_generated import OperationId

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.custom.post(
    operation=OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS,
    request={
        "string": {"key": "value"}
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

**operation:** `OperationId` — what `operation` to post
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` — The `operation` object to be sent.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.custom.<a href="src/synqly/custom/client.py">post_batch</a>(...) -> CreateBatchCustomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes a batch of `operation` objects to the Custom provider configured with the token used for authentication.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_id_generated import OperationId

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.custom.post_batch(
    operation=OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS,
    request=[
        {
            "string": {"key": "value"}
        },
        {
            "string": {"key": "value"}
        }
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

**operation:** `OperationId` — what `operation` to post
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Dict[str, typing.Any]]` — The `operation` object to be sent.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Edr
<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_endpoints</a>(...) -> QueryEndpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of endpoint assets matching the query from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_endpoints()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of endpoint assets to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/edr/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">get_endpoint</a>(...) -> GetEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a single endpoint assets matching the UID from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.get_endpoint(
    id="id",
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

**id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">execute_command</a>(...) -> ExecuteCommandResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a provider-backed command on the endpoint identified by `{uid}` and returns normalized stdout and stderr without exposing provider session details.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.execute_command(
    uid="uid",
    command="command",
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

**uid:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExecuteCommandRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">retrieve_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a file from the endpoint identified by `{uid}` and returns the provider artifact as a binary file response.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.retrieve_file(
    uid="uid",
    path="path",
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

**uid:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RetrieveFileRequest` 
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_applications</a>(...) -> QueryApplicationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of applications matching the query from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_applications()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of applications to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/edr/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">network_quarantine</a>(...) -> NetworkQuarantineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect or disconnect one or more endpoints assets to the network, allowing or disallowing connections.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.edr import ConnectionState

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.network_quarantine(
    state=ConnectionState.CONNECT,
    endpoint_ids=[
        "endpoint_ids",
        "endpoint_ids"
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

**request:** `NetworkQuarantineRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_threatevents</a>(...) -> QueryThreatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of threats that match the query from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_threatevents()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of threats to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/edr/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_alerts</a>(...) -> QueryAlertsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of alerts that match the query from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_alerts()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of threats to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/edr/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_iocs</a>(...) -> QueryIocsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of iocs that match the query from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_iocs()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of threats to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/edr/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">create_iocs</a>(...) -> CreateIocsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a list of iocs that match the stix input for the EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.stix.indicator import Indicator
import datetime

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.create_iocs(
    indicators=[
        Indicator(
            spec_version="2.1",
            id="id",
            created=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            modified=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            type="indicator",
            valid_from=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
        ),
        Indicator(
            spec_version="2.1",
            id="id",
            created=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            modified=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            type="indicator",
            valid_from=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**request:** `CreateIocsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">delete_iocs</a>(...) -> DeleteIocsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a list of iocs that match the input of ids in the query param
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.delete_iocs()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — list of ids to delete
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_posture_score</a>(...) -> QueryPostureScoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the posture score of the endpoint assets that match the query from the token-linked EDR source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_posture_score()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of scores for endpoints to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/edr/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_edr_events</a>(...) -> QueryEdrEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of EDR events that match the query from the token-linked EDR source. 
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.query_edr_events()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**passthrough_param:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Provider-specific query to pass through to the EDR. This is useful for advanced queries that require additional filtering.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter events. Multiple filters can be provided.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the EDR in the response. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `timestamp[asc]` will sort the results by `timestamp` in ascending order.
The ordering defaults to `asc` if not specified.            
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">get_threat_notes</a>(...) -> GetThreatNotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of notes for a threat.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.get_threat_notes(
    threat_id="threatId",
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

**threat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of notes to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor from a previous response to retrieve the next page of notes.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">create_threat_note</a>(...) -> CreateThreatNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a note for a threat.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_8_0.noteactivity.classes import NoteActivity
from synqly.ocsf.v_1_8_0.objects import FindingInfo, Metadata, Product, Annotation

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.edr.create_threat_note(
    threat_id="threatId",
    note=NoteActivity(
        activity_id=1,
        category_uid=1,
        class_uid=1,
        finding_info=FindingInfo(
            uid="uid",
        ),
        metadata=Metadata(
            product=Product(),
            version="version",
        ),
        note=Annotation(),
        severity_id=1,
        time=1,
        type_uid=1,
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

**threat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateThreatNoteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Emailsecurity
<details><summary><code>client.emailsecurity.<a href="src/synqly/emailsecurity/client.py">query_threats</a>(...) -> EmailSecurityQueryThreatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of threats matching the query from the token-linked Email Security provider. Defaults to the last 30 days of threats. This can be overridden by using the `time` filter. Note that some providers may have a maximum time range limit. A threat is an automated detection that was deemed to be a threat by the Email Security provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.emailsecurity.query_threats()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of threats to return. Defaults to 1000 with a maximum of 5000. If a provider has a maximum limit lower than 5000, the provider's maximum limit will be used instead.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/emailsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.emailsecurity.<a href="src/synqly/emailsecurity/client.py">get_threat_details</a>(...) -> EmailSecurityGetThreatDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of the threat matching `{threatId}` from the token-linked Email Security provider. If a provider allows for the gathering of more detailed information about a threat, the response will include the additional information. Otherwise, the response will only include the basic information about the threat returned by the query_threats endpoint.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.emailsecurity.get_threat_details(
    threat_id="threatId",
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

**threat_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.emailsecurity.<a href="src/synqly/emailsecurity/client.py">query_email_events</a>(...) -> EmailSecurityQueryEmailEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of email events matching the query from the token-linked Email Security provider. Defaults to the last 30 days of email events. This can be overridden by using the `time` filter. Note that some providers may have a maximum time range limit.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.emailsecurity.query_email_events()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of email events to return. Defaults to 1000 with a maximum of 5000. If a provider has a maximum limit lower than 5000, the provider's maximum limit will be used instead.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/emailsecurity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

## Endpointmanagement
<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">query_devices</a>(...) -> QueryEndpointManagementDevicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of managed devices matching the query from the token-linked endpoint management source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.query_devices()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of devices to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `device.name[asc]` will sort the results by `device.name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/endpointmanagement/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">get_device</a>(...) -> GetEndpointManagementDeviceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a single managed device matching the ID from the token-linked endpoint management source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.get_device(
    id="id",
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

**id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">query_compliance_findings</a>(...) -> QueryDeviceComplianceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of device compliance findings matching the query from the token-linked endpoint management source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.query_compliance_findings()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of compliance findings to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/endpointmanagement/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">remediate_device</a>(...) -> RemediateDeviceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs a remediation action on a managed device from the token-linked endpoint management source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.remediate_device()

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

**request:** `RemediationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">update_device</a>(...) -> DeviceActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers the device to check in and enforce all assigned policies, profiles, and pending updates.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.update_device(
    device_id="device_id",
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

**request:** `DeviceActionRequest` 
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">lock_device</a>(...) -> DeviceActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remotely locks the device screen.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.lock_device(
    device_id="device_id",
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

**request:** `DeviceActionRequest` 
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">restart_device</a>(...) -> DeviceActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remotely reboots the device.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.restart_device(
    device_id="device_id",
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

**request:** `DeviceActionRequest` 
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">wipe_device</a>(...) -> DeviceActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Factory resets or erases all data from the device.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.wipe_device(
    device_id="device_id",
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

**request:** `DeviceActionRequest` 
    
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

<details><summary><code>client.endpointmanagement.<a href="src/synqly/endpointmanagement/client.py">query_device_applications</a>(...) -> QueryDeviceApplicationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of applications installed on a managed device from the token-linked endpoint management source.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.endpointmanagement.query_device_applications(
    id="id",
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

**id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of applications to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `product.name[asc]` will sort the results by `product.name` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/endpointmanagement/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

## Hooks
<details><summary><code>client.hooks.<a href="src/synqly/hooks/client.py">proxy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxy webhook messages from webhook providers to webhook recievers. For exact webhook implementations please refer to providers e.g. Ticketing. This is just an API call used in that context, not a standalone implementation.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.hooks.proxy(
    token="token",
    request={"key": "value"},
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

**token:** `str` — Optional: if you can't use the HTTP Authorization Bearer, specify integration access token here.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Identity
<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_audit_log</a>(...) -> QueryIdentityAuditLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Event` objects from the token-linked audit log.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.query_audit_log()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/identity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. Defaults to `false`.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_risk_events</a>(...) -> QueryIdentityRiskEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns identity threat / risk events (for example Microsoft Entra Identity Protection risk detections for users), normalized to OCSF.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.query_risk_events()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/identity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the identity provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_risky_users</a>(...) -> QueryIdentityRiskyUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns rolled-up risky user records (for example Microsoft Entra Identity Protection riskyUsers), each normalized to an OCSF Entity Management Read event.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.query_risky_users()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of users to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/identity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the identity provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_users</a>(...) -> QueryUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `User` objects wrapped in the OCSF Entity Management event of type Read from the token-linked identity provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.query_users()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of users to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `uid`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `email_addr[asc]` will sort the results by `email_addr` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/identity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_user</a>(...) -> GetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `User` object wrapped in an OCSF Entity Management event of type Read from the token-linked identity provider. Depending 
on the providers offerings, this may include additional user information, such as the user's current groups, roles, and Identity Protection risk state (when the provider exposes it and the user has a risk record).
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.get_user(
    user_id="userId",
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

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_groups</a>(...) -> QueryGroupsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Group` objects wrapped in the OCSF Entity Management event of type Read from the token-linked identity provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.query_groups()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of users to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `uid`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `email_addr[asc]` will sort the results by `email_addr` in ascending order. The ordering defaults to `asc` if not specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/identity/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_group</a>(...) -> GetGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Group` object wrapped in an OCSF Entity Management event of type Read from the token-linked identity provider. Depending 
on the providers offerings, this may include additional group information, such as the roles assigned.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.get_group(
    group_id="groupId",
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

**group_id:** `GroupId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_group_members</a>(...) -> GetGroupMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of `User` objects wrapped in an OCSF Entity Management event of type Read from the token-linked identity provider that are members in the group referenced by ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.get_group_members(
    group_id="groupId",
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

**group_id:** `GroupId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of users to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">enable_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reenables a disabled user in the identity system based on user ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.enable_user(
    user_id="userId",
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

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">disable_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables a user in the identity system based on user ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.disable_user(
    user_id="userId",
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

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">force_user_password_reset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forces a user to reset their password before they can log in again.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.force_user_password_reset(
    user_id="userId",
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

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">expire_all_user_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Logs a user out of all current sessions so they must log in again.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.expire_all_user_sessions(
    user_id="userId",
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

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_user_picture</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the profile picture for a user as binary image data. The Content-Type header indicates the image format (e.g., image/jpeg, image/png).
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.identity.get_user_picture(
    user_id="userId",
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

**user_id:** `UserId` 
    
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

## Incidentresponse
<details><summary><code>client.incidentresponse.<a href="src/synqly/incidentresponse/client.py">query_escalation_policies</a>(...) -> IncidentResponseQueryEscalationPoliciesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of incident response escalation policies.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.incidentresponse.query_escalation_policies()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of escalation policies to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
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

<details><summary><code>client.incidentresponse.<a href="src/synqly/incidentresponse/client.py">query_escalation_policy_users_on_call</a>(...) -> IncidentResponseQueryEscalationPolicyUsersOnCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of users that are currently on call for an incident response escalation policy.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.incidentresponse.query_escalation_policy_users_on_call(
    escalation_policy_id="escalationPolicyId",
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

**escalation_policy_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## IntegrationWebhooks
<details><summary><code>client.integration_webhooks.<a href="src/synqly/integration_webhooks/client.py">create_webhook</a>(...) -> CreateIntegrationWebHookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a WebHook for the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.integration_webhooks.create_webhook(
    project="project",
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

**request:** `CreateIntegrationWebHookRequest` 
    
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

<details><summary><code>client.integration_webhooks.<a href="src/synqly/integration_webhooks/client.py">delete_webhook</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the WebHook matching the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.integration_webhooks.delete_webhook()

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

<details><summary><code>client.integration_webhooks.<a href="src/synqly/integration_webhooks/client.py">list_webhooks</a>() -> ListIntegrationWebHooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all WebHooks from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.integration_webhooks.list_webhooks()

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

## Notifications
<details><summary><code>client.notifications.<a href="src/synqly/notifications/client.py">get_message</a>(...) -> GetNotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Notification` object matching `{notificationId}` from the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.notifications.get_message(
    notification_id="notificationId",
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

**notification_id:** `NotificationId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.notifications.<a href="src/synqly/notifications/client.py">create_message</a>(...) -> CreateNotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Notification` object in the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.notifications.create_message(
    summary="summary",
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

**request:** `CreateNotificationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.notifications.<a href="src/synqly/notifications/client.py">clear_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolves a `Notification` object in the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.notifications.clear_message(
    notification_id="notificationId",
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

**notification_id:** `NotificationId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Operations
<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">get</a>(...) -> GetOperationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Asynchronous Operation` object matching `{operationId}`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.operations.get(
    operation_id="operationId",
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

**operation_id:** `AsyncOperationRequestId` 
    
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

<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">create</a>(...) -> CreateOperationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Asynchronous Operation` object.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.operation_base import OperationInput

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.operations.create(
    operation="operation",
    input=OperationInput(),
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

**request:** `CreateOperationRequest` 
    
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

<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels the `Asynchronous Operation` matching `{operationId}`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.operations.cancel(
    operation_id="operationId",
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

**operation_id:** `AsyncOperationRequestId` 
    
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

## Siem
<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_investigations</a>(...) -> QueryInvestigationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries investigations
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.query_investigations()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Investigation` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/siem/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. Defaults to `false`.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">get_investigation</a>(...) -> GetInvestigationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an investigation by ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.get_investigation(
    id="id",
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

**id:** `str` — ID of the investigation to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. Defaults to `false`.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">patch_investigation</a>(...) -> GetInvestigationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an investigation by ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.patch_investigation(
    id="id",
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

**id:** `str` — ID of the investigation to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchInvestigationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">get_evidence</a>(...) -> GetEvidenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the evidence for an investigation.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.get_evidence(
    id="id",
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

**id:** `str` — ID of the investigation to retrieve evidence for.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. Defaults to `false`.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_log_providers</a>(...) -> QueryLogProvidersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries available log providers in the source SIEM
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.query_log_providers()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of log provider objects to return in this page. Defaults to 100.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">post_events</a>(...) -> CreateSiemEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes a batch of `Event` objects to the SIEM configured with the token used for authentication.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.events import Event_AccountChange
from synqly.ocsf.v_1_3_0.objects import Metadata, Product, User

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.post_events(
    request=[
        Event_AccountChange(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
            user=User(),
        ),
        Event_AccountChange(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
            user=User(),
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

**request:** `typing.List[Event]` — The `Event` object to be sent.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_events</a>(...) -> QuerySiemEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries events from the SIEM configured with the token used for authentication.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.query_events()

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

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Account` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order. The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/siem/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**passthrough_param:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Provider-specific query to pass through to the SIEM. This is useful for advanced queries that are not
supported by the API. The keys and values are provider-specific. For example, to perform a specific
query in Rapid7 IDR, you can use the `query: "{advanced query}"` key-value pair.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. This is useful for debugging and troubleshooting. Defaults to `false`.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_alerts</a>(...) -> QuerySiemAlertsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries alerts from the SIEM configured with the token used for authentication.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.query_alerts()

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

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Account` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order. The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/siem/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. This is useful for debugging and troubleshooting. Defaults to `false`.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">get_alert</a>(...) -> GetAlertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an alert by ID.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.siem.get_alert(
    id="id",
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

**id:** `str` — ID of the alert to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the SIEM in the response. Defaults to `false`.
    
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

## Sink
<details><summary><code>client.sink.<a href="src/synqly/sink/client.py">post_events</a>(...) -> CreateSinkEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes a batch of `Event` objects to the Sink configured with the token used for authentication.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.events import Event_AccountChange
from synqly.ocsf.v_1_3_0.objects import Metadata, Product, User

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.sink.post_events(
    request=[
        Event_AccountChange(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
            user=User(),
        ),
        Event_AccountChange(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
            user=User(),
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

**request:** `typing.List[Event]` — The `Event` object to be sent.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Updates the path or queue name for the sink. If not provided, the default path or queue name is used. When provided, the path or queue name is appended to the default path or queue name.
    
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

## Storage
<details><summary><code>client.storage.<a href="src/synqly/storage/client.py">list_files</a>(...) -> ListStorageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of contents from the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.storage.list_files(
    path="path",
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to fetch the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Default is 50.
    
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

<details><summary><code>client.storage.<a href="src/synqly/storage/client.py">upload_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a file from the provided `{path}` to the token-linked `Integration`.
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
client.storage.upload_file(...)
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.storage.<a href="src/synqly/storage/client.py">download_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads a file from the provided `{path}` in the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.storage.download_file(
    path="path",
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

**path:** `str` 
    
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

<details><summary><code>client.storage.<a href="src/synqly/storage/client.py">delete_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a file from the provided `{path}` in the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.storage.delete_file(
    path="path",
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Ticketing
<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_remote_fields</a>(...) -> ListRemoteFieldsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all remote fields for all Projects in a ticketing integration. The response will include a list of fields for each issue type in the ticketing provider.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.list_remote_fields()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_projects</a>(...) -> ListProjectsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Projects` from the token-linked `Integration`. Tickets must be created and retrieved within the context of a specific Project.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.list_projects()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Projects` objects to return in this page. Defaults to 50.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">query_tickets</a>(...) -> QueryTicketsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Ticket` objects from the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.query_tickets()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to use to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of `Account` objects to return in this page. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append `[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order. The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the ordering is applied in the order the fields are specified.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/ticketing/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">get_ticket</a>(...) -> GetTicketResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Ticket` object matching `{ticketId}` from the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.get_ticket(
    ticket_id="ticketId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_ticket</a>(...) -> CreateTicketResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Ticket` object in the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.create_ticket(
    name="name",
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

**request:** `CreateTicketRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">patch_ticket</a>(...) -> PatchTicketResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `Ticket` object matching `{ticketId}` in the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.patch_ticket(
    ticket_id="ticketId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_attachment</a>(...) -> CreateAttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[beta: currently supported by Jira] Creates an `Attachment` for the ticket with id `{ticketId}` in the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.create_attachment(
    ticket_id="ticketId",
    file_name="file_name",
    content="SGVsbG8gd29ybGQh",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateAttachmentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_attachments_metadata</a>(...) -> ListAttachmentsMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[beta: currently supported by Jira] Returns metadata for all Attachments for a `Ticket` object matching `{ticketId}` from the token-linked `Integration`.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.list_attachments_metadata(
    ticket_id="ticketId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">download_attachment</a>(...) -> DownloadAttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[beta: currently supported by Jira] Downloads the Attachment object matching {attachmentId} for the Ticket matching {tickedId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.download_attachment(
    ticket_id="ticketId",
    attachment_id="attachmentId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `AttachmentId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">delete_attachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[beta: currently supported by Jira] Deletes the Attachment object matching {attachmentId} for the Ticket matching {tickedId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.delete_attachment(
    ticket_id="ticketId",
    attachment_id="attachmentId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `AttachmentId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_comments</a>(...) -> ListCommentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all comments for the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.list_comments(
    ticket_id="ticketId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_comment</a>(...) -> CreateCommentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a comment on the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.create_comment(
    ticket_id="ticketId",
    content="content",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateCommentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">delete_comment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the comment matching {commentId} form the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.delete_comment(
    ticket_id="ticketId",
    comment_id="commentId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**comment_id:** `CommentId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_note</a>(...) -> CreateNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a note on the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.create_note(
    ticket_id="ticketId",
    content="content",
    title="title",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateNoteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">delete_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the note matching {noteId} form the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.delete_note(
    ticket_id="ticketId",
    note_id="noteId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_notes</a>(...) -> ListNotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all notes for the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.list_notes(
    ticket_id="ticketId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">patch_note</a>(...) -> PatchNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a note matching {noteId} title and/or content on the ticket matching {ticketId} from the token-linked Integration.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.common import PatchOperation, PatchOp

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.patch_note(
    ticket_id="ticketId",
    note_id="noteId",
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

**ticket_id:** `TicketId` 
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchOperation]` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">query_escalation_policies</a>(...) -> QueryEscalationPoliciesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of escalation policies.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.query_escalation_policies()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of escalation policies to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/ticketing/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_on_call</a>(...) -> ListOnCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all on-call agents for an escalation policy.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.ticketing.list_on_call(
    escalation_policy_id="escalationPolicyId",
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

**escalation_policy_id:** `Id` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

## Vulnerabilities
<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_findings</a>(...) -> QueryFindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query vulnerability findings
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.query_findings()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of finding reports to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/vulnerabilities/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">create_findings</a>(...) -> CreateFindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create findings (bulk) in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_3_0.securityfinding.classes import SecurityFinding
from synqly.ocsf.v_1_3_0.objects import Finding, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.create_findings(
    findings=[
        SecurityFinding(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            finding=Finding(
                title="title",
                uid="uid",
            ),
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            state_id=1,
            time=1,
            type_uid=1,
        ),
        SecurityFinding(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            finding=Finding(
                title="title",
                uid="uid",
            ),
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            state_id=1,
            time=1,
            type_uid=1,
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

**request:** `CreateFindingsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">update_finding</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

update a finding in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.update_finding(
    finding_id="findingId",
    severity_id=1,
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

**finding_id:** `str` — Uid of the Finding (URL encoded). This will be `finding.uid` in the OCSF model.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateFindingRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_assets</a>(...) -> QueryAssetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query assets in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.query_assets()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of assets to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/vulnerabilities/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">create_asset</a>(...) -> typing.Optional[CreateAssetResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create assets in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_3_0.inventoryinfo.classes import InventoryInfo
from synqly.ocsf.v_1_3_0.objects import Device, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.create_asset(
    asset=InventoryInfo(
        activity_id=1,
        category_uid=1,
        class_uid=1,
        device=Device(
            type_id=1,
        ),
        metadata=Metadata(
            product=Product(),
            version="version",
        ),
        severity_id=1,
        time=1,
        type_uid=1,
    ),
    source_name="source_name",
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

**request:** `CreateAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">update_asset</a>(...) -> typing.Optional[Asset]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

update an asset in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_3_0.inventoryinfo.classes import InventoryInfo
from synqly.ocsf.v_1_3_0.objects import Device, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.update_asset(
    asset_id="assetId",
    asset=InventoryInfo(
        activity_id=1,
        category_uid=1,
        class_uid=1,
        device=Device(
            type_id=1,
        ),
        metadata=Metadata(
            product=Product(),
            version="version",
        ),
        severity_id=1,
        time=1,
        type_uid=1,
    ),
    source_name="source_name",
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

**asset_id:** `str` — Uid of the Asset. This will be `devices.uid` in the OCSF model.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateAssetRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_scans</a>(...) -> QueryScansResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query scans in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.query_scans()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of scans to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/vulnerabilities/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">get_scan_activity</a>(...) -> GetScanActivityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: use GET /scans/{scan_id}/activities instead, which returns the full execution history for a scan definition.
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.get_scan_activity(
    scan_id="scan_id",
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

**scan_id:** `str` — ID of the scan to get activity for (provider-specific; often scan definition or template id).
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">get_scan_activities</a>(...) -> GetScanActivitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get scan execution history for a configured scan. Returns one OCSF Scan Activity per execution (e.g. each Tenable.sc scan result for the given scan definition id).
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.get_scan_activities(
    scan_id="scan_id",
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

**scan_id:** `str` — ID of the scan definition whose execution history is requested.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">upload_scan</a>(...) -> UploadScanResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a scan in a vulnerability scanning system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment
from synqly.ocsf.v_1_3_0.inventoryinfo.classes import InventoryInfo
from synqly.ocsf.v_1_3_0.objects import Device, Metadata, Product

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.upload_scan(
    assets=[
        InventoryInfo(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            device=Device(
                type_id=1,
            ),
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
        ),
        InventoryInfo(
            activity_id=1,
            category_uid=1,
            class_uid=1,
            device=Device(
                type_id=1,
            ),
            metadata=Metadata(
                product=Product(),
                version="version",
            ),
            severity_id=1,
            time=1,
            type_uid=1,
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

**request:** `UploadScanRequest` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">get_scan_status</a>(...) -> GetScanStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a upload scan
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.get_scan_status(
    scan_id="scan_id",
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

**scan_id:** `str` — ID of the scan to get the status of.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">get_labels</a>(...) -> GetLabelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get labels from an asset inventory system
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.get_labels()

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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
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

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_scan_findings</a>(...) -> VulnerabilitiesQueryScanFindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query findings for a scan
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
from synqly import SynqlyEngine
from synqly.environment import SynqlyEngineEnvironment

client = SynqlyEngine(
    token="<token>",
    environment=SynqlyEngineEnvironment.SYNQLY,
)

client.vulnerabilities.query_scan_findings(
    scan_id="scanId",
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

**scan_id:** `str` — ID of the scan to query findings for. Use the `query_scans` API to find available scan IDs.
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for [meta functions](https://docs.synqly.com/api-reference/meta-functions) is available. Not all meta functions are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of findings to return. Defaults to 50 with a maximum of 5000. If a provider has a maximum limit lower than 5000, the provider's maximum limit will be used instead.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query. For more information on filtering, refer to our [Filtering Guide](https://docs.synqly.com/guides/connectors/vulnerabilities/query-filters). Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Start search from cursor position.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` — Include the raw data from the provider in the response. Defaults to `false`.
    
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

