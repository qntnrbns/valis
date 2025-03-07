# PublicMinutesSummary

Public Minutes Summary, child of MinutesEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes_entry_id** | **int** | unique reference identifier for Minutes Entry | [optional] 
**minutes_summary** | **str** | Minutes Summary | [optional] 

## Example

```python
from valis.models.public_minutes_summary import PublicMinutesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesSummary from a JSON string
public_minutes_summary_instance = PublicMinutesSummary.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesSummary.to_json())

# convert the object into a dict
public_minutes_summary_dict = public_minutes_summary_instance.to_dict()
# create an instance of PublicMinutesSummary from a dict
public_minutes_summary_from_dict = PublicMinutesSummary.from_dict(public_minutes_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


