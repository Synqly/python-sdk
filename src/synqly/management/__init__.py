# This file was auto-generated by Fern from our API Definition.

from .resources import (
    Account,
    AccountId,
    AccountsActions,
    AccountsPermissions,
    AdhocRole,
    ApiPermissionMap,
    ArmisCredential,
    ArmisCredential_Token,
    ArmisCredential_TokenId,
    AssetsArmisCentrix,
    AssetsNozomiVantage,
    AssetsServiceNow,
    Audit,
    AuditActions,
    AuditPermissions,
    AuthActions,
    AuthCode,
    AuthPermissions,
    AwsCredential,
    AwsCredentialId,
    AwsS3Credential,
    AwsS3Credential_Aws,
    AwsS3Credential_AwsId,
    AwsSecurityLakeCredential,
    AwsSecurityLakeCredential_Aws,
    AwsSecurityLakeCredential_AwsId,
    AwsSqsCredential,
    AwsSqsCredential_Aws,
    AwsSqsCredential_AwsId,
    AzureBlobCredential,
    AzureBlobCredential_Token,
    AzureBlobCredential_TokenId,
    AzureMonitorLogsCredential,
    AzureMonitorLogsCredential_Token,
    AzureMonitorLogsCredential_TokenId,
    BadGatewayError,
    BadRequestError,
    Base,
    BasicCredential,
    BasicCredentialId,
    BridgeGroup,
    BridgeGroupId,
    BridgeSelector,
    BridgeSelector_Id,
    BridgeSelector_Labels,
    BridgesActions,
    BridgesPermissions,
    BuiltinRoles,
    CapabilitiesActions,
    CapabilitiesPermissions,
    CapabilitiesProviderConfig,
    Category,
    CategoryId,
    ChangePasswordRequest,
    ChangePasswordResponse,
    ChangePasswordResponseResult,
    ConflictError,
    CreateAccountRequest,
    CreateAccountResponse,
    CreateAccountResponseResult,
    CreateBridgeRequest,
    CreateBridgeResponse,
    CreateBridgeResponseResult,
    CreateCredentialRequest,
    CreateCredentialResponse,
    CreateIntegrationPointRequest,
    CreateIntegrationPointResponse,
    CreateIntegrationRequest,
    CreateIntegrationResponse,
    CreateIntegrationResponseResult,
    CreateIntegrationTokenRequest,
    CreateIntegrationTokenResponse,
    CreateMemberRequest,
    CreateMemberResponse,
    CreateMemberResponseResult,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    CreateOrganizationResponseResult,
    CreateOrganizationWebhookRequest,
    CreateOrganizationWebhookResponse,
    CreateRoleRequest,
    CreateRoleResponse,
    CreateTokenRequest,
    CreateTokenResponse,
    CreateTransformRequest,
    CreateTransformResponse,
    Credential,
    CredentialConfig,
    CredentialConfigNoSecret,
    CredentialConfig_Aws,
    CredentialConfig_Basic,
    CredentialConfig_OAuthClient,
    CredentialConfig_Secret,
    CredentialConfig_Token,
    CredentialId,
    CredentialResponse,
    CredentialType,
    CredentialsActions,
    CredentialsPermissions,
    CrowdStrikeCredential,
    CrowdStrikeCredential_OAuthClient,
    CrowdStrikeCredential_OAuthClientId,
    CustomFieldMapping,
    DefenderCredential,
    DefenderCredential_OAuthClient,
    DefenderCredential_OAuthClientId,
    DefenderCredential_TenantId,
    DefenderCredential_UrlString,
    EdrCrowdStrike,
    EdrDefender,
    EdrSentinelOne,
    ElasticsearchCredential,
    ElasticsearchCredential_Token,
    ElasticsearchCredential_TokenId,
    EntraIdCredential,
    EntraIdCredential_OAuthClient,
    EntraIdCredential_OAuthClientId,
    Environment,
    ErrorBody,
    ErrorParam,
    ForbiddenError,
    GatewayTimeoutError,
    GcsCredential,
    GcsCredential_Aws,
    GcsCredential_AwsId,
    GetAccountResponse,
    GetBridgeResponse,
    GetCredentialResponse,
    GetIntegrationPointResponse,
    GetIntegrationResponse,
    GetIntegrationTimeseries,
    GetIntegrationTimeseriesResult,
    GetMemberResponse,
    GetOpenApiSpecResponse,
    GetOrganizationResponse,
    GetOrganizationWebhookResponse,
    GetPermissionSetResponse,
    GetRoleResponse,
    GetStatusResponse,
    GetStatusTimeseries,
    GetStatusTimeseriesResult,
    GetTokenResponse,
    GetTransformResponse,
    HooksHttp,
    HooksHttpCredential,
    HooksHttpCredential_Token,
    HooksHttpCredential_TokenId,
    HttpMethod,
    Id,
    IdentityEntraId,
    IdentityOkta,
    IdentityPingOne,
    Integration,
    IntegrationEnvironments,
    IntegrationId,
    IntegrationPoint,
    IntegrationPointId,
    IntegrationPointsActions,
    IntegrationPointsPermissions,
    IntegrationsActions,
    IntegrationsPermissions,
    InternalServerError,
    JiraCredential,
    JiraCredential_Basic,
    JiraCredential_BasicId,
    ListAccountIntegrationsResponse,
    ListAccountsResponse,
    ListAuditEventsResponse,
    ListBridgesResponse,
    ListCategoryCapabilitiesResponse,
    ListCredentialsResponse,
    ListIntegrationOptions,
    ListIntegrationPointsResponse,
    ListIntegrationsResponse,
    ListMembersResponse,
    ListOrganizationResponse,
    ListOrganizationWebhooksResponse,
    ListPermissionSetsResponse,
    ListProviderCapabilitiesResponse,
    ListRolesResponse,
    ListStatusEventsResponse,
    ListStatusOptions,
    ListStatusResponse,
    ListTokensResponse,
    ListTransformsResponse,
    LogonRequest,
    LogonResponse,
    LogonResponseResult,
    LookupCredentialResponse,
    ManagedType,
    Member,
    MemberId,
    MemberOptions,
    MembersActions,
    MembersPermissions,
    MethodNotAllowedError,
    NotFoundError,
    NotImplementedError,
    NotificationsJira,
    NotificationsMock,
    NotificationsSlack,
    NotificationsTeams,
    NozomiVantageCredential,
    NozomiVantageCredential_Basic,
    NozomiVantageCredential_BasicId,
    OAuthClientCredential,
    OAuthClientCredentialId,
    OktaCredential,
    OktaCredential_OAuthClient,
    OktaCredential_OAuthClientId,
    OktaCredential_Token,
    OktaCredential_TokenId,
    Options,
    Organization,
    OrganizationActions,
    OrganizationId,
    OrganizationOptions,
    OrganizationPermissions,
    OrganizationType,
    OrganizationWebhook,
    OrganizationWebhookPayload,
    OrganizationWebhookSecret,
    OwnerType,
    PagerDutyCredential,
    PagerDutyCredential_Token,
    PagerDutyCredential_TokenId,
    PatchAccountResponse,
    PatchBridgeResponse,
    PatchCredentialResponse,
    PatchIntegrationPointResponse,
    PatchIntegrationResponse,
    PatchMemberResponse,
    PatchOrganizationResponse,
    PatchOrganizationWebhookResponse,
    PatchRoleResponse,
    PatchTransformResponse,
    Permission,
    PermissionSet,
    PermissionSetActions,
    PermissionSetPermissions,
    Permissions,
    PingOneCredential,
    PingOneCredential_Token,
    PingOneCredential_TokenId,
    PriorityMapping,
    Provider,
    ProviderConfig,
    ProviderConfigId,
    ProviderConfig_AssetsArmisCentrix,
    ProviderConfig_AssetsNozomiVantage,
    ProviderConfig_AssetsServicenow,
    ProviderConfig_EdrCrowdstrike,
    ProviderConfig_EdrDefender,
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
    ProviderConfig_VulnerabilitiesCrowdstrike,
    ProviderConfig_VulnerabilitiesQualysCloud,
    ProviderConfig_VulnerabilitiesRapid7InsightCloud,
    ProviderConfig_VulnerabilitiesTaniumCloud,
    ProviderConfig_VulnerabilitiesTenableCloud,
    ProviderCredentialConfig,
    ProviderId,
    QRadarCredential,
    QRadarCredential_Token,
    QRadarCredential_TokenId,
    QualysCloudCredential,
    QualysCloudCredential_Basic,
    QualysCloudCredential_BasicId,
    Rapid7InsightCloudCredential,
    Rapid7InsightCloudCredential_Token,
    Rapid7InsightCloudCredential_TokenId,
    ReadWriteActions,
    ReadWritePermissions,
    RefreshToken,
    RefreshTokenResponse,
    ResetTokenResponse,
    ResourceRestrictions,
    Resources,
    RoleAccounts,
    RoleDefinition,
    RoleId,
    RoleIntegrations,
    RoleName,
    RoleOrganizations,
    RolesActions,
    RolesPermissions,
    SecretCredential,
    SecretCredentialId,
    SentinelOneCredential,
    SentinelOneCredential_Token,
    SentinelOneCredential_TokenId,
    ServiceNowCredential,
    ServiceNowCredential_Basic,
    ServiceNowCredential_BasicId,
    ServiceUnavailableError,
    SiemElasticsearch,
    SiemMock,
    SiemQRadar,
    SiemRapid7InsightIdr,
    SiemSplunk,
    SiemSumoLogic,
    SinkAwsSecurityLake,
    SinkAwsSqs,
    SinkAzureMonitorLogs,
    SinkMock,
    SlackCredential,
    SlackCredential_Token,
    SlackCredential_TokenId,
    SplunkHecToken,
    SplunkHecToken_Token,
    SplunkHecToken_TokenId,
    SplunkSearchCredential,
    SplunkSearchCredential_Token,
    SplunkSearchCredential_TokenId,
    State,
    Status,
    StatusActions,
    StatusEvent,
    StatusMapping,
    StatusPermissions,
    StorageAwsS3,
    StorageAzureBlob,
    StorageGcs,
    StorageMock,
    SubOrgsActions,
    SubOrgsPermissions,
    SumoLogicCollectionUrl,
    SumoLogicCollectionUrl_Secret,
    SumoLogicCollectionUrl_SecretId,
    SumoLogicCredential,
    SumoLogicCredential_Basic,
    SumoLogicCredential_BasicId,
    TaniumCloudCredential,
    TaniumCloudCredential_Token,
    TaniumCloudCredential_TokenId,
    TeamsCredential,
    TeamsCredential_Secret,
    TeamsCredential_SecretId,
    TenableCloudCredential,
    TenableCloudCredential_Token,
    TenableCloudCredential_TokenId,
    TicketingJira,
    TicketingMock,
    TicketingPagerDuty,
    TicketingServiceNow,
    TicketingTorq,
    TimeseriesResult,
    Token,
    TokenCredential,
    TokenCredentialId,
    TokenId,
    TokenOwnerType,
    TokenPair,
    TokensActions,
    TokensPermissions,
    TooManyRequestsError,
    TorqCredential,
    TorqCredential_OAuthClient,
    TorqCredential_OAuthClientId,
    Transform,
    TransformId,
    TransformsActions,
    TransformsPermissions,
    UnauthorizedError,
    UnsupportedMediaTypeError,
    UpdateAccountRequest,
    UpdateAccountResponse,
    UpdateBridgeRequest,
    UpdateBridgeResponse,
    UpdateCredentialRequest,
    UpdateCredentialResponse,
    UpdateIntegrationPointRequest,
    UpdateIntegrationPointResponse,
    UpdateIntegrationRequest,
    UpdateIntegrationResponse,
    UpdateMemberRequest,
    UpdateMemberResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateOrganizationWebhookRequest,
    UpdateOrganizationWebhookResponse,
    UpdateRoleRequest,
    UpdateRoleResponse,
    UpdateTransformRequest,
    UpdateTransformResponse,
    Usage,
    ValueMapping,
    VerifyIntegrationRequest,
    VulnerabilitiesCrowdStrike,
    VulnerabilitiesQualysCloud,
    VulnerabilitiesRapid7InsightCloud,
    VulnerabilitiesTaniumCloud,
    VulnerabilitiesTenableCloud,
    WebhookFilter,
    WebhookId,
    WebhooksActions,
    WebhooksPermissions,
    accounts,
    audit,
    auth,
    auth_base,
    bridge,
    capabilities,
    capabilities_base,
    common,
    credentials,
    integration_base,
    integration_points,
    integrations,
    member_base,
    members,
    meta,
    organization,
    organization_base,
    organization_webhook_base,
    organization_webhook_events,
    organization_webhooks,
    permissions,
    permissionset,
    permissionset_base,
    providers_generated,
    role_base,
    roles,
    status,
    sub_orgs,
    token_base,
    tokens,
    transforms,
    usage,
)
from .environment import SynqlyManagementEnvironment

__all__ = [
    "Account",
    "AccountId",
    "AccountsActions",
    "AccountsPermissions",
    "AdhocRole",
    "ApiPermissionMap",
    "ArmisCredential",
    "ArmisCredential_Token",
    "ArmisCredential_TokenId",
    "AssetsArmisCentrix",
    "AssetsNozomiVantage",
    "AssetsServiceNow",
    "Audit",
    "AuditActions",
    "AuditPermissions",
    "AuthActions",
    "AuthCode",
    "AuthPermissions",
    "AwsCredential",
    "AwsCredentialId",
    "AwsS3Credential",
    "AwsS3Credential_Aws",
    "AwsS3Credential_AwsId",
    "AwsSecurityLakeCredential",
    "AwsSecurityLakeCredential_Aws",
    "AwsSecurityLakeCredential_AwsId",
    "AwsSqsCredential",
    "AwsSqsCredential_Aws",
    "AwsSqsCredential_AwsId",
    "AzureBlobCredential",
    "AzureBlobCredential_Token",
    "AzureBlobCredential_TokenId",
    "AzureMonitorLogsCredential",
    "AzureMonitorLogsCredential_Token",
    "AzureMonitorLogsCredential_TokenId",
    "BadGatewayError",
    "BadRequestError",
    "Base",
    "BasicCredential",
    "BasicCredentialId",
    "BridgeGroup",
    "BridgeGroupId",
    "BridgeSelector",
    "BridgeSelector_Id",
    "BridgeSelector_Labels",
    "BridgesActions",
    "BridgesPermissions",
    "BuiltinRoles",
    "CapabilitiesActions",
    "CapabilitiesPermissions",
    "CapabilitiesProviderConfig",
    "Category",
    "CategoryId",
    "ChangePasswordRequest",
    "ChangePasswordResponse",
    "ChangePasswordResponseResult",
    "ConflictError",
    "CreateAccountRequest",
    "CreateAccountResponse",
    "CreateAccountResponseResult",
    "CreateBridgeRequest",
    "CreateBridgeResponse",
    "CreateBridgeResponseResult",
    "CreateCredentialRequest",
    "CreateCredentialResponse",
    "CreateIntegrationPointRequest",
    "CreateIntegrationPointResponse",
    "CreateIntegrationRequest",
    "CreateIntegrationResponse",
    "CreateIntegrationResponseResult",
    "CreateIntegrationTokenRequest",
    "CreateIntegrationTokenResponse",
    "CreateMemberRequest",
    "CreateMemberResponse",
    "CreateMemberResponseResult",
    "CreateOrganizationRequest",
    "CreateOrganizationResponse",
    "CreateOrganizationResponseResult",
    "CreateOrganizationWebhookRequest",
    "CreateOrganizationWebhookResponse",
    "CreateRoleRequest",
    "CreateRoleResponse",
    "CreateTokenRequest",
    "CreateTokenResponse",
    "CreateTransformRequest",
    "CreateTransformResponse",
    "Credential",
    "CredentialConfig",
    "CredentialConfigNoSecret",
    "CredentialConfig_Aws",
    "CredentialConfig_Basic",
    "CredentialConfig_OAuthClient",
    "CredentialConfig_Secret",
    "CredentialConfig_Token",
    "CredentialId",
    "CredentialResponse",
    "CredentialType",
    "CredentialsActions",
    "CredentialsPermissions",
    "CrowdStrikeCredential",
    "CrowdStrikeCredential_OAuthClient",
    "CrowdStrikeCredential_OAuthClientId",
    "CustomFieldMapping",
    "DefenderCredential",
    "DefenderCredential_OAuthClient",
    "DefenderCredential_OAuthClientId",
    "DefenderCredential_TenantId",
    "DefenderCredential_UrlString",
    "EdrCrowdStrike",
    "EdrDefender",
    "EdrSentinelOne",
    "ElasticsearchCredential",
    "ElasticsearchCredential_Token",
    "ElasticsearchCredential_TokenId",
    "EntraIdCredential",
    "EntraIdCredential_OAuthClient",
    "EntraIdCredential_OAuthClientId",
    "Environment",
    "ErrorBody",
    "ErrorParam",
    "ForbiddenError",
    "GatewayTimeoutError",
    "GcsCredential",
    "GcsCredential_Aws",
    "GcsCredential_AwsId",
    "GetAccountResponse",
    "GetBridgeResponse",
    "GetCredentialResponse",
    "GetIntegrationPointResponse",
    "GetIntegrationResponse",
    "GetIntegrationTimeseries",
    "GetIntegrationTimeseriesResult",
    "GetMemberResponse",
    "GetOpenApiSpecResponse",
    "GetOrganizationResponse",
    "GetOrganizationWebhookResponse",
    "GetPermissionSetResponse",
    "GetRoleResponse",
    "GetStatusResponse",
    "GetStatusTimeseries",
    "GetStatusTimeseriesResult",
    "GetTokenResponse",
    "GetTransformResponse",
    "HooksHttp",
    "HooksHttpCredential",
    "HooksHttpCredential_Token",
    "HooksHttpCredential_TokenId",
    "HttpMethod",
    "Id",
    "IdentityEntraId",
    "IdentityOkta",
    "IdentityPingOne",
    "Integration",
    "IntegrationEnvironments",
    "IntegrationId",
    "IntegrationPoint",
    "IntegrationPointId",
    "IntegrationPointsActions",
    "IntegrationPointsPermissions",
    "IntegrationsActions",
    "IntegrationsPermissions",
    "InternalServerError",
    "JiraCredential",
    "JiraCredential_Basic",
    "JiraCredential_BasicId",
    "ListAccountIntegrationsResponse",
    "ListAccountsResponse",
    "ListAuditEventsResponse",
    "ListBridgesResponse",
    "ListCategoryCapabilitiesResponse",
    "ListCredentialsResponse",
    "ListIntegrationOptions",
    "ListIntegrationPointsResponse",
    "ListIntegrationsResponse",
    "ListMembersResponse",
    "ListOrganizationResponse",
    "ListOrganizationWebhooksResponse",
    "ListPermissionSetsResponse",
    "ListProviderCapabilitiesResponse",
    "ListRolesResponse",
    "ListStatusEventsResponse",
    "ListStatusOptions",
    "ListStatusResponse",
    "ListTokensResponse",
    "ListTransformsResponse",
    "LogonRequest",
    "LogonResponse",
    "LogonResponseResult",
    "LookupCredentialResponse",
    "ManagedType",
    "Member",
    "MemberId",
    "MemberOptions",
    "MembersActions",
    "MembersPermissions",
    "MethodNotAllowedError",
    "NotFoundError",
    "NotImplementedError",
    "NotificationsJira",
    "NotificationsMock",
    "NotificationsSlack",
    "NotificationsTeams",
    "NozomiVantageCredential",
    "NozomiVantageCredential_Basic",
    "NozomiVantageCredential_BasicId",
    "OAuthClientCredential",
    "OAuthClientCredentialId",
    "OktaCredential",
    "OktaCredential_OAuthClient",
    "OktaCredential_OAuthClientId",
    "OktaCredential_Token",
    "OktaCredential_TokenId",
    "Options",
    "Organization",
    "OrganizationActions",
    "OrganizationId",
    "OrganizationOptions",
    "OrganizationPermissions",
    "OrganizationType",
    "OrganizationWebhook",
    "OrganizationWebhookPayload",
    "OrganizationWebhookSecret",
    "OwnerType",
    "PagerDutyCredential",
    "PagerDutyCredential_Token",
    "PagerDutyCredential_TokenId",
    "PatchAccountResponse",
    "PatchBridgeResponse",
    "PatchCredentialResponse",
    "PatchIntegrationPointResponse",
    "PatchIntegrationResponse",
    "PatchMemberResponse",
    "PatchOrganizationResponse",
    "PatchOrganizationWebhookResponse",
    "PatchRoleResponse",
    "PatchTransformResponse",
    "Permission",
    "PermissionSet",
    "PermissionSetActions",
    "PermissionSetPermissions",
    "Permissions",
    "PingOneCredential",
    "PingOneCredential_Token",
    "PingOneCredential_TokenId",
    "PriorityMapping",
    "Provider",
    "ProviderConfig",
    "ProviderConfigId",
    "ProviderConfig_AssetsArmisCentrix",
    "ProviderConfig_AssetsNozomiVantage",
    "ProviderConfig_AssetsServicenow",
    "ProviderConfig_EdrCrowdstrike",
    "ProviderConfig_EdrDefender",
    "ProviderConfig_EdrSentinelone",
    "ProviderConfig_HooksHttp",
    "ProviderConfig_IdentityEntraId",
    "ProviderConfig_IdentityOkta",
    "ProviderConfig_IdentityPingone",
    "ProviderConfig_NotificationsJira",
    "ProviderConfig_NotificationsMockNotifications",
    "ProviderConfig_NotificationsSlack",
    "ProviderConfig_NotificationsTeams",
    "ProviderConfig_SiemElasticsearch",
    "ProviderConfig_SiemMockSiem",
    "ProviderConfig_SiemQRadar",
    "ProviderConfig_SiemRapid7Insightidr",
    "ProviderConfig_SiemSplunk",
    "ProviderConfig_SiemSumoLogic",
    "ProviderConfig_SinkAwsSecurityLake",
    "ProviderConfig_SinkAwsSqs",
    "ProviderConfig_SinkAzureMonitorLogs",
    "ProviderConfig_SinkMockSink",
    "ProviderConfig_StorageAwsS3",
    "ProviderConfig_StorageAzureBlob",
    "ProviderConfig_StorageGcs",
    "ProviderConfig_StorageMockStorage",
    "ProviderConfig_TicketingJira",
    "ProviderConfig_TicketingMockTicketing",
    "ProviderConfig_TicketingPagerduty",
    "ProviderConfig_TicketingServicenow",
    "ProviderConfig_TicketingTorq",
    "ProviderConfig_VulnerabilitiesCrowdstrike",
    "ProviderConfig_VulnerabilitiesQualysCloud",
    "ProviderConfig_VulnerabilitiesRapid7InsightCloud",
    "ProviderConfig_VulnerabilitiesTaniumCloud",
    "ProviderConfig_VulnerabilitiesTenableCloud",
    "ProviderCredentialConfig",
    "ProviderId",
    "QRadarCredential",
    "QRadarCredential_Token",
    "QRadarCredential_TokenId",
    "QualysCloudCredential",
    "QualysCloudCredential_Basic",
    "QualysCloudCredential_BasicId",
    "Rapid7InsightCloudCredential",
    "Rapid7InsightCloudCredential_Token",
    "Rapid7InsightCloudCredential_TokenId",
    "ReadWriteActions",
    "ReadWritePermissions",
    "RefreshToken",
    "RefreshTokenResponse",
    "ResetTokenResponse",
    "ResourceRestrictions",
    "Resources",
    "RoleAccounts",
    "RoleDefinition",
    "RoleId",
    "RoleIntegrations",
    "RoleName",
    "RoleOrganizations",
    "RolesActions",
    "RolesPermissions",
    "SecretCredential",
    "SecretCredentialId",
    "SentinelOneCredential",
    "SentinelOneCredential_Token",
    "SentinelOneCredential_TokenId",
    "ServiceNowCredential",
    "ServiceNowCredential_Basic",
    "ServiceNowCredential_BasicId",
    "ServiceUnavailableError",
    "SiemElasticsearch",
    "SiemMock",
    "SiemQRadar",
    "SiemRapid7InsightIdr",
    "SiemSplunk",
    "SiemSumoLogic",
    "SinkAwsSecurityLake",
    "SinkAwsSqs",
    "SinkAzureMonitorLogs",
    "SinkMock",
    "SlackCredential",
    "SlackCredential_Token",
    "SlackCredential_TokenId",
    "SplunkHecToken",
    "SplunkHecToken_Token",
    "SplunkHecToken_TokenId",
    "SplunkSearchCredential",
    "SplunkSearchCredential_Token",
    "SplunkSearchCredential_TokenId",
    "State",
    "Status",
    "StatusActions",
    "StatusEvent",
    "StatusMapping",
    "StatusPermissions",
    "StorageAwsS3",
    "StorageAzureBlob",
    "StorageGcs",
    "StorageMock",
    "SubOrgsActions",
    "SubOrgsPermissions",
    "SumoLogicCollectionUrl",
    "SumoLogicCollectionUrl_Secret",
    "SumoLogicCollectionUrl_SecretId",
    "SumoLogicCredential",
    "SumoLogicCredential_Basic",
    "SumoLogicCredential_BasicId",
    "SynqlyManagementEnvironment",
    "TaniumCloudCredential",
    "TaniumCloudCredential_Token",
    "TaniumCloudCredential_TokenId",
    "TeamsCredential",
    "TeamsCredential_Secret",
    "TeamsCredential_SecretId",
    "TenableCloudCredential",
    "TenableCloudCredential_Token",
    "TenableCloudCredential_TokenId",
    "TicketingJira",
    "TicketingMock",
    "TicketingPagerDuty",
    "TicketingServiceNow",
    "TicketingTorq",
    "TimeseriesResult",
    "Token",
    "TokenCredential",
    "TokenCredentialId",
    "TokenId",
    "TokenOwnerType",
    "TokenPair",
    "TokensActions",
    "TokensPermissions",
    "TooManyRequestsError",
    "TorqCredential",
    "TorqCredential_OAuthClient",
    "TorqCredential_OAuthClientId",
    "Transform",
    "TransformId",
    "TransformsActions",
    "TransformsPermissions",
    "UnauthorizedError",
    "UnsupportedMediaTypeError",
    "UpdateAccountRequest",
    "UpdateAccountResponse",
    "UpdateBridgeRequest",
    "UpdateBridgeResponse",
    "UpdateCredentialRequest",
    "UpdateCredentialResponse",
    "UpdateIntegrationPointRequest",
    "UpdateIntegrationPointResponse",
    "UpdateIntegrationRequest",
    "UpdateIntegrationResponse",
    "UpdateMemberRequest",
    "UpdateMemberResponse",
    "UpdateOrganizationRequest",
    "UpdateOrganizationResponse",
    "UpdateOrganizationWebhookRequest",
    "UpdateOrganizationWebhookResponse",
    "UpdateRoleRequest",
    "UpdateRoleResponse",
    "UpdateTransformRequest",
    "UpdateTransformResponse",
    "Usage",
    "ValueMapping",
    "VerifyIntegrationRequest",
    "VulnerabilitiesCrowdStrike",
    "VulnerabilitiesQualysCloud",
    "VulnerabilitiesRapid7InsightCloud",
    "VulnerabilitiesTaniumCloud",
    "VulnerabilitiesTenableCloud",
    "WebhookFilter",
    "WebhookId",
    "WebhooksActions",
    "WebhooksPermissions",
    "accounts",
    "audit",
    "auth",
    "auth_base",
    "bridge",
    "capabilities",
    "capabilities_base",
    "common",
    "credentials",
    "integration_base",
    "integration_points",
    "integrations",
    "member_base",
    "members",
    "meta",
    "organization",
    "organization_base",
    "organization_webhook_base",
    "organization_webhook_events",
    "organization_webhooks",
    "permissions",
    "permissionset",
    "permissionset_base",
    "providers_generated",
    "role_base",
    "roles",
    "status",
    "sub_orgs",
    "token_base",
    "tokens",
    "transforms",
    "usage",
]
