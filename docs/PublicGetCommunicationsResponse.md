# PublicGetCommunicationsResponse

List of Public Get Communications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicGetCommunicationResponse]**](PublicGetCommunicationResponse.md) | list of Public Get Communications | [optional] 

## Example

```python
from valis.models.public_get_communications_response import PublicGetCommunicationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGetCommunicationsResponse from a JSON string
public_get_communications_response_instance = PublicGetCommunicationsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicGetCommunicationsResponse.to_json())

# convert the object into a dict
public_get_communications_response_dict = public_get_communications_response_instance.to_dict()
# create an instance of PublicGetCommunicationsResponse from a dict
public_get_communications_response_from_dict = PublicGetCommunicationsResponse.from_dict(public_get_communications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


