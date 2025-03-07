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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PublicPersonnelResponse(BaseModel):
    """
    Information for Public Personnel
    """ # noqa: E501
    staff_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Staff", alias="StaffID")
    affiliation_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Committee", alias="AffiliationID")
    staff_role_type_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Staff Role Type", alias="StaffRoleTypeID")
    identity_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Identity (associated person)", alias="IdentityID")
    organization_name: Optional[StrictStr] = Field(default=None, description="Organization Name", alias="OrganizationName")
    full_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Person's name", alias="FullName")
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=15)]] = Field(default=None, description="Person's phone number", alias="PhoneNumber")
    email_address: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Email address", alias="EmailAddress")
    sequence: Optional[StrictInt] = Field(default=None, description="Sequence", alias="Sequence")
    is_public: Optional[StrictBool] = Field(default=None, description="is this public?", alias="IsPublic")
    effective_begin_date: Optional[datetime] = Field(default=None, description="Effective begin date for this assignment", alias="EffectiveBeginDate")
    effective_end_date: Optional[datetime] = Field(default=None, description="Effective End date for this assignment", alias="EffectiveEndDate")
    __properties: ClassVar[List[str]] = ["StaffID", "AffiliationID", "StaffRoleTypeID", "IdentityID", "OrganizationName", "FullName", "PhoneNumber", "EmailAddress", "Sequence", "IsPublic", "EffectiveBeginDate", "EffectiveEndDate"]

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
        """Create an instance of PublicPersonnelResponse from a JSON string"""
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
        # set to None if staff_id (nullable) is None
        # and model_fields_set contains the field
        if self.staff_id is None and "staff_id" in self.model_fields_set:
            _dict['StaffID'] = None

        # set to None if affiliation_id (nullable) is None
        # and model_fields_set contains the field
        if self.affiliation_id is None and "affiliation_id" in self.model_fields_set:
            _dict['AffiliationID'] = None

        # set to None if staff_role_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.staff_role_type_id is None and "staff_role_type_id" in self.model_fields_set:
            _dict['StaffRoleTypeID'] = None

        # set to None if organization_name (nullable) is None
        # and model_fields_set contains the field
        if self.organization_name is None and "organization_name" in self.model_fields_set:
            _dict['OrganizationName'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['FullName'] = None

        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['PhoneNumber'] = None

        # set to None if email_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_address is None and "email_address" in self.model_fields_set:
            _dict['EmailAddress'] = None

        # set to None if is_public (nullable) is None
        # and model_fields_set contains the field
        if self.is_public is None and "is_public" in self.model_fields_set:
            _dict['IsPublic'] = None

        # set to None if effective_begin_date (nullable) is None
        # and model_fields_set contains the field
        if self.effective_begin_date is None and "effective_begin_date" in self.model_fields_set:
            _dict['EffectiveBeginDate'] = None

        # set to None if effective_end_date (nullable) is None
        # and model_fields_set contains the field
        if self.effective_end_date is None and "effective_end_date" in self.model_fields_set:
            _dict['EffectiveEndDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicPersonnelResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "StaffID": obj.get("StaffID"),
            "AffiliationID": obj.get("AffiliationID"),
            "StaffRoleTypeID": obj.get("StaffRoleTypeID"),
            "IdentityID": obj.get("IdentityID"),
            "OrganizationName": obj.get("OrganizationName"),
            "FullName": obj.get("FullName"),
            "PhoneNumber": obj.get("PhoneNumber"),
            "EmailAddress": obj.get("EmailAddress"),
            "Sequence": obj.get("Sequence"),
            "IsPublic": obj.get("IsPublic"),
            "EffectiveBeginDate": obj.get("EffectiveBeginDate"),
            "EffectiveEndDate": obj.get("EffectiveEndDate")
        })
        return _obj


