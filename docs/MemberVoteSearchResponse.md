# MemberVoteSearchResponse

Information for a Member Vote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Unique identifier for this Member | [optional] 
**member_number** | **str** | Member number (e.g. H289) | [optional] 
**member_display_name** | **str** | Member Display Name | [optional] 
**patron_display_name** | **str** | Patron Display Name | [optional] 
**vote_result** | [**List[VoteResultResponse]**](VoteResultResponse.md) | list of Vote Results | [optional] 

## Example

```python
from valis.models.member_vote_search_response import MemberVoteSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberVoteSearchResponse from a JSON string
member_vote_search_response_instance = MemberVoteSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MemberVoteSearchResponse.to_json())

# convert the object into a dict
member_vote_search_response_dict = member_vote_search_response_instance.to_dict()
# create an instance of MemberVoteSearchResponse from a dict
member_vote_search_response_from_dict = MemberVoteSearchResponse.from_dict(member_vote_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


