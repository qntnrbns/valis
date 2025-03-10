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
from valis.models.key_word import KeyWord
from valis.models.legislation_id import LegislationID
from valis.models.legislation_number_response import LegislationNumberResponse
from typing import Optional, Set
from typing_extensions import Self

class AdvancedSearch(BaseModel):
    """
    Information for performing a Legislation search
    """ # noqa: E501
    event_control_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Event Control", alias="EventControlID")
    start_date: Optional[datetime] = Field(default=None, description="Start Date associated with status dropdown", alias="StartDate")
    end_date: Optional[datetime] = Field(default=None, description="End Date associated with status dropdown", alias="EndDate")
    event_start_date: Optional[datetime] = Field(default=None, description="End Event Date, associated with Event Control dropdown", alias="EventStartDate")
    event_end_date: Optional[datetime] = Field(default=None, description="Start Event Date, associated with Event Control dropdown", alias="EventEndDate")
    introduction_date: Optional[datetime] = Field(default=None, alias="IntroductionDate")
    legislation_title: Optional[StrictStr] = Field(default=None, alias="LegislationTitle")
    description: Optional[StrictStr] = Field(default=None, description="Bill description", alias="Description")
    chambercode: Optional[StrictStr] = Field(default=None, description="Chamber code (H/S)", alias="Chambercode")
    legislation_status_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Legislation Status", alias="LegislationStatusID")
    legislation_category_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Legislation Category", alias="LegislationCategoryID")
    committee_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Committee", alias="CommitteeID")
    session_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Session", alias="SessionID")
    session_code: Optional[StrictInt] = Field(default=None, description="Session code (e.g. 20181)", alias="SessionCode")
    legislation_event_type_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Legislation Event Type", alias="LegislationEventTypeID")
    summary_length: Optional[StrictInt] = Field(default=None, description="Limitation on summary length", alias="SummaryLength")
    patron_types: Optional[List[StrictInt]] = Field(default=None, description="List of Patron Types", alias="PatronTypes")
    member_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Member", alias="MemberID")
    subject_index_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for Subject Index", alias="SubjectIndexID")
    most_frequent: Optional[StrictBool] = Field(default=None, description="Return most frequently accessed bills?", alias="MostFrequent")
    is_pending: Optional[StrictBool] = Field(default=None, description="Return pending bills?", alias="IsPending")
    keyword_expression: Optional[StrictStr] = Field(default=None, description="Keyword search - supports operators and parentheses", alias="KeywordExpression")
    keyword_location: Optional[StrictStr] = Field(default=None, description="Where to perform the Keyword search (Summary/Bill Text)", alias="KeywordLocation")
    keyword_summary_version_id: Optional[StrictInt] = Field(default=None, description="Unique identifier of Keyword Summary Version", alias="KeywordSummaryVersionID")
    keyword_legislation_version_id: Optional[StrictInt] = Field(default=None, description="Unique identifier of Keyword Legislation Version", alias="KeywordLegislationVersionID")
    keyword_use_global_session_search: Optional[StrictBool] = Field(default=None, description="Should the keyword search search across all sessions?", alias="KeywordUseGlobalSessionSearch")
    skip_legislation_text_calls: Optional[StrictBool] = Field(default=None, description="Skip searching legislation text?", alias="SkipLegislationTextCalls")
    current_status: Optional[StrictBool] = Field(default=None, description="Search by only the current bill status?", alias="CurrentStatus")
    keywords: Optional[List[KeyWord]] = Field(default=None, description="List of KeyWord search objects", alias="Keywords")
    exclude_failed: Optional[StrictBool] = Field(default=None, alias="ExcludeFailed")
    chapter_number: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Chapter Number", alias="ChapterNumber")
    legislation_numbers: Optional[List[LegislationNumberResponse]] = Field(default=None, description="List of Legislative Numbers", alias="LegislationNumbers")
    legislation_ids: Optional[List[LegislationID]] = Field(default=None, description="List of Legislation IDs", alias="LegislationIDs")
    __properties: ClassVar[List[str]] = ["EventControlID", "StartDate", "EndDate", "EventStartDate", "EventEndDate", "IntroductionDate", "LegislationTitle", "Description", "Chambercode", "LegislationStatusID", "LegislationCategoryID", "CommitteeID", "SessionID", "SessionCode", "LegislationEventTypeID", "SummaryLength", "PatronTypes", "MemberID", "SubjectIndexID", "MostFrequent", "IsPending", "KeywordExpression", "KeywordLocation", "KeywordSummaryVersionID", "KeywordLegislationVersionID", "KeywordUseGlobalSessionSearch", "SkipLegislationTextCalls", "CurrentStatus", "Keywords", "ExcludeFailed", "ChapterNumber", "LegislationNumbers", "LegislationIDs"]

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
        """Create an instance of AdvancedSearch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in keywords (list)
        _items = []
        if self.keywords:
            for _item_keywords in self.keywords:
                if _item_keywords:
                    _items.append(_item_keywords.to_dict())
            _dict['Keywords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in legislation_numbers (list)
        _items = []
        if self.legislation_numbers:
            for _item_legislation_numbers in self.legislation_numbers:
                if _item_legislation_numbers:
                    _items.append(_item_legislation_numbers.to_dict())
            _dict['LegislationNumbers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in legislation_ids (list)
        _items = []
        if self.legislation_ids:
            for _item_legislation_ids in self.legislation_ids:
                if _item_legislation_ids:
                    _items.append(_item_legislation_ids.to_dict())
            _dict['LegislationIDs'] = _items
        # set to None if event_control_id (nullable) is None
        # and model_fields_set contains the field
        if self.event_control_id is None and "event_control_id" in self.model_fields_set:
            _dict['EventControlID'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['StartDate'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['EndDate'] = None

        # set to None if event_start_date (nullable) is None
        # and model_fields_set contains the field
        if self.event_start_date is None and "event_start_date" in self.model_fields_set:
            _dict['EventStartDate'] = None

        # set to None if event_end_date (nullable) is None
        # and model_fields_set contains the field
        if self.event_end_date is None and "event_end_date" in self.model_fields_set:
            _dict['EventEndDate'] = None

        # set to None if introduction_date (nullable) is None
        # and model_fields_set contains the field
        if self.introduction_date is None and "introduction_date" in self.model_fields_set:
            _dict['IntroductionDate'] = None

        # set to None if legislation_title (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_title is None and "legislation_title" in self.model_fields_set:
            _dict['LegislationTitle'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if chambercode (nullable) is None
        # and model_fields_set contains the field
        if self.chambercode is None and "chambercode" in self.model_fields_set:
            _dict['Chambercode'] = None

        # set to None if legislation_status_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_status_id is None and "legislation_status_id" in self.model_fields_set:
            _dict['LegislationStatusID'] = None

        # set to None if legislation_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_category_id is None and "legislation_category_id" in self.model_fields_set:
            _dict['LegislationCategoryID'] = None

        # set to None if committee_id (nullable) is None
        # and model_fields_set contains the field
        if self.committee_id is None and "committee_id" in self.model_fields_set:
            _dict['CommitteeID'] = None

        # set to None if session_id (nullable) is None
        # and model_fields_set contains the field
        if self.session_id is None and "session_id" in self.model_fields_set:
            _dict['SessionID'] = None

        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['SessionCode'] = None

        # set to None if legislation_event_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_event_type_id is None and "legislation_event_type_id" in self.model_fields_set:
            _dict['LegislationEventTypeID'] = None

        # set to None if summary_length (nullable) is None
        # and model_fields_set contains the field
        if self.summary_length is None and "summary_length" in self.model_fields_set:
            _dict['SummaryLength'] = None

        # set to None if patron_types (nullable) is None
        # and model_fields_set contains the field
        if self.patron_types is None and "patron_types" in self.model_fields_set:
            _dict['PatronTypes'] = None

        # set to None if member_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_id is None and "member_id" in self.model_fields_set:
            _dict['MemberID'] = None

        # set to None if subject_index_id (nullable) is None
        # and model_fields_set contains the field
        if self.subject_index_id is None and "subject_index_id" in self.model_fields_set:
            _dict['SubjectIndexID'] = None

        # set to None if keyword_expression (nullable) is None
        # and model_fields_set contains the field
        if self.keyword_expression is None and "keyword_expression" in self.model_fields_set:
            _dict['KeywordExpression'] = None

        # set to None if keyword_location (nullable) is None
        # and model_fields_set contains the field
        if self.keyword_location is None and "keyword_location" in self.model_fields_set:
            _dict['KeywordLocation'] = None

        # set to None if keyword_summary_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.keyword_summary_version_id is None and "keyword_summary_version_id" in self.model_fields_set:
            _dict['KeywordSummaryVersionID'] = None

        # set to None if keyword_legislation_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.keyword_legislation_version_id is None and "keyword_legislation_version_id" in self.model_fields_set:
            _dict['KeywordLegislationVersionID'] = None

        # set to None if skip_legislation_text_calls (nullable) is None
        # and model_fields_set contains the field
        if self.skip_legislation_text_calls is None and "skip_legislation_text_calls" in self.model_fields_set:
            _dict['SkipLegislationTextCalls'] = None

        # set to None if current_status (nullable) is None
        # and model_fields_set contains the field
        if self.current_status is None and "current_status" in self.model_fields_set:
            _dict['CurrentStatus'] = None

        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict['Keywords'] = None

        # set to None if exclude_failed (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_failed is None and "exclude_failed" in self.model_fields_set:
            _dict['ExcludeFailed'] = None

        # set to None if chapter_number (nullable) is None
        # and model_fields_set contains the field
        if self.chapter_number is None and "chapter_number" in self.model_fields_set:
            _dict['ChapterNumber'] = None

        # set to None if legislation_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_numbers is None and "legislation_numbers" in self.model_fields_set:
            _dict['LegislationNumbers'] = None

        # set to None if legislation_ids (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_ids is None and "legislation_ids" in self.model_fields_set:
            _dict['LegislationIDs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvancedSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "EventControlID": obj.get("EventControlID"),
            "StartDate": obj.get("StartDate"),
            "EndDate": obj.get("EndDate"),
            "EventStartDate": obj.get("EventStartDate"),
            "EventEndDate": obj.get("EventEndDate"),
            "IntroductionDate": obj.get("IntroductionDate"),
            "LegislationTitle": obj.get("LegislationTitle"),
            "Description": obj.get("Description"),
            "Chambercode": obj.get("Chambercode"),
            "LegislationStatusID": obj.get("LegislationStatusID"),
            "LegislationCategoryID": obj.get("LegislationCategoryID"),
            "CommitteeID": obj.get("CommitteeID"),
            "SessionID": obj.get("SessionID"),
            "SessionCode": obj.get("SessionCode"),
            "LegislationEventTypeID": obj.get("LegislationEventTypeID"),
            "SummaryLength": obj.get("SummaryLength"),
            "PatronTypes": obj.get("PatronTypes"),
            "MemberID": obj.get("MemberID"),
            "SubjectIndexID": obj.get("SubjectIndexID"),
            "MostFrequent": obj.get("MostFrequent"),
            "IsPending": obj.get("IsPending"),
            "KeywordExpression": obj.get("KeywordExpression"),
            "KeywordLocation": obj.get("KeywordLocation"),
            "KeywordSummaryVersionID": obj.get("KeywordSummaryVersionID"),
            "KeywordLegislationVersionID": obj.get("KeywordLegislationVersionID"),
            "KeywordUseGlobalSessionSearch": obj.get("KeywordUseGlobalSessionSearch"),
            "SkipLegislationTextCalls": obj.get("SkipLegislationTextCalls"),
            "CurrentStatus": obj.get("CurrentStatus"),
            "Keywords": [KeyWord.from_dict(_item) for _item in obj["Keywords"]] if obj.get("Keywords") is not None else None,
            "ExcludeFailed": obj.get("ExcludeFailed"),
            "ChapterNumber": obj.get("ChapterNumber"),
            "LegislationNumbers": [LegislationNumberResponse.from_dict(_item) for _item in obj["LegislationNumbers"]] if obj.get("LegislationNumbers") is not None else None,
            "LegislationIDs": [LegislationID.from_dict(_item) for _item in obj["LegislationIDs"]] if obj.get("LegislationIDs") is not None else None
        })
        return _obj


