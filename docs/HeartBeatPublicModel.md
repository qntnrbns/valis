# HeartBeatPublicModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**date_time** | **str** |  | 
**environment** | **str** |  | 
**action_name** | **str** |  | 
**service** | **str** |  | 
**success** | **bool** |  | [optional] 
**failure_message** | **str** |  | [optional] 

## Example

```python
from valis.models.heart_beat_public_model import HeartBeatPublicModel

# TODO update the JSON string below
json = "{}"
# create an instance of HeartBeatPublicModel from a JSON string
heart_beat_public_model_instance = HeartBeatPublicModel.from_json(json)
# print the JSON string representation of the object
print(HeartBeatPublicModel.to_json())

# convert the object into a dict
heart_beat_public_model_dict = heart_beat_public_model_instance.to_dict()
# create an instance of HeartBeatPublicModel from a dict
heart_beat_public_model_from_dict = HeartBeatPublicModel.from_dict(heart_beat_public_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


