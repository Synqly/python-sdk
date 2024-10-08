# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .compliance_status_id import ComplianceStatusId
from .kb_article import KbArticle

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Compliance(pydantic.BaseModel):
    """
    The Compliance object contains information about Industry and Regulatory Framework standards, controls and requirements.
    """

    compliance_references: typing.Optional[typing.List[KbArticle]] = pydantic.Field(default=None)
    """
    A list of sources of information or tools that help organizations understand, interpret, and implement compliance standards. They provide guidance, best practices, and examples.
    """

    compliance_standards: typing.Optional[typing.List[KbArticle]] = pydantic.Field(default=None)
    """
    A list of established guidelines or criteria that define specific requirements an organization must follow.
    """

    control: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Control is prescriptive, prioritized, and simplified set of best practices that one can use to strengthen their cybersecurity posture. e.g. AWS SecurityHub Controls, CIS Controls.
    """

    requirements: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of requirements associated to a specific control in an industry or regulatory framework. e.g. <code> NIST.800-53.r5 AU-10 </code>
    """

    standards: typing.List[str] = pydantic.Field()
    """
    Security standards are a set of criteria organizations can follow to protect sensitive and confidential information. e.g. <code>NIST SP 800-53, CIS AWS Foundations Benchmark v1.4.0, ISO/IEC 27001</code>
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The resultant status of the compliance check normalized to the caption of the <code>status_id</code> value. In the case of 'Other', it is defined by the event source.
    """

    status_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The resultant status code of the compliance check.
    """

    status_detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    The contextual description of the status, status_code values.
    """

    status_id: typing.Optional[ComplianceStatusId] = pydantic.Field(default=None)
    """
    The normalized status identifier of the compliance check.
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
