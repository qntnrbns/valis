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
from typing import Optional, Set
from typing_extensions import Self

class CalendarActionReferenceResponse(BaseModel):
    """
    Calendar Action \"Action Reference\" Reference Response
    """ # noqa: E501
    action_reference_id: StrictInt = Field(description="Calendar Action unique identifier", alias="ActionReferenceID")
    is_mandatory: Optional[StrictBool] = Field(default=None, description="is this action reference required? true/false", alias="IsMandatory")
    sequence: Optional[StrictInt] = Field(default=None, description="Sequence for action reference", alias="Sequence")
    reference_text: Optional[StrictStr] = Field(default=None, description="reference text for the action reference, e.g. \"On Motion Of \"", alias="ReferenceText")
    calendar_action_id: Optional[StrictInt] = Field(default=None, description="unique identifier for associated calendar action", alias="CalendarActionID")
    action_reference_type_id: Optional[StrictInt] = Field(default=None, description="unique identifier for associated action reference type", alias="ActionReferenceTypeID")
    action_reference_type: Optional[StrictStr] = Field(default=None, description="name for for associated action reference type e.g. Member", alias="ActionReferenceType")
    __properties: ClassVar[List[str]] = ["ActionReferenceID", "IsMandatory", "Sequence", "ReferenceText", "CalendarActionID", "ActionReferenceTypeID", "ActionReferenceType"]

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
        """Create an instance of CalendarActionReferenceResponse from a JSON string"""
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
        # set to None if reference_text (nullable) is None
        # and model_fields_set contains the field
        if self.reference_text is None and "reference_text" in self.model_fields_set:
            _dict['ReferenceText'] = None

        # set to None if action_reference_type (nullable) is None
        # and model_fields_set contains the field
        if self.action_reference_type is None and "action_reference_type" in self.model_fields_set:
            _dict['ActionReferenceType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CalendarActionReferenceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActionReferenceID": obj.get("ActionReferenceID"),
            "IsMandatory": obj.get("IsMandatory"),
            "Sequence": obj.get("Sequence"),
            "ReferenceText": obj.get("ReferenceText"),
            "CalendarActionID": obj.get("CalendarActionID"),
            "ActionReferenceTypeID": obj.get("ActionReferenceTypeID"),
            "ActionReferenceType": obj.get("ActionReferenceType")
        })
        return _obj


