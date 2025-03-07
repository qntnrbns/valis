# CommunicationCategoryTypeReference

Information for Communication Category Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_category_type_id** | **int** | Unique identifier for Communication Category Type | [optional] 
**category_code** | **str** | Category code | [optional] 
**description** | **str** | Category description | [optional] 
**plural_description** | **str** | Plural Communication description | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**sequence** | **int** | Sequence | [optional] 

## Example

```python
from valis.models.communication_category_type_reference import CommunicationCategoryTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCategoryTypeReference from a JSON string
communication_category_type_reference_instance = CommunicationCategoryTypeReference.from_json(json)
# print the JSON string representation of the object
print(CommunicationCategoryTypeReference.to_json())

# convert the object into a dict
communication_category_type_reference_dict = communication_category_type_reference_instance.to_dict()
# create an instance of CommunicationCategoryTypeReference from a dict
communication_category_type_reference_from_dict = CommunicationCategoryTypeReference.from_dict(communication_category_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


