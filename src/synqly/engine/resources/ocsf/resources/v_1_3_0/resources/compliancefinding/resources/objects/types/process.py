# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.process_name import ProcessName
from ...base.types.timestamp import Timestamp
from .container import Container
from .file import File
from .group import Group
from .object import Object
from .process_integrity_id import ProcessIntegrityId
from .session import Session
from .user import User

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Process(pydantic.BaseModel):
    """
    The Process object describes a running instance of a launched program. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:Process/'>d3f:Process</a>.
    """

    auid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The audit user assigned at login by the audit subsystem.
    """

    cmd_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full command line used to launch an application, service, process, or job. For example: <code>ssh user@10.0.0.10</code>. If the command line is unavailable or missing, the empty string <code>''</code> is to be used.
    """

    container: typing.Optional[Container] = pydantic.Field(default=None)
    """
    The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the process was created/started.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the process was created/started.
    """

    egid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The effective group under which this process is running.
    """

    euid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The effective user under which this process is running.
    """

    file: typing.Optional[File] = pydantic.Field(default=None)
    """
    The process file object.
    """

    group: typing.Optional[Group] = pydantic.Field(default=None)
    """
    The group under which this process is running.
    """

    integrity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The process integrity level, normalized to the caption of the integrity_id value. In the case of 'Other', it is defined by the event source (Windows only).
    """

    integrity_id: typing.Optional[ProcessIntegrityId] = pydantic.Field(default=None)
    """
    The normalized identifier of the process integrity level (Windows only).
    """

    lineage: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The lineage of the process, represented by a list of paths for each ancestor process. For example: <code>['/usr/sbin/sshd', '/usr/bin/bash', '/usr/bin/whoami']</code>.
    """

    loaded_modules: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of loaded module names.
    """

    name: typing.Optional[ProcessName] = pydantic.Field(default=None)
    """
    The friendly name of the process, for example: <code>Notepad++</code>.
    """

    namespace_pid: typing.Optional[int] = pydantic.Field(default=None)
    """
    If running under a process namespace (such as in a container), the process identifier within that process namespace.
    """

    parent_process: typing.Optional[Object] = pydantic.Field(default=None)
    """
    The parent process of this process object. It is recommended to only populate this field for the first process object, to prevent deep nesting.
    """

    pid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The process identifier, as reported by the operating system. Process ID (PID) is a number used by the operating system to uniquely identify an active process.
    """

    sandbox: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the containment jail (i.e., sandbox). For example, hardened_ps, high_security_ps, oracle_ps, netsvcs_ps, or default_ps.
    """

    session: typing.Optional[Session] = pydantic.Field(default=None)
    """
    The user session under which this process is running.
    """

    terminated_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the process was terminated.
    """

    terminated_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the process was terminated.
    """

    tid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Identifier of the thread associated with the event, as returned by the operating system.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for this process assigned by the producer (tool). Facilitates correlation of a process event with other events for that process.
    """

    user: typing.Optional[User] = pydantic.Field(default=None)
    """
    The user under which this process is running.
    """

    xattributes: typing.Optional[Object] = pydantic.Field(default=None)
    """
    An unordered collection of zero or more name/value pairs that represent a process extended attribute.
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
