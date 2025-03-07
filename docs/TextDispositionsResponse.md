# TextDispositionsResponse

list of text dispositions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[TextDispositionResponse]**](TextDispositionResponse.md) | list of text dispositions | [optional] 

## Example

```python
from valis.models.text_dispositions_response import TextDispositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TextDispositionsResponse from a JSON string
text_dispositions_response_instance = TextDispositionsResponse.from_json(json)
# print the JSON string representation of the object
print(TextDispositionsResponse.to_json())

# convert the object into a dict
text_dispositions_response_dict = text_dispositions_response_instance.to_dict()
# create an instance of TextDispositionsResponse from a dict
text_dispositions_response_from_dict = TextDispositionsResponse.from_dict(text_dispositions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


