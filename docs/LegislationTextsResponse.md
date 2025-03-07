# LegislationTextsResponse

Legislation Texts Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationTextResponse]**](LegislationTextResponse.md) | list of legislation text | [optional] 

## Example

```python
from valis.models.legislation_texts_response import LegislationTextsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextsResponse from a JSON string
legislation_texts_response_instance = LegislationTextsResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextsResponse.to_json())

# convert the object into a dict
legislation_texts_response_dict = legislation_texts_response_instance.to_dict()
# create an instance of LegislationTextsResponse from a dict
legislation_texts_response_from_dict = LegislationTextsResponse.from_dict(legislation_texts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


