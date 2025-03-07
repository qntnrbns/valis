# CalendarCommentPublicGetResponse

Calendar Comment Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | **int** | Calendar ID | [optional] 
**comment** | **str** | Comment text | [optional] 
**sequence** | **int** | Calendar Category Sequence | [optional] 
**deletion_date** | **datetime** | Deletion Date | [optional] 
**calendar_comment_id** | **int** | Calendar Comment unique identifier | [optional] 

## Example

```python
from valis.models.calendar_comment_public_get_response import CalendarCommentPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCommentPublicGetResponse from a JSON string
calendar_comment_public_get_response_instance = CalendarCommentPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarCommentPublicGetResponse.to_json())

# convert the object into a dict
calendar_comment_public_get_response_dict = calendar_comment_public_get_response_instance.to_dict()
# create an instance of CalendarCommentPublicGetResponse from a dict
calendar_comment_public_get_response_from_dict = CalendarCommentPublicGetResponse.from_dict(calendar_comment_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


