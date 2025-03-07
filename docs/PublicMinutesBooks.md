# PublicMinutesBooks

Public Response object containing a list of Minutes Books (using PublicMinutesBook).   If no valid response could be obtained, Success boolean will be false and additional   information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicMinutesBook]**](PublicMinutesBook.md) | list of MinutesBooks | [optional] 

## Example

```python
from valis.models.public_minutes_books import PublicMinutesBooks

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMinutesBooks from a JSON string
public_minutes_books_instance = PublicMinutesBooks.from_json(json)
# print the JSON string representation of the object
print(PublicMinutesBooks.to_json())

# convert the object into a dict
public_minutes_books_dict = public_minutes_books_instance.to_dict()
# create an instance of PublicMinutesBooks from a dict
public_minutes_books_from_dict = PublicMinutesBooks.from_dict(public_minutes_books_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


