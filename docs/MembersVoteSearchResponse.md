# MembersVoteSearchResponse

List of Member Votes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[MemberVoteSearchResponse]**](MemberVoteSearchResponse.md) | list of Member Votes | [optional] 

## Example

```python
from valis.models.members_vote_search_response import MembersVoteSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembersVoteSearchResponse from a JSON string
members_vote_search_response_instance = MembersVoteSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MembersVoteSearchResponse.to_json())

# convert the object into a dict
members_vote_search_response_dict = members_vote_search_response_instance.to_dict()
# create an instance of MembersVoteSearchResponse from a dict
members_vote_search_response_from_dict = MembersVoteSearchResponse.from_dict(members_vote_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


