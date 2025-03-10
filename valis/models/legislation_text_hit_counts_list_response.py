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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from valis.models.legislation_text_hit_count_list_response import LegislationTextHitCountListResponse
from typing import Optional, Set
from typing_extensions import Self

class LegislationTextHitCountsListResponse(BaseModel):
    """
    LegislationTextHitCountsListResponse
    """ # noqa: E501
    success: Optional[StrictBool] = Field(default=None, description="Is this a successful response?", alias="Success")
    failure_message: Optional[StrictStr] = Field(default=None, description="Details if this response failed", alias="FailureMessage")
    cache_key_name: Optional[StrictStr] = Field(default=None, description="CacheKey name", alias="CacheKeyName")
    hit_counts: Optional[List[LegislationTextHitCountListResponse]] = Field(default=None, alias="HitCounts")
    __properties: ClassVar[List[str]] = ["Success", "FailureMessage", "CacheKeyName", "HitCounts"]

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
        """Create an instance of LegislationTextHitCountsListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in hit_counts (list)
        _items = []
        if self.hit_counts:
            for _item_hit_counts in self.hit_counts:
                if _item_hit_counts:
                    _items.append(_item_hit_counts.to_dict())
            _dict['HitCounts'] = _items
        # set to None if failure_message (nullable) is None
        # and model_fields_set contains the field
        if self.failure_message is None and "failure_message" in self.model_fields_set:
            _dict['FailureMessage'] = None

        # set to None if cache_key_name (nullable) is None
        # and model_fields_set contains the field
        if self.cache_key_name is None and "cache_key_name" in self.model_fields_set:
            _dict['CacheKeyName'] = None

        # set to None if hit_counts (nullable) is None
        # and model_fields_set contains the field
        if self.hit_counts is None and "hit_counts" in self.model_fields_set:
            _dict['HitCounts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LegislationTextHitCountsListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Success": obj.get("Success"),
            "FailureMessage": obj.get("FailureMessage"),
            "CacheKeyName": obj.get("CacheKeyName"),
            "HitCounts": [LegislationTextHitCountListResponse.from_dict(_item) for _item in obj["HitCounts"]] if obj.get("HitCounts") is not None else None
        })
        return _obj


