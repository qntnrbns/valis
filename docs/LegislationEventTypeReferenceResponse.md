# LegislationEventTypeReferenceResponse

Response object containing LIS Legislation events reference information.  Note: For Internal Use Only

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_event_type_id** | **int** | Legislation Event Type unique identifier | [optional] 
**event_code** | **str** | Event Code | [optional] 
**legislation_description** | **str** | Description for Legislation usage | [optional] 
**committee_description** | **str** | Description for Committee usage | [optional] 
**calendar_description** | **str** | Description for Calendar usage | [optional] 
**journal_description** | **str** | Description for Journal usage | [optional] 
**vote_description** | **str** | Description for Vote usage | [optional] 
**legislation_chamber_code** | **str** | Legislation Chamber Code | [optional] 
**actor_type_id** | **int** | Actor Type Identifier | [optional] 
**is_public** | **bool** | Is Public Event Type | [optional] 
**is_active** | **bool** | Is Active Event Type | [optional] 
**committee_complete** | **bool** | Is Committee Complete | [optional] 
**is_passed** | **bool** | Has Event Passed? | [optional] 
**action_references** | [**List[CalendarActionReferenceResponse]**](CalendarActionReferenceResponse.md) | optional list of Action References | [optional] 

## Example

```python
from valis.models.legislation_event_type_reference_response import LegislationEventTypeReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationEventTypeReferenceResponse from a JSON string
legislation_event_type_reference_response_instance = LegislationEventTypeReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationEventTypeReferenceResponse.to_json())

# convert the object into a dict
legislation_event_type_reference_response_dict = legislation_event_type_reference_response_instance.to_dict()
# create an instance of LegislationEventTypeReferenceResponse from a dict
legislation_event_type_reference_response_from_dict = LegislationEventTypeReferenceResponse.from_dict(legislation_event_type_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


