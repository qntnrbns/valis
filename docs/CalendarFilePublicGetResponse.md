# CalendarFilePublicGetResponse

CalendarFilePublicGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_file_id** | **int** | Database Unique Identifier for Files | [optional] 
**calendar_id** | **int** | Database Unique Identifier for Calendar/Docket/Agenda | [optional] 
**file_url** | **str** | File URL | [optional] 
**text_format_id** | **int** | Unique Identifier for Text format ID | 
**is_generated** | **bool** | File Generated | [optional] 
**is_public** | **bool** | File Public | [optional] 
**is_active** | **bool** | File Active | [optional] 

## Example

```python
from valis.models.calendar_file_public_get_response import CalendarFilePublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarFilePublicGetResponse from a JSON string
calendar_file_public_get_response_instance = CalendarFilePublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarFilePublicGetResponse.to_json())

# convert the object into a dict
calendar_file_public_get_response_dict = calendar_file_public_get_response_instance.to_dict()
# create an instance of CalendarFilePublicGetResponse from a dict
calendar_file_public_get_response_from_dict = CalendarFilePublicGetResponse.from_dict(calendar_file_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


