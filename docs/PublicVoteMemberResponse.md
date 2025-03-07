# PublicVoteMemberResponse

A Vote Member Vote Class   could be obtained, Success boolean will be false and additional information can be found   in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_member_id** | **int** | VoteMember unique identifier | [optional] 
**member_id** | **int** | Member unique identifier | [optional] 
**member_display_name** | **str** | Member Display Name | [optional] 
**patron_display_name** | **str** | PatronDisplayName | [optional] 
**member_number** | **str** | Member Number | [optional] 
**response_code** | **str** | Response Code | [optional] 
**vote_statement** | **str** | Vote Statement | [optional] 
**voting_sequence** | **int** | VoteMember sequence | [optional] 

## Example

```python
from valis.models.public_vote_member_response import PublicVoteMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicVoteMemberResponse from a JSON string
public_vote_member_response_instance = PublicVoteMemberResponse.from_json(json)
# print the JSON string representation of the object
print(PublicVoteMemberResponse.to_json())

# convert the object into a dict
public_vote_member_response_dict = public_vote_member_response_instance.to_dict()
# create an instance of PublicVoteMemberResponse from a dict
public_vote_member_response_from_dict = PublicVoteMemberResponse.from_dict(public_vote_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


