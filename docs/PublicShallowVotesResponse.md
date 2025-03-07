# PublicShallowVotesResponse

List of public Shallow Votes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicShallowVoteResponse]**](PublicShallowVoteResponse.md) | list of public Shallow Votes | [optional] 

## Example

```python
from valis.models.public_shallow_votes_response import PublicShallowVotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicShallowVotesResponse from a JSON string
public_shallow_votes_response_instance = PublicShallowVotesResponse.from_json(json)
# print the JSON string representation of the object
print(PublicShallowVotesResponse.to_json())

# convert the object into a dict
public_shallow_votes_response_dict = public_shallow_votes_response_instance.to_dict()
# create an instance of PublicShallowVotesResponse from a dict
public_shallow_votes_response_from_dict = PublicShallowVotesResponse.from_dict(public_shallow_votes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


