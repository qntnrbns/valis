# DocketItemPublicGetResponse

Docket Item Public Get Response which includes ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | Sequence of Docket(Committee Calendar) Items | [optional] 
**docket_id** | **int** | Docket(Committee Calendar) ID | [optional] 
**category_type** | **str** | Category Type | [optional] 
**docket_category_id** | **int** | Docket(Committee Calendar) Category ID | [optional] 
**category_code** | **str** | Category Code | [optional] 
**description** | **str** | Docket Category Description | [optional] 
**legislation_id** | **int** | Legislation ID | [optional] 
**legislation_number** | **str** | Legislation Number | [optional] 
**legislation_description** | **str** | Legislation Description | [optional] 
**ld_number** | **str** | Legislation Draft (LD)Number | [optional] 
**summary** | **str** | Legislation Summary | [optional] 
**draft_title** | **str** | Draft Title | [optional] 
**is_active** | **bool** | is Agenda Item active | [optional] 
**calendar_category_template_id** | **int** | Calendar Category Template ID | [optional] 
**communication_id** | **int** | Communication ID | [optional] 
**committee_id** | **int** | CommitteeID | [optional] 
**candidate_date** | **datetime** | Candidate Date | [optional] 
**docket_item_id** | **int** | Unique Identifier for Docket Item ID | [optional] 
**patrons** | [**List[PatronPartnerGetResponse]**](PatronPartnerGetResponse.md) | list of Patrons for an Docket Item | [optional] 

## Example

```python
from valis.models.docket_item_public_get_response import DocketItemPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketItemPublicGetResponse from a JSON string
docket_item_public_get_response_instance = DocketItemPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketItemPublicGetResponse.to_json())

# convert the object into a dict
docket_item_public_get_response_dict = docket_item_public_get_response_instance.to_dict()
# create an instance of DocketItemPublicGetResponse from a dict
docket_item_public_get_response_from_dict = DocketItemPublicGetResponse.from_dict(docket_item_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


