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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class Partner(BaseModel):
    """
    Partner
    """ # noqa: E501
    partner_id: Optional[StrictInt] = Field(default=None, alias="PartnerID")
    identity_id: Optional[StrictInt] = Field(default=None, alias="IdentityID")
    organization_name: Optional[StrictStr] = Field(default=None, alias="OrganizationName")
    contact_name: Optional[StrictStr] = Field(default=None, alias="ContactName")
    phone_number: Optional[StrictStr] = Field(default=None, alias="PhoneNumber")
    email_address: Optional[StrictStr] = Field(default=None, alias="EmailAddress")
    api_key: Optional[StrictStr] = Field(default=None, alias="APIKey")
    url: Optional[StrictStr] = Field(default=None, alias="URL")
    is_active: Optional[StrictBool] = Field(default=None, alias="IsActive")
    is_public: Optional[StrictBool] = Field(default=None, alias="IsPublic")
    last_connect_date: Optional[datetime] = Field(default=None, alias="LastConnectDate")
    eula_date: Optional[datetime] = Field(default=None, alias="EulaDate")
    modification_date: Optional[datetime] = Field(default=None, alias="ModificationDate")
    success: Optional[StrictBool] = Field(default=None, alias="Success")
    failure_message: Optional[StrictStr] = Field(default=None, alias="FailureMessage")
    __properties: ClassVar[List[str]] = ["PartnerID", "IdentityID", "OrganizationName", "ContactName", "PhoneNumber", "EmailAddress", "APIKey", "URL", "IsActive", "IsPublic", "LastConnectDate", "EulaDate", "ModificationDate", "Success", "FailureMessage"]

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
        """Create an instance of Partner from a JSON string"""
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
        # set to None if partner_id (nullable) is None
        # and model_fields_set contains the field
        if self.partner_id is None and "partner_id" in self.model_fields_set:
            _dict['PartnerID'] = None

        # set to None if identity_id (nullable) is None
        # and model_fields_set contains the field
        if self.identity_id is None and "identity_id" in self.model_fields_set:
            _dict['IdentityID'] = None

        # set to None if organization_name (nullable) is None
        # and model_fields_set contains the field
        if self.organization_name is None and "organization_name" in self.model_fields_set:
            _dict['OrganizationName'] = None

        # set to None if contact_name (nullable) is None
        # and model_fields_set contains the field
        if self.contact_name is None and "contact_name" in self.model_fields_set:
            _dict['ContactName'] = None

        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['PhoneNumber'] = None

        # set to None if email_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_address is None and "email_address" in self.model_fields_set:
            _dict['EmailAddress'] = None

        # set to None if api_key (nullable) is None
        # and model_fields_set contains the field
        if self.api_key is None and "api_key" in self.model_fields_set:
            _dict['APIKey'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['URL'] = None

        # set to None if last_connect_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_connect_date is None and "last_connect_date" in self.model_fields_set:
            _dict['LastConnectDate'] = None

        # set to None if eula_date (nullable) is None
        # and model_fields_set contains the field
        if self.eula_date is None and "eula_date" in self.model_fields_set:
            _dict['EulaDate'] = None

        # set to None if modification_date (nullable) is None
        # and model_fields_set contains the field
        if self.modification_date is None and "modification_date" in self.model_fields_set:
            _dict['ModificationDate'] = None

        # set to None if success (nullable) is None
        # and model_fields_set contains the field
        if self.success is None and "success" in self.model_fields_set:
            _dict['Success'] = None

        # set to None if failure_message (nullable) is None
        # and model_fields_set contains the field
        if self.failure_message is None and "failure_message" in self.model_fields_set:
            _dict['FailureMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Partner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PartnerID": obj.get("PartnerID"),
            "IdentityID": obj.get("IdentityID"),
            "OrganizationName": obj.get("OrganizationName"),
            "ContactName": obj.get("ContactName"),
            "PhoneNumber": obj.get("PhoneNumber"),
            "EmailAddress": obj.get("EmailAddress"),
            "APIKey": obj.get("APIKey"),
            "URL": obj.get("URL"),
            "IsActive": obj.get("IsActive"),
            "IsPublic": obj.get("IsPublic"),
            "LastConnectDate": obj.get("LastConnectDate"),
            "EulaDate": obj.get("EulaDate"),
            "ModificationDate": obj.get("ModificationDate"),
            "Success": obj.get("Success"),
            "FailureMessage": obj.get("FailureMessage")
        })
        return _obj


