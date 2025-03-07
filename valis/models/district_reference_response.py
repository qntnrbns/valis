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
from typing import Optional, Set
from typing_extensions import Self

class DistrictReferenceResponse(BaseModel):
    """
    Information for a District
    """ # noqa: E501
    chamber_code: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(default=None, description="Chamber code (H/S)", alias="ChamberCode")
    district_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for this District", alias="DistrictID")
    title: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="District title", alias="Title")
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, description="District description", alias="Description")
    __properties: ClassVar[List[str]] = ["ChamberCode", "DistrictID", "Title", "Description"]

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
        """Create an instance of DistrictReferenceResponse from a JSON string"""
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
        # set to None if chamber_code (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_code is None and "chamber_code" in self.model_fields_set:
            _dict['ChamberCode'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['Title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistrictReferenceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChamberCode": obj.get("ChamberCode"),
            "DistrictID": obj.get("DistrictID"),
            "Title": obj.get("Title"),
            "Description": obj.get("Description")
        })
        return _obj


