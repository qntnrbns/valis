# ActionReferenceTypesList

Multiple Action Reference Types List

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ActionReferenceTypeList]**](ActionReferenceTypeList.md) | list of Actions Reference Types | [optional] 

## Example

```python
from valis.models.action_reference_types_list import ActionReferenceTypesList

# TODO update the JSON string below
json = "{}"
# create an instance of ActionReferenceTypesList from a JSON string
action_reference_types_list_instance = ActionReferenceTypesList.from_json(json)
# print the JSON string representation of the object
print(ActionReferenceTypesList.to_json())

# convert the object into a dict
action_reference_types_list_dict = action_reference_types_list_instance.to_dict()
# create an instance of ActionReferenceTypesList from a dict
action_reference_types_list_from_dict = ActionReferenceTypesList.from_dict(action_reference_types_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


