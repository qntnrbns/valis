# CalendarTypesResponse

Calendars Types Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CalendarTypeResponse]**](CalendarTypeResponse.md) | list of Calendar Actions | [optional] 

## Example

```python
from valis.models.calendar_types_response import CalendarTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarTypesResponse from a JSON string
calendar_types_response_instance = CalendarTypesResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarTypesResponse.to_json())

# convert the object into a dict
calendar_types_response_dict = calendar_types_response_instance.to_dict()
# create an instance of CalendarTypesResponse from a dict
calendar_types_response_from_dict = CalendarTypesResponse.from_dict(calendar_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


