# CalendarCategoryTypeResponse

Calendar Category Type Reference Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clerks_copy** | **bool** |  | [optional] 
**calendar_category_type_id** | **int** | Calendar Category unique identifier | 
**category_code** | **str** | Category Code | 
**description** | **str** | Category Type Description | 
**plural_description** | **str** | Category Type Description if plural | [optional] 
**sequence** | **int** | Sequence | 
**chamber_code** | **str** | Category Chamber Code (H &#x3D; House, S &#x3D; Senate) | [optional] 
**calendar_type_id** | **int** | Calendar Type ID | 
**category_type_id** | **int** | Category Type ID | 
**category_type** | **str** | Category Type | [optional] 
**display_type** | **bool** | Display Type | [optional] 
**legislation_type_code** | **str** | Legislation Type Code | [optional] 
**legislation_chamber_code** | **str** | Legislation Chamber Code | [optional] 
**is_legislation_category** | **bool** | Legislation Indicator | 
**is_print** | **bool** | Printable Indicator | [optional] 

## Example

```python
from valis.models.calendar_category_type_response import CalendarCategoryTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarCategoryTypeResponse from a JSON string
calendar_category_type_response_instance = CalendarCategoryTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CalendarCategoryTypeResponse.to_json())

# convert the object into a dict
calendar_category_type_response_dict = calendar_category_type_response_instance.to_dict()
# create an instance of CalendarCategoryTypeResponse from a dict
calendar_category_type_response_from_dict = CalendarCategoryTypeResponse.from_dict(calendar_category_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


