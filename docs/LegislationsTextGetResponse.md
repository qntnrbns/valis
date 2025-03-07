# LegislationsTextGetResponse

Request and Response object containing a list of LIS Legislation Texts (using LegislationTextGetResponse).   If no valid response could be obtained, Success boolean will be false and additional information can be   found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationTextGetResponse]**](LegislationTextGetResponse.md) | list of legislation summaries | [optional] 

## Example

```python
from valis.models.legislations_text_get_response import LegislationsTextGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationsTextGetResponse from a JSON string
legislations_text_get_response_instance = LegislationsTextGetResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationsTextGetResponse.to_json())

# convert the object into a dict
legislations_text_get_response_dict = legislations_text_get_response_instance.to_dict()
# create an instance of LegislationsTextGetResponse from a dict
legislations_text_get_response_from_dict = LegislationsTextGetResponse.from_dict(legislations_text_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


