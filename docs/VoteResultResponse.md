# VoteResultResponse

Information for a Vote Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_id** | **int** | Unique identifier for a Vote | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**committee_id** | **int** | Unique identifier for Committee | [optional] 
**committee_name** | **str** | Committee Name | [optional] 
**vote_number** | **str** | Vote assigned number (e.g. H12V0164/S03V0170) | [optional] 
**session_id** | **int** | Unique identifier for Session | [optional] 
**vote_date** | **datetime** | Vote date | [optional] 
**sequence** | **int** | Sequence results | [optional] 
**vote_type_id** | **int** | Unique identifier for Vote Type | [optional] 
**vote_type** | **str** | Vote Type name | [optional] 
**vote_classification_id** | **int** | Unique identifier for Vote Classification | [optional] 
**classification_name** | **str** | Vote Classification name | [optional] 
**batch_number** | **str** | Vote batch number | [optional] 
**vote_description** | **str** | Vote description | [optional] 
**vote_action_id** | **int** | Unique identifier for Vote Action | [optional] 
**action_description** | **str** | Vote Action description | [optional] 
**pass_fail** | **str** | Vote Pass/Fail | [optional] 
**response_code** | **str** | Vote Response Code | [optional] 
**vote_statement** | **str** | Vote Statement | [optional] 
**vote_legislation_id** | **int** | Unique identifier for Vote Legislation | [optional] 
**legislation_id** | **int** | Unique identifier for Legislation | [optional] 
**legislation_number** | **str** | Legislation number | [optional] 
**legislation_description** | **str** | Legislation description | [optional] 

## Example

```python
from valis.models.vote_result_response import VoteResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteResultResponse from a JSON string
vote_result_response_instance = VoteResultResponse.from_json(json)
# print the JSON string representation of the object
print(VoteResultResponse.to_json())

# convert the object into a dict
vote_result_response_dict = vote_result_response_instance.to_dict()
# create an instance of VoteResultResponse from a dict
vote_result_response_from_dict = VoteResultResponse.from_dict(vote_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


