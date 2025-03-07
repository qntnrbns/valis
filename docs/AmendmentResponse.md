# AmendmentResponse

Amendment Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | Legislation unique identifier | [optional] 
**legislation_text_id** | **int** | Legislation Text unique identifier | [optional] 
**legislation_version_id** | **int** | Legislation Version unique identifier | [optional] 
**legislation_version** | **str** | Legislative Version | [optional] 
**text_disposition_id** | **int** | unique identifier for Text Disposition (e.g. 1&#x3D;Offered, 2&#x3D;Recommended, 3&#x3D;Reported, etc) | [optional] 
**text_disposition** | **str** | Text Disposition (e.g. Offered, Recommended, Reported, etc) | [optional] 
**is_active** | **bool** | Active for use? | [optional] 
**is_public** | **bool** | Public Consumption? | [optional] 
**document_code** | **str** | document code | [optional] 
**chamber_code** | **str** | Amendment ChamberCode | [optional] 
**description** | **str** | LegislationText Description | [optional] 
**ld_number** | **str** | LD Number | [optional] 
**version_date** | **str** | Version Date | [optional] 

## Example

```python
from valis.models.amendment_response import AmendmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AmendmentResponse from a JSON string
amendment_response_instance = AmendmentResponse.from_json(json)
# print the JSON string representation of the object
print(AmendmentResponse.to_json())

# convert the object into a dict
amendment_response_dict = amendment_response_instance.to_dict()
# create an instance of AmendmentResponse from a dict
amendment_response_from_dict = AmendmentResponse.from_dict(amendment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


