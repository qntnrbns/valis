# PublicActivityReference

Pulic Minute Activity Reference, child of MinutesActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_text** | **str** | Reference text | [optional] 
**reference_id** | **int** | unique identifier for Reference | [optional] 
**minutes_activity_id** | **int** | unique identifier for MinutesActivity parent object | [optional] 
**action_reference_type_id** | **int** | unique identifier for Action Reference Type | [optional] 
**action_reference_type** | **str** | Action Reference Type - not used for save requests | [optional] 
**sequence** | **int** | Sequence for activity reference | [optional] 

## Example

```python
from valis.models.public_activity_reference import PublicActivityReference

# TODO update the JSON string below
json = "{}"
# create an instance of PublicActivityReference from a JSON string
public_activity_reference_instance = PublicActivityReference.from_json(json)
# print the JSON string representation of the object
print(PublicActivityReference.to_json())

# convert the object into a dict
public_activity_reference_dict = public_activity_reference_instance.to_dict()
# create an instance of PublicActivityReference from a dict
public_activity_reference_from_dict = PublicActivityReference.from_dict(public_activity_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


