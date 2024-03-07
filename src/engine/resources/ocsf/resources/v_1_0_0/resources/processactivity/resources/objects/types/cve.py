# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.timestamp import Timestamp
from ...base.types.url_string import UrlString
from .cvss import Cvss
from .product import Product

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Cve(pydantic.BaseModel):
    """
    The Common Vulnerabilities and Exposures (CVE) object represents publicly disclosed cybersecurity vulnerabilities defined in CVE Program catalog (<a target='_blank' href='https://cve.mitre.org/'>CVE</a>). There is one CVE Record for each vulnerability in the catalog.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The Record Creation Date identifies when the CVE ID was issued to a CVE Numbering Authority (CNA) or the CVE Record was published on the CVE List. Note that the Record Creation Date does not necessarily indicate when this vulnerability was discovered, shared with the affected vendor, publicly disclosed, or updated in CVE."
    )
    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The Record Creation Date identifies when the CVE ID was issued to a CVE Numbering Authority (CNA) or the CVE Record was published on the CVE List. Note that the Record Creation Date does not necessarily indicate when this vulnerability was discovered, shared with the affected vendor, publicly disclosed, or updated in CVE."
    )
    cvss: typing.Optional[Cvss] = pydantic.Field(
        description="The CVSS object details Common Vulnerability Scoring System (<a target='_blank' href='https://www.first.org/cvss/'>CVSS</a>) scores from the advisory that are related to the vulnerability."
    )
    cwe_uid: typing.Optional[str] = pydantic.Field(
        description="The <a target='_blank' href='https://cwe.mitre.org/'>Common Weakness Enumeration (CWE)</a> unique identifier. For example: <code>CWE-787</code>."
    )
    cwe_url: typing.Optional[UrlString] = pydantic.Field(
        description="Common Weakness Enumeration (CWE) definition URL. For example: <code>https://cwe.mitre.org/data/definitions/787.html</code>."
    )
    modified_time: typing.Optional[Timestamp] = pydantic.Field(
        description="The Record Modified Date identifies when the CVE record was last updated."
    )
    modified_time_dt: typing.Optional[dt.datetime] = pydantic.Field(
        description="The Record Modified Date identifies when the CVE record was last updated."
    )
    product: typing.Optional[Product] = pydantic.Field(
        description="The product where the vulnerability was discovered."
    )
    type: typing.Optional[str] = pydantic.Field(
        description="<p>The vulnerability type as selected from a large dropdown menu during CVE refinement.</p>Most frequently used vulnerability types are: <code>DoS</code>, <code>Code Execution</code>, <code>Overflow</code>, <code>Memory Corruption</code>, <code>Sql Injection</code>, <code>XSS</code>, <code>Directory Traversal</code>, <code>Http Response Splitting</code>, <code>Bypass something</code>, <code>Gain Information</code>, <code>Gain Privileges</code>, <code>CSRF</code>, <code>File Inclusion</code>. For more information see <a target='_blank' href='https://www.cvedetails.com/vulnerabilities-by-types.php'>Vulnerabilities By Type</a> distributions."
    )
    uid: str = pydantic.Field(
        description="The Common Vulnerabilities and Exposures unique number assigned to a specific computer vulnerability. A CVE Identifier begins with 4 digits representing the year followed by a sequence of digits that acts as a unique identifier. For example: <code>CVE-2021-12345</code>."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
