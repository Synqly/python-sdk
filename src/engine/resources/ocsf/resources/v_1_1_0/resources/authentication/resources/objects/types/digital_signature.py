# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from .certificate import Certificate
from .digital_signature_algorithm_id import DigitalSignatureAlgorithmId
from .fingerprint import Fingerprint

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DigitalSignature(pydantic.BaseModel):
    """
    The Digital Signature object contains information about the cryptographic mechanism used to verify the authenticity, integrity, and origin of the file or application.
    """

    algorithm: typing.Optional[str] = pydantic.Field(default=None)
    """
    The digital signature algorithm used to create the signature, normalized to the caption of 'algorithm_id'. In the case of 'Other', it is defined by the event source.
    """

    algorithm_id: DigitalSignatureAlgorithmId = pydantic.Field()
    """
    The identifier of the normalized digital signature algorithm.
    """

    certificate: typing.Optional[Certificate] = pydantic.Field(default=None)
    """
    The certificate object containing information about the digital certificate.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the digital signature was created.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the digital signature was created.
    """

    developer_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The developer ID on the certificate that signed the file.
    """

    digest: typing.Optional[Fingerprint] = pydantic.Field(default=None)
    """
    The message digest attribute contains the fixed length message hash representation and the corresponding hashing algorithm information.
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
