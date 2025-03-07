# LegislationTextGetResponse

Response object containing LIS legislation Text information. If no valid response could be obtained, Success    boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_id** | **int** | LIS Text Id | [optional] 
**legislation_draft_id** | **int** | LIS Draft Id | [optional] 
**text_format** | **str** | LIS TextFormat PDF, HTML or Impact | [optional] 
**text_format_id** | **int** | LIS TextFormat Id 1&#x3D;pdf, 2&#x3D;html, 3&#x3D;impact statement | [optional] 
**legislation_version_id** | **int** | LIS Legislation Version Id | [optional] 
**legislation_version** | **str** | LIS Legislation Version Name | [optional] 
**legislation_id** | **int** | LIS Legislation Database Unique Id | [optional] 
**legislation_number** | **str** | LIS Legislation Number, eg. SB1011 | [optional] 
**chamber_code** | **str** | Legislation Text Chamber Code | [optional] 
**legislation_chamber_code** | **str** | Legislation Chamber Code | [optional] 
**session_code** | **str** | Session Code | [optional] 
**legislation_text_action_id** | **int** | LIS Legislation Text Action Id | [optional] 
**document_code** | **str** | bill number with versioning (legacy) eg., HB11H1 | [optional] 
**draft_text** | **str** | LIS legislation text | [optional] 
**draft_title** | **str** | LIS legislation title or LDTtitle --typical for most bills, but not required for all legislation | [optional] 
**ld_number** | **str** | LIS legislation Document Number (LDNummber) | [optional] 
**version_date** | **datetime** | Text Version Date | [optional] 
**release_to_print** | **datetime** | Release To Print Date | [optional] 
**version_code** | **str** | Version Code | [optional] 
**event_code** | **str** | Event Code | [optional] 
**doc_url** | **str** | DocUrl | [optional] 
**link_url** | **str** | LinkUrl | [optional] 
**description** | **str** | Legislation Text Description | [optional] 
**sponsor** | **str** | Body that authored/sponsored the Legislation Text (House/Senate/Conference/Governor) | [optional] 
**sponsor_type_id** | **int** | unique identifier for sponsor type (e.g. 1&#x3D;House of Delegates, 2&#x3D;Senate, 3&#x3D;Committee, 4&#x3D;Member, etc) | [optional] 
**session_year** | **int** | Legislation Session Year | [optional] 
**is_public** | **bool** | Is this text available to the public | 
**is_active** | **bool** | Is this text active | 
**is_complete** | **bool** | Is complete? | [optional] 
**is_ihod** | **bool** | Is text from IHOD? | [optional] 
**governors_request** | **bool** | Is this at the Request of the Governor? | [optional] 
**dls_prepared** | **bool** | Is this text prepared by DLS? | 
**consent_required** | **bool** | Is consent required for this text? | [optional] 
**is_emergency** | **bool** | Is this text emergency ? | [optional] 
**is_reprint** | **bool** | Is this text Reprint ? | [optional] 
**is_plural** | **bool** | does this contain multiple items e.g. amendments? | [optional] 
**on_reconvene** | **bool** | for a Reconvened session? | [optional] 
**reference_ld_number** | **str** | LIS Reference legislation Document Number (LDNummber) | [optional] 
**text_disposition_id** | **int** | unique identifier for Text Disposition (e.g. 1&#x3D;Offered, 2&#x3D;Recommended, 3&#x3D;Reported, etc) | [optional] 
**text_disposition** | **str** | Text Disposition (e.g. Offered, Recommended, Reported, etc) | [optional] 
**reference_text_id** | **int** | LIS Reference Text Id | [optional] 
**committee_id** | **int** | Committee unique identifier | [optional] 
**committee_name** | **str** | Committee Name | [optional] 
**committee_number** | **str** | Committee assigned number(Example: H01, S01 or 001) | [optional] 
**pdf_file** | [**List[PDFFile]**](PDFFile.md) | List of PDFFile | [optional] 
**html_file** | [**List[HTMLFile]**](HTMLFile.md) | list of HTMLFile | [optional] 
**impact_file** | [**List[ImpactFile]**](ImpactFile.md) | List of ImpactFile | [optional] 
**link_file** | [**List[LinkFile]**](LinkFile.md) | List of LinkFile | [optional] 
**json_file** | [**List[JSONFile]**](JSONFile.md) | List of JSONFile | [optional] 
**patrons** | [**List[PatronBaseModel]**](PatronBaseModel.md) | list of patrons | [optional] 
**amendment_items** | [**List[AmendmentItem]**](AmendmentItem.md) |  | [optional] 
**legislation_class_id** | **int** |  LegislationClassID further identifies type of legislation beyond the standard Joint/Bill/Resolution defined with Legislation Type Code  1 Legislation  2 Memorial Resolution  3 Commending Resolution  4 Election of Judges  5 Budget | [optional] 
**legislation_class** | **str** | LIS Legislation Description (e.g: memorial or commending resolution) | [optional] 
**legislation_type** | **str** | legislation type description e.g. \&quot;Bill\&quot; | [optional] 

## Example

```python
from valis.models.legislation_text_get_response import LegislationTextGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextGetResponse from a JSON string
legislation_text_get_response_instance = LegislationTextGetResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextGetResponse.to_json())

# convert the object into a dict
legislation_text_get_response_dict = legislation_text_get_response_instance.to_dict()
# create an instance of LegislationTextGetResponse from a dict
legislation_text_get_response_from_dict = LegislationTextGetResponse.from_dict(legislation_text_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


