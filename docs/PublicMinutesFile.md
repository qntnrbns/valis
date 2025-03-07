# PublicMinutesFile

Minute File repsonse object inside MinutesBook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes_book_id** | **int** | Minutes Book unique identifier | [optional] 
**file_url** | **str** | File URL | [optional] 
**text_format_id** | **int** | Text Format ID | [optional] 
**is_active** | **bool** | Is Active true/false | [optional] 
**minutes_file_id** | **int** | unique identifier for Minutes File | [optional] 

## Example

```python
from valis.models.public_minutes_file import PublicMinutesFile

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesFile from a JSON string
public_minutes_file_instance = PublicMinutesFile.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesFile.to_json())

# convert the object into a dict
public_minutes_file_dict = public_minutes_file_instance.to_dict()
# create an instance of PublicMinutesFile from a dict
public_minutes_file_from_dict = PublicMinutesFile.from_dict(public_minutes_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


