# LegislationAmendmentResponse

Legislation with Amendments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **int** | Unique identifier for Session | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**legislation_class_id** | **int** | Unique identifier for Legislation Class | [optional] 
**legislation_number** | **str** | Legislation number | [optional] 
**description** | **str** | Legislation Description/Catchline | [optional] 
**legislation_title** | **str** |  | [optional] 
**offered_date** | **datetime** | Legislation Offered date | [optional] 
**introduction_date** | **datetime** | Legislation Introduction date | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**legislation_type_code** | **str** | Legislation Type Code description | [optional] 
**full_number** | **str** | Full Number of the bill | [optional] 
**legislation_status_id** | **int** | Unique identifier for Legislative Status | [optional] 
**legislation_id** | **int** | Legislation unique identifier | [optional] 
**legislation_key** | **int** | Legislation Key (Numerical Part of the Legislation Number) | [optional] 
**legislation_status** | **str** | Legislative Status | [optional] 
**legislation_summary** | **str** | Legislation Summary | [optional] 
**legislation_text_id** | **int** | The ID of the latest legislation text for this piece of legislation | [optional] 
**effective_type** | **str** | Determines whether the enaction of the legislation is standard/emergency/other | [optional] 
**effective_type_id** | **int** | ID of EffectiveType | [optional] 
**pending_change** | **bool** | Tells whether a piece of legislation text on this legislation has any unpublished changes | [optional] 
**summary_version** | **str** | Summary Version | [optional] 
**session_name** | **str** | Session Name (ex. 2018 Regular Session) | [optional] 
**committee_name** | **str** | Committee Name (ex. Commerce and Labor) | [optional] 
**committee_id** | **int** | Committee ID | [optional] 
**parent_committee_name** | **str** | Parent Committee Name | [optional] 
**committee_number** | **str** | Committee Number | [optional] 
**amendments** | [**List[AmendmentResponse]**](AmendmentResponse.md) | List of Amendments on the associated Legislation | [optional] 
**patrons** | [**List[LegislationPatron]**](LegislationPatron.md) | List of Patrons on the associated Legislation | [optional] 

## Example

```python
from valis.models.legislation_amendment_response import LegislationAmendmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationAmendmentResponse from a JSON string
legislation_amendment_response_instance = LegislationAmendmentResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationAmendmentResponse.to_json())

# convert the object into a dict
legislation_amendment_response_dict = legislation_amendment_response_instance.to_dict()
# create an instance of LegislationAmendmentResponse from a dict
legislation_amendment_response_from_dict = LegislationAmendmentResponse.from_dict(legislation_amendment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


