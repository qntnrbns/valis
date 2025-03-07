# OwnerTypeReferencesResponse

Request and Response object containing a list of LIS contact references (using ContactReferenceResponse). If no valid response could be obtained, Success boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[OwnerTypeReferenceResponse]**](OwnerTypeReferenceResponse.md) | list of contact references | [optional] 

## Example

```python
from valis.models.owner_type_references_response import OwnerTypeReferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerTypeReferencesResponse from a JSON string
owner_type_references_response_instance = OwnerTypeReferencesResponse.from_json(json)
# print the JSON string representation of the object
print(OwnerTypeReferencesResponse.to_json())

# convert the object into a dict
owner_type_references_response_dict = owner_type_references_response_instance.to_dict()
# create an instance of OwnerTypeReferencesResponse from a dict
owner_type_references_response_from_dict = OwnerTypeReferencesResponse.from_dict(owner_type_references_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


