# RoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** |  | [optional] 
**role_name** | **str** |  | 
**scope** | **str** |  | 
**resource** | **str** |  | 
**component** | **str** |  | [optional] 
**action** | **str** |  | 
**modification_date** | **datetime** |  | [optional] 

## Example

```python
from valis.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print(RoleResponse.to_json())

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_from_dict = RoleResponse.from_dict(role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


