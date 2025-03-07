# LegislationTextResponse

Legislation Text Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | unique identifier for the Legislation | [optional] 
**legislation_number** | **str** | Bill # | [optional] 
**description** | **str** | Legislation Description | [optional] 
**session_id** | **int** | unique identifier for the Session | [optional] 
**legislation_text_id** | **int** | unique identifier of LegislationText | [optional] 
**draft_date** | **datetime** | Draft Date | [optional] 
**document_code** | **str** | Document Code | [optional] 
**ld_number** | **str** | Bill LD# | [optional] 
**legislation_version_id** | **int** | unique identifier of LegislationVersion | [optional] 
**version** | **str** | Version | [optional] 
**is_public** | **bool** | Is Public? | [optional] 
**is_complete** | **bool** | Is complete? | [optional] 
**governors_request** | **bool** | Is this at the Request of the Governor? | [optional] 
**pdf_file** | [**List[PDFFile]**](PDFFile.md) | List of PDFFile | [optional] 
**html_file** | [**List[HTMLFile]**](HTMLFile.md) | list of HTMLFile | [optional] 
**impact_file** | [**List[ImpactFile]**](ImpactFile.md) | List of ImpactFile | [optional] 
**link_file** | [**List[LinkFile]**](LinkFile.md) | List of LinkFile | [optional] 
**is_emergency** | **bool** | Is this text an emergency ? | [optional] 
**is_reprint** | **bool** | Is this text Reprint ? | [optional] 
**text_disposition_id** | **int** | Text Disposition ID | [optional] 

## Example

```python
from valis.models.legislation_text_response import LegislationTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextResponse from a JSON string
legislation_text_response_instance = LegislationTextResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextResponse.to_json())

# convert the object into a dict
legislation_text_response_dict = legislation_text_response_instance.to_dict()
# create an instance of LegislationTextResponse from a dict
legislation_text_response_from_dict = LegislationTextResponse.from_dict(legislation_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


