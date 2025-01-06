# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .elasticsearch_auth_options import ElasticsearchAuthOptions
from .elasticsearch_credential import ElasticsearchCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SiemElasticsearch(pydantic.BaseModel):
    """
    Configuration for Elasticsearch search and analytics engine. Supports both managed and self-hosted Elasticsearch deployments
    """

    auth_options: typing.Optional[ElasticsearchAuthOptions] = None
    create_index: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional. The index or data stream to use when writing events. Defaults to the 'index' setting if not set.
    """

    credential: ElasticsearchCredential
    index: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional. The index, data stream, or index alias to read events from.
    """

    skip_tls_verify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, skips verification of the Elasticsearch server's TLS certificate.
    """

    url: str = pydantic.Field()
    """
    URL for the Elasticsearch API. This should be the base URL for the API, without any path components and must be HTTPS. For example, "https://tenant.elastic.com".
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
