# OwnerTypesReferenceResponse

List of Owner Types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[OwnerTypeReferenceResponse1]**](OwnerTypeReferenceResponse1.md) | list of Owner Types | [optional] 

## Example

```python
from valis.models.owner_types_reference_response import OwnerTypesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerTypesReferenceResponse from a JSON string
owner_types_reference_response_instance = OwnerTypesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(OwnerTypesReferenceResponse.to_json())

# convert the object into a dict
owner_types_reference_response_dict = owner_types_reference_response_instance.to_dict()
# create an instance of OwnerTypesReferenceResponse from a dict
owner_types_reference_response_from_dict = OwnerTypesReferenceResponse.from_dict(owner_types_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


