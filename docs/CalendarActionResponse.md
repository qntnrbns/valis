# CalendarActionResponse

Calendar Action Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_action_id** | **int** | Calendar Action unique identifier | 
**vote_description** | **str** | Vote Description | 
**description** | **str** | Calendar Action Description | 
**event_code** | **str** | Corresponding Event Code | [optional] 
**chamber_code** | **str** | Chamber Code | [optional] 
**category_code** | **str** | Category Code | [optional] 
**calendar_category_type_id** | **int** | Calendar Category Type ID | [optional] 
**legislation_chamber_code** | **str** | Legislation Chamber Code | [optional] 
**is_passed** | **bool** | Has Action Passed? | [optional] 
**in_preview** | **bool** | If not set, will not show for preview/generation purposes | [optional] 
**action_references** | [**List[CalendarActionReferenceResponse]**](CalendarActionReferenceResponse.md) | optional list of Action References | [optional] 

## Example

```python
from valis.models.calendar_action_response import CalendarActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarActionResponse from a JSON string
calendar_action_response_instance = CalendarActionResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarActionResponse.to_json())

# convert the object into a dict
calendar_action_response_dict = calendar_action_response_instance.to_dict()
# create an instance of CalendarActionResponse from a dict
calendar_action_response_from_dict = CalendarActionResponse.from_dict(calendar_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


