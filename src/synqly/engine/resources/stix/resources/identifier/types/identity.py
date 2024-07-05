# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from ...common.types.common_properties import CommonProperties
from ...open_vocab.types.identity_class_ov import IdentityClassOv

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Identity(CommonProperties):
    type: str = pydantic.Field()
    """
    The value of this property MUST be identity.
    """

    name: str = pydantic.Field()
    """
    The name of this Identity. When referring to a specific entity (e.g., an individual or organization), this property SHOULD contain the canonical name of the specific entity.
    """

    description: typing.Optional[str] = None
    roles: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list of roles that this Identity performs. No open vocabulary is yet defined for this property.
    """

    identity_class: typing.Optional[IdentityClassOv] = None

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
