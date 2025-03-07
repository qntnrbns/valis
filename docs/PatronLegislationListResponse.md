# PatronLegislationListResponse

patron legislation list

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
**legislation_number** | **str** | Legislation number | [optional] 
**sequence** | **int** | Patron Sequence # (e.g. 1001 &#x3D;&#x3D;&gt; Chief Patron) | [optional] 
**is_introducing** | **bool** | Is this patron introducing the bill? | [optional] 
**by_request** | **bool** | Is this by request of an entity? | [optional] 
**legislation** | [**List[Legislation]**](Legislation.md) | legislation | [optional] 

## Example

```python
from valis.models.patron_legislation_list_response import PatronLegislationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatronLegislationListResponse from a JSON string
patron_legislation_list_response_instance = PatronLegislationListResponse.from_json(json)
# print the JSON string representation of the object
print(PatronLegislationListResponse.to_json())

# convert the object into a dict
patron_legislation_list_response_dict = patron_legislation_list_response_instance.to_dict()
# create an instance of PatronLegislationListResponse from a dict
patron_legislation_list_response_from_dict = PatronLegislationListResponse.from_dict(patron_legislation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


