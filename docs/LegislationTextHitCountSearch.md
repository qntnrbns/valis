# LegislationTextHitCountSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[LegislationTextHitCountDocument]**](LegislationTextHitCountDocument.md) |  | [optional] 
**location** | **str** |  | [optional] 
**keyword_expression** | **str** |  | [optional] 
**word_list** | [**List[LegislationTextHitCountWord]**](LegislationTextHitCountWord.md) |  | [optional] 

## Example

```python
from valis.models.legislation_text_hit_count_search import LegislationTextHitCountSearch

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextHitCountSearch from a JSON string
legislation_text_hit_count_search_instance = LegislationTextHitCountSearch.from_json(json)
# print the JSON string representation of the object
print(LegislationTextHitCountSearch.to_json())

# convert the object into a dict
legislation_text_hit_count_search_dict = legislation_text_hit_count_search_instance.to_dict()
# create an instance of LegislationTextHitCountSearch from a dict
legislation_text_hit_count_search_from_dict = LegislationTextHitCountSearch.from_dict(legislation_text_hit_count_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


