# PublicMinutesActivity

Public Minutes Activity, child of MinutesEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes_entry_id** | **int** | unique identifier for Minutes Entry | [optional] 
**description** | **str** | Activity description | [optional] 
**sequence** | **int** | Sequence | [optional] 
**calendar_action_id** | **int** | unique identifier for Calendar Action | [optional] 
**action_description** | **str** | Action description | [optional] 
**committee_complete** | **bool** | Committee Complete indicates when Committee Actions are completed | [optional] 
**vote_id** | **int** | unique identifier for Vote | [optional] 
**deletion_date** | **str** | Deletion Date | [optional] 
**is_public** | **bool** | Is public | [optional] 
**is_passed** | **bool** | Is passed | [optional] 
**in_preview** | **bool** | In Preview | [optional] 
**minutes_activity_id** | **int** | unique identifier for Minutes Activity | [optional] 
**activity_references** | [**List[PublicActivityReference]**](PublicActivityReference.md) | Collection of associated activity references | [optional] 

## Example

```python
from valis.models.public_minutes_activity import PublicMinutesActivity

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesActivity from a JSON string
public_minutes_activity_instance = PublicMinutesActivity.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesActivity.to_json())

# convert the object into a dict
public_minutes_activity_dict = public_minutes_activity_instance.to_dict()
# create an instance of PublicMinutesActivity from a dict
public_minutes_activity_from_dict = PublicMinutesActivity.from_dict(public_minutes_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


