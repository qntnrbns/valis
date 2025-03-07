# PublicLegislationEventResponse

Information for a public Legislation Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_event_id** | **int** | Legislation event unique identifier | [optional] 
**legislation_event_type_id** | **int** | Legislation Event Type Identifer (Unique for each Biennial) | [optional] 
**event_code** | **str** | Event Code (can be used in place of Legislation Event Type ID) | [optional] 
**event_date** | **datetime** | The Date the Event occurred | [optional] 
**deletion_date** | **datetime** | The Date the Event is Deleted | [optional] 
**description** | **str** | Legislation Description | [optional] 
**legislation_id** | **int** | Legislation Identifier | [optional] 
**vote_id** | **int** | VoteID | [optional] 
**effective_type** | **str** | Determines whether the enaction of the legislation is standard, emergency, or other | [optional] 
**effective_type_id** | **int** | ID of EffectiveType. | [optional] 
**legislation_number** | **str** | Human Readable Legislation Identifier | [optional] 
**chamber_code** | **str** | Chamber Code | [optional] 
**sequence** | **int** | Sequence | [optional] 
**session_code** | **str** | Human readable code for the Session that the event happened in | [optional] 
**is_public** | **bool** | Is Public Event | [optional] 
**is_passed** | **bool** | Has Event Passed? | [optional] 
**legislation_status_id** | **int** | Unique Identifier for Legislation Event Status | [optional] 
**reference_id** | **str** | Originating System code used for identifying this Event in that system | [optional] 
**reference_number** | **str** | Originating system number (e.g. Vote #, LD #, Committee #) that correlates with the ReferenceType | [optional] 
**reference_type_id** | **int** | unique identifier for the ReferenceType | [optional] 
**reference_type** | **str** | name for ReferenceType (e.g. LegislationText, Vote, Committee, Minutes) | [optional] 
**status** | **str** | Status Name | [optional] 
**actor_id** | **int** | unique identifier for the ActorType | [optional] 
**actor_type** | **str** | The subject taking the event action (i.e House/Senate/Conference/Governor) | [optional] 
**event_references** | [**List[PublicEventReferenceResponse]**](PublicEventReferenceResponse.md) | List of public Event References | [optional] 

## Example

```python
from valis.models.public_legislation_event_response import PublicLegislationEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicLegislationEventResponse from a JSON string
public_legislation_event_response_instance = PublicLegislationEventResponse.from_json(json)
# print the JSON string representation of the object
print(PublicLegislationEventResponse.to_json())

# convert the object into a dict
public_legislation_event_response_dict = public_legislation_event_response_instance.to_dict()
# create an instance of PublicLegislationEventResponse from a dict
public_legislation_event_response_from_dict = PublicLegislationEventResponse.from_dict(public_legislation_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


