# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ........core.datetime_utils import serialize_datetime
from .network_connection_info_boundary_id import NetworkConnectionInfoBoundaryId
from .network_connection_info_direction_id import NetworkConnectionInfoDirectionId
from .network_connection_info_protocol_ver_id import NetworkConnectionInfoProtocolVerId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NetworkConnectionInfo(pydantic.BaseModel):
    """
    The Network Connection Information object describes characteristics of a network connection. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:NetworkSession/'>d3f:NetworkSession</a>.
    """

    boundary: typing.Optional[str] = pydantic.Field(
        description="The boundary of the connection, normalized to the caption of 'boundary_id'. In the case of 'Other', it is defined by the event source. <p> For cloud connections, this translates to the traffic-boundary(same VPC, through IGW, etc.). For traditional networks, this is described as Local, Internal, or External.</p>"
    )
    boundary_id: typing.Optional[NetworkConnectionInfoBoundaryId] = pydantic.Field(
        description="<p>The normalized identifier of the boundary of the connection. </p><p> For cloud connections, this translates to the traffic-boundary (same VPC, through IGW, etc.). For traditional networks, this is described as Local, Internal, or External.</p>"
    )
    direction: typing.Optional[str] = pydantic.Field(
        description="The direction of the initiated connection, traffic, or email, normalized to the caption of the direction_id value. In the case of 'Other', it is defined by the event source."
    )
    direction_id: NetworkConnectionInfoDirectionId = pydantic.Field(
        description="The normalized identifier of the direction of the initiated connection, traffic, or email."
    )
    protocol_name: typing.Optional[str] = pydantic.Field(
        description="The TCP/IP protocol name in lowercase, as defined by the Internet Assigned Numbers Authority (IANA). See <a target='_blank' href='https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'>Protocol Numbers</a>. For example: <code>tcp</code> or <code>udp</code>."
    )
    protocol_num: typing.Optional[int] = pydantic.Field(
        description="The TCP/IP protocol number, as defined by the Internet Assigned Numbers Authority (IANA). Use -1 if the protocol is not defined by IANA. See <a target='_blank' href='https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'>Protocol Numbers</a>. For example: <code>6</code> for TCP and <code>17</code> for UDP."
    )
    protocol_ver: typing.Optional[str] = pydantic.Field(description="The Internet Protocol version.")
    protocol_ver_id: typing.Optional[NetworkConnectionInfoProtocolVerId] = pydantic.Field(
        description="The Internet Protocol version identifier."
    )
    tcp_flags: typing.Optional[int] = pydantic.Field(
        description="The network connection TCP header flags (i.e., control bits)."
    )
    uid: typing.Optional[str] = pydantic.Field(description="The unique identifier of the connection.")

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
