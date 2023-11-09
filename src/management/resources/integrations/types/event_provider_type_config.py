# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .aws_config import AwsConfig
from .azure_config import AzureConfig
from .elasticsearch_config import ElasticsearchConfig
from .splunk_config import SplunkConfig


class EventProviderTypeConfig_AzureMonitorLogs(AzureConfig):
    type: typing_extensions.Literal["azure_monitor_logs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class EventProviderTypeConfig_Aws(AwsConfig):
    type: typing_extensions.Literal["aws"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class EventProviderTypeConfig_Splunk(SplunkConfig):
    type: typing_extensions.Literal["splunk"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class EventProviderTypeConfig_Elasticsearch(ElasticsearchConfig):
    type: typing_extensions.Literal["elasticsearch"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


EventProviderTypeConfig = typing.Union[
    EventProviderTypeConfig_AzureMonitorLogs,
    EventProviderTypeConfig_Aws,
    EventProviderTypeConfig_Splunk,
    EventProviderTypeConfig_Elasticsearch,
]