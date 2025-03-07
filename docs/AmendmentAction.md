# AmendmentAction

AmendmentAction contains a single action in the amendment and the line afftected e.g: Strike and Insert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_class_name** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from valis.models.amendment_action import AmendmentAction

# TODO update the JSON string below
json = "{}"
# create an instance of AmendmentAction from a JSON string
amendment_action_instance = AmendmentAction.from_json(json)
# print the JSON string representation of the object
print(AmendmentAction.to_json())

# convert the object into a dict
amendment_action_dict = amendment_action_instance.to_dict()
# create an instance of AmendmentAction from a dict
amendment_action_from_dict = AmendmentAction.from_dict(amendment_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


