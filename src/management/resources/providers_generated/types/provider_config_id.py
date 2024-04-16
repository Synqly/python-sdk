# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ProviderConfigId(str, enum.Enum):
    """
    List of supported providers.
    """

    ASSETS_ARMIS_CENTRIX = "assets_armis_centrix"
    """
    Armis Centrix™ for Asset Management and Security
    """

    ASSETS_SERVICE_NOW = "assets_servicenow"
    """
    ServiceNow Configuration Management Database (CMDB)
    """

    EDR_CROWD_STRIKE = "edr_crowdstrike"
    """
    CrowdStrike Falcon® Insight EDR
    """

    EDR_SENTINEL_ONE = "edr_sentinelone"
    """
    SentinelOne Singularity™ Endpoint
    """

    HOOKS_HTTP = "hooks_http"
    """
    HTTP Webhook
    """

    IDENTITY_ENTRA_ID = "identity_entra_id"
    """
    Microsoft Entra ID
    """

    IDENTITY_OKTA = "identity_okta"
    """
    Okta Identity
    """

    IDENTITY_PING_ONE = "identity_pingone"
    """
    PingOne Cloud Platform
    """

    NOTIFICATIONS_JIRA = "notifications_jira"
    """
    Atlassian Jira
    """

    NOTIFICATIONS_MOCK = "notifications_mock_notifications"
    """
    Notifications Mock
    """

    NOTIFICATIONS_SLACK = "notifications_slack"
    """
    Slack
    """

    NOTIFICATIONS_TEAMS = "notifications_teams"
    """
    Microsoft Teams
    """

    SIEM_ELASTICSEARCH = "siem_elasticsearch"
    """
    Elastic SIEM
    """

    SIEM_MOCK = "siem_mock_siem"
    """
    SIEM Mock
    """

    SIEM_SPLUNK = "siem_splunk"
    """
    Splunk Enterprise Security
    """

    SINK_AWS_SECURITY_LAKE = "sink_aws_security_lake"
    """
    AWS Security Lake
    """

    SINK_AWS_SQS = "sink_aws_sqs"
    """
    AWS Simple Queue Service
    """

    SINK_AZURE_MONITOR_LOGS = "sink_azure_monitor_logs"
    """
    Microsoft Azure Monitor Logs
    """

    SINK_MOCK = "sink_mock_sink"
    """
    Sink Mock
    """

    STORAGE_AWS_S_3 = "storage_aws_s3"
    """
    AWS S3
    """

    STORAGE_AZURE_BLOB = "storage_azure_blob"
    """
    Microsoft Azure Blob Storage
    """

    STORAGE_GCS = "storage_gcs"
    """
    Google Cloud Storage
    """

    STORAGE_MOCK = "storage_mock_storage"
    """
    Storage Mock
    """

    TICKETING_JIRA = "ticketing_jira"
    """
    Atlassian Jira
    """

    TICKETING_MOCK = "ticketing_mock_ticketing"
    """
    Ticketing Mock
    """

    TICKETING_PAGER_DUTY = "ticketing_pagerduty"
    """
    PagerDuty Operations Cloud
    """

    TICKETING_SERVICE_NOW = "ticketing_servicenow"
    """
    ServiceNow IT Service Management (ITSM)
    """

    VULNERABILITIES_QUALYS_CLOUD = "vulnerabilities_qualys_cloud"
    """
    Qualys Vulnerability Management, Detection & Response (VMDR)
    """

    VULNERABILITIES_RAPID_7_INSIGHT_CLOUD = "vulnerabilities_rapid7_insight_cloud"
    """
    Rapid7 Insight Vulnerability Management Cloud
    """

    VULNERABILITIES_TENABLE_CLOUD = "vulnerabilities_tenable_cloud"
    """
    Tenable Vulnerability Management
    """

    def visit(
        self,
        assets_armis_centrix: typing.Callable[[], T_Result],
        assets_service_now: typing.Callable[[], T_Result],
        edr_crowd_strike: typing.Callable[[], T_Result],
        edr_sentinel_one: typing.Callable[[], T_Result],
        hooks_http: typing.Callable[[], T_Result],
        identity_entra_id: typing.Callable[[], T_Result],
        identity_okta: typing.Callable[[], T_Result],
        identity_ping_one: typing.Callable[[], T_Result],
        notifications_jira: typing.Callable[[], T_Result],
        notifications_mock: typing.Callable[[], T_Result],
        notifications_slack: typing.Callable[[], T_Result],
        notifications_teams: typing.Callable[[], T_Result],
        siem_elasticsearch: typing.Callable[[], T_Result],
        siem_mock: typing.Callable[[], T_Result],
        siem_splunk: typing.Callable[[], T_Result],
        sink_aws_security_lake: typing.Callable[[], T_Result],
        sink_aws_sqs: typing.Callable[[], T_Result],
        sink_azure_monitor_logs: typing.Callable[[], T_Result],
        sink_mock: typing.Callable[[], T_Result],
        storage_aws_s_3: typing.Callable[[], T_Result],
        storage_azure_blob: typing.Callable[[], T_Result],
        storage_gcs: typing.Callable[[], T_Result],
        storage_mock: typing.Callable[[], T_Result],
        ticketing_jira: typing.Callable[[], T_Result],
        ticketing_mock: typing.Callable[[], T_Result],
        ticketing_pager_duty: typing.Callable[[], T_Result],
        ticketing_service_now: typing.Callable[[], T_Result],
        vulnerabilities_qualys_cloud: typing.Callable[[], T_Result],
        vulnerabilities_rapid_7_insight_cloud: typing.Callable[[], T_Result],
        vulnerabilities_tenable_cloud: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderConfigId.ASSETS_ARMIS_CENTRIX:
            return assets_armis_centrix()
        if self is ProviderConfigId.ASSETS_SERVICE_NOW:
            return assets_service_now()
        if self is ProviderConfigId.EDR_CROWD_STRIKE:
            return edr_crowd_strike()
        if self is ProviderConfigId.EDR_SENTINEL_ONE:
            return edr_sentinel_one()
        if self is ProviderConfigId.HOOKS_HTTP:
            return hooks_http()
        if self is ProviderConfigId.IDENTITY_ENTRA_ID:
            return identity_entra_id()
        if self is ProviderConfigId.IDENTITY_OKTA:
            return identity_okta()
        if self is ProviderConfigId.IDENTITY_PING_ONE:
            return identity_ping_one()
        if self is ProviderConfigId.NOTIFICATIONS_JIRA:
            return notifications_jira()
        if self is ProviderConfigId.NOTIFICATIONS_MOCK:
            return notifications_mock()
        if self is ProviderConfigId.NOTIFICATIONS_SLACK:
            return notifications_slack()
        if self is ProviderConfigId.NOTIFICATIONS_TEAMS:
            return notifications_teams()
        if self is ProviderConfigId.SIEM_ELASTICSEARCH:
            return siem_elasticsearch()
        if self is ProviderConfigId.SIEM_MOCK:
            return siem_mock()
        if self is ProviderConfigId.SIEM_SPLUNK:
            return siem_splunk()
        if self is ProviderConfigId.SINK_AWS_SECURITY_LAKE:
            return sink_aws_security_lake()
        if self is ProviderConfigId.SINK_AWS_SQS:
            return sink_aws_sqs()
        if self is ProviderConfigId.SINK_AZURE_MONITOR_LOGS:
            return sink_azure_monitor_logs()
        if self is ProviderConfigId.SINK_MOCK:
            return sink_mock()
        if self is ProviderConfigId.STORAGE_AWS_S_3:
            return storage_aws_s_3()
        if self is ProviderConfigId.STORAGE_AZURE_BLOB:
            return storage_azure_blob()
        if self is ProviderConfigId.STORAGE_GCS:
            return storage_gcs()
        if self is ProviderConfigId.STORAGE_MOCK:
            return storage_mock()
        if self is ProviderConfigId.TICKETING_JIRA:
            return ticketing_jira()
        if self is ProviderConfigId.TICKETING_MOCK:
            return ticketing_mock()
        if self is ProviderConfigId.TICKETING_PAGER_DUTY:
            return ticketing_pager_duty()
        if self is ProviderConfigId.TICKETING_SERVICE_NOW:
            return ticketing_service_now()
        if self is ProviderConfigId.VULNERABILITIES_QUALYS_CLOUD:
            return vulnerabilities_qualys_cloud()
        if self is ProviderConfigId.VULNERABILITIES_RAPID_7_INSIGHT_CLOUD:
            return vulnerabilities_rapid_7_insight_cloud()
        if self is ProviderConfigId.VULNERABILITIES_TENABLE_CLOUD:
            return vulnerabilities_tenable_cloud()