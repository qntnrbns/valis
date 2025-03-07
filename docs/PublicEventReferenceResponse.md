# PublicEventReferenceResponse

Information for a public Legislation Event Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_reference_id** | **int** | Unique identifier for Event Reference | [optional] 
**reference_text** | **str** | Event Reference Text | [optional] 
**reference_id** | **int** | Unique identifier for Reference | [optional] 
**legislation_event_id** | **int** | Unique identifier for Legislation Event | [optional] 
**action_reference_type_id** | **int** | Unique identifier for Action Reference Type | [optional] 
**action_reference_type** | **str** | Action Reference Text | [optional] 
**sequence** | **int** | Sequence | [optional] 

## Example

```python
from valis.models.public_event_reference_response import PublicEventReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicEventReferenceResponse from a JSON string
public_event_reference_response_instance = PublicEventReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(PublicEventReferenceResponse.to_json())

# convert the object into a dict
public_event_reference_response_dict = public_event_reference_response_instance.to_dict()
# create an instance of PublicEventReferenceResponse from a dict
public_event_reference_response_from_dict = PublicEventReferenceResponse.from_dict(public_event_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


