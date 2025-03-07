# CalendarsPublicListGetResponse

Calendars Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CalendarPublicListGetResponse]**](CalendarPublicListGetResponse.md) | list of Calendars | [optional] 

## Example

```python
from valis.models.calendars_public_list_get_response import CalendarsPublicListGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarsPublicListGetResponse from a JSON string
calendars_public_list_get_response_instance = CalendarsPublicListGetResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarsPublicListGetResponse.to_json())

# convert the object into a dict
calendars_public_list_get_response_dict = calendars_public_list_get_response_instance.to_dict()
# create an instance of CalendarsPublicListGetResponse from a dict
calendars_public_list_get_response_from_dict = CalendarsPublicListGetResponse.from_dict(calendars_public_list_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


