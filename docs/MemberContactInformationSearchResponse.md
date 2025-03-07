# MemberContactInformationSearchResponse

Information for a Member Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Unique identifier for this Member | [optional] 
**identity_id** | **int** | Unique identifier for Identity | [optional] 
**member_number** | **str** | Member number (e.g. H289) | [optional] 
**full_name** | **str** | Member Full Name | [optional] 
**first_name** | **str** | Member First Name | [optional] 
**middle_name** | **str** | Member Middle Name | [optional] 
**last_name** | **str** | Member Last Name | [optional] 
**member_display_name** | **str** | Member Display Name | [optional] 
**room_number** | **str** | Member Room number | [optional] 
**is_public** | **bool** | Is this Member public ? | [optional] 
**gab_phone_number** | **str** | General Assembly Phone # | [optional] 
**gab_email_address** | **str** | General Assembly Email Address | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**chamber** | **str** | Chamber name | [optional] 
**party_code** | **str** | Political party (R/D/I) | [optional] 
**party_name** | **str** | Political party name | [optional] 
**district_id** | **int** | Unique identifier for District | [optional] 
**district_name** | **str** | District name (e.g. 17th) | [optional] 
**member_status_id** | **int** | Unique identifier for Member Status | [optional] 
**member_status** | **str** | Member Status name | [optional] 
**service_begin_date** | **datetime** | Begin date of Service | [optional] 
**service_end_date** | **datetime** | End date of Service (removal date) | [optional] 
**service_end_reason** | **str** | Member Service End Reason | [optional] 
**contact_information** | [**List[ContactResponse]**](ContactResponse.md) | List of Contact Information | [optional] 

## Example

```python
from valis.models.member_contact_information_search_response import MemberContactInformationSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberContactInformationSearchResponse from a JSON string
member_contact_information_search_response_instance = MemberContactInformationSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MemberContactInformationSearchResponse.to_json())

# convert the object into a dict
member_contact_information_search_response_dict = member_contact_information_search_response_instance.to_dict()
# create an instance of MemberContactInformationSearchResponse from a dict
member_contact_information_search_response_from_dict = MemberContactInformationSearchResponse.from_dict(member_contact_information_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


