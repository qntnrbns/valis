# PublicGetCommunicationLegislationResponse

Information for Public Get Communication Legislation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_category_id** | **int** | Unique identifier for Communication Category | [optional] 
**legislation_id** | **int** | Unique identifier for Legislation | [optional] 
**legislation_number** | **str** | Legislation number | [optional] 
**legislation_key** | **int** | Legislation key | [optional] 
**legislation_description** | **str** | Legislation description | [optional] 
**is_active** | **bool** | Is this active? | [optional] 
**legislation_text_id** | **int** | Unique identifier for Legislation Text | [optional] 
**committee_referred_name** | **str** | Committee Referred Name | [optional] 
**event_code** | **str** | Event code | [optional] 
**document_code** | **str** | Document code | [optional] 
**ld_number** | **str** | LD number | [optional] 
**draft_title** | **str** | Draft Title | [optional] 
**vote_id** | **int** | Unique identifier for Vote | [optional] 
**vote_number** | **str** | Vote number | [optional] 
**suffix** | **str** | Legislation suffix | [optional] 
**effective_type_id** | **int** | Unique identifier for Effective Type ID | [optional] 
**effective_type** | **str** | Effective Type | [optional] 
**is_candidate** | **bool** | Does this communication include bills that are a candidate? | [optional] 
**communication_legislation_id** | **int** | Unique identifier for CommunicationLegislation | [optional] 
**patrons** | [**List[Patron1]**](Patron1.md) | List of Patrons | [optional] 

## Example

```python
from valis.models.public_get_communication_legislation_response import PublicGetCommunicationLegislationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGetCommunicationLegislationResponse from a JSON string
public_get_communication_legislation_response_instance = PublicGetCommunicationLegislationResponse.from_json(json)
# print the JSON string representation of the object
print(PublicGetCommunicationLegislationResponse.to_json())

# convert the object into a dict
public_get_communication_legislation_response_dict = public_get_communication_legislation_response_instance.to_dict()
# create an instance of PublicGetCommunicationLegislationResponse from a dict
public_get_communication_legislation_response_from_dict = PublicGetCommunicationLegislationResponse.from_dict(public_get_communication_legislation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


