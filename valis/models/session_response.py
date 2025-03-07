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

class SessionResponse(BaseModel):
    """
    Session object to be returned within Legislation
    """ # noqa: E501
    session_id: Optional[StrictInt] = Field(default=None, description="unique identifer for session", alias="SessionID")
    session_code: Optional[StrictStr] = Field(default=None, description="Session Code identifier (e.g. 20181 for 2018 Regular Session)", alias="SessionCode")
    is_prefile: Optional[StrictBool] = Field(default=None, description="Is Prefiled Legislation", alias="IsPrefile")
    __properties: ClassVar[List[str]] = ["SessionID", "SessionCode", "IsPrefile"]

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
        """Create an instance of SessionResponse from a JSON string"""
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
        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['SessionCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SessionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "SessionID": obj.get("SessionID"),
            "SessionCode": obj.get("SessionCode"),
            "IsPrefile": obj.get("IsPrefile")
        })
        return _obj


