# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..common.errors.bad_request_error import BadRequestError
from ..common.errors.forbidden_error import ForbiddenError
from ..common.errors.not_found_error import NotFoundError
from ..common.errors.unauthorized_error import UnauthorizedError
from ..common.types.error_body import ErrorBody
from .types.query_devices_response import QueryDevicesResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AssetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def query_devices_info(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        filter: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        order: typing.Optional[str] = None,
    ) -> QueryDevicesResponse:
        """
        Query devices from an asset inventory system

        Parameters:
            - limit: typing.Optional[int]. Number of finding reports to return. Defaults to 50.

            - cursor: typing.Optional[str]. Start search from cursor position.

            - filter: typing.Optional[typing.Union[str, typing.List[str]]]. Filter results by this query. For more information on filtering, refer to the Assets Filtering Guide.
                                                                            Defaults to no filter. If used more than once, the queries are ANDed together.

            - order: typing.Optional[str]. Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
                                           `[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order.
                                           The ordering defaults to `asc` if not specified.

        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/assets/devices"),
            params=remove_none_from_dict({"limit": limit, "cursor": cursor, "filter": filter, "order": order}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(QueryDevicesResponse, _response.json())  # type: ignore
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


class AsyncAssetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def query_devices_info(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        filter: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        order: typing.Optional[str] = None,
    ) -> QueryDevicesResponse:
        """
        Query devices from an asset inventory system

        Parameters:
            - limit: typing.Optional[int]. Number of finding reports to return. Defaults to 50.

            - cursor: typing.Optional[str]. Start search from cursor position.

            - filter: typing.Optional[typing.Union[str, typing.List[str]]]. Filter results by this query. For more information on filtering, refer to the Assets Filtering Guide.
                                                                            Defaults to no filter. If used more than once, the queries are ANDed together.

            - order: typing.Optional[str]. Select a field to order the results by. Defaults to `time`. To control the direction of the sorting, append
                                           `[asc]` or `[desc]` to the field name. For example, `time[asc]` will sort the results by `time` in ascending order.
                                           The ordering defaults to `asc` if not specified.

        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/assets/devices"),
            params=remove_none_from_dict({"limit": limit, "cursor": cursor, "filter": filter, "order": order}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(QueryDevicesResponse, _response.json())  # type: ignore
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
