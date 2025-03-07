# SummaryVersionResponse

summary version response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary_version_id** | **int** | Summary Version unique identifier | [optional] 
**name** | **str** | Summary Version name | [optional] 
**version_code** | **str** | Version Code | [optional] 

## Example

```python
from valis.models.summary_version_response import SummaryVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryVersionResponse from a JSON string
summary_version_response_instance = SummaryVersionResponse.from_json(json)
# print the JSON string representation of the object
print(SummaryVersionResponse.to_json())

# convert the object into a dict
summary_version_response_dict = summary_version_response_instance.to_dict()
# create an instance of SummaryVersionResponse from a dict
summary_version_response_from_dict = SummaryVersionResponse.from_dict(summary_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


