# SessionEventPublicGetResponse

Session Event public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Session event display name | [optional] 
**actual_date** | **datetime** | Actual date for the session event | [optional] 
**internal_only** | **bool** | Is this used internally only? | [optional] 
**event_type_id** | **int** | Unique identifier for Event Type | 
**projected_date** | **datetime** | Projected date | [optional] 
**session_event_id** | **int** | Session Event unique identifier | 

## Example

```python
from valis.models.session_event_public_get_response import SessionEventPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionEventPublicGetResponse from a JSON string
session_event_public_get_response_instance = SessionEventPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(SessionEventPublicGetResponse.to_json())

# convert the object into a dict
session_event_public_get_response_dict = session_event_public_get_response_instance.to_dict()
# create an instance of SessionEventPublicGetResponse from a dict
session_event_public_get_response_from_dict = SessionEventPublicGetResponse.from_dict(session_event_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


