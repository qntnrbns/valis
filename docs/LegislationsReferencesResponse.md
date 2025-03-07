# LegislationsReferencesResponse

List of Legislation Statuses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationReferencesResponse]**](LegislationReferencesResponse.md) | List of Legislation Statuses | [optional] 

## Example

```python
from valis.models.legislations_references_response import LegislationsReferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationsReferencesResponse from a JSON string
legislations_references_response_instance = LegislationsReferencesResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationsReferencesResponse.to_json())

# convert the object into a dict
legislations_references_response_dict = legislations_references_response_instance.to_dict()
# create an instance of LegislationsReferencesResponse from a dict
legislations_references_response_from_dict = LegislationsReferencesResponse.from_dict(legislations_references_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


