# ActorTypeReferenceResponse

Response object containing LIS Legislation events reference information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_type_id** | **int** | Actor Type unique identifier | [optional] 
**name** | **str** | Description/Name of the ID | [optional] 

## Example

```python
from valis.models.actor_type_reference_response import ActorTypeReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActorTypeReferenceResponse from a JSON string
actor_type_reference_response_instance = ActorTypeReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ActorTypeReferenceResponse.to_json())

# convert the object into a dict
actor_type_reference_response_dict = actor_type_reference_response_instance.to_dict()
# create an instance of ActorTypeReferenceResponse from a dict
actor_type_reference_response_from_dict = ActorTypeReferenceResponse.from_dict(actor_type_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


