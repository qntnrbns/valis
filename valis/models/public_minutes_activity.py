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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from valis.models.public_activity_reference import PublicActivityReference
from typing import Optional, Set
from typing_extensions import Self

class PublicMinutesActivity(BaseModel):
    """
    Public Minutes Activity, child of MinutesEntry
    """ # noqa: E501
    minutes_entry_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Minutes Entry", alias="MinutesEntryID")
    description: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = Field(default=None, description="Activity description", alias="Description")
    sequence: Optional[StrictInt] = Field(default=None, description="Sequence", alias="Sequence")
    calendar_action_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Calendar Action", alias="CalendarActionID")
    action_description: Optional[StrictStr] = Field(default=None, description="Action description", alias="ActionDescription")
    committee_complete: Optional[StrictBool] = Field(default=None, description="Committee Complete indicates when Committee Actions are completed", alias="CommitteeComplete")
    vote_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Vote", alias="VoteID")
    deletion_date: Optional[StrictStr] = Field(default=None, description="Deletion Date", alias="DeletionDate")
    is_public: Optional[StrictBool] = Field(default=None, description="Is public", alias="IsPublic")
    is_passed: Optional[StrictBool] = Field(default=None, description="Is passed", alias="IsPassed")
    in_preview: Optional[StrictBool] = Field(default=None, description="In Preview", alias="InPreview")
    minutes_activity_id: Optional[StrictInt] = Field(default=None, description="unique identifier for Minutes Activity", alias="MinutesActivityID")
    activity_references: Optional[List[PublicActivityReference]] = Field(default=None, description="Collection of associated activity references", alias="ActivityReferences")
    __properties: ClassVar[List[str]] = ["MinutesEntryID", "Description", "Sequence", "CalendarActionID", "ActionDescription", "CommitteeComplete", "VoteID", "DeletionDate", "IsPublic", "IsPassed", "InPreview", "MinutesActivityID", "ActivityReferences"]

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
        """Create an instance of PublicMinutesActivity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in activity_references (list)
        _items = []
        if self.activity_references:
            for _item_activity_references in self.activity_references:
                if _item_activity_references:
                    _items.append(_item_activity_references.to_dict())
            _dict['ActivityReferences'] = _items
        # set to None if minutes_entry_id (nullable) is None
        # and model_fields_set contains the field
        if self.minutes_entry_id is None and "minutes_entry_id" in self.model_fields_set:
            _dict['MinutesEntryID'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if sequence (nullable) is None
        # and model_fields_set contains the field
        if self.sequence is None and "sequence" in self.model_fields_set:
            _dict['Sequence'] = None

        # set to None if calendar_action_id (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_action_id is None and "calendar_action_id" in self.model_fields_set:
            _dict['CalendarActionID'] = None

        # set to None if action_description (nullable) is None
        # and model_fields_set contains the field
        if self.action_description is None and "action_description" in self.model_fields_set:
            _dict['ActionDescription'] = None

        # set to None if committee_complete (nullable) is None
        # and model_fields_set contains the field
        if self.committee_complete is None and "committee_complete" in self.model_fields_set:
            _dict['CommitteeComplete'] = None

        # set to None if vote_id (nullable) is None
        # and model_fields_set contains the field
        if self.vote_id is None and "vote_id" in self.model_fields_set:
            _dict['VoteID'] = None

        # set to None if deletion_date (nullable) is None
        # and model_fields_set contains the field
        if self.deletion_date is None and "deletion_date" in self.model_fields_set:
            _dict['DeletionDate'] = None

        # set to None if is_passed (nullable) is None
        # and model_fields_set contains the field
        if self.is_passed is None and "is_passed" in self.model_fields_set:
            _dict['IsPassed'] = None

        # set to None if activity_references (nullable) is None
        # and model_fields_set contains the field
        if self.activity_references is None and "activity_references" in self.model_fields_set:
            _dict['ActivityReferences'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicMinutesActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MinutesEntryID": obj.get("MinutesEntryID"),
            "Description": obj.get("Description"),
            "Sequence": obj.get("Sequence"),
            "CalendarActionID": obj.get("CalendarActionID"),
            "ActionDescription": obj.get("ActionDescription"),
            "CommitteeComplete": obj.get("CommitteeComplete"),
            "VoteID": obj.get("VoteID"),
            "DeletionDate": obj.get("DeletionDate"),
            "IsPublic": obj.get("IsPublic"),
            "IsPassed": obj.get("IsPassed"),
            "InPreview": obj.get("InPreview"),
            "MinutesActivityID": obj.get("MinutesActivityID"),
            "ActivityReferences": [PublicActivityReference.from_dict(_item) for _item in obj["ActivityReferences"]] if obj.get("ActivityReferences") is not None else None
        })
        return _obj


