# CalendarPublicListGetResponse

Calendar Response for Public Display

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_date** | **datetime** | Calendar Date | 
**meeting_time** | **str** | Meeting Time | [optional] 
**calendar_number** | **int** | Numeric Indicator for Primary and Supplemental | [optional] 
**description** | **str** | Calendar Description | [optional] 
**is_public** | **bool** | Is Calendar for Public Consumption | [optional] 
**calendar_type** | **str** | Calendar Type | 
**calendar_type_id** | **int** | Calendar Type ID | [optional] 
**chamber_code** | **str** | Chamber Code (H&#x3D;House / S&#x3D;Senate) | [optional] 
**session_id** | **int** | Session ID | 
**session_code** | **str** | Session Code | [optional] 
**vote_room_id** | **int** | Vote Room ID | [optional] 
**room_description** | **str** | Vote Room Description | [optional] 
**comments** | **str** | Meeting Notes/Comments | [optional] 
**pending_change** | **bool** | Pending Change to Calendar | [optional] 
**reference_number** | **str** | Reference Number used for External reference to calendar | [optional] 
**is_proforma** | **bool** | IsProforma to Calendar | [optional] 
**deletion_date** | **datetime** | Calendar Deletion Date | [optional] 
**calendar_id** | **int** | Calendar unique identifier | 
**calendar_files** | [**List[CalendarFileBaseModel]**](CalendarFileBaseModel.md) | list of Calendar Files for a specific Calendar | [optional] 
**calendar_comments** | [**List[CalendarCommentPublicGetResponse]**](CalendarCommentPublicGetResponse.md) | Listing of Calendar Comments | [optional] 

## Example

```python
from valis.models.calendar_public_list_get_response import CalendarPublicListGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarPublicListGetResponse from a JSON string
calendar_public_list_get_response_instance = CalendarPublicListGetResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarPublicListGetResponse.to_json())

# convert the object into a dict
calendar_public_list_get_response_dict = calendar_public_list_get_response_instance.to_dict()
# create an instance of CalendarPublicListGetResponse from a dict
calendar_public_list_get_response_from_dict = CalendarPublicListGetResponse.from_dict(calendar_public_list_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


