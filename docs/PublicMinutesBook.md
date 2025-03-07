# PublicMinutesBook

Public Response object containing LIS Minutes Book information .

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
**minutes_book_id** | **int** | Minutes unique identifier | [optional] 
**minutes_categories** | [**List[PublicMinutesCategory]**](PublicMinutesCategory.md) | Collection of associated categories | [optional] 
**minutes_calendars** | [**List[PublicMinutesCalendar]**](PublicMinutesCalendar.md) | Collection of associated Calendars | [optional] 
**minutes_files** | [**List[PublicMinutesFile]**](PublicMinutesFile.md) | Collection of associated Files | [optional] 

## Example

```python
from valis.models.public_minutes_book import PublicMinutesBook

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesBook from a JSON string
public_minutes_book_instance = PublicMinutesBook.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesBook.to_json())

# convert the object into a dict
public_minutes_book_dict = public_minutes_book_instance.to_dict()
# create an instance of PublicMinutesBook from a dict
public_minutes_book_from_dict = PublicMinutesBook.from_dict(public_minutes_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


