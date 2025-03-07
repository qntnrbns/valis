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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class PDFFile(BaseModel):
    """
    PDF File object representing storage in Azure Blob Storage
    """ # noqa: E501
    legislation_text_id: Optional[StrictInt] = Field(default=None, description="unique identifier of LegislationText", alias="LegislationTextID")
    text_format_id: Optional[StrictInt] = Field(default=None, description="unique identifier of TextFormat", alias="TextFormatID")
    text_format: Optional[StrictStr] = Field(default=None, description="Text Format (e.g. PDF)", alias="TextFormat")
    file_url: Optional[StrictStr] = Field(default=None, description="Azure Blob Storage URL", alias="FileURL")
    reference_number: Optional[StrictStr] = Field(default=None, description="Reference Number", alias="ReferenceNumber")
    session_id: Optional[StrictInt] = Field(default=None, description="internal SessionID", alias="SessionID")
    description: Optional[StrictStr] = Field(default=None, description="Description", alias="Description")
    page_count: Optional[StrictInt] = Field(default=None, description="Page count for a particular bill pdf", alias="PageCount")
    __properties: ClassVar[List[str]] = ["LegislationTextID", "TextFormatID", "TextFormat", "FileURL", "ReferenceNumber", "SessionID", "Description", "PageCount"]

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
        """Create an instance of PDFFile from a JSON string"""
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
        # set to None if text_format (nullable) is None
        # and model_fields_set contains the field
        if self.text_format is None and "text_format" in self.model_fields_set:
            _dict['TextFormat'] = None

        # set to None if file_url (nullable) is None
        # and model_fields_set contains the field
        if self.file_url is None and "file_url" in self.model_fields_set:
            _dict['FileURL'] = None

        # set to None if reference_number (nullable) is None
        # and model_fields_set contains the field
        if self.reference_number is None and "reference_number" in self.model_fields_set:
            _dict['ReferenceNumber'] = None

        # set to None if session_id (nullable) is None
        # and model_fields_set contains the field
        if self.session_id is None and "session_id" in self.model_fields_set:
            _dict['SessionID'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if page_count (nullable) is None
        # and model_fields_set contains the field
        if self.page_count is None and "page_count" in self.model_fields_set:
            _dict['PageCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PDFFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LegislationTextID": obj.get("LegislationTextID"),
            "TextFormatID": obj.get("TextFormatID"),
            "TextFormat": obj.get("TextFormat"),
            "FileURL": obj.get("FileURL"),
            "ReferenceNumber": obj.get("ReferenceNumber"),
            "SessionID": obj.get("SessionID"),
            "Description": obj.get("Description"),
            "PageCount": obj.get("PageCount")
        })
        return _obj


