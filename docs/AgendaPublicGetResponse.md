# AgendaPublicGetResponse

Public Agenda Get Response (includes Id)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | Sequence of Agenda | [optional] 
**calendar_category_id** | **int** | Calendar Category ID | [optional] 
**is_hidden** | **bool** | Is the CalendarCategoryTemplate hidden? | [optional] 
**description** | **str** | Description | [optional] 
**legislation_id** | **int** | Legislation ID | [optional] 
**legislation_key** | **int** | Legislation Key | [optional] 
**legislation_number** | **str** | Legislation Number | [optional] 
**legislation_description** | **str** | Legislation Description | [optional] 
**ld_number** | **str** | Legislation Draft (LD)Number | [optional] 
**summary** | **str** | Legislation Summary | [optional] 
**draft_title** | **str** | Draft Title | [optional] 
**is_active** | **bool** | is Agenda Item active | [optional] 
**calendar_category_template_id** | **int** | Calendar Category Template ID | [optional] 
**communication_id** | **int** | Communication ID | [optional] 
**page_number** | **int** | Page Number | [optional] 
**effective_type** | **str** | Effective Type | [optional] 
**committee_id** | **int** |  | [optional] 
**candidate_date** | **datetime** |  | [optional] 
**agenda_id** | **int** | Agenda unique identifier | 
**patrons** | [**List[PatronPartnerGetResponse]**](PatronPartnerGetResponse.md) | list of Patrons for an agenda | [optional] 
**agenda_items** | [**List[AgendaItemPublicGetResponse]**](AgendaItemPublicGetResponse.md) | list of Agenda Items for Agenda | [optional] 
**display_type** | **bool** | should the calendar item&#39;s type be displayed | [optional] 
**legislation_title** | **str** | Legislation Title | [optional] 

## Example

```python
from valis.models.agenda_public_get_response import AgendaPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgendaPublicGetResponse from a JSON string
agenda_public_get_response_instance = AgendaPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(AgendaPublicGetResponse.to_json())

# convert the object into a dict
agenda_public_get_response_dict = agenda_public_get_response_instance.to_dict()
# create an instance of AgendaPublicGetResponse from a dict
agenda_public_get_response_from_dict = AgendaPublicGetResponse.from_dict(agenda_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


