# CommitteeByMemberResponse

Information for a Committee associated to a member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_committee_id** | **int** | Unique identifier for parent Committee | [optional] 
**committee_id** | **int** | Unique identifier for this Committee | [optional] 
**name** | **str** | Committee name | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**committee_number** | **str** | Committee number (e.g. S10) | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 

## Example

```python
from valis.models.committee_by_member_response import CommitteeByMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeByMemberResponse from a JSON string
committee_by_member_response_instance = CommitteeByMemberResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteeByMemberResponse.to_json())

# convert the object into a dict
committee_by_member_response_dict = committee_by_member_response_instance.to_dict()
# create an instance of CommitteeByMemberResponse from a dict
committee_by_member_response_from_dict = CommitteeByMemberResponse.from_dict(committee_by_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


