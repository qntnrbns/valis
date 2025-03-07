# VoteItemResponse

Information for a Vote Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ld_number** | **str** | Legislation LD # | [optional] 
**legislation_version_id** | **int** | Unique identifier for Legislation VersionID | [optional] 
**legislation_version** | **str** | Legislation Version name | [optional] 
**legislation_text_id** | **int** | Unique identifier for Legislation Text | [optional] 
**document_code** | **str** | Document Code | [optional] 
**description** | **str** | Legislation description | [optional] 
**committee_id** | **int** | Unique identifier for Committee | [optional] 

## Example

```python
from valis.models.vote_item_response import VoteItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteItemResponse from a JSON string
vote_item_response_instance = VoteItemResponse.from_json(json)
# print the JSON string representation of the object
print(VoteItemResponse.to_json())

# convert the object into a dict
vote_item_response_dict = vote_item_response_instance.to_dict()
# create an instance of VoteItemResponse from a dict
vote_item_response_from_dict = VoteItemResponse.from_dict(vote_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


