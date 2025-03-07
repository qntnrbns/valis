# ContactResponse

Information for a Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_information_id** | **int** | Unique identifier for this Contact | [optional] 
**owner_id** | **int** | Unique identifier for Owner | [optional] 
**contact_type_id** | **int** | Unique identifier for Contact Type | [optional] 
**contact_type** | **str** | Contact Type | [optional] 
**address1** | **str** | Address 1 | [optional] 
**address2** | **str** | Address 2 | [optional] 
**address3** | **str** | Address 3 | [optional] 
**city** | **str** | City | [optional] 
**state_code** | **str** | State | [optional] 
**zip_code** | **str** | Postal/Zip Code | [optional] 
**phone_number** | **str** | Phone Number | [optional] 
**email_address** | **str** | Email Address | [optional] 
**is_active** | **bool** | Is this Contact active? | [optional] 
**is_public** | **bool** | Is this Contact public? | [optional] 

## Example

```python
from valis.models.contact_response import ContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactResponse from a JSON string
contact_response_instance = ContactResponse.from_json(json)
# print the JSON string representation of the object
print(ContactResponse.to_json())

# convert the object into a dict
contact_response_dict = contact_response_instance.to_dict()
# create an instance of ContactResponse from a dict
contact_response_from_dict = ContactResponse.from_dict(contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


