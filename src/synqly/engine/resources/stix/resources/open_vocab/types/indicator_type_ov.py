# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IndicatorTypeOv(str, enum.Enum):
    ANOMALOUS_ACTIVITY = "anomalous_activity"
    ANONYMIZATION = "anonymization"
    BENIGN = "benign"
    COMPROMISED = "compromised"
    MALICIOUS_ACTIVITY = "malicious_activity"
    ATTRIBUTION = "attribution"
    UNKNOWN = "unknown"

    def visit(
        self,
        anomalous_activity: typing.Callable[[], T_Result],
        anonymization: typing.Callable[[], T_Result],
        benign: typing.Callable[[], T_Result],
        compromised: typing.Callable[[], T_Result],
        malicious_activity: typing.Callable[[], T_Result],
        attribution: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IndicatorTypeOv.ANOMALOUS_ACTIVITY:
            return anomalous_activity()
        if self is IndicatorTypeOv.ANONYMIZATION:
            return anonymization()
        if self is IndicatorTypeOv.BENIGN:
            return benign()
        if self is IndicatorTypeOv.COMPROMISED:
            return compromised()
        if self is IndicatorTypeOv.MALICIOUS_ACTIVITY:
            return malicious_activity()
        if self is IndicatorTypeOv.ATTRIBUTION:
            return attribution()
        if self is IndicatorTypeOv.UNKNOWN:
            return unknown()