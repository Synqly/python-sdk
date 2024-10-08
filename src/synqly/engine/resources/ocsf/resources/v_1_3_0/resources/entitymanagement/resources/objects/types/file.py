# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.file_name import FileName
from ...base.types.timestamp import Timestamp
from .digital_signature import DigitalSignature
from .file_confidentiality_id import FileConfidentialityId
from .file_type_id import FileTypeId
from .fingerprint import Fingerprint
from .object import Object
from .product import Product
from .user import User

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class File(pydantic.BaseModel):
    """
    The File object represents the metadata associated with a file stored in a computer system. It encompasses information about the file itself, including its attributes, properties, and organizational details. Defined by D3FEND <a target='_blank' href='https://next.d3fend.mitre.org/dao/artifact/d3f:File/'>d3f:File</a>.
    """

    accessed_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the file was last accessed.
    """

    accessed_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the file was last accessed.
    """

    accessor: typing.Optional[User] = pydantic.Field(default=None)
    """
    The name of the user who last accessed the object.
    """

    attributes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The bitmask value that represents the file attributes.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the company that published the file. For example: <code>Microsoft Corporation</code>.
    """

    confidentiality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file content confidentiality, normalized to the confidentiality_id value. In the case of 'Other', it is defined by the event source.
    """

    confidentiality_id: typing.Optional[FileConfidentialityId] = pydantic.Field(default=None)
    """
    The normalized identifier of the file content confidentiality indicator.
    """

    created_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the file was created.
    """

    created_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the file was created.
    """

    creator: typing.Optional[User] = pydantic.Field(default=None)
    """
    The user that created the file.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the file, as returned by file system. For example: the description as returned by the Unix file command or the Windows file type.
    """

    ext: typing.Optional[str] = pydantic.Field(default=None)
    """
    The extension of the file, excluding the leading dot. For example: <code>exe</code> from <code>svchost.exe</code>, or <code>gz</code> from <code>export.tar.gz</code>.
    """

    hashes: typing.Optional[typing.List[Fingerprint]] = pydantic.Field(default=None)
    """
    An array of hash attributes.
    """

    is_system: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The indication of whether the object is part of the operating system.
    """

    mime_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Multipurpose Internet Mail Extensions (MIME) type of the file, if applicable.
    """

    modified_time: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The time when the file was last modified.
    """

    modified_time_dt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the file was last modified.
    """

    modifier: typing.Optional[User] = pydantic.Field(default=None)
    """
    The user that last modified the file.
    """

    name: FileName = pydantic.Field()
    """
    The name of the file. For example: <code>svchost.exe</code>
    """

    owner: typing.Optional[User] = pydantic.Field(default=None)
    """
    The user that owns the file/object.
    """

    parent_folder: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parent folder in which the file resides. For example: <code>c:\windows\system32</code>
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full path to the file. For example: <code>c:\windows\system32\svchost.exe</code>.
    """

    product: typing.Optional[Product] = pydantic.Field(default=None)
    """
    The product that created or installed the file.
    """

    security_descriptor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The object security descriptor.
    """

    signature: typing.Optional[DigitalSignature] = pydantic.Field(default=None)
    """
    The digital signature of the file.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of data, in bytes.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file type.
    """

    type_id: FileTypeId = pydantic.Field()
    """
    The file type ID.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the file as defined by the storage system, such the file system file ID.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file version. For example: <code>8.0.7601.17514</code>.
    """

    xattributes: typing.Optional[Object] = pydantic.Field(default=None)
    """
    An unordered collection of zero or more name/value pairs where each pair represents a file or folder extended attribute.</p>For example: Windows alternate data stream attributes (ADS stream name, ADS size, etc.), user-defined or application-defined attributes, ACL, owner, primary group, etc. Examples from DCS: </p><ul><li><strong>ads_name</strong></li><li><strong>ads_size</strong></li><li><strong>dacl</strong></li><li><strong>owner</strong></li><li><strong>primary_group</strong></li><li><strong>link_name</strong> - name of the link associated to the file.</li><li><strong>hard_link_count</strong> - the number of links that are associated to the file.</li></ul>
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
