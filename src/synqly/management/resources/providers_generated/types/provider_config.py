# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .assets_armis_centrix import AssetsArmisCentrix
from .assets_nozomi_vantage import AssetsNozomiVantage
from .assets_service_now import AssetsServiceNow
from .edr_crowd_strike import EdrCrowdStrike
from .edr_sentinel_one import EdrSentinelOne
from .hooks_http import HooksHttp
from .identity_entra_id import IdentityEntraId
from .identity_okta import IdentityOkta
from .identity_ping_one import IdentityPingOne
from .notifications_jira import NotificationsJira
from .notifications_mock import NotificationsMock
from .notifications_slack import NotificationsSlack
from .notifications_teams import NotificationsTeams
from .siem_elasticsearch import SiemElasticsearch
from .siem_mock import SiemMock
from .siem_q_radar import SiemQRadar
from .siem_rapid_7_insight_idr import SiemRapid7InsightIdr
from .siem_splunk import SiemSplunk
from .siem_sumo_logic import SiemSumoLogic
from .sink_aws_security_lake import SinkAwsSecurityLake
from .sink_aws_sqs import SinkAwsSqs
from .sink_azure_monitor_logs import SinkAzureMonitorLogs
from .sink_mock import SinkMock
from .storage_aws_s_3 import StorageAwsS3
from .storage_azure_blob import StorageAzureBlob
from .storage_gcs import StorageGcs
from .storage_mock import StorageMock
from .ticketing_jira import TicketingJira
from .ticketing_mock import TicketingMock
from .ticketing_pager_duty import TicketingPagerDuty
from .ticketing_service_now import TicketingServiceNow
from .ticketing_torq import TicketingTorq
from .vulnerabilities_qualys_cloud import VulnerabilitiesQualysCloud
from .vulnerabilities_rapid_7_insight_cloud import VulnerabilitiesRapid7InsightCloud
from .vulnerabilities_tanium_cloud import VulnerabilitiesTaniumCloud
from .vulnerabilities_tenable_cloud import VulnerabilitiesTenableCloud


class ProviderConfig_AssetsArmisCentrix(AssetsArmisCentrix):
    type: typing.Literal["assets_armis_centrix"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_AssetsNozomiVantage(AssetsNozomiVantage):
    type: typing.Literal["assets_nozomi_vantage"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_AssetsServicenow(AssetsServiceNow):
    type: typing.Literal["assets_servicenow"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_EdrCrowdstrike(EdrCrowdStrike):
    type: typing.Literal["edr_crowdstrike"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_EdrSentinelone(EdrSentinelOne):
    type: typing.Literal["edr_sentinelone"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_HooksHttp(HooksHttp):
    type: typing.Literal["hooks_http"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_IdentityEntraId(IdentityEntraId):
    type: typing.Literal["identity_entra_id"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_IdentityOkta(IdentityOkta):
    type: typing.Literal["identity_okta"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_IdentityPingone(IdentityPingOne):
    type: typing.Literal["identity_pingone"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_NotificationsJira(NotificationsJira):
    type: typing.Literal["notifications_jira"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_NotificationsMockNotifications(NotificationsMock):
    type: typing.Literal["notifications_mock_notifications"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_NotificationsSlack(NotificationsSlack):
    type: typing.Literal["notifications_slack"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_NotificationsTeams(NotificationsTeams):
    type: typing.Literal["notifications_teams"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SiemElasticsearch(SiemElasticsearch):
    type: typing.Literal["siem_elasticsearch"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SiemMockSiem(SiemMock):
    type: typing.Literal["siem_mock_siem"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SiemQRadar(SiemQRadar):
    type: typing.Literal["siem_q_radar"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SiemRapid7Insightidr(SiemRapid7InsightIdr):
    type: typing.Literal["siem_rapid7_insightidr"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SiemSplunk(SiemSplunk):
    type: typing.Literal["siem_splunk"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SiemSumoLogic(SiemSumoLogic):
    type: typing.Literal["siem_sumo_logic"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SinkAwsSecurityLake(SinkAwsSecurityLake):
    type: typing.Literal["sink_aws_security_lake"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SinkAwsSqs(SinkAwsSqs):
    type: typing.Literal["sink_aws_sqs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SinkAzureMonitorLogs(SinkAzureMonitorLogs):
    type: typing.Literal["sink_azure_monitor_logs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_SinkMockSink(SinkMock):
    type: typing.Literal["sink_mock_sink"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_StorageAwsS3(StorageAwsS3):
    type: typing.Literal["storage_aws_s3"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_StorageAzureBlob(StorageAzureBlob):
    type: typing.Literal["storage_azure_blob"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_StorageGcs(StorageGcs):
    type: typing.Literal["storage_gcs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_StorageMockStorage(StorageMock):
    type: typing.Literal["storage_mock_storage"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_TicketingJira(TicketingJira):
    type: typing.Literal["ticketing_jira"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_TicketingMockTicketing(TicketingMock):
    type: typing.Literal["ticketing_mock_ticketing"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_TicketingPagerduty(TicketingPagerDuty):
    type: typing.Literal["ticketing_pagerduty"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_TicketingServicenow(TicketingServiceNow):
    type: typing.Literal["ticketing_servicenow"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_TicketingTorq(TicketingTorq):
    type: typing.Literal["ticketing_torq"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_VulnerabilitiesQualysCloud(VulnerabilitiesQualysCloud):
    type: typing.Literal["vulnerabilities_qualys_cloud"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_VulnerabilitiesRapid7InsightCloud(VulnerabilitiesRapid7InsightCloud):
    type: typing.Literal["vulnerabilities_rapid7_insight_cloud"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_VulnerabilitiesTaniumCloud(VulnerabilitiesTaniumCloud):
    type: typing.Literal["vulnerabilities_tanium_cloud"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ProviderConfig_VulnerabilitiesTenableCloud(VulnerabilitiesTenableCloud):
    type: typing.Literal["vulnerabilities_tenable_cloud"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ProviderConfig = typing.Union[
    ProviderConfig_AssetsArmisCentrix,
    ProviderConfig_AssetsNozomiVantage,
    ProviderConfig_AssetsServicenow,
    ProviderConfig_EdrCrowdstrike,
    ProviderConfig_EdrSentinelone,
    ProviderConfig_HooksHttp,
    ProviderConfig_IdentityEntraId,
    ProviderConfig_IdentityOkta,
    ProviderConfig_IdentityPingone,
    ProviderConfig_NotificationsJira,
    ProviderConfig_NotificationsMockNotifications,
    ProviderConfig_NotificationsSlack,
    ProviderConfig_NotificationsTeams,
    ProviderConfig_SiemElasticsearch,
    ProviderConfig_SiemMockSiem,
    ProviderConfig_SiemQRadar,
    ProviderConfig_SiemRapid7Insightidr,
    ProviderConfig_SiemSplunk,
    ProviderConfig_SiemSumoLogic,
    ProviderConfig_SinkAwsSecurityLake,
    ProviderConfig_SinkAwsSqs,
    ProviderConfig_SinkAzureMonitorLogs,
    ProviderConfig_SinkMockSink,
    ProviderConfig_StorageAwsS3,
    ProviderConfig_StorageAzureBlob,
    ProviderConfig_StorageGcs,
    ProviderConfig_StorageMockStorage,
    ProviderConfig_TicketingJira,
    ProviderConfig_TicketingMockTicketing,
    ProviderConfig_TicketingPagerduty,
    ProviderConfig_TicketingServicenow,
    ProviderConfig_TicketingTorq,
    ProviderConfig_VulnerabilitiesQualysCloud,
    ProviderConfig_VulnerabilitiesRapid7InsightCloud,
    ProviderConfig_VulnerabilitiesTaniumCloud,
    ProviderConfig_VulnerabilitiesTenableCloud,
]
