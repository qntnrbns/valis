# AmendmentChange

AmendmentChange that contains list of changes in the amendment e.g: Strikes and Inserts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | [optional] 
**amendment_actions** | [**List[AmendmentAction]**](AmendmentAction.md) |  | [optional] 

## Example

```python
from valis.models.amendment_change import AmendmentChange

# TODO update the JSON string below
json = "{}"
# create an instance of AmendmentChange from a JSON string
amendment_change_instance = AmendmentChange.from_json(json)
# print the JSON string representation of the object
print(AmendmentChange.to_json())

# convert the object into a dict
amendment_change_dict = amendment_change_instance.to_dict()
# create an instance of AmendmentChange from a dict
amendment_change_from_dict = AmendmentChange.from_dict(amendment_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


