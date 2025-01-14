# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...account_base.types.account_id import AccountId
from ...common.types.base import Base
from ...integration_base.types.integration_id import IntegrationId
from ...integration_points.types.integration_point_id import IntegrationPointId
from ...organization_webhook_base.types.webhook_id import WebhookId
from .credential_config import CredentialConfig
from .credential_id import CredentialId
from .managed_type import ManagedType
from .owner_type import OwnerType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Credential(Base):
    """
    Credential to access an integration. Each credential is owned by an Account, Integration, IntegrationPoint or OrganizationWebhook.
    """

    id: CredentialId
    account_id: typing.Optional[AccountId] = pydantic.Field(default=None)
    """
    Account that manages this credential.
    """

    integration_id: typing.Optional[IntegrationId] = pydantic.Field(default=None)
    """
    Integration associated with this credential.
    """

    integration_point_id: typing.Optional[IntegrationPointId] = pydantic.Field(default=None)
    """
    Integration Point associated with this credential.
    """

    organization_webhook_id: typing.Optional[WebhookId] = pydantic.Field(default=None)
    """
    Organization Webhook associated with this credential.
    """

    owner_type: OwnerType = pydantic.Field()
    """
    One of `account` or `integration_point`.
    """

    fullname: str = pydantic.Field()
    """
    Human friendly display name for this Credential
    """

    config: typing.Optional[CredentialConfig] = pydantic.Field(default=None)
    """
    Credential configuration
    """

    expires: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Time when this credential expires and can no longer be used again.
    """

    managed: ManagedType = pydantic.Field()
    """
    Field is set by the management process. Determines lifecycle and ownership of the credential.
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
        allow_population_by_field_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
