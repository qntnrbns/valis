# SessionTypeReferenceResponse

Response object containing LIS Session events reference information. If no valid response   could be obtained, Success boolean will be false and additional information can be found   in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Description/Name of the ID | [optional] 
**id** | **int** | Session Event Type unique identifier | [optional] 

## Example

```python
from valis.models.session_type_reference_response import SessionTypeReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionTypeReferenceResponse from a JSON string
session_type_reference_response_instance = SessionTypeReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(SessionTypeReferenceResponse.to_json())

# convert the object into a dict
session_type_reference_response_dict = session_type_reference_response_instance.to_dict()
# create an instance of SessionTypeReferenceResponse from a dict
session_type_reference_response_from_dict = SessionTypeReferenceResponse.from_dict(session_type_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


