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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class DocketFilePublicGetResponse(BaseModel):
    """
    Docket Files
    """ # noqa: E501
    calendar_file_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Files", alias="CalendarFileID")
    calendar_id: Optional[StrictInt] = Field(default=None, description="Database Unique Identifier for Calendar/Docket/Agenda", alias="CalendarID")
    file_url: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="File URL", alias="FileURL")
    text_format_id: StrictInt = Field(description="Unique Identifier for Text format ID", alias="TextFormatID")
    is_generated: Optional[StrictBool] = Field(default=None, description="File Generated", alias="IsGenerated")
    is_public: Optional[StrictBool] = Field(default=None, description="File Public", alias="IsPublic")
    is_active: Optional[StrictBool] = Field(default=None, description="File Active", alias="IsActive")
    __properties: ClassVar[List[str]] = ["CalendarFileID", "CalendarID", "FileURL", "TextFormatID", "IsGenerated", "IsPublic", "IsActive"]

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
        """Create an instance of DocketFilePublicGetResponse from a JSON string"""
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
        # set to None if calendar_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_file_id is None and "calendar_file_id" in self.model_fields_set:
            _dict['CalendarFileID'] = None

        # set to None if calendar_id (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_id is None and "calendar_id" in self.model_fields_set:
            _dict['CalendarID'] = None

        # set to None if file_url (nullable) is None
        # and model_fields_set contains the field
        if self.file_url is None and "file_url" in self.model_fields_set:
            _dict['FileURL'] = None

        # set to None if is_generated (nullable) is None
        # and model_fields_set contains the field
        if self.is_generated is None and "is_generated" in self.model_fields_set:
            _dict['IsGenerated'] = None

        # set to None if is_public (nullable) is None
        # and model_fields_set contains the field
        if self.is_public is None and "is_public" in self.model_fields_set:
            _dict['IsPublic'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['IsActive'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocketFilePublicGetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CalendarFileID": obj.get("CalendarFileID"),
            "CalendarID": obj.get("CalendarID"),
            "FileURL": obj.get("FileURL"),
            "TextFormatID": obj.get("TextFormatID"),
            "IsGenerated": obj.get("IsGenerated"),
            "IsPublic": obj.get("IsPublic"),
            "IsActive": obj.get("IsActive")
        })
        return _obj


