# PatronBaseModel

Patron Base Model - Use this base model for all Patron Objects.

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

## Example

```python
from valis.models.patron_base_model import PatronBaseModel

# TODO update the JSON string below
json = "{}"
# create an instance of PatronBaseModel from a JSON string
patron_base_model_instance = PatronBaseModel.from_json(json)
# print the JSON string representation of the object
print(PatronBaseModel.to_json())

# convert the object into a dict
patron_base_model_dict = patron_base_model_instance.to_dict()
# create an instance of PatronBaseModel from a dict
patron_base_model_from_dict = PatronBaseModel.from_dict(patron_base_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


