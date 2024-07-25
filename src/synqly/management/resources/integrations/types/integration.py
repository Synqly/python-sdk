# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...accounts.types.account import Account
from ...accounts.types.account_id import AccountId
from ...capabilities_base.types.category_id import CategoryId
from ...common.types.base import Base
from ...integration_base.types.integration_id import IntegrationId
from ...integration_points.types.integration_point import IntegrationPoint
from ...integration_points.types.integration_point_id import IntegrationPointId
from ...providers_generated.types.provider_config import ProviderConfig
from ...token_base.types.token_id import TokenId
from .bridge_selector import BridgeSelector

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Integration(Base):
    """
    Connects an Account to an external service
    """

    id: IntegrationId
    fullname: str = pydantic.Field()
    """
    Human friendly display name for this integration.
    """

    refresh_token_id: TokenId = pydantic.Field()
    """
    Integration refresh token id
    """

    account_id: AccountId = pydantic.Field()
    """
    Account associated with this integration. Use the expand=account parameter with the List and ListAccount APIs to expand the Account to the full object
    """

    account: typing.Optional[Account] = pydantic.Field(default=None)
    """
    When using the expand option on the List or ListAccount APIs, the full account object is included in the response
    """

    category: CategoryId = pydantic.Field()
    """
    Id of the Connector Category for this Integration.
    """

    provider_config: ProviderConfig = pydantic.Field()
    """
    Provider configuration for this Integration.
    """

    provider_fullname: str = pydantic.Field()
    """
    Human friendly display name for the provider.
    """

    provider_type: str = pydantic.Field()
    """
    Type of the provider for this Integration.
    """

    integration_point_id: typing.Optional[IntegrationPointId] = pydantic.Field(default=None)
    """
    Integration Point associated with this integration. Use the expand=integration_point parameter with the List and ListAccount APIs to expand the Integration Point to the full object
    """

    integration_point: typing.Optional[IntegrationPoint] = pydantic.Field(default=None)
    """
    When using the expand option on the List or ListAccount APIs, the full integration_point object is included in the response
    """

    bridge_selector: typing.Optional[BridgeSelector] = pydantic.Field(default=None)
    """
    Use a Bridge to connect to the provider.
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
