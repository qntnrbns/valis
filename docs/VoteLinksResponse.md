# VoteLinksResponse

List of Vote Links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[VoteLinkResponse]**](VoteLinkResponse.md) | list of Vote Links | [optional] 

## Example

```python
from valis.models.vote_links_response import VoteLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteLinksResponse from a JSON string
vote_links_response_instance = VoteLinksResponse.from_json(json)
# print the JSON string representation of the object
print(VoteLinksResponse.to_json())

# convert the object into a dict
vote_links_response_dict = vote_links_response_instance.to_dict()
# create an instance of VoteLinksResponse from a dict
vote_links_response_from_dict = VoteLinksResponse.from_dict(vote_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


