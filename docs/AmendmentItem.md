# AmendmentItem

AmendmentItem Model - for breaking up the legislation amendment drafttext into json object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sponsor** | [**Sponsor**](Sponsor.md) |  | [optional] 
**line** | **str** | Amendment Line | [optional] 
**line_number** | **int** | Amendment Line Number | [optional] 
**line_class_name** | **str** | Amendment Line ClassName, always &#x3D; textbi | [optional] 
**item_order** | **int** | Item Number | [optional] 
**item_condition** | **str** | Amendment Condition e.g: Agreed, Rejected | [optional] 
**amendment_changes** | [**List[AmendmentChange]**](AmendmentChange.md) | Amendment Changes e.g: Strikes and Inserts | [optional] 

## Example

```python
from valis.models.amendment_item import AmendmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of AmendmentItem from a JSON string
amendment_item_instance = AmendmentItem.from_json(json)
# print the JSON string representation of the object
print(AmendmentItem.to_json())

# convert the object into a dict
amendment_item_dict = amendment_item_instance.to_dict()
# create an instance of AmendmentItem from a dict
amendment_item_from_dict = AmendmentItem.from_dict(amendment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


