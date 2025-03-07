# LegislationTextDraftResponse

Slim class for used to get Legislation Draft from Legislation service call to legislationText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_text** | **str** |  | [optional] 

## Example

```python
from valis.models.legislation_text_draft_response import LegislationTextDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextDraftResponse from a JSON string
legislation_text_draft_response_instance = LegislationTextDraftResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextDraftResponse.to_json())

# convert the object into a dict
legislation_text_draft_response_dict = legislation_text_draft_response_instance.to_dict()
# create an instance of LegislationTextDraftResponse from a dict
legislation_text_draft_response_from_dict = LegislationTextDraftResponse.from_dict(legislation_text_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


