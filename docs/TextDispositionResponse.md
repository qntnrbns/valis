# TextDispositionResponse

Text Disposition reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_disposition_id** | **int** | unique identifier of the Text Disposition | [optional] 
**name** | **str** | name of the Text Disposition | [optional] 

## Example

```python
from valis.models.text_disposition_response import TextDispositionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TextDispositionResponse from a JSON string
text_disposition_response_instance = TextDispositionResponse.from_json(json)
# print the JSON string representation of the object
print(TextDispositionResponse.to_json())

# convert the object into a dict
text_disposition_response_dict = text_disposition_response_instance.to_dict()
# create an instance of TextDispositionResponse from a dict
text_disposition_response_from_dict = TextDispositionResponse.from_dict(text_disposition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


