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
from valis.models.calendar_display_public_get_response import CalendarDisplayPublicGetResponse
from valis.models.committee_member_partner_get_response import CommitteeMemberPartnerGetResponse
from valis.models.docket_category_public_get_response import DocketCategoryPublicGetResponse
from valis.models.docket_file_partner_get_response import DocketFilePartnerGetResponse
from valis.models.public_schedule_response import PublicScheduleResponse
from valis.models.staff_partner_get_response import StaffPartnerGetResponse
from typing import Optional, Set
from typing_extensions import Self

class DocketWithSchedulePublicGetResponse(BaseModel):
    """
    Docket Public Get Response with potential list of Schedule Responses
    """ # noqa: E501
    docket_date: datetime = Field(description="Docket(Committee Calendar) Date", alias="DocketDate")
    meeting_time: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Meeting Time", alias="MeetingTime")
    docket_number: Optional[StrictInt] = Field(default=None, description="Docket(Committee Calendar) Number", alias="DocketNumber")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Docket(Committee Calendar) Description", alias="Description")
    is_public: Optional[StrictBool] = Field(default=None, description="Is Docket(Committee Calendar) for Public Consumption", alias="IsPublic")
    docket_type_id: Optional[StrictInt] = Field(default=None, description="Docket(Committee Calendar) Type ID", alias="DocketTypeID")
    docket_type: Annotated[str, Field(strict=True, max_length=25)] = Field(description="Docket Type", alias="DocketType")
    chamber_code: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Chamber Code is always defaulted to S for Senate", alias="ChamberCode")
    session_id: StrictInt = Field(description="Session ID", alias="SessionID")
    session_code: Optional[StrictStr] = Field(default=None, description="Session Code", alias="SessionCode")
    vote_room_id: Optional[StrictInt] = Field(default=None, description="Vote Room ID", alias="VoteRoomID")
    comments: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = Field(default=None, description="Meeting Notes/Comments", alias="Comments")
    committee_id: StrictInt = Field(description="Committee ID", alias="CommitteeID")
    committee_name: Optional[StrictStr] = Field(default=None, description="Committee Name", alias="CommitteeName")
    parent_committee_name: Optional[StrictStr] = Field(default=None, description="Parent Committee Name", alias="ParentCommitteeName")
    pending_change: Optional[StrictBool] = Field(default=None, description="Pending Change to Docket", alias="PendingChange")
    reference_number: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="Reference Number used for External Reference to Docket", alias="ReferenceNumber")
    is_proforma: Optional[StrictBool] = Field(default=None, description="IsProforma to Calendar", alias="IsProforma")
    deletion_date: Optional[datetime] = Field(default=None, description="Docket(Committee Calendar) Deletion Date", alias="DeletionDate")
    docket_id: StrictInt = Field(description="Docket unique identifier", alias="DocketID")
    calendar_display: Optional[List[CalendarDisplayPublicGetResponse]] = Field(default=None, description="Listing of Calendar Displays", alias="CalendarDisplay")
    committee_member: Optional[List[CommitteeMemberPartnerGetResponse]] = Field(default=None, description="Listing of Committee Members", alias="CommitteeMember")
    staff: Optional[List[StaffPartnerGetResponse]] = Field(default=None, description="Listing of Staff", alias="Staff")
    docket_categories: Optional[List[DocketCategoryPublicGetResponse]] = Field(default=None, description="Listing of Calendar Categories", alias="DocketCategories")
    docket_files: Optional[List[DocketFilePartnerGetResponse]] = Field(default=None, description="Listing of Docket Files", alias="DocketFiles")
    schedules: Optional[List[PublicScheduleResponse]] = Field(default=None, description="Schedules", alias="Schedules")
    __properties: ClassVar[List[str]] = ["DocketDate", "MeetingTime", "DocketNumber", "Description", "IsPublic", "DocketTypeID", "DocketType", "ChamberCode", "SessionID", "SessionCode", "VoteRoomID", "Comments", "CommitteeID", "CommitteeName", "ParentCommitteeName", "PendingChange", "ReferenceNumber", "IsProforma", "DeletionDate", "DocketID", "CalendarDisplay", "CommitteeMember", "Staff", "DocketCategories", "DocketFiles", "Schedules"]

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
        """Create an instance of DocketWithSchedulePublicGetResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in calendar_display (list)
        _items = []
        if self.calendar_display:
            for _item_calendar_display in self.calendar_display:
                if _item_calendar_display:
                    _items.append(_item_calendar_display.to_dict())
            _dict['CalendarDisplay'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in committee_member (list)
        _items = []
        if self.committee_member:
            for _item_committee_member in self.committee_member:
                if _item_committee_member:
                    _items.append(_item_committee_member.to_dict())
            _dict['CommitteeMember'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in staff (list)
        _items = []
        if self.staff:
            for _item_staff in self.staff:
                if _item_staff:
                    _items.append(_item_staff.to_dict())
            _dict['Staff'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in docket_categories (list)
        _items = []
        if self.docket_categories:
            for _item_docket_categories in self.docket_categories:
                if _item_docket_categories:
                    _items.append(_item_docket_categories.to_dict())
            _dict['DocketCategories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in docket_files (list)
        _items = []
        if self.docket_files:
            for _item_docket_files in self.docket_files:
                if _item_docket_files:
                    _items.append(_item_docket_files.to_dict())
            _dict['DocketFiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in schedules (list)
        _items = []
        if self.schedules:
            for _item_schedules in self.schedules:
                if _item_schedules:
                    _items.append(_item_schedules.to_dict())
            _dict['Schedules'] = _items
        # set to None if meeting_time (nullable) is None
        # and model_fields_set contains the field
        if self.meeting_time is None and "meeting_time" in self.model_fields_set:
            _dict['MeetingTime'] = None

        # set to None if docket_number (nullable) is None
        # and model_fields_set contains the field
        if self.docket_number is None and "docket_number" in self.model_fields_set:
            _dict['DocketNumber'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if is_public (nullable) is None
        # and model_fields_set contains the field
        if self.is_public is None and "is_public" in self.model_fields_set:
            _dict['IsPublic'] = None

        # set to None if docket_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.docket_type_id is None and "docket_type_id" in self.model_fields_set:
            _dict['DocketTypeID'] = None

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

        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['Comments'] = None

        # set to None if committee_name (nullable) is None
        # and model_fields_set contains the field
        if self.committee_name is None and "committee_name" in self.model_fields_set:
            _dict['CommitteeName'] = None

        # set to None if parent_committee_name (nullable) is None
        # and model_fields_set contains the field
        if self.parent_committee_name is None and "parent_committee_name" in self.model_fields_set:
            _dict['ParentCommitteeName'] = None

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

        # set to None if calendar_display (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_display is None and "calendar_display" in self.model_fields_set:
            _dict['CalendarDisplay'] = None

        # set to None if committee_member (nullable) is None
        # and model_fields_set contains the field
        if self.committee_member is None and "committee_member" in self.model_fields_set:
            _dict['CommitteeMember'] = None

        # set to None if staff (nullable) is None
        # and model_fields_set contains the field
        if self.staff is None and "staff" in self.model_fields_set:
            _dict['Staff'] = None

        # set to None if docket_categories (nullable) is None
        # and model_fields_set contains the field
        if self.docket_categories is None and "docket_categories" in self.model_fields_set:
            _dict['DocketCategories'] = None

        # set to None if docket_files (nullable) is None
        # and model_fields_set contains the field
        if self.docket_files is None and "docket_files" in self.model_fields_set:
            _dict['DocketFiles'] = None

        # set to None if schedules (nullable) is None
        # and model_fields_set contains the field
        if self.schedules is None and "schedules" in self.model_fields_set:
            _dict['Schedules'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocketWithSchedulePublicGetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DocketDate": obj.get("DocketDate"),
            "MeetingTime": obj.get("MeetingTime"),
            "DocketNumber": obj.get("DocketNumber"),
            "Description": obj.get("Description"),
            "IsPublic": obj.get("IsPublic"),
            "DocketTypeID": obj.get("DocketTypeID"),
            "DocketType": obj.get("DocketType"),
            "ChamberCode": obj.get("ChamberCode"),
            "SessionID": obj.get("SessionID"),
            "SessionCode": obj.get("SessionCode"),
            "VoteRoomID": obj.get("VoteRoomID"),
            "Comments": obj.get("Comments"),
            "CommitteeID": obj.get("CommitteeID"),
            "CommitteeName": obj.get("CommitteeName"),
            "ParentCommitteeName": obj.get("ParentCommitteeName"),
            "PendingChange": obj.get("PendingChange"),
            "ReferenceNumber": obj.get("ReferenceNumber"),
            "IsProforma": obj.get("IsProforma"),
            "DeletionDate": obj.get("DeletionDate"),
            "DocketID": obj.get("DocketID"),
            "CalendarDisplay": [CalendarDisplayPublicGetResponse.from_dict(_item) for _item in obj["CalendarDisplay"]] if obj.get("CalendarDisplay") is not None else None,
            "CommitteeMember": [CommitteeMemberPartnerGetResponse.from_dict(_item) for _item in obj["CommitteeMember"]] if obj.get("CommitteeMember") is not None else None,
            "Staff": [StaffPartnerGetResponse.from_dict(_item) for _item in obj["Staff"]] if obj.get("Staff") is not None else None,
            "DocketCategories": [DocketCategoryPublicGetResponse.from_dict(_item) for _item in obj["DocketCategories"]] if obj.get("DocketCategories") is not None else None,
            "DocketFiles": [DocketFilePartnerGetResponse.from_dict(_item) for _item in obj["DocketFiles"]] if obj.get("DocketFiles") is not None else None,
            "Schedules": [PublicScheduleResponse.from_dict(_item) for _item in obj["Schedules"]] if obj.get("Schedules") is not None else None
        })
        return _obj


