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
from valis.models.public_communication_file import PublicCommunicationFile
from typing import Optional, Set
from typing_extensions import Self

class PublicGetCommunicationFilesResponse(BaseModel):
    """
    List of Public Communication Files
    """ # noqa: E501
    success: Optional[StrictBool] = Field(default=None, description="Is this a successful response?", alias="Success")
    failure_message: Optional[StrictStr] = Field(default=None, description="Details if this response failed", alias="FailureMessage")
    cache_key_name: Optional[StrictStr] = Field(default=None, description="CacheKey name", alias="CacheKeyName")
    list_items: Optional[List[PublicCommunicationFile]] = Field(default=None, description="List of Public Communication Files", alias="ListItems")
    __properties: ClassVar[List[str]] = ["Success", "FailureMessage", "CacheKeyName", "ListItems"]

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
        """Create an instance of PublicGetCommunicationFilesResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in list_items (list)
        _items = []
        if self.list_items:
            for _item_list_items in self.list_items:
                if _item_list_items:
                    _items.append(_item_list_items.to_dict())
            _dict['ListItems'] = _items
        # set to None if failure_message (nullable) is None
        # and model_fields_set contains the field
        if self.failure_message is None and "failure_message" in self.model_fields_set:
            _dict['FailureMessage'] = None

        # set to None if cache_key_name (nullable) is None
        # and model_fields_set contains the field
        if self.cache_key_name is None and "cache_key_name" in self.model_fields_set:
            _dict['CacheKeyName'] = None

        # set to None if list_items (nullable) is None
        # and model_fields_set contains the field
        if self.list_items is None and "list_items" in self.model_fields_set:
            _dict['ListItems'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicGetCommunicationFilesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Success": obj.get("Success"),
            "FailureMessage": obj.get("FailureMessage"),
            "CacheKeyName": obj.get("CacheKeyName"),
            "ListItems": [PublicCommunicationFile.from_dict(_item) for _item in obj["ListItems"]] if obj.get("ListItems") is not None else None
        })
        return _obj


