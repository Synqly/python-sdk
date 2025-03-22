# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.problem import Problem


class GatewayTimeoutError(ApiError):
    def __init__(self, body: Problem):
        super().__init__(status_code=504, body=body)
