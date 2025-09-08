# Reference
## Appsec
<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">query_applications</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.appsec.query_applications(
    meta="string",
    limit=1,
    order="string",
    filter="string",
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of applications to return.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">query_application_findings</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.appsec.query_application_findings(
    application_id="string",
    meta="string",
    limit=1,
    order="string",
    filter="string",
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of findings to return.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">query_findings</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.appsec.query_findings(
    filter="string",
    limit=1,
    cursor="string",
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

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of findings to return.
    
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

<details><summary><code>client.appsec.<a href="src/synqly/appsec/client.py">get_application_finding_details</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.appsec.get_application_finding_details(
    application_id="string",
    finding_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assets
<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">query_devices</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.assets.query_devices(
    meta="string",
    limit=1,
    cursor="string",
    filter="string",
    order="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to the Assets Filtering Guide.
Defaults to no filter. If used more than once, the queries are ANDed together.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">create_asset</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.inventoryinfo import (
    Account,
    Actor,
    Agent,
    Api,
    Cloud,
    Container,
    Device,
    DeviceHwInfo,
    Display,
    Enrichment,
    Extension,
    Fingerprint,
    Group,
    Idp,
    Image,
    InventoryInfo,
    KeyboardInfo,
    Location,
    Logger,
    Metadata,
    NetworkInterface,
    Observable,
    Organization,
    Os,
    Osint,
    Process,
    Product,
    Request,
    Response,
    Service,
    Session,
    User,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.assets.create_asset(
    device=InventoryInfo(
        activity_id=1,
        activity_name="string",
        actor=Actor(
            actor_type="string",
            actor_type_id=1,
            app_name="string",
            app_uid="string",
            authorizations=[],
            groups=[],
            idp=Idp(),
            invoked_by="string",
            process=Process(),
            session=Session(),
            user=User(),
        ),
        api=Api(
            group=Group(),
            operation="string",
            request=Request(
                uid="string",
            ),
            response=Response(),
            service=Service(),
            version="string",
        ),
        category_name="string",
        category_uid=1,
        class_uid=1,
        cloud=Cloud(
            account=Account(),
            org=Organization(),
            project_uid="string",
            provider="string",
            region="string",
            zone="string",
        ),
        count=1,
        custom_fields={"string": {"key": "value"}},
        device=Device(
            agent_list=[Agent()],
            autoscale_uid="string",
            boot_time=1,
            boot_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            container=Container(
                hash=Fingerprint(
                    algorithm_id=1,
                    value="string",
                ),
                image=Image(
                    uid="string",
                ),
                name="string",
                network_driver="string",
                orchestrator="string",
                pod_uuid="string",
                runtime="string",
                size=1,
                tag="string",
                uid="string",
            ),
            created_time=1,
            created_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            desc="string",
            domain="string",
            first_seen_time=1,
            first_seen_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            groups=[Group()],
            hostname="string",
            hw_info=DeviceHwInfo(
                bios_date="string",
                bios_manufacturer="string",
                bios_uid="string",
                bios_ver="string",
                chassis="string",
                cpu_bits=1,
                cpu_cores=1,
                cpu_count=1,
                cpu_speed=1,
                cpu_type="string",
                desktop_display=Display(),
                keyboard_info=KeyboardInfo(),
                ram_size=1,
                serial_number="string",
            ),
            hypervisor="string",
            image=Image(
                uid="string",
            ),
            imei="string",
            instance_uid="string",
            interface_name="string",
            interface_uid="string",
            ip="string",
            ip_addresses=["string"],
            is_compliant=True,
            is_managed=True,
            is_personal=True,
            is_trusted=True,
            last_seen_time=1,
            last_seen_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            location=Location(
                city="string",
                continent="string",
                coordinates=[],
                country="string",
                desc="string",
                geohash="string",
                is_on_premises=True,
                isp="string",
                lat=1.1,
                long_=1.1,
                postal_code="string",
                provider="string",
                region="string",
                timezone="string",
            ),
            mac="string",
            mac_addresses=["string"],
            modified_time=1,
            modified_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            name="string",
            namespace_pid=1,
            netbios_names=["string"],
            network_interfaces=[
                NetworkInterface(
                    type_id=1,
                )
            ],
            network_status="string",
            network_status_id=1,
            org=Organization(),
            os=Os(
                build="string",
                country="string",
                cpe_name="string",
                cpu_bits=1,
                edition="string",
                lang="string",
                name="string",
                sp_name="string",
                sp_ver=1,
                type="string",
                type_id=1,
                version="string",
            ),
            owner=User(),
            region="string",
            risk_level="string",
            risk_level_id=1,
            risk_score=1,
            subnet="string",
            subnet_uid="string",
            sw_info=[
                Product(
                    vendor_name="string",
                )
            ],
            type="string",
            type_id=1,
            uid="string",
            uid_alt="string",
            vendor=Organization(),
            vlan_uid="string",
            vpc_uid="string",
            zone="string",
        ),
        duration=1,
        end_time=1,
        end_time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        enrichments=[
            Enrichment(
                data={"key": "value"},
                name="string",
                value="string",
            )
        ],
        message="string",
        metadata=Metadata(
            correlation_uid="string",
            event_code="string",
            extension=Extension(
                name="string",
                uid="string",
                version="string",
            ),
            extensions=[
                Extension(
                    name="string",
                    uid="string",
                    version="string",
                )
            ],
            labels=["string"],
            log_level="string",
            log_name="string",
            log_provider="string",
            log_version="string",
            logged_time=1,
            logged_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            loggers=[Logger()],
            modified_time=1,
            modified_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            original_time="string",
            processed_time=1,
            processed_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            product=Product(
                vendor_name="string",
            ),
            profiles=["string"],
            sequence=1,
            tenant_uid="string",
            uid="string",
            version="string",
        ),
        observables=[
            Observable(
                name="string",
                type_id=1,
            )
        ],
        osint=[
            Osint(
                type_id=1,
                value="string",
            )
        ],
        raw_data="string",
        severity="string",
        severity_id=1,
        start_time=1,
        start_time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        status="string",
        status_code="string",
        status_detail="string",
        status_id=1,
        time=1,
        time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        timezone_offset=1,
        type_name="string",
        type_uid=1,
        unmapped={"string": {"key": "value"}},
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

**device:** `Device` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/synqly/assets/client.py">get_labels</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.assets.get_labels(
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

**filter:** `typing.Optional[str]` 

Filter results by this query. For more information on filtering, refer to the Assets Filtering Guide.
Defaults to no filter.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_events</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.cloudsecurity.query_events(
    meta="string",
    limit=1,
    order="string",
    filter="string",
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_ioms</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.cloudsecurity.query_ioms(
    meta="string",
    limit=1,
    order="string",
    filter="string",
    cursor="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of cloud resources to return. Defaults to 500.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_cloud_resource_inventory</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.cloudsecurity.query_cloud_resource_inventory(
    meta="string",
    limit=1,
    order="string",
    filter="string",
    cursor="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of cloud resources to return. Defaults to 500.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.cloudsecurity.<a href="src/synqly/cloudsecurity/client.py">query_compliance_findings</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.cloudsecurity.query_compliance_findings(
    meta="string",
    limit=1,
    cursor="string",
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

## Edr
<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_endpoints</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_endpoints(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">get_endpoint</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.get_endpoint(
    id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_applications</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_applications(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">network_quarantine</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.network_quarantine(
    state="Connect",
    endpoint_ids=["string"],
    comment="string",
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

**state:** `ConnectionState` — The connection state (Connect or Disconnect) to enforce for the provided endpoint IDs.
    
</dd>
</dl>

<dl>
<dd>

**endpoint_ids:** `typing.Sequence[str]` — The list of endpoint IDs to enforce the connection state on.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — A comment to include with the quarantine action.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_threatevents</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_threatevents(
    meta="string",
    limit=1,
    cursor="string",
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_alerts</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_alerts(
    meta="string",
    limit=1,
    cursor="string",
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_iocs</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_iocs(
    meta="string",
    limit=1,
    cursor="string",
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">create_iocs</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine
from synqly.stix import Identity, Indicator

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.create_iocs(
    indicators=[
        Indicator(
            name="string",
            description="string",
            indicator_types=[],
            pattern="string",
            pattern_type="stix",
            pattern_version="string",
            valid_from=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            valid_until=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            kill_chain_phases=[],
            raw_data="string",
            id="string",
            created_by_ref=Identity(
                type="string",
                name="string",
                id="string",
                created=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                modified=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            ),
            created=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            modified=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            revoked=True,
            labels=[],
            confidence=1,
            lang="string",
            external_references=[],
            object_marking_refs=[],
            granular_markings=[],
            extensions={},
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

**indicators:** `typing.Sequence[Indicator]` — The list of iocs to create
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">delete_iocs</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.delete_iocs(
    meta="string",
    ids="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_posture_score</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_posture_score(
    meta="string",
    limit=1,
    cursor="string",
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `name[asc]` will sort the results by `name` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.edr.<a href="src/synqly/edr/client.py">query_edr_events</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.edr.query_edr_events(
    meta="string",
    filter="string",
    include_raw_data=True,
    limit=1,
    order="string",
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.hooks.proxy(
    meta="string",
    token="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.<a href="src/synqly/hooks/client.py">passthrough</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.hooks.passthrough(
    web_hook_cursor="string",
    meta="string",
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

**web_hook_cursor:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_audit_log</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.query_audit_log(
    meta="string",
    limit=1,
    cursor="string",
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order.
The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_users</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.query_users(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `uid`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `email_addr[asc]` will sort the results by `email_addr` in
ascending order. The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `User` object wrapped in an OCSF Entity Management event of type Read from the token-linked identity provider. Depending
on the providers offerings, this may include additional user information, such as the user's current groups and roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.get_user(
    user_id="string",
    meta="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">query_groups</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.query_groups(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `uid`. To control the direction of the sorting, append
`[asc]` or `[desc]` to the field name. For example, `email_addr[asc]` will sort the results by `email_addr` in
ascending order. The ordering defaults to `asc` if not specified.
    
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

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_group</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.get_group(
    group_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.identity.<a href="src/synqly/identity/client.py">get_group_members</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.get_group_members(
    group_id="string",
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.enable_user(
    user_id="string",
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.disable_user(
    user_id="string",
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.force_user_password_reset(
    user_id="string",
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.identity.expire_all_user_sessions(
    user_id="string",
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

## IntegrationWebhooks
<details><summary><code>client.integration_webhooks.<a href="src/synqly/integration_webhooks/client.py">create_webhook</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.integration_webhooks.create_webhook(
    project="string",
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

**project:** `str` — Project or Table to link the webhook.
    
</dd>
</dl>

<dl>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
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

<details><summary><code>client.integration_webhooks.<a href="src/synqly/integration_webhooks/client.py">list_webhooks</a>()</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
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
<details><summary><code>client.notifications.<a href="src/synqly/notifications/client.py">get_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the `Notification` object matching `{notificationId}` from the token-linked
`Integration`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.notifications.get_message(
    notification_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/synqly/notifications/client.py">create_message</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.notifications.create_message(
    name="string",
    summary="string",
    priority="URGENT",
    project="string",
    status="string",
    description="string",
    issue_type="string",
    creator="string",
    assignee="string",
    contact="string",
    tags=["string"],
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

**summary:** `str` — Notification summary.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This field is deprecated and no longer used.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[Priority]` — Notification priority
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — Notification project
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The current status of the notification.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Notification description.
    
</dd>
</dl>

<dl>
<dd>

**issue_type:** `typing.Optional[str]` — The notification's type.
    
</dd>
</dl>

<dl>
<dd>

**creator:** `typing.Optional[str]` — The user who created this notification.
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[str]` — Who notification is assigned to.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[str]` — The notification contact information.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Associate tags with Notification
    
</dd>
</dl>

<dl>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.notifications.clear_message(
    notification_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Operations
<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">get</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.operations.get(
    operation_id="string",
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

<details><summary><code>client.operations.<a href="src/synqly/operations/client.py">create</a>(...)</code></summary>
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
import datetime

from synqly import OperationInput, OperationSchedule
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.operations.create(
    schedule=OperationSchedule(
        run_at=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        interval="string",
    ),
    operation="string",
    input=OperationInput(
        filters=["string"],
        limit=1,
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

**operation:** `str` — Name of the operation that will be run for this operation.
    
</dd>
</dl>

<dl>
<dd>

**input:** `OperationInput` — Input parameters to the operation that will be run for this operation.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[OperationSchedule]` — Run now or on the specified schedule.
    
</dd>
</dl>

<dl>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.operations.cancel(
    operation_id="string",
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
<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_investigations</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.query_investigations(
    meta="string",
    cursor="string",
    limit=1,
    order="string",
    filter="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter results by this query.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">get_investigation</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.get_investigation(
    id="string",
    meta="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">patch_investigation</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.patch_investigation(
    id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">get_evidence</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.get_evidence(
    id="string",
    meta="string",
    include_raw_data=True,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_log_providers</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.query_log_providers(
    meta="string",
    cursor="string",
    limit=1,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">post_events</a>(...)</code></summary>
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
import datetime

from synqly import Event_AccountChange
from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.accountchange import (
    Account,
    Actor,
    Api,
    AutonomousSystem,
    Cloud,
    Container,
    Device,
    DeviceHwInfo,
    Enrichment,
    Extension,
    Feature,
    Group,
    HttpRequest,
    Idp,
    Image,
    Location,
    Logger,
    Metadata,
    NetworkEndpoint,
    NetworkProxy,
    Observable,
    Organization,
    Os,
    Osint,
    Policy,
    Process,
    Product,
    Request,
    Response,
    Service,
    Session,
    Url,
    User,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.post_events(
    request=[
        Event_AccountChange(
            activity_id=1,
            activity_name="string",
            actor=Actor(
                actor_type="string",
                actor_type_id=1,
                app_name="string",
                app_uid="string",
                authorizations=[],
                groups=[],
                idp=Idp(),
                invoked_by="string",
                process=Process(),
                session=Session(),
                user=User(),
            ),
            api=Api(
                group=Group(),
                operation="string",
                request=Request(
                    uid="string",
                ),
                response=Response(),
                service=Service(),
                version="string",
            ),
            category_name="string",
            category_uid=1,
            class_uid=1,
            cloud=Cloud(
                account=Account(),
                org=Organization(),
                project_uid="string",
                provider="string",
                region="string",
                zone="string",
            ),
            count=1,
            custom_fields={"string": {"key": "value"}},
            device=Device(
                agent_list=[],
                autoscale_uid="string",
                boot_time=1,
                boot_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                container=Container(),
                created_time=1,
                created_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                desc="string",
                domain="string",
                first_seen_time=1,
                first_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                groups=[],
                hostname="string",
                hw_info=DeviceHwInfo(),
                hypervisor="string",
                image=Image(
                    uid="string",
                ),
                imei="string",
                instance_uid="string",
                interface_name="string",
                interface_uid="string",
                ip="string",
                ip_addresses=[],
                is_compliant=True,
                is_managed=True,
                is_personal=True,
                is_trusted=True,
                last_seen_time=1,
                last_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                location=Location(),
                mac="string",
                mac_addresses=[],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                name="string",
                namespace_pid=1,
                netbios_names=[],
                network_interfaces=[],
                network_status="string",
                network_status_id=1,
                org=Organization(),
                os=Os(
                    name="string",
                    type_id=1,
                ),
                owner=User(),
                region="string",
                risk_level="string",
                risk_level_id=1,
                risk_score=1,
                subnet="string",
                subnet_uid="string",
                sw_info=[],
                type="string",
                type_id=1,
                uid="string",
                uid_alt="string",
                vendor=Organization(),
                vlan_uid="string",
                vpc_uid="string",
                zone="string",
            ),
            duration=1,
            end_time=1,
            end_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            enrichments=[
                Enrichment(
                    data={"key": "value"},
                    name="string",
                    value="string",
                )
            ],
            http_request=HttpRequest(
                args="string",
                http_headers=[],
                http_method="string",
                length=1,
                referrer="string",
                uid="string",
                url=Url(),
                user_agent="string",
                user_agent_name="string",
                version="string",
                x_forwarded_for=[],
            ),
            message="string",
            metadata=Metadata(
                correlation_uid="string",
                event_code="string",
                extension=Extension(
                    name="string",
                    uid="string",
                    version="string",
                ),
                extensions=[
                    Extension(
                        name="string",
                        uid="string",
                        version="string",
                    )
                ],
                labels=["string"],
                log_level="string",
                log_name="string",
                log_provider="string",
                log_version="string",
                logged_time=1,
                logged_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                loggers=[Logger()],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                original_time="string",
                processed_time=1,
                processed_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                product=Product(
                    cpe_name="string",
                    distribution_mode="string",
                    feature=Feature(
                        name="string",
                        uid="string",
                        version="string",
                    ),
                    lang="string",
                    name="string",
                    path="string",
                    uid="string",
                    url_string="string",
                    vendor_name="string",
                    version="string",
                    workload="string",
                ),
                profiles=["string"],
                sequence=1,
                tenant_uid="string",
                uid="string",
                version="string",
            ),
            observables=[
                Observable(
                    name="string",
                    type_id=1,
                )
            ],
            osint=[
                Osint(
                    type_id=1,
                    value="string",
                )
            ],
            policy=Policy(
                desc="string",
                group=Group(),
                is_applied=True,
                name="string",
                uid="string",
                version="string",
            ),
            raw_data="string",
            severity="string",
            severity_id=1,
            src_endpoint=NetworkEndpoint(
                agent_list=[],
                autonomous_system=AutonomousSystem(),
                container=Container(),
                domain="string",
                hostname="string",
                hw_info=DeviceHwInfo(),
                instance_uid="string",
                interface_name="string",
                interface_uid="string",
                intermediate_ips=[],
                ip="string",
                location=Location(),
                mac="string",
                name="string",
                namespace_pid=1,
                os=Os(
                    name="string",
                    type_id=1,
                ),
                owner=User(),
                port=1,
                proxy_endpoint=NetworkProxy(),
                subnet_uid="string",
                svc_name="string",
                type="string",
                type_id=1,
                uid="string",
                vlan_uid="string",
                vpc_uid="string",
                zone="string",
            ),
            start_time=1,
            start_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            status="string",
            status_code="string",
            status_detail="string",
            status_id=1,
            time=1,
            time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            timezone_offset=1,
            type_name="string",
            type_uid=1,
            unmapped={"string": {"key": "value"}},
            user=User(),
            user_result=User(),
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

**request:** `typing.Sequence[Event]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_events</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.query_events(
    cursor="string",
    limit=1,
    order="string",
    filter="string",
    meta="string",
    passthrough_param="string",
    include_raw_data=True,
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**passthrough_param:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Provider-specific query to pass through to the SIEM. This is useful for advanced queries that are not
supported by the API. The keys and values are provider-specific. For example, to perform a specific query in
Rapid7 IDR, you can use the `query: "{advanced query}"` key-value pair.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` 

Include the raw data from the SIEM in the response. This is useful for debugging and troubleshooting.
Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.siem.<a href="src/synqly/siem/client.py">query_alerts</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.siem.query_alerts(
    cursor="string",
    limit=1,
    order="string",
    filter="string",
    meta="string",
    include_raw_data=True,
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_raw_data:** `typing.Optional[bool]` 

Include the raw data from the SIEM in the response. This is useful for debugging and troubleshooting.
Defaults to `false`.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.sink.<a href="src/synqly/sink/client.py">post_events</a>(...)</code></summary>
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
import datetime

from synqly import Event_AccountChange
from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.accountchange import (
    Account,
    Actor,
    Api,
    AutonomousSystem,
    Cloud,
    Container,
    Device,
    DeviceHwInfo,
    Enrichment,
    Extension,
    Feature,
    Group,
    HttpRequest,
    Idp,
    Image,
    Location,
    Logger,
    Metadata,
    NetworkEndpoint,
    NetworkProxy,
    Observable,
    Organization,
    Os,
    Osint,
    Policy,
    Process,
    Product,
    Request,
    Response,
    Service,
    Session,
    Url,
    User,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.sink.post_events(
    location="string",
    request=[
        Event_AccountChange(
            activity_id=1,
            activity_name="string",
            actor=Actor(
                actor_type="string",
                actor_type_id=1,
                app_name="string",
                app_uid="string",
                authorizations=[],
                groups=[],
                idp=Idp(),
                invoked_by="string",
                process=Process(),
                session=Session(),
                user=User(),
            ),
            api=Api(
                group=Group(),
                operation="string",
                request=Request(
                    uid="string",
                ),
                response=Response(),
                service=Service(),
                version="string",
            ),
            category_name="string",
            category_uid=1,
            class_uid=1,
            cloud=Cloud(
                account=Account(),
                org=Organization(),
                project_uid="string",
                provider="string",
                region="string",
                zone="string",
            ),
            count=1,
            custom_fields={"string": {"key": "value"}},
            device=Device(
                agent_list=[],
                autoscale_uid="string",
                boot_time=1,
                boot_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                container=Container(),
                created_time=1,
                created_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                desc="string",
                domain="string",
                first_seen_time=1,
                first_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                groups=[],
                hostname="string",
                hw_info=DeviceHwInfo(),
                hypervisor="string",
                image=Image(
                    uid="string",
                ),
                imei="string",
                instance_uid="string",
                interface_name="string",
                interface_uid="string",
                ip="string",
                ip_addresses=[],
                is_compliant=True,
                is_managed=True,
                is_personal=True,
                is_trusted=True,
                last_seen_time=1,
                last_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                location=Location(),
                mac="string",
                mac_addresses=[],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                name="string",
                namespace_pid=1,
                netbios_names=[],
                network_interfaces=[],
                network_status="string",
                network_status_id=1,
                org=Organization(),
                os=Os(
                    name="string",
                    type_id=1,
                ),
                owner=User(),
                region="string",
                risk_level="string",
                risk_level_id=1,
                risk_score=1,
                subnet="string",
                subnet_uid="string",
                sw_info=[],
                type="string",
                type_id=1,
                uid="string",
                uid_alt="string",
                vendor=Organization(),
                vlan_uid="string",
                vpc_uid="string",
                zone="string",
            ),
            duration=1,
            end_time=1,
            end_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            enrichments=[
                Enrichment(
                    data={"key": "value"},
                    name="string",
                    value="string",
                )
            ],
            http_request=HttpRequest(
                args="string",
                http_headers=[],
                http_method="string",
                length=1,
                referrer="string",
                uid="string",
                url=Url(),
                user_agent="string",
                user_agent_name="string",
                version="string",
                x_forwarded_for=[],
            ),
            message="string",
            metadata=Metadata(
                correlation_uid="string",
                event_code="string",
                extension=Extension(
                    name="string",
                    uid="string",
                    version="string",
                ),
                extensions=[
                    Extension(
                        name="string",
                        uid="string",
                        version="string",
                    )
                ],
                labels=["string"],
                log_level="string",
                log_name="string",
                log_provider="string",
                log_version="string",
                logged_time=1,
                logged_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                loggers=[Logger()],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                original_time="string",
                processed_time=1,
                processed_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                product=Product(
                    cpe_name="string",
                    distribution_mode="string",
                    feature=Feature(
                        name="string",
                        uid="string",
                        version="string",
                    ),
                    lang="string",
                    name="string",
                    path="string",
                    uid="string",
                    url_string="string",
                    vendor_name="string",
                    version="string",
                    workload="string",
                ),
                profiles=["string"],
                sequence=1,
                tenant_uid="string",
                uid="string",
                version="string",
            ),
            observables=[
                Observable(
                    name="string",
                    type_id=1,
                )
            ],
            osint=[
                Osint(
                    type_id=1,
                    value="string",
                )
            ],
            policy=Policy(
                desc="string",
                group=Group(),
                is_applied=True,
                name="string",
                uid="string",
                version="string",
            ),
            raw_data="string",
            severity="string",
            severity_id=1,
            src_endpoint=NetworkEndpoint(
                agent_list=[],
                autonomous_system=AutonomousSystem(),
                container=Container(),
                domain="string",
                hostname="string",
                hw_info=DeviceHwInfo(),
                instance_uid="string",
                interface_name="string",
                interface_uid="string",
                intermediate_ips=[],
                ip="string",
                location=Location(),
                mac="string",
                name="string",
                namespace_pid=1,
                os=Os(
                    name="string",
                    type_id=1,
                ),
                owner=User(),
                port=1,
                proxy_endpoint=NetworkProxy(),
                subnet_uid="string",
                svc_name="string",
                type="string",
                type_id=1,
                uid="string",
                vlan_uid="string",
                vpc_uid="string",
                zone="string",
            ),
            start_time=1,
            start_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            status="string",
            status_code="string",
            status_detail="string",
            status_id=1,
            time=1,
            time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            timezone_offset=1,
            type_name="string",
            type_uid=1,
            unmapped={"string": {"key": "value"}},
            user=User(),
            user_result=User(),
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

**request:** `typing.Sequence[Event]` 
    
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
<details><summary><code>client.storage.<a href="src/synqly/storage/client.py">list_files</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.storage.list_files(
    path="string",
    cursor="string",
    limit=1,
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.storage.upload_file(
    path="string",
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

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/synqly/storage/client.py">download_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads a file from the provided `{path}` in the token-linked
`Integration`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.storage.download_file(
    path="string",
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.storage.delete_file(
    path="string",
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

## Ticketing
<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_remote_fields</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all remote fields for all Projects in a ticketing integration. The response will include a list of
fields for each issue type in the ticketing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_projects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Projects` from the token-linked `Integration`.
Tickets must be created and retrieved within the context of a specific Project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.list_projects(
    cursor="string",
    limit=1,
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">query_tickets</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.query_tickets(
    meta="string",
    cursor="string",
    limit=1,
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**order:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">get_ticket</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.get_ticket(
    ticket_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_ticket</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.create_ticket(
    summary="string",
    creator="string",
    assignee="string",
    contact="string",
    description="string",
    priority="URGENT",
    due_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    completion_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    status="string",
    project="string",
    issue_type="string",
    tags=["string"],
    custom_fields={"string": {"key": "value"}},
    name="string",
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

**name:** `str` — Human-readable name for this resource
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` — Ticket summary.
    
</dd>
</dl>

<dl>
<dd>

**creator:** `typing.Optional[str]` — User who created this ticket.
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[str]` — Who ticket is assigned to.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[str]` — Ticket contact information.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Ticket description.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[Priority]` — The priority of the Ticket
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.datetime]` — The ticket's due date.
    
</dd>
</dl>

<dl>
<dd>

**completion_date:** `typing.Optional[dt.datetime]` — The ticket's complete date.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[Status]` — The current status of the ticket.
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — The ticket project.
    
</dd>
</dl>

<dl>
<dd>

**issue_type:** `typing.Optional[str]` — The ticket's type.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Associate tags with Ticket
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Dict[str, typing.Any]]` — Set custom fields for this ticket, keys are the custom field names.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">patch_ticket</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.patch_ticket(
    ticket_id="string",
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

**ticket_id:** `TicketId` 
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_attachment</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.create_attachment(
    ticket_id="string",
    file_name="string",
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

**file_name:** `str` — The name of the file.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — File contents
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_attachments_metadata</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.list_attachments_metadata(
    ticket_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">download_attachment</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.download_attachment(
    ticket_id="string",
    attachment_id="string",
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.delete_attachment(
    ticket_id="string",
    attachment_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_comments</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.list_comments(
    ticket_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_comment</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.create_comment(
    ticket_id="string",
    creator="string",
    content="string",
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

**content:** `str` — The content of the comment.
    
</dd>
</dl>

<dl>
<dd>

**creator:** `typing.Optional[str]` — Email address of user who created this ticket. Required by PagerDuty. Not supported by Jira, ServiceNow, or Torq.
    
</dd>
</dl>

<dl>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.delete_comment(
    ticket_id="string",
    comment_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">create_note</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.create_note(
    ticket_id="string",
    content="string",
    title="string",
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

**content:** `str` — The content of the note formatted as markdown.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the note.
    
</dd>
</dl>

<dl>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.delete_note(
    ticket_id="string",
    note_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_notes</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.list_notes(
    ticket_id="string",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">patch_note</a>(...)</code></summary>
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
from synqly import PatchOperation
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.patch_note(
    ticket_id="string",
    note_id="string",
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">query_escalation_policies</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.query_escalation_policies(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

<details><summary><code>client.ticketing.<a href="src/synqly/ticketing/client.py">list_on_call</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.ticketing.list_on_call(
    escalation_policy_id="string",
    meta="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_findings</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.query_findings(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to the Vulnerability Filtering Guide.
Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">create_findings</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.securityfinding import (
    Account,
    Analytic,
    Api,
    Attack,
    CisCsc,
    Cloud,
    Compliance,
    Container,
    Enrichment,
    Extension,
    Feature,
    File,
    Finding,
    Group,
    KillChainPhase,
    Logger,
    Malware,
    Metadata,
    Observable,
    Organization,
    Osint,
    Process,
    Product,
    RelatedEvent,
    Remediation,
    Request,
    ResourceDetails,
    Response,
    SecurityFinding,
    Service,
    Session,
    User,
    Vulnerability,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.create_findings(
    findings=[
        SecurityFinding(
            activity_id=1,
            activity_name="string",
            analytic=Analytic(
                category="string",
                desc="string",
                name="string",
                related_analytics=[],
                type="string",
                type_id=1,
                uid="string",
                version="string",
            ),
            api=Api(
                group=Group(),
                operation="string",
                request=Request(
                    uid="string",
                ),
                response=Response(),
                service=Service(),
                version="string",
            ),
            attacks=[Attack()],
            category_name="string",
            category_uid=1,
            cis_csc=[
                CisCsc(
                    control="string",
                )
            ],
            class_uid=1,
            cloud=Cloud(
                account=Account(),
                org=Organization(),
                project_uid="string",
                provider="string",
                region="string",
                zone="string",
            ),
            compliance=Compliance(
                compliance_references=[],
                compliance_standards=[],
                control="string",
                requirements=[],
                standards=["string"],
                status="string",
                status_code="string",
                status_detail="string",
                status_id=1,
            ),
            confidence="string",
            confidence_id=1,
            confidence_score=1,
            count=1,
            custom_fields={"string": {"key": "value"}},
            data_sources=["string"],
            duration=1,
            end_time=1,
            end_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            enrichments=[
                Enrichment(
                    data={"key": "value"},
                    name="string",
                    value="string",
                )
            ],
            evidence={"key": "value"},
            finding=Finding(
                created_time=1,
                created_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                desc="string",
                first_seen_time=1,
                first_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                last_seen_time=1,
                last_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                product_uid="string",
                related_events=[
                    RelatedEvent(
                        uid="string",
                    )
                ],
                remediation=Remediation(
                    desc="string",
                    kb_article_list=[],
                    kb_articles=[],
                    references=[],
                ),
                src_url="string",
                supporting_data={"key": "value"},
                title="string",
                types=["string"],
                uid="string",
            ),
            impact="string",
            impact_id=1,
            impact_score=1,
            kill_chain=[
                KillChainPhase(
                    phase_id=1,
                )
            ],
            malware=[
                Malware(
                    classification_ids=[],
                )
            ],
            message="string",
            metadata=Metadata(
                correlation_uid="string",
                event_code="string",
                extension=Extension(
                    name="string",
                    uid="string",
                    version="string",
                ),
                extensions=[
                    Extension(
                        name="string",
                        uid="string",
                        version="string",
                    )
                ],
                labels=["string"],
                log_level="string",
                log_name="string",
                log_provider="string",
                log_version="string",
                logged_time=1,
                logged_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                loggers=[Logger()],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                original_time="string",
                processed_time=1,
                processed_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                product=Product(
                    cpe_name="string",
                    distribution_mode="string",
                    feature=Feature(
                        name="string",
                        uid="string",
                        version="string",
                    ),
                    lang="string",
                    name="string",
                    path="string",
                    uid="string",
                    url_string="string",
                    vendor_name="string",
                    version="string",
                    workload="string",
                ),
                profiles=["string"],
                sequence=1,
                tenant_uid="string",
                uid="string",
                version="string",
            ),
            nist=["string"],
            observables=[
                Observable(
                    name="string",
                    type_id=1,
                )
            ],
            osint=[
                Osint(
                    type_id=1,
                    value="string",
                )
            ],
            process=Process(
                auid=1,
                cmd_line="string",
                container=Container(),
                created_time=1,
                created_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                egid=1,
                euid=1,
                file=File(
                    name="string",
                    type_id=1,
                ),
                group=Group(),
                integrity="string",
                integrity_id=1,
                lineage=[],
                loaded_modules=[],
                name="string",
                namespace_pid=1,
                parent_process={},
                pid=1,
                sandbox="string",
                session=Session(),
                terminated_time=1,
                terminated_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                tid=1,
                uid="string",
                user=User(),
                xattributes={},
            ),
            raw_data="string",
            resources=[ResourceDetails()],
            risk_level="string",
            risk_level_id=1,
            risk_score=1,
            severity="string",
            severity_id=1,
            start_time=1,
            start_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            state="string",
            state_id=1,
            status="string",
            status_code="string",
            status_detail="string",
            status_id=1,
            time=1,
            time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            timezone_offset=1,
            type_name="string",
            type_uid=1,
            unmapped={"string": {"key": "value"}},
            vulnerabilities=[Vulnerability()],
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

**findings:** `typing.Sequence[SecurityFinding]` 
    
</dd>
</dl>

<dl>
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
from synqly import ProviderSpecificFindingState_Nucleus
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.update_finding(
    finding_id="string",
    severity_id=1,
    severity="critical",
    state="Unknown",
    unmapped=ProviderSpecificFindingState_Nucleus(),
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

**severity_id:** `SeverityId` 
    
</dd>
</dl>

<dl>
<dd>

**severity:** `typing.Optional[VulnerabilitySeverityFilterValue]` — severity of the finding
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[VulnerabilityStateFilterValue]` — state of the finding
    
</dd>
</dl>

<dl>
<dd>

**unmapped:** `typing.Optional[ProviderSpecificFindingState]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_assets</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.query_assets(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**filter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Filter results by this query. For more information on filtering, refer to the Vulnerability Filtering Guide.
Defaults to no filter. If used more than once, the queries are ANDed together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">create_asset</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.inventoryinfo import (
    Account,
    Actor,
    Agent,
    Api,
    Cloud,
    Container,
    Device,
    DeviceHwInfo,
    Display,
    Enrichment,
    Extension,
    Fingerprint,
    Group,
    Idp,
    Image,
    InventoryInfo,
    KeyboardInfo,
    Location,
    Logger,
    Metadata,
    NetworkInterface,
    Observable,
    Organization,
    Os,
    Osint,
    Process,
    Product,
    Request,
    Response,
    Service,
    Session,
    User,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.create_asset(
    asset=InventoryInfo(
        activity_id=1,
        activity_name="string",
        actor=Actor(
            actor_type="string",
            actor_type_id=1,
            app_name="string",
            app_uid="string",
            authorizations=[],
            groups=[],
            idp=Idp(),
            invoked_by="string",
            process=Process(),
            session=Session(),
            user=User(),
        ),
        api=Api(
            group=Group(),
            operation="string",
            request=Request(
                uid="string",
            ),
            response=Response(),
            service=Service(),
            version="string",
        ),
        category_name="string",
        category_uid=1,
        class_uid=1,
        cloud=Cloud(
            account=Account(),
            org=Organization(),
            project_uid="string",
            provider="string",
            region="string",
            zone="string",
        ),
        count=1,
        custom_fields={"string": {"key": "value"}},
        device=Device(
            agent_list=[Agent()],
            autoscale_uid="string",
            boot_time=1,
            boot_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            container=Container(
                hash=Fingerprint(
                    algorithm_id=1,
                    value="string",
                ),
                image=Image(
                    uid="string",
                ),
                name="string",
                network_driver="string",
                orchestrator="string",
                pod_uuid="string",
                runtime="string",
                size=1,
                tag="string",
                uid="string",
            ),
            created_time=1,
            created_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            desc="string",
            domain="string",
            first_seen_time=1,
            first_seen_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            groups=[Group()],
            hostname="string",
            hw_info=DeviceHwInfo(
                bios_date="string",
                bios_manufacturer="string",
                bios_uid="string",
                bios_ver="string",
                chassis="string",
                cpu_bits=1,
                cpu_cores=1,
                cpu_count=1,
                cpu_speed=1,
                cpu_type="string",
                desktop_display=Display(),
                keyboard_info=KeyboardInfo(),
                ram_size=1,
                serial_number="string",
            ),
            hypervisor="string",
            image=Image(
                uid="string",
            ),
            imei="string",
            instance_uid="string",
            interface_name="string",
            interface_uid="string",
            ip="string",
            ip_addresses=["string"],
            is_compliant=True,
            is_managed=True,
            is_personal=True,
            is_trusted=True,
            last_seen_time=1,
            last_seen_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            location=Location(
                city="string",
                continent="string",
                coordinates=[],
                country="string",
                desc="string",
                geohash="string",
                is_on_premises=True,
                isp="string",
                lat=1.1,
                long_=1.1,
                postal_code="string",
                provider="string",
                region="string",
                timezone="string",
            ),
            mac="string",
            mac_addresses=["string"],
            modified_time=1,
            modified_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            name="string",
            namespace_pid=1,
            netbios_names=["string"],
            network_interfaces=[
                NetworkInterface(
                    type_id=1,
                )
            ],
            network_status="string",
            network_status_id=1,
            org=Organization(),
            os=Os(
                build="string",
                country="string",
                cpe_name="string",
                cpu_bits=1,
                edition="string",
                lang="string",
                name="string",
                sp_name="string",
                sp_ver=1,
                type="string",
                type_id=1,
                version="string",
            ),
            owner=User(),
            region="string",
            risk_level="string",
            risk_level_id=1,
            risk_score=1,
            subnet="string",
            subnet_uid="string",
            sw_info=[
                Product(
                    vendor_name="string",
                )
            ],
            type="string",
            type_id=1,
            uid="string",
            uid_alt="string",
            vendor=Organization(),
            vlan_uid="string",
            vpc_uid="string",
            zone="string",
        ),
        duration=1,
        end_time=1,
        end_time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        enrichments=[
            Enrichment(
                data={"key": "value"},
                name="string",
                value="string",
            )
        ],
        message="string",
        metadata=Metadata(
            correlation_uid="string",
            event_code="string",
            extension=Extension(
                name="string",
                uid="string",
                version="string",
            ),
            extensions=[
                Extension(
                    name="string",
                    uid="string",
                    version="string",
                )
            ],
            labels=["string"],
            log_level="string",
            log_name="string",
            log_provider="string",
            log_version="string",
            logged_time=1,
            logged_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            loggers=[Logger()],
            modified_time=1,
            modified_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            original_time="string",
            processed_time=1,
            processed_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            product=Product(
                vendor_name="string",
            ),
            profiles=["string"],
            sequence=1,
            tenant_uid="string",
            uid="string",
            version="string",
        ),
        observables=[
            Observable(
                name="string",
                type_id=1,
            )
        ],
        osint=[
            Osint(
                type_id=1,
                value="string",
            )
        ],
        raw_data="string",
        severity="string",
        severity_id=1,
        start_time=1,
        start_time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        status="string",
        status_code="string",
        status_detail="string",
        status_id=1,
        time=1,
        time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        timezone_offset=1,
        type_name="string",
        type_uid=1,
        unmapped={"string": {"key": "value"}},
    ),
    source_name="string",
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

**asset:** `Asset` — Asset to create in the vulnerability scanning system.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `str` — Name of the source that created the asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">update_asset</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.inventoryinfo import (
    Account,
    Actor,
    Agent,
    Api,
    Cloud,
    Container,
    Device,
    DeviceHwInfo,
    Display,
    Enrichment,
    Extension,
    Fingerprint,
    Group,
    Idp,
    Image,
    InventoryInfo,
    KeyboardInfo,
    Location,
    Logger,
    Metadata,
    NetworkInterface,
    Observable,
    Organization,
    Os,
    Osint,
    Process,
    Product,
    Request,
    Response,
    Service,
    Session,
    User,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.update_asset(
    asset_id="string",
    asset=InventoryInfo(
        activity_id=1,
        activity_name="string",
        actor=Actor(
            actor_type="string",
            actor_type_id=1,
            app_name="string",
            app_uid="string",
            authorizations=[],
            groups=[],
            idp=Idp(),
            invoked_by="string",
            process=Process(),
            session=Session(),
            user=User(),
        ),
        api=Api(
            group=Group(),
            operation="string",
            request=Request(
                uid="string",
            ),
            response=Response(),
            service=Service(),
            version="string",
        ),
        category_name="string",
        category_uid=1,
        class_uid=1,
        cloud=Cloud(
            account=Account(),
            org=Organization(),
            project_uid="string",
            provider="string",
            region="string",
            zone="string",
        ),
        count=1,
        custom_fields={"string": {"key": "value"}},
        device=Device(
            agent_list=[Agent()],
            autoscale_uid="string",
            boot_time=1,
            boot_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            container=Container(
                hash=Fingerprint(
                    algorithm_id=1,
                    value="string",
                ),
                image=Image(
                    uid="string",
                ),
                name="string",
                network_driver="string",
                orchestrator="string",
                pod_uuid="string",
                runtime="string",
                size=1,
                tag="string",
                uid="string",
            ),
            created_time=1,
            created_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            desc="string",
            domain="string",
            first_seen_time=1,
            first_seen_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            groups=[Group()],
            hostname="string",
            hw_info=DeviceHwInfo(
                bios_date="string",
                bios_manufacturer="string",
                bios_uid="string",
                bios_ver="string",
                chassis="string",
                cpu_bits=1,
                cpu_cores=1,
                cpu_count=1,
                cpu_speed=1,
                cpu_type="string",
                desktop_display=Display(),
                keyboard_info=KeyboardInfo(),
                ram_size=1,
                serial_number="string",
            ),
            hypervisor="string",
            image=Image(
                uid="string",
            ),
            imei="string",
            instance_uid="string",
            interface_name="string",
            interface_uid="string",
            ip="string",
            ip_addresses=["string"],
            is_compliant=True,
            is_managed=True,
            is_personal=True,
            is_trusted=True,
            last_seen_time=1,
            last_seen_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            location=Location(
                city="string",
                continent="string",
                coordinates=[],
                country="string",
                desc="string",
                geohash="string",
                is_on_premises=True,
                isp="string",
                lat=1.1,
                long_=1.1,
                postal_code="string",
                provider="string",
                region="string",
                timezone="string",
            ),
            mac="string",
            mac_addresses=["string"],
            modified_time=1,
            modified_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            name="string",
            namespace_pid=1,
            netbios_names=["string"],
            network_interfaces=[
                NetworkInterface(
                    type_id=1,
                )
            ],
            network_status="string",
            network_status_id=1,
            org=Organization(),
            os=Os(
                build="string",
                country="string",
                cpe_name="string",
                cpu_bits=1,
                edition="string",
                lang="string",
                name="string",
                sp_name="string",
                sp_ver=1,
                type="string",
                type_id=1,
                version="string",
            ),
            owner=User(),
            region="string",
            risk_level="string",
            risk_level_id=1,
            risk_score=1,
            subnet="string",
            subnet_uid="string",
            sw_info=[
                Product(
                    vendor_name="string",
                )
            ],
            type="string",
            type_id=1,
            uid="string",
            uid_alt="string",
            vendor=Organization(),
            vlan_uid="string",
            vpc_uid="string",
            zone="string",
        ),
        duration=1,
        end_time=1,
        end_time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        enrichments=[
            Enrichment(
                data={"key": "value"},
                name="string",
                value="string",
            )
        ],
        message="string",
        metadata=Metadata(
            correlation_uid="string",
            event_code="string",
            extension=Extension(
                name="string",
                uid="string",
                version="string",
            ),
            extensions=[
                Extension(
                    name="string",
                    uid="string",
                    version="string",
                )
            ],
            labels=["string"],
            log_level="string",
            log_name="string",
            log_provider="string",
            log_version="string",
            logged_time=1,
            logged_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            loggers=[Logger()],
            modified_time=1,
            modified_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            original_time="string",
            processed_time=1,
            processed_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            product=Product(
                vendor_name="string",
            ),
            profiles=["string"],
            sequence=1,
            tenant_uid="string",
            uid="string",
            version="string",
        ),
        observables=[
            Observable(
                name="string",
                type_id=1,
            )
        ],
        osint=[
            Osint(
                type_id=1,
                value="string",
            )
        ],
        raw_data="string",
        severity="string",
        severity_id=1,
        start_time=1,
        start_time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        status="string",
        status_code="string",
        status_detail="string",
        status_id=1,
        time=1,
        time_dt=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        timezone_offset=1,
        type_name="string",
        type_uid=1,
        unmapped={"string": {"key": "value"}},
    ),
    source_name="string",
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

**asset:** `Asset` — Asset to create in the vulnerability scanning system.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `str` — Name of the source that created the asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">query_scans</a>(...)</code></summary>
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
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.query_scans(
    meta="string",
    limit=1,
    cursor="string",
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

**meta:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Add metadata to the response by invoking meta functions. Documentation for meta functions is available at https://docs.synqly.com/api-reference/meta-functions. Not all meta function are available at every endpoint.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">get_scan_activity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of activity generated by a configured scan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.get_scan_activity(
    scan_id="string",
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

**scan_id:** `str` — ID of the scan to get its activity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vulnerabilities.<a href="src/synqly/vulnerabilities/client.py">upload_scan</a>(...)</code></summary>
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
import datetime

from synqly.client import SynqlyEngine
from synqly.ocsf.v_1_3_0.inventoryinfo import (
    Account,
    Actor,
    Agent,
    Api,
    Cloud,
    Container,
    Device,
    DeviceHwInfo,
    Display,
    Enrichment,
    Extension,
    Fingerprint,
    Group,
    Idp,
    Image,
    InventoryInfo,
    KeyboardInfo,
    Location,
    Logger,
    Metadata,
    NetworkInterface,
    Observable,
    Organization,
    Os,
    Osint,
    Process,
    Product,
    Request,
    Response,
    Service,
    Session,
    User,
)

client = SynqlyEngine(
    token="YOUR_TOKEN",
)
client.vulnerabilities.upload_scan(
    assets=[
        InventoryInfo(
            activity_id=1,
            activity_name="string",
            actor=Actor(
                actor_type="string",
                actor_type_id=1,
                app_name="string",
                app_uid="string",
                authorizations=[],
                groups=[],
                idp=Idp(),
                invoked_by="string",
                process=Process(),
                session=Session(),
                user=User(),
            ),
            api=Api(
                group=Group(),
                operation="string",
                request=Request(
                    uid="string",
                ),
                response=Response(),
                service=Service(),
                version="string",
            ),
            category_name="string",
            category_uid=1,
            class_uid=1,
            cloud=Cloud(
                account=Account(),
                org=Organization(),
                project_uid="string",
                provider="string",
                region="string",
                zone="string",
            ),
            count=1,
            custom_fields={"string": {"key": "value"}},
            device=Device(
                agent_list=[Agent()],
                autoscale_uid="string",
                boot_time=1,
                boot_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                container=Container(
                    hash=Fingerprint(
                        algorithm_id=1,
                        value="string",
                    ),
                    image=Image(
                        uid="string",
                    ),
                    name="string",
                    network_driver="string",
                    orchestrator="string",
                    pod_uuid="string",
                    runtime="string",
                    size=1,
                    tag="string",
                    uid="string",
                ),
                created_time=1,
                created_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                desc="string",
                domain="string",
                first_seen_time=1,
                first_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                groups=[Group()],
                hostname="string",
                hw_info=DeviceHwInfo(
                    bios_date="string",
                    bios_manufacturer="string",
                    bios_uid="string",
                    bios_ver="string",
                    chassis="string",
                    cpu_bits=1,
                    cpu_cores=1,
                    cpu_count=1,
                    cpu_speed=1,
                    cpu_type="string",
                    desktop_display=Display(),
                    keyboard_info=KeyboardInfo(),
                    ram_size=1,
                    serial_number="string",
                ),
                hypervisor="string",
                image=Image(
                    uid="string",
                ),
                imei="string",
                instance_uid="string",
                interface_name="string",
                interface_uid="string",
                ip="string",
                ip_addresses=["string"],
                is_compliant=True,
                is_managed=True,
                is_personal=True,
                is_trusted=True,
                last_seen_time=1,
                last_seen_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                location=Location(
                    city="string",
                    continent="string",
                    coordinates=[],
                    country="string",
                    desc="string",
                    geohash="string",
                    is_on_premises=True,
                    isp="string",
                    lat=1.1,
                    long_=1.1,
                    postal_code="string",
                    provider="string",
                    region="string",
                    timezone="string",
                ),
                mac="string",
                mac_addresses=["string"],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                name="string",
                namespace_pid=1,
                netbios_names=["string"],
                network_interfaces=[
                    NetworkInterface(
                        type_id=1,
                    )
                ],
                network_status="string",
                network_status_id=1,
                org=Organization(),
                os=Os(
                    build="string",
                    country="string",
                    cpe_name="string",
                    cpu_bits=1,
                    edition="string",
                    lang="string",
                    name="string",
                    sp_name="string",
                    sp_ver=1,
                    type="string",
                    type_id=1,
                    version="string",
                ),
                owner=User(),
                region="string",
                risk_level="string",
                risk_level_id=1,
                risk_score=1,
                subnet="string",
                subnet_uid="string",
                sw_info=[
                    Product(
                        vendor_name="string",
                    )
                ],
                type="string",
                type_id=1,
                uid="string",
                uid_alt="string",
                vendor=Organization(),
                vlan_uid="string",
                vpc_uid="string",
                zone="string",
            ),
            duration=1,
            end_time=1,
            end_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            enrichments=[
                Enrichment(
                    data={"key": "value"},
                    name="string",
                    value="string",
                )
            ],
            message="string",
            metadata=Metadata(
                correlation_uid="string",
                event_code="string",
                extension=Extension(
                    name="string",
                    uid="string",
                    version="string",
                ),
                extensions=[
                    Extension(
                        name="string",
                        uid="string",
                        version="string",
                    )
                ],
                labels=["string"],
                log_level="string",
                log_name="string",
                log_provider="string",
                log_version="string",
                logged_time=1,
                logged_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                loggers=[Logger()],
                modified_time=1,
                modified_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                original_time="string",
                processed_time=1,
                processed_time_dt=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                product=Product(
                    vendor_name="string",
                ),
                profiles=["string"],
                sequence=1,
                tenant_uid="string",
                uid="string",
                version="string",
            ),
            observables=[
                Observable(
                    name="string",
                    type_id=1,
                )
            ],
            osint=[
                Osint(
                    type_id=1,
                    value="string",
                )
            ],
            raw_data="string",
            severity="string",
            severity_id=1,
            start_time=1,
            start_time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            status="string",
            status_code="string",
            status_detail="string",
            status_id=1,
            time=1,
            time_dt=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            timezone_offset=1,
            type_name="string",
            type_uid=1,
            unmapped={"string": {"key": "value"}},
        )
    ],
    source_name="string",
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

**assets:** `typing.Sequence[Asset]` — Assets and optional findings to upload in the vulnerability scanning system.
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[str]` — Name of the source for this scan, such as a tool or process. Does not have to be unique, defaults to `Integration import`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

