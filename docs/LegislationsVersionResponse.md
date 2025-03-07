# LegislationsVersionResponse

Request and Response object containing a list of LIS Legislation Version. If no valid response could be obtained, Success boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationVersionResponse]**](LegislationVersionResponse.md) | list of Legislation Version | [optional] 
**search_criteria** | **str** | Search JSON used to product these results | [optional] 

## Example

```python
from valis.models.legislations_version_response import LegislationsVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationsVersionResponse from a JSON string
legislations_version_response_instance = LegislationsVersionResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationsVersionResponse.to_json())

# convert the object into a dict
legislations_version_response_dict = legislations_version_response_instance.to_dict()
# create an instance of LegislationsVersionResponse from a dict
legislations_version_response_from_dict = LegislationsVersionResponse.from_dict(legislations_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


