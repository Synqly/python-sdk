# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.url_string import UrlString
from .cvss_depth import CvssDepth
from .metric import Metric

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Cvss(pydantic.BaseModel):
    """
    The Common Vulnerability Scoring System (<a target='_blank' href='https://www.first.org/cvss/'>CVSS</a>) object provides a way to capture the principal characteristics of a vulnerability and produce a numerical score reflecting its severity.
    """

    base_score: float = pydantic.Field()
    """
    The CVSS base score. For example: <code>9.1</code>.
    """

    depth: typing.Optional[CvssDepth] = pydantic.Field(default=None)
    """
    The CVSS depth represents a depth of the equation used to calculate CVSS score.
    """

    metrics: typing.Optional[typing.List[Metric]] = pydantic.Field(default=None)
    """
    The Common Vulnerability Scoring System metrics. This attribute contains information on the CVE's impact. If the CVE has been analyzed, this attribute will contain any CVSSv2 or CVSSv3 information associated with the vulnerability. For example: <code>{ {"Access Vector", "Network"}, {"Access Complexity", "Low"}, ...}</code>.
    """

    overall_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    The CVSS overall score, impacted by base, temporal, and environmental metrics. For example: <code>9.1</code>.
    """

    severity: typing.Optional[str] = pydantic.Field(default=None)
    """
    <p>The Common Vulnerability Scoring System (CVSS) Qualitative Severity Rating. A textual representation of the numeric score.</p><strong>CVSS v2.0</strong><ul><li>Low (0.0 – 3.9)</li><li>Medium (4.0 – 6.9)</li><li>High (7.0 – 10.0)</li></ul></p><strong>CVSS v3.0</strong><ul><li>None (0.0)</li><li>Low (0.1 - 3.9)</li><li>Medium (4.0 - 6.9)</li><li>High (7.0 - 8.9)</li><li>Critical (9.0 - 10.0)</li></ul>
    """

    src_url: typing.Optional[UrlString] = pydantic.Field(default=None)
    """
    The source URL for the CVSS score. For example: <code>https://nvd.nist.gov/vuln/detail/CVE-2021-44228</code>
    """

    vector_string: typing.Optional[str] = pydantic.Field(default=None)
    """
    The CVSS vector string is a text representation of a set of CVSS metrics. It is commonly used to record or transfer CVSS metric information in a concise form. For example: <code>3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H</code>.
    """

    vendor_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The vendor that provided the CVSS score. For example: <code>NVD, REDHAT</code> etc.
    """

    version: str = pydantic.Field()
    """
    The CVSS version. For example: <code>3.1</code>.
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
