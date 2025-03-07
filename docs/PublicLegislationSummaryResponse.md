# PublicLegislationSummaryResponse

legislation summary response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_number** | **str** | legislation bill number | [optional] 
**summary** | **str** | legislation summary text | [optional] 
**document_code** | **str** | document code | [optional] 
**ld_number** | **str** | legislation document number (LDNumber) | [optional] 
**summary_date** | **datetime** | legislation summary date | [optional] 
**summary_version_id** | **int** | summary version id | [optional] 
**is_public** | **bool** | is legislation public? | [optional] 
**is_active** | **bool** | is legislation active? | [optional] 
**legislation_id** | **int** | unique id for legislation | [optional] 
**session_id** | **int** | unique id for session | [optional] 
**legislation_summary_id** | **int** | legislation summary id | [optional] 
**summary_version** | **str** | legislation summary version | [optional] 

## Example

```python
from valis.models.public_legislation_summary_response import PublicLegislationSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicLegislationSummaryResponse from a JSON string
public_legislation_summary_response_instance = PublicLegislationSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PublicLegislationSummaryResponse.to_json())

# convert the object into a dict
public_legislation_summary_response_dict = public_legislation_summary_response_instance.to_dict()
# create an instance of PublicLegislationSummaryResponse from a dict
public_legislation_summary_response_from_dict = PublicLegislationSummaryResponse.from_dict(public_legislation_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


