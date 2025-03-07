# LegislationEventTypesReferenceResponse

Request and Response object containing a list of LIS LegislationEventTypesReferences (using LegislationEventTypeReferenceResponse)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationEventTypeReferenceResponse]**](LegislationEventTypeReferenceResponse.md) | list of LegislationEventTypeReferenceResponse | [optional] 

## Example

```python
from valis.models.legislation_event_types_reference_response import LegislationEventTypesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationEventTypesReferenceResponse from a JSON string
legislation_event_types_reference_response_instance = LegislationEventTypesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationEventTypesReferenceResponse.to_json())

# convert the object into a dict
legislation_event_types_reference_response_dict = legislation_event_types_reference_response_instance.to_dict()
# create an instance of LegislationEventTypesReferenceResponse from a dict
legislation_event_types_reference_response_from_dict = LegislationEventTypesReferenceResponse.from_dict(legislation_event_types_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


