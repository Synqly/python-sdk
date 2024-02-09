# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..accounts.types.account_id import AccountId
from ..common.errors.bad_request_error import BadRequestError
from ..common.errors.conflict_error import ConflictError
from ..common.errors.forbidden_error import ForbiddenError
from ..common.errors.not_found_error import NotFoundError
from ..common.errors.unauthorized_error import UnauthorizedError
from ..common.types.error_body import ErrorBody
from .types.create_credential_request import CreateCredentialRequest
from .types.create_credential_response import CreateCredentialResponse
from .types.credential_id import CredentialId
from .types.get_credential_response import GetCredentialResponse
from .types.list_credentials_response import ListCredentialsResponse
from .types.patch_credential_response import PatchCredentialResponse
from .types.update_credential_request import UpdateCredentialRequest
from .types.update_credential_response import UpdateCredentialResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_credentials(
        self,
        account_id: AccountId,
        *,
        limit: typing.Optional[int] = None,
        start_after: typing.Optional[str] = None,
        end_before: typing.Optional[str] = None,
        order: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        filter: typing.Optional[typing.Union[str, typing.List[str]]] = None,
    ) -> ListCredentialsResponse:
        """
        Returns a list of all `Credential` objects belonging to the `Account` matching
        `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - limit: typing.Optional[int]. Number of `Credential` objects to return in this page. Defaults to 100.

            - start_after: typing.Optional[str]. Return `Credential` objects starting after this `name`.

            - end_before: typing.Optional[str]. Return `Credential` objects ending before this `name`.

            - order: typing.Optional[typing.Union[str, typing.List[str]]]. Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
                                                                           `[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
                                                                           The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
                                                                           ordering is applied in the order the fields are specified.

            - filter: typing.Optional[typing.Union[str, typing.List[str]]]. Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
                                                                            If used more than once, the queries are ANDed together.

        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}"),
            params=remove_none_from_dict(
                {"limit": limit, "start_after": start_after, "end_before": end_before, "order": order, "filter": filter}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListCredentialsResponse, _response.json())  # type: ignore
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

    def get_credential(self, account_id: AccountId, credential_id: CredentialId) -> GetCredentialResponse:
        """
        Returns the `Credential` object matching `{credentialId}` where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetCredentialResponse, _response.json())  # type: ignore
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

    def create_credential(self, account_id: AccountId, *, request: CreateCredentialRequest) -> CreateCredentialResponse:
        """
        Creates a `Credential` object in the `Account` matching matching
        `{accountId}`. A `Credential` may only by used by a single `Account`;
        however, `Credential` objects can be shared by multiple `Integrations`
        within an `Account`.

        Parameters:
            - account_id: AccountId.

            - request: CreateCredentialRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateCredentialResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_credential(
        self, account_id: AccountId, credential_id: CredentialId, *, request: UpdateCredentialRequest
    ) -> UpdateCredentialResponse:
        """
        Updates the `Credential` object matching `{credentialId}`, where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.

            - request: UpdateCredentialRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateCredentialResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch_credential(
        self, account_id: AccountId, credential_id: CredentialId, *, request: typing.List[typing.Dict[str, typing.Any]]
    ) -> PatchCredentialResponse:
        """
        Patches the `Credential` object matching `{credentialId}`, where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.

            - request: typing.List[typing.Dict[str, typing.Any]].
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatchCredentialResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
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

    def delete_credential(self, account_id: AccountId, credential_id: CredentialId) -> None:
        """
        Deletes the `Credential` object matching `{credentialId}`, where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
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


class AsyncCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_credentials(
        self,
        account_id: AccountId,
        *,
        limit: typing.Optional[int] = None,
        start_after: typing.Optional[str] = None,
        end_before: typing.Optional[str] = None,
        order: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        filter: typing.Optional[typing.Union[str, typing.List[str]]] = None,
    ) -> ListCredentialsResponse:
        """
        Returns a list of all `Credential` objects belonging to the `Account` matching
        `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - limit: typing.Optional[int]. Number of `Credential` objects to return in this page. Defaults to 100.

            - start_after: typing.Optional[str]. Return `Credential` objects starting after this `name`.

            - end_before: typing.Optional[str]. Return `Credential` objects ending before this `name`.

            - order: typing.Optional[typing.Union[str, typing.List[str]]]. Select a field to order the results by. Defaults to `name`. To control the direction of the sorting, append
                                                                           `[asc]` or `[desc]` to the field name. For example, `name[desc]` will sort the results by `name` in descending order.
                                                                           The ordering defaults to `asc` if not specified. May be used multiple times to order by multiple fields, and the
                                                                           ordering is applied in the order the fields are specified.

            - filter: typing.Optional[typing.Union[str, typing.List[str]]]. Filter results by this query. For more information on filtering, refer to our Filtering Guide. Defaults to no filter.
                                                                            If used more than once, the queries are ANDed together.

        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}"),
            params=remove_none_from_dict(
                {"limit": limit, "start_after": start_after, "end_before": end_before, "order": order, "filter": filter}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListCredentialsResponse, _response.json())  # type: ignore
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

    async def get_credential(self, account_id: AccountId, credential_id: CredentialId) -> GetCredentialResponse:
        """
        Returns the `Credential` object matching `{credentialId}` where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetCredentialResponse, _response.json())  # type: ignore
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

    async def create_credential(
        self, account_id: AccountId, *, request: CreateCredentialRequest
    ) -> CreateCredentialResponse:
        """
        Creates a `Credential` object in the `Account` matching matching
        `{accountId}`. A `Credential` may only by used by a single `Account`;
        however, `Credential` objects can be shared by multiple `Integrations`
        within an `Account`.

        Parameters:
            - account_id: AccountId.

            - request: CreateCredentialRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateCredentialResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_credential(
        self, account_id: AccountId, credential_id: CredentialId, *, request: UpdateCredentialRequest
    ) -> UpdateCredentialResponse:
        """
        Updates the `Credential` object matching `{credentialId}`, where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.

            - request: UpdateCredentialRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateCredentialResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch_credential(
        self, account_id: AccountId, credential_id: CredentialId, *, request: typing.List[typing.Dict[str, typing.Any]]
    ) -> PatchCredentialResponse:
        """
        Patches the `Credential` object matching `{credentialId}`, where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.

            - request: typing.List[typing.Dict[str, typing.Any]].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatchCredentialResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorBody, _response.json()))  # type: ignore
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

    async def delete_credential(self, account_id: AccountId, credential_id: CredentialId) -> None:
        """
        Deletes the `Credential` object matching `{credentialId}`, where the
        `Credential` belongs to the `Account` matching `{accountId}`.

        Parameters:
            - account_id: AccountId.

            - credential_id: CredentialId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/credentials/{account_id}/{credential_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
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
