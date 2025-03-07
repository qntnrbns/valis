# ImpactFile

Impact Statement file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_id** | **int** | unique identifier of LegislationText | [optional] 
**text_format_id** | **int** | unique identifier of TextFormat | [optional] 
**text_format** | **str** | Text Format (e.g. PDF) | [optional] 
**file_url** | **str** | Azure Blob Storage URL | [optional] 
**reference_number** | **str** | Reference Number | [optional] 
**session_id** | **int** | internal SessionID | [optional] 
**description** | **str** | Description | [optional] 

## Example

```python
from valis.models.impact_file import ImpactFile

# TODO update the JSON string below
json = "{}"
# create an instance of ImpactFile from a JSON string
impact_file_instance = ImpactFile.from_json(json)
# print the JSON string representation of the object
print(ImpactFile.to_json())

# convert the object into a dict
impact_file_dict = impact_file_instance.to_dict()
# create an instance of ImpactFile from a dict
impact_file_from_dict = ImpactFile.from_dict(impact_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


