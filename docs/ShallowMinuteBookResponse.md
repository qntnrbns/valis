# ShallowMinuteBookResponse

Shallow information for MinutesBook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote_room_id** | **int** | Vote Room unique identifier | [optional] 
**session_name** | **str** | Session Display Name (e.g. 2019 Regular Session) | [optional] 
**session_code** | **str** |  | [optional] 
**session_id** | **int** | Unique identifier of Session (e.g. 41 &#x3D; 2018 Regular Session) | 
**committee_id** | **int** | Unique identifier of Committee | [optional] 
**committee_name** | **str** |  | [optional] 
**chamber_code** | **str** | Chamber Code (H&#x3D;House/S&#x3D;Senate) | 
**minutes_date** | **datetime** | Minutes Date | 
**minutes_number** | **int** | Minutes Number | [optional] 
**minutes_status_id** | **int** | Unique identifier of Minutes Status | [optional] 
**minutes_status** | **str** | Minutes Status (eg. Closed, Created...) | [optional] 
**minutes_book_id** | **int** | Unique identifier for MinutesBook | [optional] 
**status** | **str** | MinutesBook Status (e.g. Pending/Published) | [optional] 
**pending_change** | **bool** | Are there any pending changes? | [optional] 
**minutes_calendars** | [**List[PublicMinutesCalendar]**](PublicMinutesCalendar.md) | List of Minutes Calendars | [optional] 
**minutes_files** | [**List[PublicMinutesFile]**](PublicMinutesFile.md) | List of Minutes Files | [optional] 

## Example

```python
from valis.models.shallow_minute_book_response import ShallowMinuteBookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShallowMinuteBookResponse from a JSON string
shallow_minute_book_response_instance = ShallowMinuteBookResponse.from_json(json)
# print the JSON string representation of the object
print(ShallowMinuteBookResponse.to_json())

# convert the object into a dict
shallow_minute_book_response_dict = shallow_minute_book_response_instance.to_dict()
# create an instance of ShallowMinuteBookResponse from a dict
shallow_minute_book_response_from_dict = ShallowMinuteBookResponse.from_dict(shallow_minute_book_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


