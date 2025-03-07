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

class PublicLegislationSummaryResponse(BaseModel):
    """
    legislation summary response
    """ # noqa: E501
    legislation_number: Optional[StrictStr] = Field(default=None, description="legislation bill number", alias="LegislationNumber")
    summary: Optional[StrictStr] = Field(default=None, description="legislation summary text", alias="Summary")
    document_code: Optional[StrictStr] = Field(default=None, description="document code", alias="DocumentCode")
    ld_number: Optional[StrictStr] = Field(default=None, description="legislation document number (LDNumber)", alias="LDNumber")
    summary_date: Optional[datetime] = Field(default=None, description="legislation summary date", alias="SummaryDate")
    summary_version_id: Optional[StrictInt] = Field(default=None, description="summary version id", alias="SummaryVersionID")
    is_public: Optional[StrictBool] = Field(default=None, description="is legislation public?", alias="IsPublic")
    is_active: Optional[StrictBool] = Field(default=None, description="is legislation active?", alias="IsActive")
    legislation_id: Optional[StrictInt] = Field(default=None, description="unique id for legislation", alias="LegislationID")
    session_id: Optional[StrictInt] = Field(default=None, description="unique id for session", alias="SessionID")
    legislation_summary_id: Optional[StrictInt] = Field(default=None, description="legislation summary id", alias="LegislationSummaryID")
    summary_version: Optional[StrictStr] = Field(default=None, description="legislation summary version", alias="SummaryVersion")
    __properties: ClassVar[List[str]] = ["LegislationNumber", "Summary", "DocumentCode", "LDNumber", "SummaryDate", "SummaryVersionID", "IsPublic", "IsActive", "LegislationID", "SessionID", "LegislationSummaryID", "SummaryVersion"]

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
        """Create an instance of PublicLegislationSummaryResponse from a JSON string"""
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
        # set to None if legislation_number (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_number is None and "legislation_number" in self.model_fields_set:
            _dict['LegislationNumber'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['Summary'] = None

        # set to None if document_code (nullable) is None
        # and model_fields_set contains the field
        if self.document_code is None and "document_code" in self.model_fields_set:
            _dict['DocumentCode'] = None

        # set to None if ld_number (nullable) is None
        # and model_fields_set contains the field
        if self.ld_number is None and "ld_number" in self.model_fields_set:
            _dict['LDNumber'] = None

        # set to None if summary_version (nullable) is None
        # and model_fields_set contains the field
        if self.summary_version is None and "summary_version" in self.model_fields_set:
            _dict['SummaryVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicLegislationSummaryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LegislationNumber": obj.get("LegislationNumber"),
            "Summary": obj.get("Summary"),
            "DocumentCode": obj.get("DocumentCode"),
            "LDNumber": obj.get("LDNumber"),
            "SummaryDate": obj.get("SummaryDate"),
            "SummaryVersionID": obj.get("SummaryVersionID"),
            "IsPublic": obj.get("IsPublic"),
            "IsActive": obj.get("IsActive"),
            "LegislationID": obj.get("LegislationID"),
            "SessionID": obj.get("SessionID"),
            "LegislationSummaryID": obj.get("LegislationSummaryID"),
            "SummaryVersion": obj.get("SummaryVersion")
        })
        return _obj


