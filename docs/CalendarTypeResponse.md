# CalendarTypeResponse

Calendar Type Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Description/Name of the ID | [optional] 
**id** | **int** | Category Type unique identifier | [optional] 

## Example

```python
from valis.models.calendar_type_response import CalendarTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarTypeResponse from a JSON string
calendar_type_response_instance = CalendarTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarTypeResponse.to_json())

# convert the object into a dict
calendar_type_response_dict = calendar_type_response_instance.to_dict()
# create an instance of CalendarTypeResponse from a dict
calendar_type_response_from_dict = CalendarTypeResponse.from_dict(calendar_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


