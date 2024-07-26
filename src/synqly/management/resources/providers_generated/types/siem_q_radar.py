# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .q_radar_credential import QRadarCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SiemQRadar(pydantic.BaseModel):
    """
    Configuration for IBM QRadar as a SIEM Provider.
    """

    collection_port: int = pydantic.Field()
    """
    The QRadar HTTP Receiver URL, stored as a secret. This URL has a special port in QRadar and is stored in a credential to protect that information. See https://www.youtube.com/watch?v=UEBLVVNpyfg for a demonstration of setting up and mapping and HTTP Receiver in QRadar.
    """

    credential: QRadarCredential
    skip_tls_verify: bool = pydantic.Field()
    """
    If true, skips verification of the QRadar server's TLS certificate. Defaults to false.
    """

    url: str = pydantic.Field()
    """
    URL for the QRadar instance. This should be the base URL instance, without any path components and must be HTTPS. For example, "https://qradar.westus2.cloudapp.azure.com".
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
