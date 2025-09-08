# Synqly Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Synqly%2FPython)
[![pypi](https://img.shields.io/pypi/v/synqly)](https://pypi.python.org/pypi/synqly)

The Synqly Python library provides convenient access to the Synqly APIs from Python.

## Installation

```sh
pip install synqly
```

## Usage

Instantiate and use the client with the following:

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

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio
import datetime

from synqly.client import AsyncSynqlyEngine
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

client = AsyncSynqlyEngine(
    token="YOUR_TOKEN",
)


async def main() -> None:
    await client.assets.create_asset(
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


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from .api_error import ApiError

try:
    client.assets.create_asset(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.assets.create_asset(...,{
    max_retries=1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from synqly.client import SynqlyEngine

client = SynqlyEngine(..., { timeout=20.0 }, )


# Override timeout for a specific method
client.assets.create_asset(...,{
    timeout_in_seconds=1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from synqly.client import SynqlyEngine

client = SynqlyEngine(
    ...,
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
