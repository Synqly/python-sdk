# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.error_body import ErrorBody


class BadRequestError(ApiError):
    def __init__(self, body: ErrorBody):
        super().__init__(status_code=400, body=body)
