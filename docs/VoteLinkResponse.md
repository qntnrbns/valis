# VoteLinkResponse

Information for a Vote Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_id** | **int** | unique identifier for Vote | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | 
**committee_id** | **int** | unique identifier for Committee | [optional] 
**parent_committee_id** | **int** | unique identifier for parent Committee | [optional] 
**vote_file_id** | **int** | unique identifier for Vote File | [optional] 
**reference_type** | **str** | Reference type | [optional] 
**reference_id** | **int** | Unique identifier for Reference | [optional] 
**session_id** | **int** | Unique identifier for Session | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**is_public** | **bool** | Is Public? | [optional] 
**file_url** | **str** | File URL | [optional] 

## Example

```python
from valis.models.vote_link_response import VoteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteLinkResponse from a JSON string
vote_link_response_instance = VoteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(VoteLinkResponse.to_json())

# convert the object into a dict
vote_link_response_dict = vote_link_response_instance.to_dict()
# create an instance of VoteLinkResponse from a dict
vote_link_response_from_dict = VoteLinkResponse.from_dict(vote_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


