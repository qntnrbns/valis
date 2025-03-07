# PublicVoteLegislationResponse

Information for a Public Vote Legislation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_legislation_id** | **int** | Unique identifier for Vote Legislation | [optional] 
**legislation_id** | **int** | Unique identifier for Legislation | [optional] 
**legislation_number** | **str** | Legislation number | [optional] 
**description** | **str** | Vote description | [optional] 
**vote_number** | **str** | Vote number | [optional] 
**minutes_entry_id** | **int** | Unique identifier for Minutes Entry | [optional] 
**vote_items** | [**List[VoteItemResponse]**](VoteItemResponse.md) | List of Vote Items | [optional] 

## Example

```python
from valis.models.public_vote_legislation_response import PublicVoteLegislationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicVoteLegislationResponse from a JSON string
public_vote_legislation_response_instance = PublicVoteLegislationResponse.from_json(json)
# print the JSON string representation of the object
print(PublicVoteLegislationResponse.to_json())

# convert the object into a dict
public_vote_legislation_response_dict = public_vote_legislation_response_instance.to_dict()
# create an instance of PublicVoteLegislationResponse from a dict
public_vote_legislation_response_from_dict = PublicVoteLegislationResponse.from_dict(public_vote_legislation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


