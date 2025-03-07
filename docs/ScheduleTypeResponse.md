# ScheduleTypeResponse

Schedule type reference list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_type_id** | **int** | id for schedule type | [optional] 
**schedule_type** | **str** | Schedule Type Name | [optional] 

## Example

```python
from valis.models.schedule_type_response import ScheduleTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTypeResponse from a JSON string
schedule_type_response_instance = ScheduleTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleTypeResponse.to_json())

# convert the object into a dict
schedule_type_response_dict = schedule_type_response_instance.to_dict()
# create an instance of ScheduleTypeResponse from a dict
schedule_type_response_from_dict = ScheduleTypeResponse.from_dict(schedule_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


