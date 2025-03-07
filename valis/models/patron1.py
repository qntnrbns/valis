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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Patron1(BaseModel):
    """
    Information for Patron
    """ # noqa: E501
    legislation_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Legislation", alias="LegislationID")
    legislation_text_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Legislation Text", alias="LegislationTextID")
    chamber_code: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Chamber Code", alias="ChamberCode")
    member_id: Optional[StrictInt] = Field(default=None, description="Databse Unique Identifier for Member", alias="MemberID")
    member_number: Optional[StrictStr] = Field(default=None, description="Member Number", alias="MemberNumber")
    patron_type_id: Optional[StrictInt] = Field(default=None, description="Databse Unique Identifier for Patron Type ID", alias="PatronTypeID")
    name: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="Role Name", alias="Name")
    display_name: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="Role Display Name", alias="DisplayName")
    member_display_name: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="Member Display Name", alias="MemberDisplayName")
    patron_display_name: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="Patron Display Name", alias="PatronDisplayName")
    by_request: Optional[StrictBool] = Field(default=None, description="Is this patronage by request of a state agency/entity?", alias="ByRequest")
    __properties: ClassVar[List[str]] = ["LegislationID", "LegislationTextID", "ChamberCode", "MemberID", "MemberNumber", "PatronTypeID", "Name", "DisplayName", "MemberDisplayName", "PatronDisplayName", "ByRequest"]

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
        """Create an instance of Patron1 from a JSON string"""
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
        # set to None if legislation_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_id is None and "legislation_id" in self.model_fields_set:
            _dict['LegislationID'] = None

        # set to None if legislation_text_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_text_id is None and "legislation_text_id" in self.model_fields_set:
            _dict['LegislationTextID'] = None

        # set to None if chamber_code (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_code is None and "chamber_code" in self.model_fields_set:
            _dict['ChamberCode'] = None

        # set to None if member_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_id is None and "member_id" in self.model_fields_set:
            _dict['MemberID'] = None

        # set to None if member_number (nullable) is None
        # and model_fields_set contains the field
        if self.member_number is None and "member_number" in self.model_fields_set:
            _dict['MemberNumber'] = None

        # set to None if patron_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.patron_type_id is None and "patron_type_id" in self.model_fields_set:
            _dict['PatronTypeID'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['Name'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['DisplayName'] = None

        # set to None if member_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.member_display_name is None and "member_display_name" in self.model_fields_set:
            _dict['MemberDisplayName'] = None

        # set to None if patron_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.patron_display_name is None and "patron_display_name" in self.model_fields_set:
            _dict['PatronDisplayName'] = None

        # set to None if by_request (nullable) is None
        # and model_fields_set contains the field
        if self.by_request is None and "by_request" in self.model_fields_set:
            _dict['ByRequest'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Patron1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LegislationID": obj.get("LegislationID"),
            "LegislationTextID": obj.get("LegislationTextID"),
            "ChamberCode": obj.get("ChamberCode"),
            "MemberID": obj.get("MemberID"),
            "MemberNumber": obj.get("MemberNumber"),
            "PatronTypeID": obj.get("PatronTypeID"),
            "Name": obj.get("Name"),
            "DisplayName": obj.get("DisplayName"),
            "MemberDisplayName": obj.get("MemberDisplayName"),
            "PatronDisplayName": obj.get("PatronDisplayName"),
            "ByRequest": obj.get("ByRequest")
        })
        return _obj


