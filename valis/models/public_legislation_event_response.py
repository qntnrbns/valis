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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from valis.models.public_event_reference_response import PublicEventReferenceResponse
from typing import Optional, Set
from typing_extensions import Self

class PublicLegislationEventResponse(BaseModel):
    """
    Information for a public Legislation Event
    """ # noqa: E501
    legislation_event_id: Optional[StrictInt] = Field(default=None, description="Legislation event unique identifier", alias="LegislationEventID")
    legislation_event_type_id: Optional[StrictInt] = Field(default=None, description="Legislation Event Type Identifer (Unique for each Biennial)", alias="LegislationEventTypeID")
    event_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Event Code (can be used in place of Legislation Event Type ID)", alias="EventCode")
    event_date: Optional[datetime] = Field(default=None, description="The Date the Event occurred", alias="EventDate")
    deletion_date: Optional[datetime] = Field(default=None, description="The Date the Event is Deleted", alias="DeletionDate")
    description: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, description="Legislation Description", alias="Description")
    legislation_id: Optional[StrictInt] = Field(default=None, description="Legislation Identifier", alias="LegislationID")
    vote_id: Optional[StrictInt] = Field(default=None, description="VoteID", alias="VoteID")
    effective_type: Optional[StrictStr] = Field(default=None, description="Determines whether the enaction of the legislation is standard, emergency, or other", alias="EffectiveType")
    effective_type_id: Optional[StrictInt] = Field(default=None, description="ID of EffectiveType.", alias="EffectiveTypeID")
    legislation_number: Optional[StrictStr] = Field(default=None, description="Human Readable Legislation Identifier", alias="LegislationNumber")
    chamber_code: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Chamber Code", alias="ChamberCode")
    sequence: Optional[StrictInt] = Field(default=None, description="Sequence", alias="Sequence")
    session_code: Optional[StrictStr] = Field(default=None, description="Human readable code for the Session that the event happened in", alias="SessionCode")
    is_public: Optional[StrictBool] = Field(default=None, description="Is Public Event", alias="IsPublic")
    is_passed: Optional[StrictBool] = Field(default=None, description="Has Event Passed?", alias="IsPassed")
    legislation_status_id: Optional[StrictInt] = Field(default=None, description="Unique Identifier for Legislation Event Status", alias="LegislationStatusID")
    reference_id: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, description="Originating System code used for identifying this Event in that system", alias="ReferenceID")
    reference_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Originating system number (e.g. Vote #, LD #, Committee #) that correlates with the ReferenceType", alias="ReferenceNumber")
    reference_type_id: Optional[StrictInt] = Field(default=None, description="unique identifier for the ReferenceType", alias="ReferenceTypeID")
    reference_type: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="name for ReferenceType (e.g. LegislationText, Vote, Committee, Minutes)", alias="ReferenceType")
    status: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Status Name", alias="Status")
    actor_id: Optional[StrictInt] = Field(default=None, description="unique identifier for the ActorType", alias="ActorID")
    actor_type: Optional[StrictStr] = Field(default=None, description="The subject taking the event action (i.e House/Senate/Conference/Governor)", alias="ActorType")
    event_references: Optional[List[PublicEventReferenceResponse]] = Field(default=None, description="List of public Event References", alias="EventReferences")
    __properties: ClassVar[List[str]] = ["LegislationEventID", "LegislationEventTypeID", "EventCode", "EventDate", "DeletionDate", "Description", "LegislationID", "VoteID", "EffectiveType", "EffectiveTypeID", "LegislationNumber", "ChamberCode", "Sequence", "SessionCode", "IsPublic", "IsPassed", "LegislationStatusID", "ReferenceID", "ReferenceNumber", "ReferenceTypeID", "ReferenceType", "Status", "ActorID", "ActorType", "EventReferences"]

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
        """Create an instance of PublicLegislationEventResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in event_references (list)
        _items = []
        if self.event_references:
            for _item_event_references in self.event_references:
                if _item_event_references:
                    _items.append(_item_event_references.to_dict())
            _dict['EventReferences'] = _items
        # set to None if legislation_event_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_event_id is None and "legislation_event_id" in self.model_fields_set:
            _dict['LegislationEventID'] = None

        # set to None if legislation_event_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_event_type_id is None and "legislation_event_type_id" in self.model_fields_set:
            _dict['LegislationEventTypeID'] = None

        # set to None if event_code (nullable) is None
        # and model_fields_set contains the field
        if self.event_code is None and "event_code" in self.model_fields_set:
            _dict['EventCode'] = None

        # set to None if deletion_date (nullable) is None
        # and model_fields_set contains the field
        if self.deletion_date is None and "deletion_date" in self.model_fields_set:
            _dict['DeletionDate'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['Description'] = None

        # set to None if legislation_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_id is None and "legislation_id" in self.model_fields_set:
            _dict['LegislationID'] = None

        # set to None if vote_id (nullable) is None
        # and model_fields_set contains the field
        if self.vote_id is None and "vote_id" in self.model_fields_set:
            _dict['VoteID'] = None

        # set to None if effective_type (nullable) is None
        # and model_fields_set contains the field
        if self.effective_type is None and "effective_type" in self.model_fields_set:
            _dict['EffectiveType'] = None

        # set to None if effective_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.effective_type_id is None and "effective_type_id" in self.model_fields_set:
            _dict['EffectiveTypeID'] = None

        # set to None if legislation_number (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_number is None and "legislation_number" in self.model_fields_set:
            _dict['LegislationNumber'] = None

        # set to None if chamber_code (nullable) is None
        # and model_fields_set contains the field
        if self.chamber_code is None and "chamber_code" in self.model_fields_set:
            _dict['ChamberCode'] = None

        # set to None if sequence (nullable) is None
        # and model_fields_set contains the field
        if self.sequence is None and "sequence" in self.model_fields_set:
            _dict['Sequence'] = None

        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['SessionCode'] = None

        # set to None if is_passed (nullable) is None
        # and model_fields_set contains the field
        if self.is_passed is None and "is_passed" in self.model_fields_set:
            _dict['IsPassed'] = None

        # set to None if legislation_status_id (nullable) is None
        # and model_fields_set contains the field
        if self.legislation_status_id is None and "legislation_status_id" in self.model_fields_set:
            _dict['LegislationStatusID'] = None

        # set to None if reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.reference_id is None and "reference_id" in self.model_fields_set:
            _dict['ReferenceID'] = None

        # set to None if reference_number (nullable) is None
        # and model_fields_set contains the field
        if self.reference_number is None and "reference_number" in self.model_fields_set:
            _dict['ReferenceNumber'] = None

        # set to None if reference_type (nullable) is None
        # and model_fields_set contains the field
        if self.reference_type is None and "reference_type" in self.model_fields_set:
            _dict['ReferenceType'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['Status'] = None

        # set to None if actor_id (nullable) is None
        # and model_fields_set contains the field
        if self.actor_id is None and "actor_id" in self.model_fields_set:
            _dict['ActorID'] = None

        # set to None if actor_type (nullable) is None
        # and model_fields_set contains the field
        if self.actor_type is None and "actor_type" in self.model_fields_set:
            _dict['ActorType'] = None

        # set to None if event_references (nullable) is None
        # and model_fields_set contains the field
        if self.event_references is None and "event_references" in self.model_fields_set:
            _dict['EventReferences'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicLegislationEventResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LegislationEventID": obj.get("LegislationEventID"),
            "LegislationEventTypeID": obj.get("LegislationEventTypeID"),
            "EventCode": obj.get("EventCode"),
            "EventDate": obj.get("EventDate"),
            "DeletionDate": obj.get("DeletionDate"),
            "Description": obj.get("Description"),
            "LegislationID": obj.get("LegislationID"),
            "VoteID": obj.get("VoteID"),
            "EffectiveType": obj.get("EffectiveType"),
            "EffectiveTypeID": obj.get("EffectiveTypeID"),
            "LegislationNumber": obj.get("LegislationNumber"),
            "ChamberCode": obj.get("ChamberCode"),
            "Sequence": obj.get("Sequence"),
            "SessionCode": obj.get("SessionCode"),
            "IsPublic": obj.get("IsPublic"),
            "IsPassed": obj.get("IsPassed"),
            "LegislationStatusID": obj.get("LegislationStatusID"),
            "ReferenceID": obj.get("ReferenceID"),
            "ReferenceNumber": obj.get("ReferenceNumber"),
            "ReferenceTypeID": obj.get("ReferenceTypeID"),
            "ReferenceType": obj.get("ReferenceType"),
            "Status": obj.get("Status"),
            "ActorID": obj.get("ActorID"),
            "ActorType": obj.get("ActorType"),
            "EventReferences": [PublicEventReferenceResponse.from_dict(_item) for _item in obj["EventReferences"]] if obj.get("EventReferences") is not None else None
        })
        return _obj


