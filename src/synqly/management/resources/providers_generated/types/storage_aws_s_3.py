# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...transforms.types.transform_id import TransformId
from .aws_s_3_credential import AwsS3Credential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class StorageAwsS3(pydantic.BaseModel):
    """
    Configuration for AWS S3 as a Storage Provider
    """

    bucket: str = pydantic.Field()
    """
    Name of the AWS S3 bucket where files are stored.
    """

    credential: AwsS3Credential
    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Endpoint used for connecting to the external service. If not provided, will connect to the default endpoint for the Provider.
    """

    region: str = pydantic.Field()
    """
    AWS region where the S3 bucket is located.
    """

    transforms: typing.Optional[typing.List[TransformId]] = pydantic.Field(default=None)
    """
    Optional list of transformations used to modify requests before they are sent to the external service.
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
