# CategoryTypeResponse

Category Type Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Description/Name of the ID | [optional] 
**id** | **int** | Category Type unique identifier | [optional] 

## Example

```python
from valis.models.category_type_response import CategoryTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryTypeResponse from a JSON string
category_type_response_instance = CategoryTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryTypeResponse.to_json())

# convert the object into a dict
category_type_response_dict = category_type_response_instance.to_dict()
# create an instance of CategoryTypeResponse from a dict
category_type_response_from_dict = CategoryTypeResponse.from_dict(category_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


