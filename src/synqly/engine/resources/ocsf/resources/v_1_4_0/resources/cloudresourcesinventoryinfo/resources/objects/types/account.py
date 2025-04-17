# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .account_type_id import AccountTypeId
from .key_value_object import KeyValueObject

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Account(pydantic.BaseModel):
    """
    The Account object contains details about the account that initiated or performed a specific activity within a system or application. Additionally, the Account object refers to logical Cloud and Software-as-a-Service (SaaS) based containers such as AWS Accounts, Azure Subscriptions, Oracle Cloud Compartments, Google Cloud Projects, and otherwise.
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of labels associated to the account.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account (e.g. <code> GCP Project name </code>, <code> Linux Account name </code> or <code> AWS Account name</code>).
    """

    tags: typing.Optional[typing.List[KeyValueObject]] = pydantic.Field(default=None)
    """
    The list of tags; <code>{key:value}</code> pairs associated to the account.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account type, normalized to the caption of 'account_type_id'. In the case of 'Other', it is defined by the event source.
    """

    type_id: typing.Optional[AccountTypeId] = pydantic.Field(default=None)
    """
    The normalized account type identifier.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the account (e.g. <code> AWS Account ID </code>, <code> OCID </code>, <code> GCP Project ID </code>, <code> Azure Subscription ID </code>, <code> Google Workspace Customer ID </code>, or <code> M365 Tenant UID</code>).
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
