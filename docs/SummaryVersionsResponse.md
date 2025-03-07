# SummaryVersionsResponse

Response object containing a list of Summary Versions. If no valid response could be obtained, Success boolean will be false and   additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[SummaryVersionResponse]**](SummaryVersionResponse.md) | list of Summary Versions | [optional] 

## Example

```python
from valis.models.summary_versions_response import SummaryVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryVersionsResponse from a JSON string
summary_versions_response_instance = SummaryVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(SummaryVersionsResponse.to_json())

# convert the object into a dict
summary_versions_response_dict = summary_versions_response_instance.to_dict()
# create an instance of SummaryVersionsResponse from a dict
summary_versions_response_from_dict = SummaryVersionsResponse.from_dict(summary_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


