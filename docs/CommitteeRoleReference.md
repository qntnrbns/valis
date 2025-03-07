# CommitteeRoleReference

Information for a Committee Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_role_id** | **int** | Unique identifier for this Committee Role | [optional] 
**title** | **str** | Role title | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 

## Example

```python
from valis.models.committee_role_reference import CommitteeRoleReference

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeRoleReference from a JSON string
committee_role_reference_instance = CommitteeRoleReference.from_json(json)
# print the JSON string representation of the object
print(CommitteeRoleReference.to_json())

# convert the object into a dict
committee_role_reference_dict = committee_role_reference_instance.to_dict()
# create an instance of CommitteeRoleReference from a dict
committee_role_reference_from_dict = CommitteeRoleReference.from_dict(committee_role_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


