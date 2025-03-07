# CommitteeMemberPartnerGetResponse

Partner Get for Committee Member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_member_id** | **int** | Database Unique Identifier for Committee Member Relationship | [optional] 
**committee_id** | **int** | Database Unique Identifier for Committee | [optional] 
**committee_number** | **str** | Committee Number | [optional] 
**member_id** | **int** | Database Unique Identifier for Member | [optional] 
**member_number** | **str** | Member Number | [optional] 
**member_display_name** | **str** | Member Display Name | [optional] 
**patron_display_name** | **str** | Patron Display Name | [optional] 
**party_code** | **str** | Party Code | [optional] 
**voting_sequence** | **int** | Voting Sequence | [optional] 
**display_sequence** | **int** | Display Sequence | [optional] 
**committee_role_id** | **int** | Database Unique Identifier for Committee Role ID | [optional] 
**title** | **str** | Member Title | [optional] 
**effective_date** | **datetime** | Effective Date | [optional] 
**is_public** | **bool** | Is Member Public | [optional] 

## Example

```python
from valis.models.committee_member_partner_get_response import CommitteeMemberPartnerGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeMemberPartnerGetResponse from a JSON string
committee_member_partner_get_response_instance = CommitteeMemberPartnerGetResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteeMemberPartnerGetResponse.to_json())

# convert the object into a dict
committee_member_partner_get_response_dict = committee_member_partner_get_response_instance.to_dict()
# create an instance of CommitteeMemberPartnerGetResponse from a dict
committee_member_partner_get_response_from_dict = CommitteeMemberPartnerGetResponse.from_dict(committee_member_partner_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


