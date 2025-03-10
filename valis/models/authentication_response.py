# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from valis.models.group_roles_response import GroupRolesResponse
from typing import Optional, Set
from typing_extensions import Self

class AuthenticationResponse(BaseModel):
    """
    AuthenticationResponse
    """ # noqa: E501
    email_address: Optional[StrictStr] = Field(default=None, description="Email Address (\"UserPrincipalName\")", alias="EmailAddress")
    last_name: Optional[StrictStr] = Field(default=None, description="First Name (\"GivenName\")", alias="LastName")
    first_name: Optional[StrictStr] = Field(default=None, description="Last Name (\"Surname\")", alias="FirstName")
    unique_id: Optional[StrictStr] = Field(default=None, description="Active Directory unique identifier (\"Id\")", alias="UniqueID")
    groups: Optional[StrictStr] = Field(default=None, description="list of groups the user is part of", alias="Groups")
    access_token: Optional[StrictStr] = Field(default=None, description="JWT access token created by LIS to contain the the user group claims", alias="AccessToken")
    graph_token: Optional[StrictStr] = Field(default=None, description="JWT access token issued by Graph API when successfully logged in", alias="GraphToken")
    refresh_token: Optional[StrictStr] = Field(default=None, description="JWT refresh token which can be used to obtain new access tokens", alias="RefreshToken")
    access_token_lifetime: Optional[StrictInt] = Field(default=None, description="Access Token Lifetime in seconds - returned when successfully logged in", alias="AccessTokenLifetime")
    claims: Optional[GroupRolesResponse] = Field(default=None, alias="Claims")
    success: Optional[StrictBool] = Field(default=None, description="is this response valid? (true=success, false=unsuccessful)", alias="Success")
    failure_message: Optional[StrictStr] = Field(default=None, description="message describing why this response was not successful", alias="FailureMessage")
    cache_key_name: Optional[StrictStr] = Field(default=None, description="Cache Key Name for GetResponses", alias="CacheKeyName")
    is_password_temporary_or_expired: Optional[StrictBool] = Field(default=None, description="Boolean flags password if it's temporary or expired", alias="IsPasswordTemporaryOrExpired")
    __properties: ClassVar[List[str]] = ["EmailAddress", "LastName", "FirstName", "UniqueID", "Groups", "AccessToken", "GraphToken", "RefreshToken", "AccessTokenLifetime", "Claims", "Success", "FailureMessage", "CacheKeyName", "IsPasswordTemporaryOrExpired"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AuthenticationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of claims
        if self.claims:
            _dict['Claims'] = self.claims.to_dict()
        # set to None if email_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_address is None and "email_address" in self.model_fields_set:
            _dict['EmailAddress'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['LastName'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['FirstName'] = None

        # set to None if unique_id (nullable) is None
        # and model_fields_set contains the field
        if self.unique_id is None and "unique_id" in self.model_fields_set:
            _dict['UniqueID'] = None

        # set to None if groups (nullable) is None
        # and model_fields_set contains the field
        if self.groups is None and "groups" in self.model_fields_set:
            _dict['Groups'] = None

        # set to None if access_token (nullable) is None
        # and model_fields_set contains the field
        if self.access_token is None and "access_token" in self.model_fields_set:
            _dict['AccessToken'] = None

        # set to None if graph_token (nullable) is None
        # and model_fields_set contains the field
        if self.graph_token is None and "graph_token" in self.model_fields_set:
            _dict['GraphToken'] = None

        # set to None if refresh_token (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_token is None and "refresh_token" in self.model_fields_set:
            _dict['RefreshToken'] = None

        # set to None if failure_message (nullable) is None
        # and model_fields_set contains the field
        if self.failure_message is None and "failure_message" in self.model_fields_set:
            _dict['FailureMessage'] = None

        # set to None if cache_key_name (nullable) is None
        # and model_fields_set contains the field
        if self.cache_key_name is None and "cache_key_name" in self.model_fields_set:
            _dict['CacheKeyName'] = None

        # set to None if is_password_temporary_or_expired (nullable) is None
        # and model_fields_set contains the field
        if self.is_password_temporary_or_expired is None and "is_password_temporary_or_expired" in self.model_fields_set:
            _dict['IsPasswordTemporaryOrExpired'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "EmailAddress": obj.get("EmailAddress"),
            "LastName": obj.get("LastName"),
            "FirstName": obj.get("FirstName"),
            "UniqueID": obj.get("UniqueID"),
            "Groups": obj.get("Groups"),
            "AccessToken": obj.get("AccessToken"),
            "GraphToken": obj.get("GraphToken"),
            "RefreshToken": obj.get("RefreshToken"),
            "AccessTokenLifetime": obj.get("AccessTokenLifetime"),
            "Claims": GroupRolesResponse.from_dict(obj["Claims"]) if obj.get("Claims") is not None else None,
            "Success": obj.get("Success"),
            "FailureMessage": obj.get("FailureMessage"),
            "CacheKeyName": obj.get("CacheKeyName"),
            "IsPasswordTemporaryOrExpired": obj.get("IsPasswordTemporaryOrExpired")
        })
        return _obj


