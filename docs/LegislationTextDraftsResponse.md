# LegislationTextDraftsResponse

list of LegislationTextDraftResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationTextDraftResponse]**](LegislationTextDraftResponse.md) | list of text drafts | [optional] 

## Example

```python
from valis.models.legislation_text_drafts_response import LegislationTextDraftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextDraftsResponse from a JSON string
legislation_text_drafts_response_instance = LegislationTextDraftsResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextDraftsResponse.to_json())

# convert the object into a dict
legislation_text_drafts_response_dict = legislation_text_drafts_response_instance.to_dict()
# create an instance of LegislationTextDraftsResponse from a dict
legislation_text_drafts_response_from_dict = LegislationTextDraftsResponse.from_dict(legislation_text_drafts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


