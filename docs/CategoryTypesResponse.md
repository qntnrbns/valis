# CategoryTypesResponse

Categories Types Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CategoryTypeResponse]**](CategoryTypeResponse.md) | list of Calendar Actions | [optional] 

## Example

```python
from valis.models.category_types_response import CategoryTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryTypesResponse from a JSON string
category_types_response_instance = CategoryTypesResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryTypesResponse.to_json())

# convert the object into a dict
category_types_response_dict = category_types_response_instance.to_dict()
# create an instance of CategoryTypesResponse from a dict
category_types_response_from_dict = CategoryTypesResponse.from_dict(category_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


