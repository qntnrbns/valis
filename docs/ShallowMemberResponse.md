# ShallowMemberResponse

Shallow information for member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Unique identifier for this Member | [optional] 
**identity_id** | **int** | Unique identifier for Identity | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**member_number** | **str** | Member&#39;s assigned Number | [optional] 
**list_display_name** | **str** | Member&#39;s Name to be displayed for List purposes | [optional] 
**member_display_name** | **str** | Member&#39;s Name to be displayed | [optional] 
**patron_display_name** | **str** | Member&#39;s Patron Display Name | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**party_code** | **str** | Political party (R/D/I) | [optional] 
**member_status_id** | **int** | Unique identifier for Member Status | [optional] 
**member_status** | **str** | Member Status name | [optional] 
**service_begin_date** | **datetime** | Member&#39;s beginning service date (assignment date) | [optional] 
**service_end_date** | **datetime** | Member&#39;s ending service date (removal date) | [optional] 
**service_end_reason** | **str** | Member Service End Reason | [optional] 
**gab_phone_number** | **str** | General Assembly Phone # | [optional] 
**gab_email_address** | **str** | General Assembly Email Address | [optional] 
**is_public** | **bool** | Is this Member public ? | [optional] 

## Example

```python
from valis.models.shallow_member_response import ShallowMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShallowMemberResponse from a JSON string
shallow_member_response_instance = ShallowMemberResponse.from_json(json)
# print the JSON string representation of the object
print(ShallowMemberResponse.to_json())

# convert the object into a dict
shallow_member_response_dict = shallow_member_response_instance.to_dict()
# create an instance of ShallowMemberResponse from a dict
shallow_member_response_from_dict = ShallowMemberResponse.from_dict(shallow_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


