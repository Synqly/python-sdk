# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OperationId(str, enum.Enum):
    APPSEC_GET_APPLICATION_FINDING_DETAILS = "appsec_get_application_finding_details"
    APPSEC_QUERY_APPLICATION_FINDINGS = "appsec_query_application_findings"
    APPSEC_QUERY_APPLICATIONS = "appsec_query_applications"
    APPSEC_QUERY_FINDINGS = "appsec_query_findings"
    ASSETS_CREATE_ASSET = "assets_create_asset"
    ASSETS_GET_LABELS = "assets_get_labels"
    ASSETS_QUERY_DEVICES = "assets_query_devices"
    CLOUDSECURITY_QUERY_CLOUD_RESOURCE_INVENTORY = "cloudsecurity_query_cloud_resource_inventory"
    CLOUDSECURITY_QUERY_COMPLIANCE_FINDINGS = "cloudsecurity_query_compliance_findings"
    CLOUDSECURITY_QUERY_EVENTS = "cloudsecurity_query_events"
    CLOUDSECURITY_QUERY_IOMS = "cloudsecurity_query_ioms"
    EDR_CREATE_IOCS = "edr_create_iocs"
    EDR_DELETE_IOCS = "edr_delete_iocs"
    EDR_GET_ENDPOINT = "edr_get_endpoint"
    EDR_NETWORK_QUARANTINE = "edr_network_quarantine"
    EDR_QUERY_ALERTS = "edr_query_alerts"
    EDR_QUERY_APPLICATIONS = "edr_query_applications"
    EDR_QUERY_EDR_EVENTS = "edr_query_edr_events"
    EDR_QUERY_ENDPOINTS = "edr_query_endpoints"
    EDR_QUERY_IOCS = "edr_query_iocs"
    EDR_QUERY_POSTURE_SCORE = "edr_query_posture_score"
    EDR_QUERY_THREATEVENTS = "edr_query_threatevents"
    IDENTITY_DISABLE_USER = "identity_disable_user"
    IDENTITY_ENABLE_USER = "identity_enable_user"
    IDENTITY_EXPIRE_ALL_USER_SESSIONS = "identity_expire_all_user_sessions"
    IDENTITY_FORCE_USER_PASSWORD_RESET = "identity_force_user_password_reset"
    IDENTITY_GET_GROUP = "identity_get_group"
    IDENTITY_GET_GROUP_MEMBERS = "identity_get_group_members"
    IDENTITY_GET_USER = "identity_get_user"
    IDENTITY_QUERY_AUDIT_LOG = "identity_query_audit_log"
    IDENTITY_QUERY_GROUPS = "identity_query_groups"
    IDENTITY_QUERY_USERS = "identity_query_users"
    NOTIFICATIONS_CLEAR_MESSAGE = "notifications_clear_message"
    NOTIFICATIONS_CREATE_MESSAGE = "notifications_create_message"
    NOTIFICATIONS_GET_MESSAGE = "notifications_get_message"
    SIEM_GET_EVIDENCE = "siem_get_evidence"
    SIEM_GET_INVESTIGATION = "siem_get_investigation"
    SIEM_PATCH_INVESTIGATION = "siem_patch_investigation"
    SIEM_POST_EVENTS = "siem_post_events"
    SIEM_QUERY_ALERTS = "siem_query_alerts"
    SIEM_QUERY_EVENTS = "siem_query_events"
    SIEM_QUERY_INVESTIGATIONS = "siem_query_investigations"
    SIEM_QUERY_LOG_PROVIDERS = "siem_query_log_providers"
    SINK_POST_EVENTS = "sink_post_events"
    STORAGE_DELETE_FILE = "storage_delete_file"
    STORAGE_DOWNLOAD_FILE = "storage_download_file"
    STORAGE_LIST_FILES = "storage_list_files"
    STORAGE_UPLOAD_FILE = "storage_upload_file"
    TICKETING_CREATE_ATTACHMENT = "ticketing_create_attachment"
    TICKETING_CREATE_COMMENT = "ticketing_create_comment"
    TICKETING_CREATE_NOTE = "ticketing_create_note"
    TICKETING_CREATE_TICKET = "ticketing_create_ticket"
    TICKETING_DELETE_ATTACHMENT = "ticketing_delete_attachment"
    TICKETING_DELETE_COMMENT = "ticketing_delete_comment"
    TICKETING_DELETE_NOTE = "ticketing_delete_note"
    TICKETING_DOWNLOAD_ATTACHMENT = "ticketing_download_attachment"
    TICKETING_GET_TICKET = "ticketing_get_ticket"
    TICKETING_LIST_ATTACHMENTS_METADATA = "ticketing_list_attachments_metadata"
    TICKETING_LIST_COMMENTS = "ticketing_list_comments"
    TICKETING_LIST_NOTES = "ticketing_list_notes"
    TICKETING_LIST_ON_CALL = "ticketing_list_on_call"
    TICKETING_LIST_PROJECTS = "ticketing_list_projects"
    TICKETING_LIST_REMOTE_FIELDS = "ticketing_list_remote_fields"
    TICKETING_PATCH_NOTE = "ticketing_patch_note"
    TICKETING_PATCH_TICKET = "ticketing_patch_ticket"
    TICKETING_QUERY_ESCALATION_POLICIES = "ticketing_query_escalation_policies"
    TICKETING_QUERY_TICKETS = "ticketing_query_tickets"
    VULNERABILITIES_CREATE_ASSET = "vulnerabilities_create_asset"
    VULNERABILITIES_CREATE_FINDINGS = "vulnerabilities_create_findings"
    VULNERABILITIES_GET_SCAN_ACTIVITY = "vulnerabilities_get_scan_activity"
    VULNERABILITIES_QUERY_ASSETS = "vulnerabilities_query_assets"
    VULNERABILITIES_QUERY_FINDINGS = "vulnerabilities_query_findings"
    VULNERABILITIES_QUERY_SCANS = "vulnerabilities_query_scans"
    VULNERABILITIES_UPDATE_ASSET = "vulnerabilities_update_asset"
    VULNERABILITIES_UPDATE_FINDING = "vulnerabilities_update_finding"

    def visit(
        self,
        appsec_get_application_finding_details: typing.Callable[[], T_Result],
        appsec_query_application_findings: typing.Callable[[], T_Result],
        appsec_query_applications: typing.Callable[[], T_Result],
        appsec_query_findings: typing.Callable[[], T_Result],
        assets_create_asset: typing.Callable[[], T_Result],
        assets_get_labels: typing.Callable[[], T_Result],
        assets_query_devices: typing.Callable[[], T_Result],
        cloudsecurity_query_cloud_resource_inventory: typing.Callable[[], T_Result],
        cloudsecurity_query_compliance_findings: typing.Callable[[], T_Result],
        cloudsecurity_query_events: typing.Callable[[], T_Result],
        cloudsecurity_query_ioms: typing.Callable[[], T_Result],
        edr_create_iocs: typing.Callable[[], T_Result],
        edr_delete_iocs: typing.Callable[[], T_Result],
        edr_get_endpoint: typing.Callable[[], T_Result],
        edr_network_quarantine: typing.Callable[[], T_Result],
        edr_query_alerts: typing.Callable[[], T_Result],
        edr_query_applications: typing.Callable[[], T_Result],
        edr_query_edr_events: typing.Callable[[], T_Result],
        edr_query_endpoints: typing.Callable[[], T_Result],
        edr_query_iocs: typing.Callable[[], T_Result],
        edr_query_posture_score: typing.Callable[[], T_Result],
        edr_query_threatevents: typing.Callable[[], T_Result],
        identity_disable_user: typing.Callable[[], T_Result],
        identity_enable_user: typing.Callable[[], T_Result],
        identity_expire_all_user_sessions: typing.Callable[[], T_Result],
        identity_force_user_password_reset: typing.Callable[[], T_Result],
        identity_get_group: typing.Callable[[], T_Result],
        identity_get_group_members: typing.Callable[[], T_Result],
        identity_get_user: typing.Callable[[], T_Result],
        identity_query_audit_log: typing.Callable[[], T_Result],
        identity_query_groups: typing.Callable[[], T_Result],
        identity_query_users: typing.Callable[[], T_Result],
        notifications_clear_message: typing.Callable[[], T_Result],
        notifications_create_message: typing.Callable[[], T_Result],
        notifications_get_message: typing.Callable[[], T_Result],
        siem_get_evidence: typing.Callable[[], T_Result],
        siem_get_investigation: typing.Callable[[], T_Result],
        siem_patch_investigation: typing.Callable[[], T_Result],
        siem_post_events: typing.Callable[[], T_Result],
        siem_query_alerts: typing.Callable[[], T_Result],
        siem_query_events: typing.Callable[[], T_Result],
        siem_query_investigations: typing.Callable[[], T_Result],
        siem_query_log_providers: typing.Callable[[], T_Result],
        sink_post_events: typing.Callable[[], T_Result],
        storage_delete_file: typing.Callable[[], T_Result],
        storage_download_file: typing.Callable[[], T_Result],
        storage_list_files: typing.Callable[[], T_Result],
        storage_upload_file: typing.Callable[[], T_Result],
        ticketing_create_attachment: typing.Callable[[], T_Result],
        ticketing_create_comment: typing.Callable[[], T_Result],
        ticketing_create_note: typing.Callable[[], T_Result],
        ticketing_create_ticket: typing.Callable[[], T_Result],
        ticketing_delete_attachment: typing.Callable[[], T_Result],
        ticketing_delete_comment: typing.Callable[[], T_Result],
        ticketing_delete_note: typing.Callable[[], T_Result],
        ticketing_download_attachment: typing.Callable[[], T_Result],
        ticketing_get_ticket: typing.Callable[[], T_Result],
        ticketing_list_attachments_metadata: typing.Callable[[], T_Result],
        ticketing_list_comments: typing.Callable[[], T_Result],
        ticketing_list_notes: typing.Callable[[], T_Result],
        ticketing_list_on_call: typing.Callable[[], T_Result],
        ticketing_list_projects: typing.Callable[[], T_Result],
        ticketing_list_remote_fields: typing.Callable[[], T_Result],
        ticketing_patch_note: typing.Callable[[], T_Result],
        ticketing_patch_ticket: typing.Callable[[], T_Result],
        ticketing_query_escalation_policies: typing.Callable[[], T_Result],
        ticketing_query_tickets: typing.Callable[[], T_Result],
        vulnerabilities_create_asset: typing.Callable[[], T_Result],
        vulnerabilities_create_findings: typing.Callable[[], T_Result],
        vulnerabilities_get_scan_activity: typing.Callable[[], T_Result],
        vulnerabilities_query_assets: typing.Callable[[], T_Result],
        vulnerabilities_query_findings: typing.Callable[[], T_Result],
        vulnerabilities_query_scans: typing.Callable[[], T_Result],
        vulnerabilities_update_asset: typing.Callable[[], T_Result],
        vulnerabilities_update_finding: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OperationId.APPSEC_GET_APPLICATION_FINDING_DETAILS:
            return appsec_get_application_finding_details()
        if self is OperationId.APPSEC_QUERY_APPLICATION_FINDINGS:
            return appsec_query_application_findings()
        if self is OperationId.APPSEC_QUERY_APPLICATIONS:
            return appsec_query_applications()
        if self is OperationId.APPSEC_QUERY_FINDINGS:
            return appsec_query_findings()
        if self is OperationId.ASSETS_CREATE_ASSET:
            return assets_create_asset()
        if self is OperationId.ASSETS_GET_LABELS:
            return assets_get_labels()
        if self is OperationId.ASSETS_QUERY_DEVICES:
            return assets_query_devices()
        if self is OperationId.CLOUDSECURITY_QUERY_CLOUD_RESOURCE_INVENTORY:
            return cloudsecurity_query_cloud_resource_inventory()
        if self is OperationId.CLOUDSECURITY_QUERY_COMPLIANCE_FINDINGS:
            return cloudsecurity_query_compliance_findings()
        if self is OperationId.CLOUDSECURITY_QUERY_EVENTS:
            return cloudsecurity_query_events()
        if self is OperationId.CLOUDSECURITY_QUERY_IOMS:
            return cloudsecurity_query_ioms()
        if self is OperationId.EDR_CREATE_IOCS:
            return edr_create_iocs()
        if self is OperationId.EDR_DELETE_IOCS:
            return edr_delete_iocs()
        if self is OperationId.EDR_GET_ENDPOINT:
            return edr_get_endpoint()
        if self is OperationId.EDR_NETWORK_QUARANTINE:
            return edr_network_quarantine()
        if self is OperationId.EDR_QUERY_ALERTS:
            return edr_query_alerts()
        if self is OperationId.EDR_QUERY_APPLICATIONS:
            return edr_query_applications()
        if self is OperationId.EDR_QUERY_EDR_EVENTS:
            return edr_query_edr_events()
        if self is OperationId.EDR_QUERY_ENDPOINTS:
            return edr_query_endpoints()
        if self is OperationId.EDR_QUERY_IOCS:
            return edr_query_iocs()
        if self is OperationId.EDR_QUERY_POSTURE_SCORE:
            return edr_query_posture_score()
        if self is OperationId.EDR_QUERY_THREATEVENTS:
            return edr_query_threatevents()
        if self is OperationId.IDENTITY_DISABLE_USER:
            return identity_disable_user()
        if self is OperationId.IDENTITY_ENABLE_USER:
            return identity_enable_user()
        if self is OperationId.IDENTITY_EXPIRE_ALL_USER_SESSIONS:
            return identity_expire_all_user_sessions()
        if self is OperationId.IDENTITY_FORCE_USER_PASSWORD_RESET:
            return identity_force_user_password_reset()
        if self is OperationId.IDENTITY_GET_GROUP:
            return identity_get_group()
        if self is OperationId.IDENTITY_GET_GROUP_MEMBERS:
            return identity_get_group_members()
        if self is OperationId.IDENTITY_GET_USER:
            return identity_get_user()
        if self is OperationId.IDENTITY_QUERY_AUDIT_LOG:
            return identity_query_audit_log()
        if self is OperationId.IDENTITY_QUERY_GROUPS:
            return identity_query_groups()
        if self is OperationId.IDENTITY_QUERY_USERS:
            return identity_query_users()
        if self is OperationId.NOTIFICATIONS_CLEAR_MESSAGE:
            return notifications_clear_message()
        if self is OperationId.NOTIFICATIONS_CREATE_MESSAGE:
            return notifications_create_message()
        if self is OperationId.NOTIFICATIONS_GET_MESSAGE:
            return notifications_get_message()
        if self is OperationId.SIEM_GET_EVIDENCE:
            return siem_get_evidence()
        if self is OperationId.SIEM_GET_INVESTIGATION:
            return siem_get_investigation()
        if self is OperationId.SIEM_PATCH_INVESTIGATION:
            return siem_patch_investigation()
        if self is OperationId.SIEM_POST_EVENTS:
            return siem_post_events()
        if self is OperationId.SIEM_QUERY_ALERTS:
            return siem_query_alerts()
        if self is OperationId.SIEM_QUERY_EVENTS:
            return siem_query_events()
        if self is OperationId.SIEM_QUERY_INVESTIGATIONS:
            return siem_query_investigations()
        if self is OperationId.SIEM_QUERY_LOG_PROVIDERS:
            return siem_query_log_providers()
        if self is OperationId.SINK_POST_EVENTS:
            return sink_post_events()
        if self is OperationId.STORAGE_DELETE_FILE:
            return storage_delete_file()
        if self is OperationId.STORAGE_DOWNLOAD_FILE:
            return storage_download_file()
        if self is OperationId.STORAGE_LIST_FILES:
            return storage_list_files()
        if self is OperationId.STORAGE_UPLOAD_FILE:
            return storage_upload_file()
        if self is OperationId.TICKETING_CREATE_ATTACHMENT:
            return ticketing_create_attachment()
        if self is OperationId.TICKETING_CREATE_COMMENT:
            return ticketing_create_comment()
        if self is OperationId.TICKETING_CREATE_NOTE:
            return ticketing_create_note()
        if self is OperationId.TICKETING_CREATE_TICKET:
            return ticketing_create_ticket()
        if self is OperationId.TICKETING_DELETE_ATTACHMENT:
            return ticketing_delete_attachment()
        if self is OperationId.TICKETING_DELETE_COMMENT:
            return ticketing_delete_comment()
        if self is OperationId.TICKETING_DELETE_NOTE:
            return ticketing_delete_note()
        if self is OperationId.TICKETING_DOWNLOAD_ATTACHMENT:
            return ticketing_download_attachment()
        if self is OperationId.TICKETING_GET_TICKET:
            return ticketing_get_ticket()
        if self is OperationId.TICKETING_LIST_ATTACHMENTS_METADATA:
            return ticketing_list_attachments_metadata()
        if self is OperationId.TICKETING_LIST_COMMENTS:
            return ticketing_list_comments()
        if self is OperationId.TICKETING_LIST_NOTES:
            return ticketing_list_notes()
        if self is OperationId.TICKETING_LIST_ON_CALL:
            return ticketing_list_on_call()
        if self is OperationId.TICKETING_LIST_PROJECTS:
            return ticketing_list_projects()
        if self is OperationId.TICKETING_LIST_REMOTE_FIELDS:
            return ticketing_list_remote_fields()
        if self is OperationId.TICKETING_PATCH_NOTE:
            return ticketing_patch_note()
        if self is OperationId.TICKETING_PATCH_TICKET:
            return ticketing_patch_ticket()
        if self is OperationId.TICKETING_QUERY_ESCALATION_POLICIES:
            return ticketing_query_escalation_policies()
        if self is OperationId.TICKETING_QUERY_TICKETS:
            return ticketing_query_tickets()
        if self is OperationId.VULNERABILITIES_CREATE_ASSET:
            return vulnerabilities_create_asset()
        if self is OperationId.VULNERABILITIES_CREATE_FINDINGS:
            return vulnerabilities_create_findings()
        if self is OperationId.VULNERABILITIES_GET_SCAN_ACTIVITY:
            return vulnerabilities_get_scan_activity()
        if self is OperationId.VULNERABILITIES_QUERY_ASSETS:
            return vulnerabilities_query_assets()
        if self is OperationId.VULNERABILITIES_QUERY_FINDINGS:
            return vulnerabilities_query_findings()
        if self is OperationId.VULNERABILITIES_QUERY_SCANS:
            return vulnerabilities_query_scans()
        if self is OperationId.VULNERABILITIES_UPDATE_ASSET:
            return vulnerabilities_update_asset()
        if self is OperationId.VULNERABILITIES_UPDATE_FINDING:
            return vulnerabilities_update_finding()
