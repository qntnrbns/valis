# SessionsPublicGetResponse

Sessions Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[SessionPublicGetResponse]**](SessionPublicGetResponse.md) | list of sessions | [optional] 

## Example

```python
from valis.models.sessions_public_get_response import SessionsPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionsPublicGetResponse from a JSON string
sessions_public_get_response_instance = SessionsPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(SessionsPublicGetResponse.to_json())

# convert the object into a dict
sessions_public_get_response_dict = sessions_public_get_response_instance.to_dict()
# create an instance of SessionsPublicGetResponse from a dict
sessions_public_get_response_from_dict = SessionsPublicGetResponse.from_dict(sessions_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


