# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .account import Account
from .organization import Organization

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Cloud(pydantic.BaseModel):
    """
    The Cloud object contains information about a cloud or Software-as-a-Service account or similar construct, such as AWS Account ID, regions, organizations, folders, compartments, tenants, etc.
    """

    account: typing.Optional[Account] = pydantic.Field(default=None)
    """
    The account object describes details about the account that was the source or target of the activity.
    """

    cloud_partition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The canonical cloud partition name to which the region is assigned (e.g. AWS Partitions: aws, aws-cn, aws-us-gov).
    """

    org: typing.Optional[Organization] = pydantic.Field(default=None)
    """
    Organization and org unit relevant to the event or object.
    """

    project_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of a Cloud project.
    """

    provider: str = pydantic.Field()
    """
    The unique name of the Cloud services provider, such as AWS, MS Azure, GCP, etc.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the cloud region, as defined by the cloud provider.
    """

    zone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The availability zone in the cloud region, as defined by the cloud provider.
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
