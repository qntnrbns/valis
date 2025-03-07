# PublicLegislationEventsResponse

List of public Legislation Events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**legislation_events** | [**List[PublicLegislationEventResponse]**](PublicLegislationEventResponse.md) | List of public Legislation Events | [optional] 

## Example

```python
from valis.models.public_legislation_events_response import PublicLegislationEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicLegislationEventsResponse from a JSON string
public_legislation_events_response_instance = PublicLegislationEventsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicLegislationEventsResponse.to_json())

# convert the object into a dict
public_legislation_events_response_dict = public_legislation_events_response_instance.to_dict()
# create an instance of PublicLegislationEventsResponse from a dict
public_legislation_events_response_from_dict = PublicLegislationEventsResponse.from_dict(public_legislation_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


