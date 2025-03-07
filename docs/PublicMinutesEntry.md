# PublicMinutesEntry

Public information for a Minutes Entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes_category_id** | **int** | unique identifier for Minutes Category | [optional] 
**sequence** | **int** | Minutes Entry order | [optional] 
**legislation_id** | **int** | unique identifier for Legislation | [optional] 
**legislation_number** | **str** | Legislation Number | [optional] 
**legislation_description** | **str** | Legislation Description | [optional] 
**agenda_id** | **int** | unique identifier for Agenda | [optional] 
**entry_text** | **str** | Entry Text | [optional] 
**communication_id** | **int** | unique identifier for Communication | [optional] 
**legislation_chamber_code** | **str** | Legislation Chamber Code | [optional] 
**communication_reference_number** | **str** | Communication Reference Number | [optional] 
**is_public** | **bool** | is Minutesentry public ? | [optional] 
**communication_chamber_code** | **str** | Communication Chamber Code | [optional] 
**communication_date** | **datetime** | Communication Date | [optional] 
**communication_number** | **int** | Communication Number | [optional] 
**is_oob** | **bool** | Is Out of Block? | [optional] 
**release_to_preview** | **bool** | Release to Preview? | [optional] 
**minutes_date** | **datetime** |  | [optional] 
**minutes_entry_id** | **int** | Unique identifier for Minutes Entry | [optional] 
**minutes_activities** | [**List[PublicMinutesActivity]**](PublicMinutesActivity.md) | List of  Minutes Activities | [optional] 
**minutes_summaries** | [**List[PublicMinutesSummary]**](PublicMinutesSummary.md) | List of Minutes Summaries | [optional] 

## Example

```python
from valis.models.public_minutes_entry import PublicMinutesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesEntry from a JSON string
public_minutes_entry_instance = PublicMinutesEntry.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesEntry.to_json())

# convert the object into a dict
public_minutes_entry_dict = public_minutes_entry_instance.to_dict()
# create an instance of PublicMinutesEntry from a dict
public_minutes_entry_from_dict = PublicMinutesEntry.from_dict(public_minutes_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


