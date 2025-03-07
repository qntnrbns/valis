# GroupRolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[RoleResponse]**](RoleResponse.md) |  | [optional] 
**success** | **bool** | is this response valid? (true&#x3D;success, false&#x3D;unsuccessful) | [optional] 
**failure_message** | **str** | message describing why the action taken was not successful | [optional] 

## Example

```python
from valis.models.group_roles_response import GroupRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRolesResponse from a JSON string
group_roles_response_instance = GroupRolesResponse.from_json(json)
# print the JSON string representation of the object
print(GroupRolesResponse.to_json())

# convert the object into a dict
group_roles_response_dict = group_roles_response_instance.to_dict()
# create an instance of GroupRolesResponse from a dict
group_roles_response_from_dict = GroupRolesResponse.from_dict(group_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


