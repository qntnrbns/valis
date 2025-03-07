# CalendarFileBaseModel

Base Model for Calendar Files

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
from valis.models.calendar_file_base_model import CalendarFileBaseModel

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarFileBaseModel from a JSON string
calendar_file_base_model_instance = CalendarFileBaseModel.from_json(json)
# print the JSON string representation of the object
print(CalendarFileBaseModel.to_json())

# convert the object into a dict
calendar_file_base_model_dict = calendar_file_base_model_instance.to_dict()
# create an instance of CalendarFileBaseModel from a dict
calendar_file_base_model_from_dict = CalendarFileBaseModel.from_dict(calendar_file_base_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


