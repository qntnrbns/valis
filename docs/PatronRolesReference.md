# PatronRolesReference

Patron Roles Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PatronRoleReference]**](PatronRoleReference.md) | list of committee roles | [optional] 

## Example

```python
from valis.models.patron_roles_reference import PatronRolesReference

# TODO update the JSON string below
json = "{}"
# create an instance of PatronRolesReference from a JSON string
patron_roles_reference_instance = PatronRolesReference.from_json(json)
# print the JSON string representation of the object
print(PatronRolesReference.to_json())

# convert the object into a dict
patron_roles_reference_dict = patron_roles_reference_instance.to_dict()
# create an instance of PatronRolesReference from a dict
patron_roles_reference_from_dict = PatronRolesReference.from_dict(patron_roles_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


