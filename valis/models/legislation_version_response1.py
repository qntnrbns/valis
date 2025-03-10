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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class LegislationVersionResponse1(BaseModel):
    """
    Different types of versions for legislation
    """ # noqa: E501
    legislation_version_id: Optional[StrictInt] = Field(default=None, description="unique identifier of the LegislationVersion", alias="LegislationVersionID")
    name: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="name of the LegislationVersion", alias="Name")
    version_code: Optional[Annotated[str, Field(strict=True, max_length=5)]] = Field(default=None, description="code for the LegislationVersion", alias="VersionCode")
    legislation_status_id: Optional[StrictInt] = Field(default=None, description="ID for what legislation status this version correlates to", alias="LegislationStatusID")
    suffix: Optional[Annotated[str, Field(strict=True, max_length=5)]] = Field(default=None, description="The suffix that is added to the end of the legislation number on the printed legislation text", alias="Suffix")
    authoring_label: Optional[StrictStr] = Field(default=None, description="legislation version label for authoring purposes", alias="AuthoringLabel")
    __properties: ClassVar[List[str]] = ["LegislationVersionID", "Name", "VersionCode", "LegislationStatusID", "Suffix", "AuthoringLabel"]

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
        """Create an instance of LegislationVersionResponse1 from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['Name'] = None

        # set to None if version_code (nullable) is None
        # and model_fields_set contains the field
        if self.version_code is None and "version_code" in self.model_fields_set:
            _dict['VersionCode'] = None

        # set to None if legislation_status_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_status_id is None and "legislation_status_id" in self.model_fields_set:
            _dict['LegislationStatusID'] = None

        # set to None if suffix (nullable) is None
        # and model_fields_set contains the field
        if self.suffix is None and "suffix" in self.model_fields_set:
            _dict['Suffix'] = None

        # set to None if authoring_label (nullable) is None
        # and model_fields_set contains the field
        if self.authoring_label is None and "authoring_label" in self.model_fields_set:
            _dict['AuthoringLabel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LegislationVersionResponse1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LegislationVersionID": obj.get("LegislationVersionID"),
            "Name": obj.get("Name"),
            "VersionCode": obj.get("VersionCode"),
            "LegislationStatusID": obj.get("LegislationStatusID"),
            "Suffix": obj.get("Suffix"),
            "AuthoringLabel": obj.get("AuthoringLabel")
        })
        return _obj


