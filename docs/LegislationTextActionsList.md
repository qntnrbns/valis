# LegislationTextActionsList

list of legislation text actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationTextActionResponse]**](LegislationTextActionResponse.md) | list of Legislation Text Actions | [optional] 

## Example

```python
from valis.models.legislation_text_actions_list import LegislationTextActionsList

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextActionsList from a JSON string
legislation_text_actions_list_instance = LegislationTextActionsList.from_json(json)
# print the JSON string representation of the object
print(LegislationTextActionsList.to_json())

# convert the object into a dict
legislation_text_actions_list_dict = legislation_text_actions_list_instance.to_dict()
# create an instance of LegislationTextActionsList from a dict
legislation_text_actions_list_from_dict = LegislationTextActionsList.from_dict(legislation_text_actions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


