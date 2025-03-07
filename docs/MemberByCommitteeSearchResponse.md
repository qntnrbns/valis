# MemberByCommitteeSearchResponse

Search information for a Member by Committee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_member_id** | **int** | Unique identifier for this Committee Member | [optional] 
**committee_id** | **int** | Unique identifier for this Committee | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**member_id** | **int** | Unique identifier for Member | [optional] 
**member_display_name** | **str** | Member&#39;s Name to be displayed | [optional] 
**patron_display_name** | **str** | Patron Display Name | [optional] 
**voting_sequence** | **int** | Member voting order | [optional] 
**seniority** | **int** | Member seniority ranking | [optional] 
**committee_role_id** | **int** | Unique identifier for Committee Role | [optional] 
**committee_role_title** | **str** | Committee Role title | [optional] 
**assign_date** | **datetime** | Assignment date | [optional] 
**remove_date** | **datetime** | Removal date | [optional] 
**is_public** | **bool** | Is this Member by Committee public? | [optional] 
**member_number** | **str** | Member number (e.g. H289) | [optional] 

## Example

```python
from valis.models.member_by_committee_search_response import MemberByCommitteeSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberByCommitteeSearchResponse from a JSON string
member_by_committee_search_response_instance = MemberByCommitteeSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MemberByCommitteeSearchResponse.to_json())

# convert the object into a dict
member_by_committee_search_response_dict = member_by_committee_search_response_instance.to_dict()
# create an instance of MemberByCommitteeSearchResponse from a dict
member_by_committee_search_response_from_dict = MemberByCommitteeSearchResponse.from_dict(member_by_committee_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


