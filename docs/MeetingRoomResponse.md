# MeetingRoomResponse

Meeting Room Reference object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_room_id** | **int** | unique identifier for VoteRoom | 
**description** | **str** | Meeting Room Description | [optional] 
**room_number** | **str** | Meeting Room # | [optional] 
**seat_count** | **int** | Count of Seats | [optional] 
**chamber_code** | **str** | Chamber Code (H &#x3D; House and S &#x3D; Senate) | 

## Example

```python
from valis.models.meeting_room_response import MeetingRoomResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingRoomResponse from a JSON string
meeting_room_response_instance = MeetingRoomResponse.from_json(json)
# print the JSON string representation of the object
print(MeetingRoomResponse.to_json())

# convert the object into a dict
meeting_room_response_dict = meeting_room_response_instance.to_dict()
# create an instance of MeetingRoomResponse from a dict
meeting_room_response_from_dict = MeetingRoomResponse.from_dict(meeting_room_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


