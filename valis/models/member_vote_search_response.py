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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from valis.models.vote_result_response import VoteResultResponse
from typing import Optional, Set
from typing_extensions import Self

class MemberVoteSearchResponse(BaseModel):
    """
    Information for a Member Vote
    """ # noqa: E501
    member_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for this Member", alias="MemberID")
    member_number: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Member number (e.g. H289)", alias="MemberNumber")
    member_display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Member Display Name", alias="MemberDisplayName")
    patron_display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Patron Display Name", alias="PatronDisplayName")
    vote_result: Optional[List[VoteResultResponse]] = Field(default=None, description="list of Vote Results", alias="VoteResult")
    __properties: ClassVar[List[str]] = ["MemberID", "MemberNumber", "MemberDisplayName", "PatronDisplayName", "VoteResult"]

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
        """Create an instance of MemberVoteSearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vote_result (list)
        _items = []
        if self.vote_result:
            for _item_vote_result in self.vote_result:
                if _item_vote_result:
                    _items.append(_item_vote_result.to_dict())
            _dict['VoteResult'] = _items
        # set to None if member_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_id is None and "member_id" in self.model_fields_set:
            _dict['MemberID'] = None

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

        # set to None if vote_result (nullable) is None
        # and model_fields_set contains the field
        if self.vote_result is None and "vote_result" in self.model_fields_set:
            _dict['VoteResult'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberVoteSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MemberID": obj.get("MemberID"),
            "MemberNumber": obj.get("MemberNumber"),
            "MemberDisplayName": obj.get("MemberDisplayName"),
            "PatronDisplayName": obj.get("PatronDisplayName"),
            "VoteResult": [VoteResultResponse.from_dict(_item) for _item in obj["VoteResult"]] if obj.get("VoteResult") is not None else None
        })
        return _obj


