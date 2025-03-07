# ContactPublicGetResponse

Contact Public Get Response inheriting from Contact Base Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **int** | Unique identifier for Owner | [optional] 
**contact_type_id** | **int** | Unique identifier for Contact Type | [optional] 
**contact_type** | **str** | Contact Type description | [optional] 
**address1** | **str** | Address 1 | [optional] 
**address2** | **str** | Address 2 | [optional] 
**address3** | **str** | Address 3 | [optional] 
**city** | **str** | City | [optional] 
**state_code** | **str** | State | [optional] 
**zip_code** | **str** | Postal/Zip Code | [optional] 
**phone_number** | **str** | Phone Number | [optional] 
**email_address** | **str** | Email Address | [optional] 
**is_active** | **bool** | Is this active? | [optional] 
**is_public** | **bool** | Is this public? | [optional] 
**contact_information_id** | **int** | Contact unique identifier | [optional] 

## Example

```python
from valis.models.contact_public_get_response import ContactPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPublicGetResponse from a JSON string
contact_public_get_response_instance = ContactPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(ContactPublicGetResponse.to_json())

# convert the object into a dict
contact_public_get_response_dict = contact_public_get_response_instance.to_dict()
# create an instance of ContactPublicGetResponse from a dict
contact_public_get_response_from_dict = ContactPublicGetResponse.from_dict(contact_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


