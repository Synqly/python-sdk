# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class AwsCredential(pydantic.BaseModel):
    """
    AWS access key to authenticate with AWS. Access keys are long-term credentials for an IAM user and consist of an ID and secret. Follow [this guide to generate access and secret keys](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys). You may optionally provide a session token if you are using temporary credentials.
    """

    access_key_id: str = pydantic.Field(description="ID portion of the AWS access key pair.")
    secret_access_key: str = pydantic.Field(description="Secret portion of the AWS access key pair.")
    session: typing.Optional[str] = pydantic.Field(
        description="A temporary session token. Session tokens are optional and are only necessary if you are using temporary credentials."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}