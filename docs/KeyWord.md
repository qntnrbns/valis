# KeyWord

Compound Keyword search ... and now supports major combinational concepts with operator and nested List of KeyWord objects (for parentheses)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword string to search on | [optional] 
**operator** | **str** | operator (defaults to OR, but can be AND instead) | [optional] 
**keywords** | [**List[KeyWord]**](KeyWord.md) | if this object serves as placeholder for parentheses, all KeyWord objects within this List are the elements (e.g. A and B) | [optional] 

## Example

```python
from valis.models.key_word import KeyWord

# TODO update the JSON string below
json = "{}"
# create an instance of KeyWord from a JSON string
key_word_instance = KeyWord.from_json(json)
# print the JSON string representation of the object
print(KeyWord.to_json())

# convert the object into a dict
key_word_dict = key_word_instance.to_dict()
# create an instance of KeyWord from a dict
key_word_from_dict = KeyWord.from_dict(key_word_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


