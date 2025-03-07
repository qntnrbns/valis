# StaffPartnerGetResponse

Staff Partner Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staff_id** | **int** | Database Unique Indentifier for Staff | [optional] 
**affiliation_id** | **int** | Database Unique Indentifier for Affiliation | [optional] 
**staff_role_type_id** | **int** | Database Unique Indentifier for Staff Role Type | [optional] 
**identity_id** | **int** | Database Unique Indentifier for Identity | [optional] 
**full_name** | **str** | Staff Full Name | [optional] 
**sequence** | **int** | Staff Sequence | [optional] 
**is_public** | **bool** | Is Staff Public Viewable | [optional] 
**effective_date** | **datetime** | Staff Effective Date | [optional] 
**modification_date** | **datetime** | Modification Date | [optional] 

## Example

```python
from valis.models.staff_partner_get_response import StaffPartnerGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaffPartnerGetResponse from a JSON string
staff_partner_get_response_instance = StaffPartnerGetResponse.from_json(json)
# print the JSON string representation of the object
print(StaffPartnerGetResponse.to_json())

# convert the object into a dict
staff_partner_get_response_dict = staff_partner_get_response_instance.to_dict()
# create an instance of StaffPartnerGetResponse from a dict
staff_partner_get_response_from_dict = StaffPartnerGetResponse.from_dict(staff_partner_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


