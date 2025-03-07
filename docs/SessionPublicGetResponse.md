# SessionPublicGetResponse

Session Response for Public Display

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_code** | **str** | Session code (e.g. 20181) | 
**display_name** | **str** | Session descriptive name | [optional] 
**session_year** | **int** | Session Year | 
**session_type** | **str** | Session Type description | [optional] 
**start_date** | **datetime** | Effective date for start of session | [optional] 
**is_default** | **bool** | Is it default? | [optional] 
**is_active** | **bool** | Is it active? | [optional] 
**session_id** | **int** | Session unique identifier | 
**session_type_id** | **int** | Session type id ie, 1&#x3D; regular vs. 2&#x3D;special | 
**session_events** | [**List[SessionEventPublicGetResponse]**](SessionEventPublicGetResponse.md) | Listing of Session Events | [optional] 

## Example

```python
from valis.models.session_public_get_response import SessionPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionPublicGetResponse from a JSON string
session_public_get_response_instance = SessionPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(SessionPublicGetResponse.to_json())

# convert the object into a dict
session_public_get_response_dict = session_public_get_response_instance.to_dict()
# create an instance of SessionPublicGetResponse from a dict
session_public_get_response_from_dict = SessionPublicGetResponse.from_dict(session_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


