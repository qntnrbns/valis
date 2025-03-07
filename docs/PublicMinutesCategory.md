# PublicMinutesCategory

Public Minutes Category that usually contains multiple entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes_book_id** | **int** | unique identifier for Minutes Book | [optional] 
**sequence** | **int** | unique identifier for Sequence | [optional] 
**calendar_category_type_id** | **int** | unique identifier for Calendar Category type | [optional] 
**category_description** | **str** | Category description | [optional] 
**category_text** | **str** | Category Text | [optional] 
**release_to_preview** | **bool** | is it Released To Preview or not | [optional] 
**category_type_id** | **int** | unique identifier for Category type | [optional] 
**category_type** | **str** | Category type | [optional] 
**display_type** | **bool** | display type is true/false | [optional] 
**chamber_code** | **str** | Chamber Code (H&#x3D;House/S&#x3D;Senate) | [optional] 
**category_code** | **str** | Category Code | [optional] 
**deletion_date** | **datetime** | Deletion Date | [optional] 
**minutes_category_id** | **int** | unique identifier for Minutes Category | [optional] 
**minutes_entries** | [**List[PublicMinutesEntry]**](PublicMinutesEntry.md) | Collection of associated entries | [optional] 

## Example

```python
from valis.models.public_minutes_category import PublicMinutesCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesCategory from a JSON string
public_minutes_category_instance = PublicMinutesCategory.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesCategory.to_json())

# convert the object into a dict
public_minutes_category_dict = public_minutes_category_instance.to_dict()
# create an instance of PublicMinutesCategory from a dict
public_minutes_category_from_dict = PublicMinutesCategory.from_dict(public_minutes_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


