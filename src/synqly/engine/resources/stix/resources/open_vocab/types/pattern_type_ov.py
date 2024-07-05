# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatternTypeOv(str, enum.Enum):
    """
    covers common pattern languages
    """

    STIX = "stix"
    PCRE = "pcre"
    SIGMA = "sigma"
    SNORT = "snort"
    SURICATA = "suricata"
    YARA = "yara"

    def visit(
        self,
        stix: typing.Callable[[], T_Result],
        pcre: typing.Callable[[], T_Result],
        sigma: typing.Callable[[], T_Result],
        snort: typing.Callable[[], T_Result],
        suricata: typing.Callable[[], T_Result],
        yara: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatternTypeOv.STIX:
            return stix()
        if self is PatternTypeOv.PCRE:
            return pcre()
        if self is PatternTypeOv.SIGMA:
            return sigma()
        if self is PatternTypeOv.SNORT:
            return snort()
        if self is PatternTypeOv.SURICATA:
            return suricata()
        if self is PatternTypeOv.YARA:
            return yara()
