# VoteMemberPublicGetResponse

Public Agenda Item response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Database Unique Identifier for Member | [optional] 
**member_number** | **str** | Member Number | [optional] 
**member_display_name** | **str** | Member Display Name | [optional] 
**patron_display_name** | **str** | Patron Display Name | [optional] 
**response_code** | **str** | Response Code | [optional] 
**vote_member_id** | **int** | Vote Member ID | [optional] 

## Example

```python
from valis.models.vote_member_public_get_response import VoteMemberPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteMemberPublicGetResponse from a JSON string
vote_member_public_get_response_instance = VoteMemberPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(VoteMemberPublicGetResponse.to_json())

# convert the object into a dict
vote_member_public_get_response_dict = vote_member_public_get_response_instance.to_dict()
# create an instance of VoteMemberPublicGetResponse from a dict
vote_member_public_get_response_from_dict = VoteMemberPublicGetResponse.from_dict(vote_member_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


