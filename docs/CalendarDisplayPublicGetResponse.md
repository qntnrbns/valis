# CalendarDisplayPublicGetResponse

Calendar Display Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_column** | **str** | Display Column | [optional] 
**is_displayed** | **bool** | Is Displayed | [optional] 

## Example

```python
from valis.models.calendar_display_public_get_response import CalendarDisplayPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarDisplayPublicGetResponse from a JSON string
calendar_display_public_get_response_instance = CalendarDisplayPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarDisplayPublicGetResponse.to_json())

# convert the object into a dict
calendar_display_public_get_response_dict = calendar_display_public_get_response_instance.to_dict()
# create an instance of CalendarDisplayPublicGetResponse from a dict
calendar_display_public_get_response_from_dict = CalendarDisplayPublicGetResponse.from_dict(calendar_display_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


