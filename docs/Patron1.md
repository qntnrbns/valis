# Patron1

Information for Patron

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
**by_request** | **bool** | Is this patronage by request of a state agency/entity? | [optional] 

## Example

```python
from valis.models.patron1 import Patron1

# TODO update the JSON string below
json = "{}"
# create an instance of Patron1 from a JSON string
patron1_instance = Patron1.from_json(json)
# print the JSON string representation of the object
print(Patron1.to_json())

# convert the object into a dict
patron1_dict = patron1_instance.to_dict()
# create an instance of Patron1 from a dict
patron1_from_dict = Patron1.from_dict(patron1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


