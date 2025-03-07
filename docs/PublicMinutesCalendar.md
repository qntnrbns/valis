# PublicMinutesCalendar

public minute calendars

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes_book_id** | **int** | Minutes unique identifier | [optional] 
**calendar_id** | **int** | unique identifier for Calendar | [optional] 
**calendar_number** | **int** | Number for Calendar | [optional] 
**description** | **str** | Calendar description | [optional] 
**minutes_status_id** | **int** | Minutes Status ID | [optional] 
**calendar_date** | **datetime** | Calendar Date | [optional] 
**status** | **str** | Status | [optional] 
**status_date** | **datetime** | Status Date | [optional] 
**deletion_date** | **datetime** | Deletion Date | [optional] 

## Example

```python
from valis.models.public_minutes_calendar import PublicMinutesCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesCalendar from a JSON string
public_minutes_calendar_instance = PublicMinutesCalendar.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesCalendar.to_json())

# convert the object into a dict
public_minutes_calendar_dict = public_minutes_calendar_instance.to_dict()
# create an instance of PublicMinutesCalendar from a dict
public_minutes_calendar_from_dict = PublicMinutesCalendar.from_dict(public_minutes_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


