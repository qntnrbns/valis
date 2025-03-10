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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PublicMemberResponse(BaseModel):
    """
    Public information for a Member
    """ # noqa: E501
    member_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for this Member", alias="MemberID")
    identity_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Identity", alias="IdentityID")
    member_detail_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Member Detail", alias="MemberDetailID")
    session_code: Optional[StrictStr] = Field(default=None, description="Session code (e.g. 20181)", alias="SessionCode")
    member_number: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Member number (e.g. H289)", alias="MemberNumber")
    list_display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Member's Name to be displayed for List purposes", alias="ListDisplayName")
    member_display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Member's Name to be displayed", alias="MemberDisplayName")
    patron_display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Patron Display Name", alias="PatronDisplayName")
    salutation: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member Salutation", alias="Salutation")
    service_begin_date: Optional[datetime] = Field(default=None, description="Begin date of Service for this Member", alias="ServiceBeginDate")
    service_end_date: Optional[datetime] = Field(default=None, description="End date of Service for this Member", alias="ServiceEndDate")
    last_election_date: Optional[datetime] = Field(default=None, description="Last election date for this Member", alias="LastElectionDate")
    room_number: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Member Room number", alias="RoomNumber")
    service_end_reason: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member Service End Reason", alias="ServiceEndReason")
    gab_phone_number: Optional[StrictStr] = Field(default=None, description="General Assembly Phone #", alias="GABPhoneNumber")
    gab_email_address: Optional[StrictStr] = Field(default=None, description="General Assembly Email Address", alias="GABEmailAddress")
    seat_number: Optional[StrictInt] = Field(default=None, description="Member chamber floor seat number", alias="SeatNumber")
    seniority: Optional[StrictInt] = Field(default=None, description="Member seniority ranking", alias="Seniority")
    voting_sequence: Optional[StrictInt] = Field(default=None, description="Member voting order", alias="VotingSequence")
    chamber_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="Chamber code (H/S)", alias="ChamberCode")
    chamber_name: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Chamber Name", alias="ChamberName")
    district_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for District", alias="DistrictID")
    district_name: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="District name", alias="DistrictName")
    party_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="Political party (R/D/I)", alias="PartyCode")
    member_status_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Member Status", alias="MemberStatusID")
    member_status: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Member Status name", alias="MemberStatus")
    status_reason: Optional[StrictStr] = Field(default=None, description="Member status reason", alias="StatusReason")
    is_public: Optional[StrictBool] = Field(default=None, description="Is this Member public ?", alias="IsPublic")
    __properties: ClassVar[List[str]] = ["MemberID", "IdentityID", "MemberDetailID", "SessionCode", "MemberNumber", "ListDisplayName", "MemberDisplayName", "PatronDisplayName", "Salutation", "ServiceBeginDate", "ServiceEndDate", "LastElectionDate", "RoomNumber", "ServiceEndReason", "GABPhoneNumber", "GABEmailAddress", "SeatNumber", "Seniority", "VotingSequence", "ChamberCode", "ChamberName", "DistrictID", "DistrictName", "PartyCode", "MemberStatusID", "MemberStatus", "StatusReason", "IsPublic"]

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
        """Create an instance of PublicMemberResponse from a JSON string"""
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
        # set to None if member_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_id is None and "member_id" in self.model_fields_set:
            _dict['MemberID'] = None

        # set to None if identity_id (nullable) is None
        # and model_fields_set contains the field
        if self.identity_id is None and "identity_id" in self.model_fields_set:
            _dict['IdentityID'] = None

        # set to None if member_detail_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_detail_id is None and "member_detail_id" in self.model_fields_set:
            _dict['MemberDetailID'] = None

        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['SessionCode'] = None

        # set to None if member_number (nullable) is None
        # and model_fields_set contains the field
        if self.member_number is None and "member_number" in self.model_fields_set:
            _dict['MemberNumber'] = None

        # set to None if list_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.list_display_name is None and "list_display_name" in self.model_fields_set:
            _dict['ListDisplayName'] = None

        # set to None if member_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.member_display_name is None and "member_display_name" in self.model_fields_set:
            _dict['MemberDisplayName'] = None

        # set to None if patron_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.patron_display_name is None and "patron_display_name" in self.model_fields_set:
            _dict['PatronDisplayName'] = None

        # set to None if salutation (nullable) is None
        # and model_fields_set contains the field
        if self.salutation is None and "salutation" in self.model_fields_set:
            _dict['Salutation'] = None

        # set to None if service_begin_date (nullable) is None
        # and model_fields_set contains the field
        if self.service_begin_date is None and "service_begin_date" in self.model_fields_set:
            _dict['ServiceBeginDate'] = None

        # set to None if service_end_date (nullable) is None
        # and model_fields_set contains the field
        if self.service_end_date is None and "service_end_date" in self.model_fields_set:
            _dict['ServiceEndDate'] = None

        # set to None if last_election_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_election_date is None and "last_election_date" in self.model_fields_set:
            _dict['LastElectionDate'] = None

        # set to None if room_number (nullable) is None
        # and model_fields_set contains the field
        if self.room_number is None and "room_number" in self.model_fields_set:
            _dict['RoomNumber'] = None

        # set to None if service_end_reason (nullable) is None
        # and model_fields_set contains the field
        if self.service_end_reason is None and "service_end_reason" in self.model_fields_set:
            _dict['ServiceEndReason'] = None

        # set to None if gab_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.gab_phone_number is None and "gab_phone_number" in self.model_fields_set:
            _dict['GABPhoneNumber'] = None

        # set to None if gab_email_address (nullable) is None
        # and model_fields_set contains the field
        if self.gab_email_address is None and "gab_email_address" in self.model_fields_set:
            _dict['GABEmailAddress'] = None

        # set to None if seat_number (nullable) is None
        # and model_fields_set contains the field
        if self.seat_number is None and "seat_number" in self.model_fields_set:
            _dict['SeatNumber'] = None

        # set to None if seniority (nullable) is None
        # and model_fields_set contains the field
        if self.seniority is None and "seniority" in self.model_fields_set:
            _dict['Seniority'] = None

        # set to None if voting_sequence (nullable) is None
        # and model_fields_set contains the field
        if self.voting_sequence is None and "voting_sequence" in self.model_fields_set:
            _dict['VotingSequence'] = None

        # set to None if chamber_code (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_code is None and "chamber_code" in self.model_fields_set:
            _dict['ChamberCode'] = None

        # set to None if chamber_name (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_name is None and "chamber_name" in self.model_fields_set:
            _dict['ChamberName'] = None

        # set to None if district_id (nullable) is None
        # and model_fields_set contains the field
        if self.district_id is None and "district_id" in self.model_fields_set:
            _dict['DistrictID'] = None

        # set to None if district_name (nullable) is None
        # and model_fields_set contains the field
        if self.district_name is None and "district_name" in self.model_fields_set:
            _dict['DistrictName'] = None

        # set to None if party_code (nullable) is None
        # and model_fields_set contains the field
        if self.party_code is None and "party_code" in self.model_fields_set:
            _dict['PartyCode'] = None

        # set to None if member_status_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_status_id is None and "member_status_id" in self.model_fields_set:
            _dict['MemberStatusID'] = None

        # set to None if member_status (nullable) is None
        # and model_fields_set contains the field
        if self.member_status is None and "member_status" in self.model_fields_set:
            _dict['MemberStatus'] = None

        # set to None if status_reason (nullable) is None
        # and model_fields_set contains the field
        if self.status_reason is None and "status_reason" in self.model_fields_set:
            _dict['StatusReason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicMemberResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MemberID": obj.get("MemberID"),
            "IdentityID": obj.get("IdentityID"),
            "MemberDetailID": obj.get("MemberDetailID"),
            "SessionCode": obj.get("SessionCode"),
            "MemberNumber": obj.get("MemberNumber"),
            "ListDisplayName": obj.get("ListDisplayName"),
            "MemberDisplayName": obj.get("MemberDisplayName"),
            "PatronDisplayName": obj.get("PatronDisplayName"),
            "Salutation": obj.get("Salutation"),
            "ServiceBeginDate": obj.get("ServiceBeginDate"),
            "ServiceEndDate": obj.get("ServiceEndDate"),
            "LastElectionDate": obj.get("LastElectionDate"),
            "RoomNumber": obj.get("RoomNumber"),
            "ServiceEndReason": obj.get("ServiceEndReason"),
            "GABPhoneNumber": obj.get("GABPhoneNumber"),
            "GABEmailAddress": obj.get("GABEmailAddress"),
            "SeatNumber": obj.get("SeatNumber"),
            "Seniority": obj.get("Seniority"),
            "VotingSequence": obj.get("VotingSequence"),
            "ChamberCode": obj.get("ChamberCode"),
            "ChamberName": obj.get("ChamberName"),
            "DistrictID": obj.get("DistrictID"),
            "DistrictName": obj.get("DistrictName"),
            "PartyCode": obj.get("PartyCode"),
            "MemberStatusID": obj.get("MemberStatusID"),
            "MemberStatus": obj.get("MemberStatus"),
            "StatusReason": obj.get("StatusReason"),
            "IsPublic": obj.get("IsPublic")
        })
        return _obj


