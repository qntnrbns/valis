# CommitteeRolesReference

List of Committee Roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CommitteeRoleReference]**](CommitteeRoleReference.md) | List of Committee Roles | [optional] 

## Example

```python
from valis.models.committee_roles_reference import CommitteeRolesReference

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeRolesReference from a JSON string
committee_roles_reference_instance = CommitteeRolesReference.from_json(json)
# print the JSON string representation of the object
print(CommitteeRolesReference.to_json())

# convert the object into a dict
committee_roles_reference_dict = committee_roles_reference_instance.to_dict()
# create an instance of CommitteeRolesReference from a dict
committee_roles_reference_from_dict = CommitteeRolesReference.from_dict(committee_roles_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


