# PublicGetCommunicationCategoryResponse

Information for Public Communication Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_id** | **int** | Unique identifier for Communication | [optional] 
**communication_category_type_id** | **int** | Unique identifier for Communication Category Type | [optional] 
**category_code** | **str** | Category code | [optional] 
**category_description** | **str** | Category description | [optional] 
**minutes_summary** | **str** | Minutes Summary (built from Legislation Communications) | [optional] 
**sequence** | **int** | Sequence | [optional] 
**plural_description** | **str** | Plural Communication description | [optional] 
**description** | **str** | Description | [optional] 
**communication_category_id** | **int** | Unique identifier for Communication Category | [optional] 
**communication_legislation** | [**List[PublicGetCommunicationLegislationResponse]**](PublicGetCommunicationLegislationResponse.md) | List of Communication Legislation | [optional] 

## Example

```python
from valis.models.public_get_communication_category_response import PublicGetCommunicationCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGetCommunicationCategoryResponse from a JSON string
public_get_communication_category_response_instance = PublicGetCommunicationCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(PublicGetCommunicationCategoryResponse.to_json())

# convert the object into a dict
public_get_communication_category_response_dict = public_get_communication_category_response_instance.to_dict()
# create an instance of PublicGetCommunicationCategoryResponse from a dict
public_get_communication_category_response_from_dict = PublicGetCommunicationCategoryResponse.from_dict(public_get_communication_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


