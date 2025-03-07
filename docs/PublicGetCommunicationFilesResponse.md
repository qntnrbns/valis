# PublicGetCommunicationFilesResponse

List of Public Communication Files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicCommunicationFile]**](PublicCommunicationFile.md) | List of Public Communication Files | [optional] 

## Example

```python
from valis.models.public_get_communication_files_response import PublicGetCommunicationFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGetCommunicationFilesResponse from a JSON string
public_get_communication_files_response_instance = PublicGetCommunicationFilesResponse.from_json(json)
# print the JSON string representation of the object
print(PublicGetCommunicationFilesResponse.to_json())

# convert the object into a dict
public_get_communication_files_response_dict = public_get_communication_files_response_instance.to_dict()
# create an instance of PublicGetCommunicationFilesResponse from a dict
public_get_communication_files_response_from_dict = PublicGetCommunicationFilesResponse.from_dict(public_get_communication_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


