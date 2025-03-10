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
from valis.models.contact_response import ContactResponse
from typing import Optional, Set
from typing_extensions import Self

class MemberContactInformationSearchResponse(BaseModel):
    """
    Information for a Member Contact
    """ # noqa: E501
    member_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for this Member", alias="MemberID")
    identity_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Identity", alias="IdentityID")
    member_number: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Member number (e.g. H289)", alias="MemberNumber")
    full_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Member Full Name", alias="FullName")
    first_name: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member First Name", alias="FirstName")
    middle_name: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member Middle Name", alias="MiddleName")
    last_name: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member Last Name", alias="LastName")
    member_display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Member Display Name", alias="MemberDisplayName")
    room_number: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Member Room number", alias="RoomNumber")
    is_public: Optional[StrictBool] = Field(default=None, description="Is this Member public ?", alias="IsPublic")
    gab_phone_number: Optional[StrictStr] = Field(default=None, description="General Assembly Phone #", alias="GABPhoneNumber")
    gab_email_address: Optional[StrictStr] = Field(default=None, description="General Assembly Email Address", alias="GABEmailAddress")
    chamber_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="Chamber code (H/S)", alias="ChamberCode")
    chamber: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Chamber name", alias="Chamber")
    party_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="Political party (R/D/I)", alias="PartyCode")
    party_name: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Political party name", alias="PartyName")
    district_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for District", alias="DistrictID")
    district_name: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="District name (e.g. 17th)", alias="DistrictName")
    member_status_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Member Status", alias="MemberStatusID")
    member_status: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member Status name", alias="MemberStatus")
    service_begin_date: Optional[datetime] = Field(default=None, description="Begin date of Service", alias="ServiceBeginDate")
    service_end_date: Optional[datetime] = Field(default=None, description="End date of Service (removal date)", alias="ServiceEndDate")
    service_end_reason: Optional[StrictStr] = Field(default=None, description="Member Service End Reason", alias="ServiceEndReason")
    contact_information: Optional[List[ContactResponse]] = Field(default=None, description="List of Contact Information", alias="ContactInformation")
    __properties: ClassVar[List[str]] = ["MemberID", "IdentityID", "MemberNumber", "FullName", "FirstName", "MiddleName", "LastName", "MemberDisplayName", "RoomNumber", "IsPublic", "GABPhoneNumber", "GABEmailAddress", "ChamberCode", "Chamber", "PartyCode", "PartyName", "DistrictID", "DistrictName", "MemberStatusID", "MemberStatus", "ServiceBeginDate", "ServiceEndDate", "ServiceEndReason", "ContactInformation"]

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
        """Create an instance of MemberContactInformationSearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contact_information (list)
        _items = []
        if self.contact_information:
            for _item_contact_information in self.contact_information:
                if _item_contact_information:
                    _items.append(_item_contact_information.to_dict())
            _dict['ContactInformation'] = _items
        # set to None if member_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_id is None and "member_id" in self.model_fields_set:
            _dict['MemberID'] = None

        # set to None if member_number (nullable) is None
        # and model_fields_set contains the field
        if self.member_number is None and "member_number" in self.model_fields_set:
            _dict['MemberNumber'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['FullName'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['FirstName'] = None

        # set to None if middle_name (nullable) is None
        # and model_fields_set contains the field
        if self.middle_name is None and "middle_name" in self.model_fields_set:
            _dict['MiddleName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['LastName'] = None

        # set to None if member_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.member_display_name is None and "member_display_name" in self.model_fields_set:
            _dict['MemberDisplayName'] = None

        # set to None if room_number (nullable) is None
        # and model_fields_set contains the field
        if self.room_number is None and "room_number" in self.model_fields_set:
            _dict['RoomNumber'] = None

        # set to None if gab_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.gab_phone_number is None and "gab_phone_number" in self.model_fields_set:
            _dict['GABPhoneNumber'] = None

        # set to None if gab_email_address (nullable) is None
        # and model_fields_set contains the field
        if self.gab_email_address is None and "gab_email_address" in self.model_fields_set:
            _dict['GABEmailAddress'] = None

        # set to None if chamber_code (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_code is None and "chamber_code" in self.model_fields_set:
            _dict['ChamberCode'] = None

        # set to None if chamber (nullable) is None
        # and model_fields_set contains the field
        if self.chamber is None and "chamber" in self.model_fields_set:
            _dict['Chamber'] = None

        # set to None if party_code (nullable) is None
        # and model_fields_set contains the field
        if self.party_code is None and "party_code" in self.model_fields_set:
            _dict['PartyCode'] = None

        # set to None if party_name (nullable) is None
        # and model_fields_set contains the field
        if self.party_name is None and "party_name" in self.model_fields_set:
            _dict['PartyName'] = None

        # set to None if district_name (nullable) is None
        # and model_fields_set contains the field
        if self.district_name is None and "district_name" in self.model_fields_set:
            _dict['DistrictName'] = None

        # set to None if member_status (nullable) is None
        # and model_fields_set contains the field
        if self.member_status is None and "member_status" in self.model_fields_set:
            _dict['MemberStatus'] = None

        # set to None if service_begin_date (nullable) is None
        # and model_fields_set contains the field
        if self.service_begin_date is None and "service_begin_date" in self.model_fields_set:
            _dict['ServiceBeginDate'] = None

        # set to None if service_end_date (nullable) is None
        # and model_fields_set contains the field
        if self.service_end_date is None and "service_end_date" in self.model_fields_set:
            _dict['ServiceEndDate'] = None

        # set to None if service_end_reason (nullable) is None
        # and model_fields_set contains the field
        if self.service_end_reason is None and "service_end_reason" in self.model_fields_set:
            _dict['ServiceEndReason'] = None

        # set to None if contact_information (nullable) is None
        # and model_fields_set contains the field
        if self.contact_information is None and "contact_information" in self.model_fields_set:
            _dict['ContactInformation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberContactInformationSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MemberID": obj.get("MemberID"),
            "IdentityID": obj.get("IdentityID"),
            "MemberNumber": obj.get("MemberNumber"),
            "FullName": obj.get("FullName"),
            "FirstName": obj.get("FirstName"),
            "MiddleName": obj.get("MiddleName"),
            "LastName": obj.get("LastName"),
            "MemberDisplayName": obj.get("MemberDisplayName"),
            "RoomNumber": obj.get("RoomNumber"),
            "IsPublic": obj.get("IsPublic"),
            "GABPhoneNumber": obj.get("GABPhoneNumber"),
            "GABEmailAddress": obj.get("GABEmailAddress"),
            "ChamberCode": obj.get("ChamberCode"),
            "Chamber": obj.get("Chamber"),
            "PartyCode": obj.get("PartyCode"),
            "PartyName": obj.get("PartyName"),
            "DistrictID": obj.get("DistrictID"),
            "DistrictName": obj.get("DistrictName"),
            "MemberStatusID": obj.get("MemberStatusID"),
            "MemberStatus": obj.get("MemberStatus"),
            "ServiceBeginDate": obj.get("ServiceBeginDate"),
            "ServiceEndDate": obj.get("ServiceEndDate"),
            "ServiceEndReason": obj.get("ServiceEndReason"),
            "ContactInformation": [ContactResponse.from_dict(_item) for _item in obj["ContactInformation"]] if obj.get("ContactInformation") is not None else None
        })
        return _obj


