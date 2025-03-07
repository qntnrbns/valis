# PublicVoteResponse

Information for a Public Vote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_id** | **int** | Unique identifier for Vote | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**committee_id** | **int** | Unique identifier for Committee | [optional] 
**committee_name** | **str** | Committee name | [optional] 
**legislation_number** | **str** | Legislation number | [optional] 
**reference_id** | **int** | Unique identifier for Reference | [optional] 
**reference_number** | **str** | Reference number | [optional] 
**vote_number** | **str** | Vote number | [optional] 
**is_voice** | **bool** | Is it a voice vote? | [optional] 
**is_block** | **bool** | Is it a block vote? | [optional] 
**is_public** | **bool** | Is it public? | [optional] 
**session_id** | **int** | Unique identifier for Session | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**vote_date** | **datetime** | Vote date | 
**sequence** | **int** | Vote Sequence | [optional] 
**vote_type_id** | **int** | Unique identifier for Vote Type | [optional] 
**vote_type** | **str** | Vote Type name | [optional] 
**batch_number** | **str** | Vote Batch number | [optional] 
**description** | **str** | Vote description | [optional] 
**vote_tally** | **str** | Vote Tally | [optional] 
**vote_room_id** | **int** | Unique identifier for Vote Room | [optional] 
**room_description** | **str** | Room description | [optional] 
**event_code** | **str** | Event Code (motion code / history action) | [optional] 
**vote_action_description** | **str** | Vote Action description | [optional] 
**vote_action_id** | **int** | Unique identifier for Vote Action | [optional] 
**vote_classification_id** | **int** | Unique identifier for Vote Classification | [optional] 
**refer_to_committee_id** | **int** | Unique identifier for Refer to Committee | [optional] 
**refer_to_committee_number** | **str** | Refer to Committee number | [optional] 
**classification_name** | **str** | Vote Classification name | [optional] 
**is_unanimous** | **bool** | Is the vote unanimous? | [optional] 
**legislation_action_description** | **str** | Bill Action description | [optional] 
**parent_committee_id** | **int** | Unique identifier for Parent Committee | [optional] 
**parent_committee_name** | **str** | Parent Committee name | [optional] 
**vote_legislation** | [**List[PublicVoteLegislationResponse]**](PublicVoteLegislationResponse.md) | List of Vote Legislation | [optional] 
**vote_member** | [**List[PublicVoteMemberResponse]**](PublicVoteMemberResponse.md) | List of Public Member Votes | [optional] 
**vote_files** | [**List[PublicVoteFile]**](PublicVoteFile.md) | List of Public Vote Files | [optional] 

## Example

```python
from valis.models.public_vote_response import PublicVoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicVoteResponse from a JSON string
public_vote_response_instance = PublicVoteResponse.from_json(json)
# print the JSON string representation of the object
print(PublicVoteResponse.to_json())

# convert the object into a dict
public_vote_response_dict = public_vote_response_instance.to_dict()
# create an instance of PublicVoteResponse from a dict
public_vote_response_from_dict = PublicVoteResponse.from_dict(public_vote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


