# DocketCategoryPublicGetResponse

Docket Category Public Get Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | **int** | Calendar ID | [optional] 
**calendar_category_type_id** | **int** | Calendar Category Type ID | [optional] 
**category_code** | **str** | Category Code | [optional] 
**category_type** | **str** | Category Type | [optional] 
**description** | **str** | Calendar Category Type Description | [optional] 
**plural_description** | **str** | Calendar Category Type Description if plural | [optional] 
**sequence** | **int** | Calendar Category Sequence | [optional] 
**display_type** | **bool** | Display Calendar Category Type | [optional] 
**is_legislation_category** | **bool** | Legislation Indicator | [optional] 
**is_print** | **bool** | Printable Indicator | [optional] 
**calendar_category_id** | **int** | Calendar Category unique identifier | 
**docket_items** | [**List[DocketItemPublicGetResponse]**](DocketItemPublicGetResponse.md) | Listing of Docket Items | [optional] 

## Example

```python
from valis.models.docket_category_public_get_response import DocketCategoryPublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketCategoryPublicGetResponse from a JSON string
docket_category_public_get_response_instance = DocketCategoryPublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketCategoryPublicGetResponse.to_json())

# convert the object into a dict
docket_category_public_get_response_dict = docket_category_public_get_response_instance.to_dict()
# create an instance of DocketCategoryPublicGetResponse from a dict
docket_category_public_get_response_from_dict = DocketCategoryPublicGetResponse.from_dict(docket_category_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


