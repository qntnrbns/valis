# File

Legislation Version File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_id** | **int** | Legislation Text ID | [optional] 
**text_format_id** | **int** | Text Format ID | [optional] 
**text_format** | **str** | Text Format | [optional] 
**file_url** | **str** | File URL | [optional] 

## Example

```python
from valis.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


