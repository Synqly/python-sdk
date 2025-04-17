# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .authorization import Authorization
from .idp import Idp
from .process import Process
from .session import Session
from .user import User

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Actor(pydantic.BaseModel):
    """
    The Actor object contains details about the user, role, application, service, or process that initiated or performed a specific activity. Note that Actor is not the threat actor of a campaign but may be part of a campaign.
    """

    app_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The client application or service that initiated the activity. This can be in conjunction with the <code>user</code> if present. Note that <code>app_name</code> is distinct from the <code>process</code> if present.
    """

    app_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the client application or service that initiated the activity. This can be in conjunction with the <code>user</code> if present. Note that <code>app_name</code> is distinct from the <code>process.pid</code> or <code>process.uid</code> if present.
    """

    authorizations: typing.Optional[typing.List[Authorization]] = pydantic.Field(default=None)
    """
    Provides details about an authorization, such as authorization outcome, and any associated policies related to the activity/event.
    """

    idp: typing.Optional[Idp] = pydantic.Field(default=None)
    """
    This object describes details about the Identity Provider used.
    """

    invoked_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the service that invoked the activity as described in the event.
    """

    process: typing.Optional[Process] = pydantic.Field(default=None)
    """
    The process that initiated the activity.
    """

    session: typing.Optional[Session] = pydantic.Field(default=None)
    """
    The user session from which the activity was initiated.
    """

    user: typing.Optional[User] = pydantic.Field(default=None)
    """
    The user that initiated the activity or the user context from which the activity was initiated.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
