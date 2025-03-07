# LegislationsResponse

legislations response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationResponse]**](LegislationResponse.md) | list of legislation | [optional] 
**search_criteria** | **str** | Search JSON used to product these results | [optional] 

## Example

```python
from valis.models.legislations_response import LegislationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationsResponse from a JSON string
legislations_response_instance = LegislationsResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationsResponse.to_json())

# convert the object into a dict
legislations_response_dict = legislations_response_instance.to_dict()
# create an instance of LegislationsResponse from a dict
legislations_response_from_dict = LegislationsResponse.from_dict(legislations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


