# PatronRoleReference

Response object for Role lookup of different committee types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patron_type_id** | **int** | Unique ID for patron Type ID | [optional] 
**name** | **str** | Patron name | [optional] 
**display_name** | **str** | Patron public display name | [optional] 

## Example

```python
from valis.models.patron_role_reference import PatronRoleReference

# TODO update the JSON string below
json = "{}"
# create an instance of PatronRoleReference from a JSON string
patron_role_reference_instance = PatronRoleReference.from_json(json)
# print the JSON string representation of the object
print(PatronRoleReference.to_json())

# convert the object into a dict
patron_role_reference_dict = patron_role_reference_instance.to_dict()
# create an instance of PatronRoleReference from a dict
patron_role_reference_from_dict = PatronRoleReference.from_dict(patron_role_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


