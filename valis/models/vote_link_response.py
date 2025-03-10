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

class VoteLinkResponse(BaseModel):
    """
    Information for a Vote Link
    """ # noqa: E501
    vote_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Vote", alias="VoteID")
    chamber_code: Annotated[str, Field(min_length=1, strict=True, max_length=1)] = Field(description="Chamber code (H/S)", alias="ChamberCode")
    committee_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Committee", alias="CommitteeID")
    parent_committee_id: Optional[StrictInt] = Field(default=None, description="unique identifier for parent Committee", alias="ParentCommitteeID")
    vote_file_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Vote File", alias="VoteFileID")
    reference_type: Optional[StrictStr] = Field(default=None, description="Reference type", alias="ReferenceType")
    reference_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Reference", alias="ReferenceID")
    session_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Session", alias="SessionID")
    session_code: Optional[StrictStr] = Field(default=None, description="Session code (e.g. 20181)", alias="SessionCode")
    is_public: Optional[StrictBool] = Field(default=None, description="Is Public?", alias="IsPublic")
    file_url: Optional[StrictStr] = Field(default=None, description="File URL", alias="FileURL")
    __properties: ClassVar[List[str]] = ["VoteID", "ChamberCode", "CommitteeID", "ParentCommitteeID", "VoteFileID", "ReferenceType", "ReferenceID", "SessionID", "SessionCode", "IsPublic", "FileURL"]

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
        """Create an instance of VoteLinkResponse from a JSON string"""
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
        # set to None if vote_id (nullable) is None
        # and model_fields_set contains the field
        if self.vote_id is None and "vote_id" in self.model_fields_set:
            _dict['VoteID'] = None

        # set to None if committee_id (nullable) is None
        # and model_fields_set contains the field
        if self.committee_id is None and "committee_id" in self.model_fields_set:
            _dict['CommitteeID'] = None

        # set to None if parent_committee_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_committee_id is None and "parent_committee_id" in self.model_fields_set:
            _dict['ParentCommitteeID'] = None

        # set to None if vote_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.vote_file_id is None and "vote_file_id" in self.model_fields_set:
            _dict['VoteFileID'] = None

        # set to None if reference_type (nullable) is None
        # and model_fields_set contains the field
        if self.reference_type is None and "reference_type" in self.model_fields_set:
            _dict['ReferenceType'] = None

        # set to None if reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.reference_id is None and "reference_id" in self.model_fields_set:
            _dict['ReferenceID'] = None

        # set to None if session_id (nullable) is None
        # and model_fields_set contains the field
        if self.session_id is None and "session_id" in self.model_fields_set:
            _dict['SessionID'] = None

        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['SessionCode'] = None

        # set to None if file_url (nullable) is None
        # and model_fields_set contains the field
        if self.file_url is None and "file_url" in self.model_fields_set:
            _dict['FileURL'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VoteLinkResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "VoteID": obj.get("VoteID"),
            "ChamberCode": obj.get("ChamberCode"),
            "CommitteeID": obj.get("CommitteeID"),
            "ParentCommitteeID": obj.get("ParentCommitteeID"),
            "VoteFileID": obj.get("VoteFileID"),
            "ReferenceType": obj.get("ReferenceType"),
            "ReferenceID": obj.get("ReferenceID"),
            "SessionID": obj.get("SessionID"),
            "SessionCode": obj.get("SessionCode"),
            "IsPublic": obj.get("IsPublic"),
            "FileURL": obj.get("FileURL")
        })
        return _obj


