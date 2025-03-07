# CalendarActionReferenceResponse

Calendar Action \"Action Reference\" Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_reference_id** | **int** | Calendar Action unique identifier | 
**is_mandatory** | **bool** | is this action reference required? true/false | [optional] 
**sequence** | **int** | Sequence for action reference | [optional] 
**reference_text** | **str** | reference text for the action reference, e.g. \&quot;On Motion Of \&quot; | [optional] 
**calendar_action_id** | **int** | unique identifier for associated calendar action | [optional] 
**action_reference_type_id** | **int** | unique identifier for associated action reference type | [optional] 
**action_reference_type** | **str** | name for for associated action reference type e.g. Member | [optional] 

## Example

```python
from valis.models.calendar_action_reference_response import CalendarActionReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarActionReferenceResponse from a JSON string
calendar_action_reference_response_instance = CalendarActionReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarActionReferenceResponse.to_json())

# convert the object into a dict
calendar_action_reference_response_dict = calendar_action_reference_response_instance.to_dict()
# create an instance of CalendarActionReferenceResponse from a dict
calendar_action_reference_response_from_dict = CalendarActionReferenceResponse.from_dict(calendar_action_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


