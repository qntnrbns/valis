# PublicCommunicationFile

Information for a Public Communication File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_file_id** | **int** | Unique identifier for Communication File | [optional] 
**communication_id** | **int** | Unique identifier for Communication | [optional] 
**file_url** | **str** | File URL | [optional] 
**text_format_id** | **int** | Unique identifier for Text Format | [optional] 
**is_generated** | **bool** | Is this generated? | [optional] 
**is_public** | **bool** | Is this public? | [optional] 
**is_active** | **bool** | Is this active? | [optional] 

## Example

```python
from valis.models.public_communication_file import PublicCommunicationFile

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCommunicationFile from a JSON string
public_communication_file_instance = PublicCommunicationFile.from_json(json)
# print the JSON string representation of the object
print(PublicCommunicationFile.to_json())

# convert the object into a dict
public_communication_file_dict = public_communication_file_instance.to_dict()
# create an instance of PublicCommunicationFile from a dict
public_communication_file_from_dict = PublicCommunicationFile.from_dict(public_communication_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


