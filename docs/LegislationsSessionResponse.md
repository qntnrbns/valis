# LegislationsSessionResponse

LegislationsSessionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationSessionResponse]**](LegislationSessionResponse.md) | list of Legislations | [optional] 

## Example

```python
from valis.models.legislations_session_response import LegislationsSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationsSessionResponse from a JSON string
legislations_session_response_instance = LegislationsSessionResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationsSessionResponse.to_json())

# convert the object into a dict
legislations_session_response_dict = legislations_session_response_instance.to_dict()
# create an instance of LegislationsSessionResponse from a dict
legislations_session_response_from_dict = LegislationsSessionResponse.from_dict(legislations_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


