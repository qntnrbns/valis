# Legislation

Legislation Patron Response that uses the Legislation Base Model in the DAL

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
**legislation_class** | **str** | Legislation LegislationClass (identified by ID above) | [optional] 
**legislation_id** | **int** | Legislation ID | [optional] 
**legislation_key** | **int** | Legislation Key | [optional] 
**legislation_status** | **str** | Legislation Status | [optional] 
**effective_type** | **str** | Effective Type | [optional] 
**session_name** | **str** | Session Name | [optional] 
**is_prefile** | **bool** | IsPrefile | [optional] 

## Example

```python
from valis.models.legislation import Legislation

# TODO update the JSON string below
json = "{}"
# create an instance of Legislation from a JSON string
legislation_instance = Legislation.from_json(json)
# print the JSON string representation of the object
print(Legislation.to_json())

# convert the object into a dict
legislation_dict = legislation_instance.to_dict()
# create an instance of Legislation from a dict
legislation_from_dict = Legislation.from_dict(legislation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


