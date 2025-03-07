# ShallowMinutesBooksResponse

Shallow list of MinutesBooks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ShallowMinuteBookResponse]**](ShallowMinuteBookResponse.md) | List of MinutesBooks | [optional] 

## Example

```python
from valis.models.shallow_minutes_books_response import ShallowMinutesBooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShallowMinutesBooksResponse from a JSON string
shallow_minutes_books_response_instance = ShallowMinutesBooksResponse.from_json(json)
# print the JSON string representation of the object
print(ShallowMinutesBooksResponse.to_json())

# convert the object into a dict
shallow_minutes_books_response_dict = shallow_minutes_books_response_instance.to_dict()
# create an instance of ShallowMinutesBooksResponse from a dict
shallow_minutes_books_response_from_dict = ShallowMinutesBooksResponse.from_dict(shallow_minutes_books_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


