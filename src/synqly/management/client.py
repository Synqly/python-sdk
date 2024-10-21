# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SynqlyManagementEnvironment
from .resources.accounts.client import AccountsClient, AsyncAccountsClient
from .resources.audit.client import AsyncAuditClient, AuditClient
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.bridges.client import AsyncBridgesClient, BridgesClient
from .resources.capabilities.client import AsyncCapabilitiesClient, CapabilitiesClient
from .resources.capabilities_deprecated.client import AsyncCapabilitiesDeprecatedClient, CapabilitiesDeprecatedClient
from .resources.credentials.client import AsyncCredentialsClient, CredentialsClient
from .resources.integration_points.client import AsyncIntegrationPointsClient, IntegrationPointsClient
from .resources.integrations.client import AsyncIntegrationsClient, IntegrationsClient
from .resources.members.client import AsyncMembersClient, MembersClient
from .resources.meta.client import AsyncMetaClient, MetaClient
from .resources.organization.client import AsyncOrganizationClient, OrganizationClient
from .resources.organization_webhooks.client import AsyncOrganizationWebhooksClient, OrganizationWebhooksClient
from .resources.permissionset.client import AsyncPermissionsetClient, PermissionsetClient
from .resources.roles.client import AsyncRolesClient, RolesClient
from .resources.status.client import AsyncStatusClient, StatusClient
from .resources.sub_orgs.client import AsyncSubOrgsClient, SubOrgsClient
from .resources.tokens.client import AsyncTokensClient, TokensClient
from .resources.transforms.client import AsyncTransformsClient, TransformsClient


class SynqlyManagement:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SynqlyManagementEnvironment. The environment to use for requests from the client. from .environment import SynqlyManagementEnvironment

                                                    Defaults to SynqlyManagementEnvironment.SYNQLY

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from synqly.client import SynqlyManagement

    client = SynqlyManagement(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SynqlyManagementEnvironment = SynqlyManagementEnvironment.SYNQLY,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.accounts = AccountsClient(client_wrapper=self._client_wrapper)
        self.audit = AuditClient(client_wrapper=self._client_wrapper)
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.bridges = BridgesClient(client_wrapper=self._client_wrapper)
        self.capabilities_deprecated = CapabilitiesDeprecatedClient(client_wrapper=self._client_wrapper)
        self.capabilities = CapabilitiesClient(client_wrapper=self._client_wrapper)
        self.credentials = CredentialsClient(client_wrapper=self._client_wrapper)
        self.integration_points = IntegrationPointsClient(client_wrapper=self._client_wrapper)
        self.integrations = IntegrationsClient(client_wrapper=self._client_wrapper)
        self.members = MembersClient(client_wrapper=self._client_wrapper)
        self.meta = MetaClient(client_wrapper=self._client_wrapper)
        self.organization_webhooks = OrganizationWebhooksClient(client_wrapper=self._client_wrapper)
        self.organization = OrganizationClient(client_wrapper=self._client_wrapper)
        self.permissionset = PermissionsetClient(client_wrapper=self._client_wrapper)
        self.roles = RolesClient(client_wrapper=self._client_wrapper)
        self.status = StatusClient(client_wrapper=self._client_wrapper)
        self.sub_orgs = SubOrgsClient(client_wrapper=self._client_wrapper)
        self.tokens = TokensClient(client_wrapper=self._client_wrapper)
        self.transforms = TransformsClient(client_wrapper=self._client_wrapper)


class AsyncSynqlyManagement:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SynqlyManagementEnvironment. The environment to use for requests from the client. from .environment import SynqlyManagementEnvironment

                                                    Defaults to SynqlyManagementEnvironment.SYNQLY

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from synqly.client import AsyncSynqlyManagement

    client = AsyncSynqlyManagement(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SynqlyManagementEnvironment = SynqlyManagementEnvironment.SYNQLY,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.accounts = AsyncAccountsClient(client_wrapper=self._client_wrapper)
        self.audit = AsyncAuditClient(client_wrapper=self._client_wrapper)
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.bridges = AsyncBridgesClient(client_wrapper=self._client_wrapper)
        self.capabilities_deprecated = AsyncCapabilitiesDeprecatedClient(client_wrapper=self._client_wrapper)
        self.capabilities = AsyncCapabilitiesClient(client_wrapper=self._client_wrapper)
        self.credentials = AsyncCredentialsClient(client_wrapper=self._client_wrapper)
        self.integration_points = AsyncIntegrationPointsClient(client_wrapper=self._client_wrapper)
        self.integrations = AsyncIntegrationsClient(client_wrapper=self._client_wrapper)
        self.members = AsyncMembersClient(client_wrapper=self._client_wrapper)
        self.meta = AsyncMetaClient(client_wrapper=self._client_wrapper)
        self.organization_webhooks = AsyncOrganizationWebhooksClient(client_wrapper=self._client_wrapper)
        self.organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        self.permissionset = AsyncPermissionsetClient(client_wrapper=self._client_wrapper)
        self.roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        self.status = AsyncStatusClient(client_wrapper=self._client_wrapper)
        self.sub_orgs = AsyncSubOrgsClient(client_wrapper=self._client_wrapper)
        self.tokens = AsyncTokensClient(client_wrapper=self._client_wrapper)
        self.transforms = AsyncTransformsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: SynqlyManagementEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
