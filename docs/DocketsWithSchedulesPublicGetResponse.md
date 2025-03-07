# DocketsWithSchedulesPublicGetResponse

List of Dockets with Schedules for Public consumption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[DocketWithSchedulePublicGetResponse]**](DocketWithSchedulePublicGetResponse.md) | list of Dockets | [optional] 

## Example

```python
from valis.models.dockets_with_schedules_public_get_response import DocketsWithSchedulesPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketsWithSchedulesPublicGetResponse from a JSON string
dockets_with_schedules_public_get_response_instance = DocketsWithSchedulesPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketsWithSchedulesPublicGetResponse.to_json())

# convert the object into a dict
dockets_with_schedules_public_get_response_dict = dockets_with_schedules_public_get_response_instance.to_dict()
# create an instance of DocketsWithSchedulesPublicGetResponse from a dict
dockets_with_schedules_public_get_response_from_dict = DocketsWithSchedulesPublicGetResponse.from_dict(dockets_with_schedules_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


