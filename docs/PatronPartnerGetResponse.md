# PatronPartnerGetResponse

Patron Response for Calendars, Dockets and House Agendas(Potentially)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | Database Unique Identifier for Legislation | [optional] 
**legislation_text_id** | **int** | Database Unique Identifier for Legislation Text | [optional] 
**chamber_code** | **str** | Chamber Code | [optional] 
**member_id** | **int** | Databse Unique Identifier for Member | [optional] 
**member_number** | **str** | Member Number | [optional] 
**patron_type_id** | **int** | Databse Unique Identifier for Patron Type ID | [optional] 
**name** | **str** | Role Name | [optional] 
**display_name** | **str** | Role Display Name | [optional] 
**member_display_name** | **str** | Member Display Name | [optional] 
**patron_display_name** | **str** | Patron Display Name | [optional] 
**by_request** | **bool** | Is this draft by request of a state agency or entity ? | [optional] 

## Example

```python
from valis.models.patron_partner_get_response import PatronPartnerGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatronPartnerGetResponse from a JSON string
patron_partner_get_response_instance = PatronPartnerGetResponse.from_json(json)
# print the JSON string representation of the object
print(PatronPartnerGetResponse.to_json())

# convert the object into a dict
patron_partner_get_response_dict = patron_partner_get_response_instance.to_dict()
# create an instance of PatronPartnerGetResponse from a dict
patron_partner_get_response_from_dict = PatronPartnerGetResponse.from_dict(patron_partner_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


