# PublicScheduleResponse

Public Schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_sequence** | **int** | optional display sequence | [optional] 
**owner_id** | **int** | id for schedule owner | [optional] 
**owner_name** | **str** | owner&#39;s name | [optional] 
**schedule_type_id** | **int** | id for schedule type | [optional] 
**schedule_type** | **str** | Schedule Type Name | [optional] 
**vote_room_id** | **int** | id for vote room | [optional] 
**room_description** | **str** | Room Description | [optional] 
**schedule_date** | **date** | schedule Date | [optional] 
**schedule_time** | **str** | schedule Time | [optional] 
**comments** | **str** | Comments | [optional] 
**is_cancelled** | **bool** | is this canceled | [optional] 
**is_public** | **bool** | is this publicly viewable | [optional] 
**link_url** | **str** | LinkURL | [optional] 
**schedule_id** | **int** | id for schedule | [optional] 
**version_sequence** | **int** | Version Sequence number - used for iCalendar (ICS) file versioning; automatically incremented by database when updates are made | [optional] 

## Example

```python
from valis.models.public_schedule_response import PublicScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicScheduleResponse from a JSON string
public_schedule_response_instance = PublicScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(PublicScheduleResponse.to_json())

# convert the object into a dict
public_schedule_response_dict = public_schedule_response_instance.to_dict()
# create an instance of PublicScheduleResponse from a dict
public_schedule_response_from_dict = PublicScheduleResponse.from_dict(public_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


