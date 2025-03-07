# PublicVoteFile

Information for a Public Vote File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_file_id** | **int** | Unique identifier for Vote File | [optional] 
**vote_id** | **int** | Unique identifier for Vote | [optional] 
**file_url** | **str** | File URL | [optional] 
**text_format_id** | **str** | Unique identifier for Text Format | [optional] 
**is_generated** | **bool** | Has the file been generated yet? | [optional] 
**is_active** | **bool** | is it active? | [optional] 

## Example

```python
from valis.models.public_vote_file import PublicVoteFile

# TODO update the JSON string below
json = "{}"
# create an instance of PublicVoteFile from a JSON string
public_vote_file_instance = PublicVoteFile.from_json(json)
# print the JSON string representation of the object
print(PublicVoteFile.to_json())

# convert the object into a dict
public_vote_file_dict = public_vote_file_instance.to_dict()
# create an instance of PublicVoteFile from a dict
public_vote_file_from_dict = PublicVoteFile.from_dict(public_vote_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


