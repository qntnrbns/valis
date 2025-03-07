# CalendarCategoryTypesResponse

Calendar Categories Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CalendarCategoryTypeResponse]**](CalendarCategoryTypeResponse.md) | list of Calendar Actions | [optional] 

## Example

```python
from valis.models.calendar_category_types_response import CalendarCategoryTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCategoryTypesResponse from a JSON string
calendar_category_types_response_instance = CalendarCategoryTypesResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarCategoryTypesResponse.to_json())

# convert the object into a dict
calendar_category_types_response_dict = calendar_category_types_response_instance.to_dict()
# create an instance of CalendarCategoryTypesResponse from a dict
calendar_category_types_response_from_dict = CalendarCategoryTypesResponse.from_dict(calendar_category_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


