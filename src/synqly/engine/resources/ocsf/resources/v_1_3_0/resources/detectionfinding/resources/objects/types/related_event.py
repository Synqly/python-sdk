# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .attack import Attack
from .kill_chain_phase import KillChainPhase
from .observable import Observable

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RelatedEvent(pydantic.BaseModel):
    """
    The Related Event object describes an OCSF event related to a finding.
    """

    attacks: typing.Optional[typing.List[Attack]] = pydantic.Field(default=None)
    """
    An array of <a target='_blank' href='https://attack.mitre.org'>MITRE ATT&CK®</a> objects describing the tactics, techniques & sub-techniques identified by a security control or finding.
    """

    kill_chain: typing.Optional[typing.List[KillChainPhase]] = pydantic.Field(default=None)
    """
    The <a target='_blank' href='https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html'>Cyber Kill Chain®</a> provides a detailed description of each phase and its associated activities within the broader context of a cyber attack.
    """

    observables: typing.Optional[typing.List[Observable]] = pydantic.Field(default=None)
    """
    The observables associated with the event or a finding.
    """

    product_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the product that reported the related event.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the related event, as defined by <code>type_uid</code>. <p>For example: <code>Process Activity: Launch.</code></p>
    """

    type_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the related OCSF event, as defined by <code>type_uid</code>. <p>For example: <code>Process Activity: Launch.</code></p>
    """

    type_uid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier of the related OCSF event type. <p>For example: <code>100701.</code></p>
    """

    uid: str = pydantic.Field()
    """
    The unique identifier of the related OCSF event. This value must be equal to <code>metadata.uid</code> in the corresponding related event.
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
