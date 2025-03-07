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
from typing import Any, ClassVar, Dict, List, Optional
from valis.models.amendment_change import AmendmentChange
from valis.models.sponsor import Sponsor
from typing import Optional, Set
from typing_extensions import Self

class AmendmentItem(BaseModel):
    """
    AmendmentItem Model - for breaking up the legislation amendment drafttext into json object
    """ # noqa: E501
    sponsor: Optional[Sponsor] = Field(default=None, alias="Sponsor")
    line: Optional[StrictStr] = Field(default=None, description="Amendment Line", alias="Line")
    line_number: Optional[StrictInt] = Field(default=None, description="Amendment Line Number", alias="LineNumber")
    line_class_name: Optional[StrictStr] = Field(default=None, description="Amendment Line ClassName, always = textbi", alias="LineClassName")
    item_order: Optional[StrictInt] = Field(default=None, description="Item Number", alias="ItemOrder")
    item_condition: Optional[StrictStr] = Field(default=None, description="Amendment Condition e.g: Agreed, Rejected", alias="ItemCondition")
    amendment_changes: Optional[List[AmendmentChange]] = Field(default=None, description="Amendment Changes e.g: Strikes and Inserts", alias="amendmentChanges")
    __properties: ClassVar[List[str]] = ["Sponsor", "Line", "LineNumber", "LineClassName", "ItemOrder", "ItemCondition", "amendmentChanges"]

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
        """Create an instance of AmendmentItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sponsor
        if self.sponsor:
            _dict['Sponsor'] = self.sponsor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in amendment_changes (list)
        _items = []
        if self.amendment_changes:
            for _item_amendment_changes in self.amendment_changes:
                if _item_amendment_changes:
                    _items.append(_item_amendment_changes.to_dict())
            _dict['amendmentChanges'] = _items
        # set to None if line (nullable) is None
        # and model_fields_set contains the field
        if self.line is None and "line" in self.model_fields_set:
            _dict['Line'] = None

        # set to None if line_class_name (nullable) is None
        # and model_fields_set contains the field
        if self.line_class_name is None and "line_class_name" in self.model_fields_set:
            _dict['LineClassName'] = None

        # set to None if item_condition (nullable) is None
        # and model_fields_set contains the field
        if self.item_condition is None and "item_condition" in self.model_fields_set:
            _dict['ItemCondition'] = None

        # set to None if amendment_changes (nullable) is None
        # and model_fields_set contains the field
        if self.amendment_changes is None and "amendment_changes" in self.model_fields_set:
            _dict['amendmentChanges'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AmendmentItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Sponsor": Sponsor.from_dict(obj["Sponsor"]) if obj.get("Sponsor") is not None else None,
            "Line": obj.get("Line"),
            "LineNumber": obj.get("LineNumber"),
            "LineClassName": obj.get("LineClassName"),
            "ItemOrder": obj.get("ItemOrder"),
            "ItemCondition": obj.get("ItemCondition"),
            "amendmentChanges": [AmendmentChange.from_dict(_item) for _item in obj["amendmentChanges"]] if obj.get("amendmentChanges") is not None else None
        })
        return _obj


