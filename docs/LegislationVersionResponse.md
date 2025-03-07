# LegislationVersionResponse

legislation version response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | Legislation unique identifier | [optional] 
**legislation_number** | **str** | Legislation Number (Unique for each Biennial) | [optional] 
**chamber_code** | **str** | ChamberCode, H&#x3D;House, S&#x3D;Senate | [optional] 
**session_id** | **int** | Session ID | [optional] 
**legislation_text_id** | **int** | Legislation Text Id | [optional] 
**draft_date** | **datetime** | Draft Date | [optional] 
**document_code** | **str** | Document Number (Unique for each Biennial) | [optional] 
**description** | **str** | Legislation Text Description | [optional] 
**sponsor** | **str** | Body that authored/sponsored the Legislation Text (House/Senate/Conference/Governor) | [optional] 
**ld_number** | **str** | Legislation Document Number | [optional] 
**legislation_version_id** | **int** | Legislation Version ID | [optional] 
**version** | **str** | Version | [optional] 
**is_public** | **bool** | Public | [optional] 
**is_active** | **bool** | Active | [optional] 
**pdf_file** | [**List[File]**](File.md) | PDF File(s) | [optional] 
**html_file** | [**List[File]**](File.md) | HTML File(s) | [optional] 
**link_file** | [**List[File]**](File.md) | Link File(s) | [optional] 
**impact_file** | [**List[File]**](File.md) | Impact Statement File(s) | [optional] 
**text_disposition_id** | **int** | unique identifier for Text Disposition (e.g. 1&#x3D;Offered, 2&#x3D;Recommended, 3&#x3D;Reported, etc) | [optional] 
**text_disposition** | **str** | Text Disposition (e.g. Offered, Recommended, Reported, etc) | [optional] 

## Example

```python
from valis.models.legislation_version_response import LegislationVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationVersionResponse from a JSON string
legislation_version_response_instance = LegislationVersionResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationVersionResponse.to_json())

# convert the object into a dict
legislation_version_response_dict = legislation_version_response_instance.to_dict()
# create an instance of LegislationVersionResponse from a dict
legislation_version_response_from_dict = LegislationVersionResponse.from_dict(legislation_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


