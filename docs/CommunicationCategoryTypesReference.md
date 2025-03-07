# CommunicationCategoryTypesReference

List of Communication Category Types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CommunicationCategoryTypeReference]**](CommunicationCategoryTypeReference.md) | list of Communication Category Types | [optional] 

## Example

```python
from valis.models.communication_category_types_reference import CommunicationCategoryTypesReference

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCategoryTypesReference from a JSON string
communication_category_types_reference_instance = CommunicationCategoryTypesReference.from_json(json)
# print the JSON string representation of the object
print(CommunicationCategoryTypesReference.to_json())

# convert the object into a dict
communication_category_types_reference_dict = communication_category_types_reference_instance.to_dict()
# create an instance of CommunicationCategoryTypesReference from a dict
communication_category_types_reference_from_dict = CommunicationCategoryTypesReference.from_dict(communication_category_types_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


