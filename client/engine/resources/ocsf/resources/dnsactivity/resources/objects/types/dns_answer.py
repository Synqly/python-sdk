# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime
from .dns_answer_flag_ids import DnsAnswerFlagIds


class DnsAnswer(pydantic.BaseModel):
    """
    The DNS Answer object represents a specific response provided by the Domain Name System (DNS) when querying for information about a domain or performing a DNS operation. It encapsulates the relevant details and data returned by the DNS server in response to a query.
    """

    class_: str = pydantic.Field(
        alias="class",
        description="The class of DNS data contained in this resource record. See <a target='_blank' href='https://www.rfc-editor.org/rfc/rfc1035.txt'>RFC1035</a>. For example: <code>IN</code>.",
    )
    flag_ids: typing.Optional[typing.List[DnsAnswerFlagIds]] = pydantic.Field(
        description="The list of DNS answer header flag IDs."
    )
    flags: typing.Optional[typing.List[str]] = pydantic.Field(description="The list of DNS answer header flags.")
    packet_uid: typing.Optional[int] = pydantic.Field(
        description="The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response."
    )
    rdata: str = pydantic.Field(
        description="The data describing the DNS resource. The meaning of this data depends on the type and class of the resource record."
    )
    ttl: typing.Optional[int] = pydantic.Field(
        description="The time interval that the resource record may be cached. Zero value means that the resource record can only be used for the transaction in progress, and should not be cached."
    )
    type: str = pydantic.Field(
        description="The type of data contained in this resource record. See <a target='_blank' href='https://www.rfc-editor.org/rfc/rfc1035.txt'>RFC1035</a>. For example: <code>CNAME</code>."
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
