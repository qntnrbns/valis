# ConferenceLegislationList

Conference Legislation Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | Legislation unique identifier | [optional] 
**legislation_number** | **str** | Legislation Number (Numerical Part of the Legislation Number) | [optional] 
**full_number** | **str** | Full Legislation Number | [optional] 
**description** | **str** | Legislation Description | [optional] 
**introduction_date** | **datetime** | Introduction Date | [optional] 
**offered_date** | **datetime** | Offered Date | [optional] 
**chamber_code** | **str** | Chamber Code Example: H &#x3D; House or S &#x3D; Summary | [optional] 
**legislation_type_code** | **str** | Legislation Type Code | [optional] 
**legislation_class_id** | **int** | Legislation Class ID | [optional] 
**legislation_class** | **str** | Legislation Class | [optional] 
**legislation_key** | **int** | Legislation Key | [optional] 
**legislation_status** | **str** | Legislation Status | [optional] 
**effective_type** | **str** | Effective Type | [optional] 
**session_id** | **int** | Session ID | [optional] 
**session_name** | **str** | Session Name | [optional] 
**is_prefile** | **bool** | Is Prefiled Legislation | [optional] 

## Example

```python
from valis.models.conference_legislation_list import ConferenceLegislationList

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceLegislationList from a JSON string
conference_legislation_list_instance = ConferenceLegislationList.from_json(json)
# print the JSON string representation of the object
print(ConferenceLegislationList.to_json())

# convert the object into a dict
conference_legislation_list_dict = conference_legislation_list_instance.to_dict()
# create an instance of ConferenceLegislationList from a dict
conference_legislation_list_from_dict = ConferenceLegislationList.from_dict(conference_legislation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


