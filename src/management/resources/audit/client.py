# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..common.errors.forbidden_error import ForbiddenError
from ..common.errors.not_found_error import NotFoundError
from ..common.errors.unauthorized_error import UnauthorizedError
from ..common.types.error_body import ErrorBody
from .types.list_audit_events_response import ListAuditEventsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        start_after: typing.Optional[str] = None,
        end_before: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[typing.Union[str, typing.List[str]]] = None,
    ) -> ListAuditEventsResponse:
        """
        Returns a list of all Synqly `Audit` events for the `Organization`.

        Parameters:
            - limit: typing.Optional[int]. Number of `Audit` objects to return in this page. Defaults to 100.

            - start_after: typing.Optional[str]. Return `Audit` objects starting after this `created_at`.

            - end_before: typing.Optional[str]. Return `Audit` objects ending before this `created_at`.

            - order: typing.Optional[str]. The order defaults to created_at[asc] and can changed to descending order by specifying created_at[desc].

            - filter: typing.Optional[typing.Union[str, typing.List[str]]]. Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
                                                                            If used more than once, the queries are ANDed together.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/audit/organizations"),
            params=remove_none_from_dict(
                {"limit": limit, "start_after": start_after, "end_before": end_before, "order": order, "filter": filter}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListAuditEventsResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        start_after: typing.Optional[str] = None,
        end_before: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[typing.Union[str, typing.List[str]]] = None,
    ) -> ListAuditEventsResponse:
        """
        Returns a list of all Synqly `Audit` events for the `Organization`.

        Parameters:
            - limit: typing.Optional[int]. Number of `Audit` objects to return in this page. Defaults to 100.

            - start_after: typing.Optional[str]. Return `Audit` objects starting after this `created_at`.

            - end_before: typing.Optional[str]. Return `Audit` objects ending before this `created_at`.

            - order: typing.Optional[str]. The order defaults to created_at[asc] and can changed to descending order by specifying created_at[desc].

            - filter: typing.Optional[typing.Union[str, typing.List[str]]]. Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
                                                                            If used more than once, the queries are ANDed together.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/audit/organizations"),
            params=remove_none_from_dict(
                {"limit": limit, "start_after": start_after, "end_before": end_before, "order": order, "filter": filter}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListAuditEventsResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
