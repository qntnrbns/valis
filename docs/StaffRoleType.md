# StaffRoleType

Staff Role Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staff_role_type_id** | **int** | Staff Role Type ID - unique Identifier for staff Roles | [optional] 
**name** | **str** | Staff Role Name | [optional] 

## Example

```python
from valis.models.staff_role_type import StaffRoleType

# TODO update the JSON string below
json = "{}"
# create an instance of StaffRoleType from a JSON string
staff_role_type_instance = StaffRoleType.from_json(json)
# print the JSON string representation of the object
print(StaffRoleType.to_json())

# convert the object into a dict
staff_role_type_dict = staff_role_type_instance.to_dict()
# create an instance of StaffRoleType from a dict
staff_role_type_from_dict = StaffRoleType.from_dict(staff_role_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


