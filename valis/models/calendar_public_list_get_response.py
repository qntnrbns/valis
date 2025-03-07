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
from valis.models.calendar_comment_public_get_response import CalendarCommentPublicGetResponse
from valis.models.calendar_file_base_model import CalendarFileBaseModel
from typing import Optional, Set
from typing_extensions import Self

class CalendarPublicListGetResponse(BaseModel):
    """
    Calendar Response for Public Display
    """ # noqa: E501
    calendar_date: datetime = Field(description="Calendar Date", alias="CalendarDate")
    meeting_time: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Meeting Time", alias="MeetingTime")
    calendar_number: Optional[StrictInt] = Field(default=None, description="Numeric Indicator for Primary and Supplemental", alias="CalendarNumber")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Calendar Description", alias="Description")
    is_public: Optional[StrictBool] = Field(default=None, description="Is Calendar for Public Consumption", alias="IsPublic")
    calendar_type: Annotated[str, Field(strict=True, max_length=25)] = Field(description="Calendar Type", alias="CalendarType")
    calendar_type_id: Optional[StrictInt] = Field(default=None, description="Calendar Type ID", alias="CalendarTypeID")
    chamber_code: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Chamber Code (H=House / S=Senate)", alias="ChamberCode")
    session_id: StrictInt = Field(description="Session ID", alias="SessionID")
    session_code: Optional[StrictStr] = Field(default=None, description="Session Code", alias="SessionCode")
    vote_room_id: Optional[StrictInt] = Field(default=None, description="Vote Room ID", alias="VoteRoomID")
    room_description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Vote Room Description", alias="RoomDescription")
    comments: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = Field(default=None, description="Meeting Notes/Comments", alias="Comments")
    pending_change: Optional[StrictBool] = Field(default=None, description="Pending Change to Calendar", alias="PendingChange")
    reference_number: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Reference Number used for External reference to calendar", alias="ReferenceNumber")
    is_proforma: Optional[StrictBool] = Field(default=None, description="IsProforma to Calendar", alias="IsProforma")
    deletion_date: Optional[datetime] = Field(default=None, description="Calendar Deletion Date", alias="DeletionDate")
    calendar_id: StrictInt = Field(description="Calendar unique identifier", alias="CalendarID")
    calendar_files: Optional[List[CalendarFileBaseModel]] = Field(default=None, description="list of Calendar Files for a specific Calendar", alias="CalendarFiles")
    calendar_comments: Optional[List[CalendarCommentPublicGetResponse]] = Field(default=None, description="Listing of Calendar Comments", alias="CalendarComments")
    __properties: ClassVar[List[str]] = ["CalendarDate", "MeetingTime", "CalendarNumber", "Description", "IsPublic", "CalendarType", "CalendarTypeID", "ChamberCode", "SessionID", "SessionCode", "VoteRoomID", "RoomDescription", "Comments", "PendingChange", "ReferenceNumber", "IsProforma", "DeletionDate", "CalendarID", "CalendarFiles", "CalendarComments"]

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
        """Create an instance of CalendarPublicListGetResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in calendar_files (list)
        _items = []
        if self.calendar_files:
            for _item_calendar_files in self.calendar_files:
                if _item_calendar_files:
                    _items.append(_item_calendar_files.to_dict())
            _dict['CalendarFiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in calendar_comments (list)
        _items = []
        if self.calendar_comments:
            for _item_calendar_comments in self.calendar_comments:
                if _item_calendar_comments:
                    _items.append(_item_calendar_comments.to_dict())
            _dict['CalendarComments'] = _items
        # set to None if meeting_time (nullable) is None
        # and model_fields_set contains the field
        if self.meeting_time is None and "meeting_time" in self.model_fields_set:
            _dict['MeetingTime'] = None

        # set to None if calendar_number (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_number is None and "calendar_number" in self.model_fields_set:
            _dict['CalendarNumber'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if is_public (nullable) is None
        # and model_fields_set contains the field
        if self.is_public is None and "is_public" in self.model_fields_set:
            _dict['IsPublic'] = None

        # set to None if calendar_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_type_id is None and "calendar_type_id" in self.model_fields_set:
            _dict['CalendarTypeID'] = None

        # set to None if chamber_code (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_code is None and "chamber_code" in self.model_fields_set:
            _dict['ChamberCode'] = None

        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['SessionCode'] = None

        # set to None if vote_room_id (nullable) is None
        # and model_fields_set contains the field
        if self.vote_room_id is None and "vote_room_id" in self.model_fields_set:
            _dict['VoteRoomID'] = None

        # set to None if room_description (nullable) is None
        # and model_fields_set contains the field
        if self.room_description is None and "room_description" in self.model_fields_set:
            _dict['RoomDescription'] = None

        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['Comments'] = None

        # set to None if pending_change (nullable) is None
        # and model_fields_set contains the field
        if self.pending_change is None and "pending_change" in self.model_fields_set:
            _dict['PendingChange'] = None

        # set to None if reference_number (nullable) is None
        # and model_fields_set contains the field
        if self.reference_number is None and "reference_number" in self.model_fields_set:
            _dict['ReferenceNumber'] = None

        # set to None if is_proforma (nullable) is None
        # and model_fields_set contains the field
        if self.is_proforma is None and "is_proforma" in self.model_fields_set:
            _dict['IsProforma'] = None

        # set to None if deletion_date (nullable) is None
        # and model_fields_set contains the field
        if self.deletion_date is None and "deletion_date" in self.model_fields_set:
            _dict['DeletionDate'] = None

        # set to None if calendar_files (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_files is None and "calendar_files" in self.model_fields_set:
            _dict['CalendarFiles'] = None

        # set to None if calendar_comments (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_comments is None and "calendar_comments" in self.model_fields_set:
            _dict['CalendarComments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CalendarPublicListGetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CalendarDate": obj.get("CalendarDate"),
            "MeetingTime": obj.get("MeetingTime"),
            "CalendarNumber": obj.get("CalendarNumber"),
            "Description": obj.get("Description"),
            "IsPublic": obj.get("IsPublic"),
            "CalendarType": obj.get("CalendarType"),
            "CalendarTypeID": obj.get("CalendarTypeID"),
            "ChamberCode": obj.get("ChamberCode"),
            "SessionID": obj.get("SessionID"),
            "SessionCode": obj.get("SessionCode"),
            "VoteRoomID": obj.get("VoteRoomID"),
            "RoomDescription": obj.get("RoomDescription"),
            "Comments": obj.get("Comments"),
            "PendingChange": obj.get("PendingChange"),
            "ReferenceNumber": obj.get("ReferenceNumber"),
            "IsProforma": obj.get("IsProforma"),
            "DeletionDate": obj.get("DeletionDate"),
            "CalendarID": obj.get("CalendarID"),
            "CalendarFiles": [CalendarFileBaseModel.from_dict(_item) for _item in obj["CalendarFiles"]] if obj.get("CalendarFiles") is not None else None,
            "CalendarComments": [CalendarCommentPublicGetResponse.from_dict(_item) for _item in obj["CalendarComments"]] if obj.get("CalendarComments") is not None else None
        })
        return _obj


