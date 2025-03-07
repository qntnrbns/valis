# ContactsPublicGetResponse

Contacts Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ContactPublicGetResponse]**](ContactPublicGetResponse.md) | list of contacts for Public Consumption | [optional] 

## Example

```python
from valis.models.contacts_public_get_response import ContactsPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsPublicGetResponse from a JSON string
contacts_public_get_response_instance = ContactsPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(ContactsPublicGetResponse.to_json())

# convert the object into a dict
contacts_public_get_response_dict = contacts_public_get_response_instance.to_dict()
# create an instance of ContactsPublicGetResponse from a dict
contacts_public_get_response_from_dict = ContactsPublicGetResponse.from_dict(contacts_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


