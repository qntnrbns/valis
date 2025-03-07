# PublicMemberResponse

Public information for a Member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Unique identifier for this Member | [optional] 
**identity_id** | **int** | Unique identifier for Identity | [optional] 
**member_detail_id** | **int** | Unique identifier for Member Detail | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**member_number** | **str** | Member number (e.g. H289) | [optional] 
**list_display_name** | **str** | Member&#39;s Name to be displayed for List purposes | [optional] 
**member_display_name** | **str** | Member&#39;s Name to be displayed | [optional] 
**patron_display_name** | **str** | Patron Display Name | [optional] 
**salutation** | **str** | Member Salutation | [optional] 
**service_begin_date** | **datetime** | Begin date of Service for this Member | [optional] 
**service_end_date** | **datetime** | End date of Service for this Member | [optional] 
**last_election_date** | **datetime** | Last election date for this Member | [optional] 
**room_number** | **str** | Member Room number | [optional] 
**service_end_reason** | **str** | Member Service End Reason | [optional] 
**gab_phone_number** | **str** | General Assembly Phone # | [optional] 
**gab_email_address** | **str** | General Assembly Email Address | [optional] 
**seat_number** | **int** | Member chamber floor seat number | [optional] 
**seniority** | **int** | Member seniority ranking | [optional] 
**voting_sequence** | **int** | Member voting order | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**chamber_name** | **str** | Chamber Name | [optional] 
**district_id** | **int** | Unique identifier for District | [optional] 
**district_name** | **str** | District name | [optional] 
**party_code** | **str** | Political party (R/D/I) | [optional] 
**member_status_id** | **int** | Unique identifier for Member Status | [optional] 
**member_status** | **str** | Member Status name | [optional] 
**status_reason** | **str** | Member status reason | [optional] 
**is_public** | **bool** | Is this Member public ? | [optional] 

## Example

```python
from valis.models.public_member_response import PublicMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMemberResponse from a JSON string
public_member_response_instance = PublicMemberResponse.from_json(json)
# print the JSON string representation of the object
print(PublicMemberResponse.to_json())

# convert the object into a dict
public_member_response_dict = public_member_response_instance.to_dict()
# create an instance of PublicMemberResponse from a dict
public_member_response_from_dict = PublicMemberResponse.from_dict(public_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


