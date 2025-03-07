# DocketsPublicListGetResponse

Dockets Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[DocketPublicListGetResponse]**](DocketPublicListGetResponse.md) | list of Dockets | [optional] 

## Example

```python
from valis.models.dockets_public_list_get_response import DocketsPublicListGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketsPublicListGetResponse from a JSON string
dockets_public_list_get_response_instance = DocketsPublicListGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketsPublicListGetResponse.to_json())

# convert the object into a dict
dockets_public_list_get_response_dict = dockets_public_list_get_response_instance.to_dict()
# create an instance of DocketsPublicListGetResponse from a dict
dockets_public_list_get_response_from_dict = DocketsPublicListGetResponse.from_dict(dockets_public_list_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


