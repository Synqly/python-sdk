# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..common.errors.bad_request_error import BadRequestError
from ..common.errors.forbidden_error import ForbiddenError
from ..common.errors.not_found_error import NotFoundError
from ..common.errors.unauthorized_error import UnauthorizedError
from ..common.types.error_body import ErrorBody
from .types.query_findings_response import QueryFindingsResponse
from .types.query_vulnerability_assets_response import QueryVulnerabilityAssetsResponse


class VulnerabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def query_vulnerability_findings(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        filter: typing.Union[typing.Optional[str], typing.List[str]],
    ) -> QueryFindingsResponse:
        """
        Query vulnerability findings

        Parameters:
            - limit: typing.Optional[int]. Number of finding reports to return. Defaults to 50.

            - cursor: typing.Optional[str]. Start search from cursor position.

            - filter: typing.Union[typing.Optional[str], typing.List[str]]. Filter results by this query. For more information on filtering, refer to the Vulnerability Filtering Guide.
                                                                            Defaults to no filter. If used more than once, the queries are ANDed together.

        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/vulnerabilities/findings"),
            params=remove_none_from_dict({"limit": limit, "cursor": cursor, "filter": filter}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(QueryFindingsResponse, _response.json())  # type: ignore
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

    def query_vulnerability_assets(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        filter: typing.Union[typing.Optional[str], typing.List[str]],
    ) -> QueryVulnerabilityAssetsResponse:
        """
        Query assets in a vulnerability scanning system

        Parameters:
            - limit: typing.Optional[int]. Number of assets to return. Defaults to 50.

            - cursor: typing.Optional[str]. Start search from cursor position.

            - filter: typing.Union[typing.Optional[str], typing.List[str]]. Filter results by this query. For more information on filtering, refer to the Vulnerability Filtering Guide.
                                                                            Defaults to no filter. If used more than once, the queries are ANDed together.

        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/vulnerabilities/assets"),
            params=remove_none_from_dict({"limit": limit, "cursor": cursor, "filter": filter}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(QueryVulnerabilityAssetsResponse, _response.json())  # type: ignore
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


class AsyncVulnerabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def query_vulnerability_findings(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        filter: typing.Union[typing.Optional[str], typing.List[str]],
    ) -> QueryFindingsResponse:
        """
        Query vulnerability findings

        Parameters:
            - limit: typing.Optional[int]. Number of finding reports to return. Defaults to 50.

            - cursor: typing.Optional[str]. Start search from cursor position.

            - filter: typing.Union[typing.Optional[str], typing.List[str]]. Filter results by this query. For more information on filtering, refer to the Vulnerability Filtering Guide.
                                                                            Defaults to no filter. If used more than once, the queries are ANDed together.

        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/vulnerabilities/findings"),
            params=remove_none_from_dict({"limit": limit, "cursor": cursor, "filter": filter}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(QueryFindingsResponse, _response.json())  # type: ignore
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

    async def query_vulnerability_assets(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        filter: typing.Union[typing.Optional[str], typing.List[str]],
    ) -> QueryVulnerabilityAssetsResponse:
        """
        Query assets in a vulnerability scanning system

        Parameters:
            - limit: typing.Optional[int]. Number of assets to return. Defaults to 50.

            - cursor: typing.Optional[str]. Start search from cursor position.

            - filter: typing.Union[typing.Optional[str], typing.List[str]]. Filter results by this query. For more information on filtering, refer to the Vulnerability Filtering Guide.
                                                                            Defaults to no filter. If used more than once, the queries are ANDed together.

        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/vulnerabilities/assets"),
            params=remove_none_from_dict({"limit": limit, "cursor": cursor, "filter": filter}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(QueryVulnerabilityAssetsResponse, _response.json())  # type: ignore
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
