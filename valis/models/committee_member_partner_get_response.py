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

class CommitteeMemberPartnerGetResponse(BaseModel):
    """
    Partner Get for Committee Member
    """ # noqa: E501
    committee_member_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Committee Member Relationship", alias="CommitteeMemberID")
    committee_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Committee", alias="CommitteeID")
    committee_number: Optional[StrictStr] = Field(default=None, description="Committee Number", alias="CommitteeNumber")
    member_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Member", alias="MemberID")
    member_number: Optional[StrictStr] = Field(default=None, description="Member Number", alias="MemberNumber")
    member_display_name: Optional[StrictStr] = Field(default=None, description="Member Display Name", alias="MemberDisplayName")
    patron_display_name: Optional[StrictStr] = Field(default=None, description="Patron Display Name", alias="PatronDisplayName")
    party_code: Optional[StrictStr] = Field(default=None, description="Party Code", alias="PartyCode")
    voting_sequence: Optional[StrictInt] = Field(default=None, description="Voting Sequence", alias="VotingSequence")
    display_sequence: Optional[StrictInt] = Field(default=None, description="Display Sequence", alias="DisplaySequence")
    committee_role_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Committee Role ID", alias="CommitteeRoleID")
    title: Optional[StrictStr] = Field(default=None, description="Member Title", alias="Title")
    effective_date: Optional[datetime] = Field(default=None, description="Effective Date", alias="EffectiveDate")
    is_public: Optional[StrictBool] = Field(default=None, description="Is Member Public", alias="IsPublic")
    __properties: ClassVar[List[str]] = ["CommitteeMemberID", "CommitteeID", "CommitteeNumber", "MemberID", "MemberNumber", "MemberDisplayName", "PatronDisplayName", "PartyCode", "VotingSequence", "DisplaySequence", "CommitteeRoleID", "Title", "EffectiveDate", "IsPublic"]

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
        """Create an instance of CommitteeMemberPartnerGetResponse from a JSON string"""
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
        # set to None if committee_number (nullable) is None
        # and model_fields_set contains the field
        if self.committee_number is None and "committee_number" in self.model_fields_set:
            _dict['CommitteeNumber'] = None

        # set to None if member_number (nullable) is None
        # and model_fields_set contains the field
        if self.member_number is None and "member_number" in self.model_fields_set:
            _dict['MemberNumber'] = None

        # set to None if member_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.member_display_name is None and "member_display_name" in self.model_fields_set:
            _dict['MemberDisplayName'] = None

        # set to None if patron_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.patron_display_name is None and "patron_display_name" in self.model_fields_set:
            _dict['PatronDisplayName'] = None

        # set to None if party_code (nullable) is None
        # and model_fields_set contains the field
        if self.party_code is None and "party_code" in self.model_fields_set:
            _dict['PartyCode'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['Title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommitteeMemberPartnerGetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CommitteeMemberID": obj.get("CommitteeMemberID"),
            "CommitteeID": obj.get("CommitteeID"),
            "CommitteeNumber": obj.get("CommitteeNumber"),
            "MemberID": obj.get("MemberID"),
            "MemberNumber": obj.get("MemberNumber"),
            "MemberDisplayName": obj.get("MemberDisplayName"),
            "PatronDisplayName": obj.get("PatronDisplayName"),
            "PartyCode": obj.get("PartyCode"),
            "VotingSequence": obj.get("VotingSequence"),
            "DisplaySequence": obj.get("DisplaySequence"),
            "CommitteeRoleID": obj.get("CommitteeRoleID"),
            "Title": obj.get("Title"),
            "EffectiveDate": obj.get("EffectiveDate"),
            "IsPublic": obj.get("IsPublic")
        })
        return _obj


