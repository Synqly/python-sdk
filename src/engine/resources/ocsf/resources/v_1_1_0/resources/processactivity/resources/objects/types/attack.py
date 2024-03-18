# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .sub_technique import SubTechnique
from .tactic import Tactic
from .technique import Technique

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Attack(pydantic.BaseModel):
    """
    The <a target='_blank' href='https://attack.mitre.org'>MITRE ATT&CK®</a> object describes the tactic, technique & sub-technique associated to an attack as defined in <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a>.
    """

    sub_technique: typing.Optional[SubTechnique] = pydantic.Field(default=None)
    """
    The Sub Technique object describes the sub technique ID and/or name associated to an attack, as defined by <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a>.
    """

    tactic: typing.Optional[Tactic] = pydantic.Field(default=None)
    """
    The Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a>.
    """

    tactics: typing.Optional[typing.List[Tactic]] = pydantic.Field(default=None)
    """
    The Tactic object describes the tactic ID and/or tactic name that are associated with the attack technique, as defined by <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a>.
    """

    technique: typing.Optional[Technique] = pydantic.Field(default=None)
    """
    The Technique object describes the technique ID and/or name associated to an attack, as defined by <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a>.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The <a target='_blank' href='https://attack.mitre.org/wiki/ATT&CK_Matrix'>ATT&CK Matrix<sup>TM</sup></a> version.
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