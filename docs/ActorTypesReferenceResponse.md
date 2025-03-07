# ActorTypesReferenceResponse

Request and Response object containing a list of LIS contacts (using ContactResponse). If no valid response could be obtained, Success boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ActorTypeReferenceResponse]**](ActorTypeReferenceResponse.md) | list of contacts | [optional] 

## Example

```python
from valis.models.actor_types_reference_response import ActorTypesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActorTypesReferenceResponse from a JSON string
actor_types_reference_response_instance = ActorTypesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ActorTypesReferenceResponse.to_json())

# convert the object into a dict
actor_types_reference_response_dict = actor_types_reference_response_instance.to_dict()
# create an instance of ActorTypesReferenceResponse from a dict
actor_types_reference_response_from_dict = ActorTypesReferenceResponse.from_dict(actor_types_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


