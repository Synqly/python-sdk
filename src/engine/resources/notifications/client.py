# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ..common.errors.bad_request_error import BadRequestError
from ..common.errors.forbidden_error import ForbiddenError
from ..common.errors.not_allowed_error import NotAllowedError
from ..common.errors.not_found_error import NotFoundError
from ..common.errors.unauthorized_error import UnauthorizedError
from ..common.types.error_body import ErrorBody
from .types.create_notification_request import CreateNotificationRequest
from .types.create_notification_response import CreateNotificationResponse
from .types.get_notification_response import GetNotificationResponse
from .types.notification_id import NotificationId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_notification(self, notification_id: NotificationId) -> GetNotificationResponse:
        """
        Returns the `Notification` object matching `{notificationId}` from the token-linked
        `Integration`.

        Parameters:
            - notification_id: NotificationId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/notifications/get/{notification_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetNotificationResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise NotAllowedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_notification(self, *, request: CreateNotificationRequest) -> CreateNotificationResponse:
        """
        Creates a `Notification` object in the token-linked `Integration`.

        Parameters:
            - request: CreateNotificationRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/notifications/create"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateNotificationResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def clear_notification(self, notification_id: NotificationId) -> None:
        """
        Resolves a `Notification` object in the token-linked `Integration`.

        Parameters:
            - notification_id: NotificationId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/notifications/clear/{notification_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_notification(self, notification_id: NotificationId) -> GetNotificationResponse:
        """
        Returns the `Notification` object matching `{notificationId}` from the token-linked
        `Integration`.

        Parameters:
            - notification_id: NotificationId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/notifications/get/{notification_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetNotificationResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise NotAllowedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_notification(self, *, request: CreateNotificationRequest) -> CreateNotificationResponse:
        """
        Creates a `Notification` object in the token-linked `Integration`.

        Parameters:
            - request: CreateNotificationRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/notifications/create"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateNotificationResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def clear_notification(self, notification_id: NotificationId) -> None:
        """
        Resolves a `Notification` object in the token-linked `Integration`.

        Parameters:
            - notification_id: NotificationId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/notifications/clear/{notification_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
