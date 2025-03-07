# PublicCommitteeFileResponse

Information for Public Committee File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **int** | Unique Identifier for Committee | [optional] 
**file_url** | **str** | File URL | [optional] 
**text_format_id** | **int** | Unique identifier for Text Format | [optional] 
**is_generated** | **bool** | Is this generated? | [optional] 
**is_public** | **bool** | is this public? | [optional] 
**is_active** | **bool** | is this active? | [optional] 
**description** | **str** | Link description | [optional] 
**committee_file_id** | **int** | Unique identifier for Committee File | [optional] 

## Example

```python
from valis.models.public_committee_file_response import PublicCommitteeFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCommitteeFileResponse from a JSON string
public_committee_file_response_instance = PublicCommitteeFileResponse.from_json(json)
# print the JSON string representation of the object
print(PublicCommitteeFileResponse.to_json())

# convert the object into a dict
public_committee_file_response_dict = public_committee_file_response_instance.to_dict()
# create an instance of PublicCommitteeFileResponse from a dict
public_committee_file_response_from_dict = PublicCommitteeFileResponse.from_dict(public_committee_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


