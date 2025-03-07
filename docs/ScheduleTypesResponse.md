# ScheduleTypesResponse

List of Schedule types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ScheduleTypeResponse]**](ScheduleTypeResponse.md) | list of schedules | [optional] 

## Example

```python
from valis.models.schedule_types_response import ScheduleTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTypesResponse from a JSON string
schedule_types_response_instance = ScheduleTypesResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleTypesResponse.to_json())

# convert the object into a dict
schedule_types_response_dict = schedule_types_response_instance.to_dict()
# create an instance of ScheduleTypesResponse from a dict
schedule_types_response_from_dict = ScheduleTypesResponse.from_dict(schedule_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


