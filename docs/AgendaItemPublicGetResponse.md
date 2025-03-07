# AgendaItemPublicGetResponse

Public Agenda Item response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agenda_id** | **int** | Agenda ID | [optional] 
**description** | **str** | Agenda Item Description | [optional] 
**calendar_description** | **str** | Agenda Item Calendar Description (will be set with HTML formatting) | [optional] 
**ld_title** | **str** | LD Draft Title | [optional] 
**legislation_text_id** | **int** | Calendar Category Sequence | [optional] 
**ld_number** | **str** | Legislation Draft (LD)Number of the Amemdments | [optional] 
**draft_text** | **str** | Legislation Draft Text | [optional] 
**vote_id** | **int** | Vote unique Identifier | [optional] 
**is_active** | **bool** | is Agenda Item active | [optional] 
**sequence** | **int** | Sequence | [optional] 
**legislation_event_id** | **int** | unique identifier for legislation event | [optional] 
**agenda_item_id** | **int** | Agenda Item ID | [optional] 
**vote_member** | [**List[VoteMemberPublicGetResponse]**](VoteMemberPublicGetResponse.md) | list of Vote Members for Agenda Item | [optional] 

## Example

```python
from valis.models.agenda_item_public_get_response import AgendaItemPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgendaItemPublicGetResponse from a JSON string
agenda_item_public_get_response_instance = AgendaItemPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(AgendaItemPublicGetResponse.to_json())

# convert the object into a dict
agenda_item_public_get_response_dict = agenda_item_public_get_response_instance.to_dict()
# create an instance of AgendaItemPublicGetResponse from a dict
agenda_item_public_get_response_from_dict = AgendaItemPublicGetResponse.from_dict(agenda_item_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


