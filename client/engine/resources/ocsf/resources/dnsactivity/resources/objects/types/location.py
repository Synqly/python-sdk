# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime


class Location(pydantic.BaseModel):
    """
    The Geo Location object describes a geographical location, usually associated with an IP address. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:PhysicalLocation/'>d3f:PhysicalLocation</a>.
    """

    city: typing.Optional[str] = pydantic.Field(description="The name of the city.")
    continent: typing.Optional[str] = pydantic.Field(description="The name of the continent.")
    coordinates: typing.List[float] = pydantic.Field(
        description="A two-element array, containing a longitude/latitude pair. The format conforms with <a target='_blank' href='https://geojson.org'>GeoJSON</a>. For example: <code>[-73.983, 40.719]</code>."
    )
    country: typing.Optional[str] = pydantic.Field(
        description="The ISO 3166-1 Alpha-2 country code. For the complete list of country codes see <a target='_blank' href='https://www.iso.org/obp/ui/#iso:pub:PUB500001:en' >ISO 3166-1 alpha-2 codes</a>.<p><b>Note:</b> The two letter country code should be capitalized. For example: <code>US</code> or <code>CA</code>.</p>"
    )
    desc: typing.Optional[str] = pydantic.Field(description="The description of the geographical location.")
    is_on_premises: typing.Optional[bool] = pydantic.Field(
        description="The indication of whether the location is on premises."
    )
    isp: typing.Optional[str] = pydantic.Field(description="The name of the Internet Service Provider (ISP).")
    postal_code: typing.Optional[str] = pydantic.Field(description="The postal code of the location.")
    provider: typing.Optional[str] = pydantic.Field(description="The provider of the geographical location data.")
    region: typing.Optional[str] = pydantic.Field(
        description="The alphanumeric code that identifies the principal subdivision (e.g. province or state) of the country. Region codes are defined at <a target='_blank' href='https://www.iso.org/iso-3166-country-codes.html'>ISO 3166-2</a> and have a limit of three characters. For example, see <a target='_blank' href='https://www.iso.org/obp/ui/#iso:code:3166:US'>the region codes for the US</a>."
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
