# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .splunk_hec_token import SplunkHecToken
from .splunk_search_credential import SplunkSearchCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SiemSplunk(pydantic.BaseModel):
    """
    Configuration for Splunk as a SIEM Provider. This integration allows sending data to Splunk using an HTTP Event Collector (HEC). Additionally, it can be used to query Splunk using the Splunk Search Service.
    """

    hec_credential: typing.Optional[SplunkHecToken] = pydantic.Field(default=None)
    """
    Optional token credential to use for connecting to the Splunk HEC service. If not provided, sending events to Splunk is disabled.
    """

    hec_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for the Splunk HEC endpoint. This must include the full path to the HEC endpoint. For example, "https://tenant.cloud.splunk.com:8088/services_collector_event".
    """

    index: typing.Optional[str] = pydantic.Field(default=None)
    """
    Splunk index to send events to. If not provided, will use the default index for the Splunk collector.
    """

    search_service_credential: SplunkSearchCredential = pydantic.Field()
    """
    Token credential used for connecting to the Splunk search service.
    """

    search_service_url: str = pydantic.Field()
    """
    URL used for connecting to the Splunk search service.
    """

    skip_tls_verify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, skips verification of the Splunk server's TLS certificate.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Splunk source to send events to. If not provided, will use the default source for the Splunk collector.
    """

    source_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Splunk source type to send events to. If not provided, will use the default source type for the Splunk collector.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
