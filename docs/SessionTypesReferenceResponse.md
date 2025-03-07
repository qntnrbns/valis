# SessionTypesReferenceResponse

Request and Response object containing a list of LIS Sessions with Events (using SessionResponse). If no valid response could be obtained, Success boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[SessionTypeReferenceResponse]**](SessionTypeReferenceResponse.md) | list of Session Types | [optional] 

## Example

```python
from valis.models.session_types_reference_response import SessionTypesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionTypesReferenceResponse from a JSON string
session_types_reference_response_instance = SessionTypesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(SessionTypesReferenceResponse.to_json())

# convert the object into a dict
session_types_reference_response_dict = session_types_reference_response_instance.to_dict()
# create an instance of SessionTypesReferenceResponse from a dict
session_types_reference_response_from_dict = SessionTypesReferenceResponse.from_dict(session_types_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


