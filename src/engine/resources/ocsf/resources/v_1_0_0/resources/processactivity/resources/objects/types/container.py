# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .fingerprint import Fingerprint
from .image import Image

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Container(pydantic.BaseModel):
    """
    The Container object describes an instance of a specific container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
    """

    hash: typing.Optional[Fingerprint] = pydantic.Field(default=None)
    """
    Commit hash of image created for docker or the SHA256 hash of the container. For example: <code>13550340a8681c84c861aac2e5b440161c2b33a3e4f302ac680ca5b686de48de</code>.
    """

    image: typing.Optional[Image] = pydantic.Field(default=None)
    """
    The container image used as a template to run the container.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The container name.
    """

    network_driver: typing.Optional[str] = pydantic.Field(default=None)
    """
    The network driver used by the container. For example, bridge, overlay, host, none, etc.
    """

    orchestrator: typing.Optional[str] = pydantic.Field(default=None)
    """
    The orchestrator managing the container, such as ECS, EKS, K8s, or OpenShift.
    """

    pod_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the pod (or equivalent) that the container is executing on.
    """

    runtime: typing.Optional[str] = pydantic.Field(default=None)
    """
    The backend running the container, such as containerd or cri-o.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the container image.
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag used by the container. It can indicate version, format, OS.
    """

    uid: str = pydantic.Field()
    """
    The full container unique identifier for this instantiation of the container. For example: <code>ac2ea168264a08f9aaca0dfc82ff3551418dfd22d02b713142a6843caa2f61bf</code>.
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
