# MeetingRoomsResponse

Meeting Rooms Reference List

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[MeetingRoomResponse]**](MeetingRoomResponse.md) | list of Meeting Rooms | [optional] 

## Example

```python
from valis.models.meeting_rooms_response import MeetingRoomsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingRoomsResponse from a JSON string
meeting_rooms_response_instance = MeetingRoomsResponse.from_json(json)
# print the JSON string representation of the object
print(MeetingRoomsResponse.to_json())

# convert the object into a dict
meeting_rooms_response_dict = meeting_rooms_response_instance.to_dict()
# create an instance of MeetingRoomsResponse from a dict
meeting_rooms_response_from_dict = MeetingRoomsResponse.from_dict(meeting_rooms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


