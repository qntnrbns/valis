# ActionReferenceTypeList

List of Action Reference Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_reference_type_id** | **int** | Action Reference Type unique identifier | [optional] 
**action_reference_type** | **str** | Action Reference Type | [optional] 
**object_name** | **str** | Corresponding Event Code | [optional] 

## Example

```python
from valis.models.action_reference_type_list import ActionReferenceTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of ActionReferenceTypeList from a JSON string
action_reference_type_list_instance = ActionReferenceTypeList.from_json(json)
# print the JSON string representation of the object
print(ActionReferenceTypeList.to_json())

# convert the object into a dict
action_reference_type_list_dict = action_reference_type_list_instance.to_dict()
# create an instance of ActionReferenceTypeList from a dict
action_reference_type_list_from_dict = ActionReferenceTypeList.from_dict(action_reference_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


