# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SynqlyEngineEnvironment
from .resources.appsec.client import AppsecClient, AsyncAppsecClient
from .resources.assets.client import AssetsClient, AsyncAssetsClient
from .resources.cloudsecurity.client import AsyncCloudsecurityClient, CloudsecurityClient
from .resources.edr.client import AsyncEdrClient, EdrClient
from .resources.hooks.client import AsyncHooksClient, HooksClient
from .resources.identity.client import AsyncIdentityClient, IdentityClient
from .resources.integration_webhooks.client import AsyncIntegrationWebhooksClient, IntegrationWebhooksClient
from .resources.notifications.client import AsyncNotificationsClient, NotificationsClient
from .resources.operations.client import AsyncOperationsClient, OperationsClient
from .resources.siem.client import AsyncSiemClient, SiemClient
from .resources.sink.client import AsyncSinkClient, SinkClient
from .resources.storage.client import AsyncStorageClient, StorageClient
from .resources.ticketing.client import AsyncTicketingClient, TicketingClient
from .resources.vulnerabilities.client import AsyncVulnerabilitiesClient, VulnerabilitiesClient


class SynqlyEngine:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SynqlyEngineEnvironment. The environment to use for requests from the client. from .environment import SynqlyEngineEnvironment

                                                Defaults to SynqlyEngineEnvironment.SYNQLY

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from synqly.client import SynqlyEngine

    client = SynqlyEngine(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SynqlyEngineEnvironment = SynqlyEngineEnvironment.SYNQLY,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.appsec = AppsecClient(client_wrapper=self._client_wrapper)
        self.assets = AssetsClient(client_wrapper=self._client_wrapper)
        self.cloudsecurity = CloudsecurityClient(client_wrapper=self._client_wrapper)
        self.edr = EdrClient(client_wrapper=self._client_wrapper)
        self.hooks = HooksClient(client_wrapper=self._client_wrapper)
        self.identity = IdentityClient(client_wrapper=self._client_wrapper)
        self.integration_webhooks = IntegrationWebhooksClient(client_wrapper=self._client_wrapper)
        self.notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        self.operations = OperationsClient(client_wrapper=self._client_wrapper)
        self.siem = SiemClient(client_wrapper=self._client_wrapper)
        self.sink = SinkClient(client_wrapper=self._client_wrapper)
        self.storage = StorageClient(client_wrapper=self._client_wrapper)
        self.ticketing = TicketingClient(client_wrapper=self._client_wrapper)
        self.vulnerabilities = VulnerabilitiesClient(client_wrapper=self._client_wrapper)


class AsyncSynqlyEngine:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SynqlyEngineEnvironment. The environment to use for requests from the client. from .environment import SynqlyEngineEnvironment

                                                Defaults to SynqlyEngineEnvironment.SYNQLY

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from synqly.client import AsyncSynqlyEngine

    client = AsyncSynqlyEngine(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SynqlyEngineEnvironment = SynqlyEngineEnvironment.SYNQLY,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.appsec = AsyncAppsecClient(client_wrapper=self._client_wrapper)
        self.assets = AsyncAssetsClient(client_wrapper=self._client_wrapper)
        self.cloudsecurity = AsyncCloudsecurityClient(client_wrapper=self._client_wrapper)
        self.edr = AsyncEdrClient(client_wrapper=self._client_wrapper)
        self.hooks = AsyncHooksClient(client_wrapper=self._client_wrapper)
        self.identity = AsyncIdentityClient(client_wrapper=self._client_wrapper)
        self.integration_webhooks = AsyncIntegrationWebhooksClient(client_wrapper=self._client_wrapper)
        self.notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        self.operations = AsyncOperationsClient(client_wrapper=self._client_wrapper)
        self.siem = AsyncSiemClient(client_wrapper=self._client_wrapper)
        self.sink = AsyncSinkClient(client_wrapper=self._client_wrapper)
        self.storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        self.ticketing = AsyncTicketingClient(client_wrapper=self._client_wrapper)
        self.vulnerabilities = AsyncVulnerabilitiesClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: SynqlyEngineEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
