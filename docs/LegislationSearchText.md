# LegislationSearchText

Information for Legislation Version Keyword Searching

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_id** | **int** | Unique identifier for Legislation Text | [optional] 
**description** | **str** | Legislation Version description | [optional] 
**document_code** | **str** | Legislation Document code | [optional] 
**count_matches** | **int** | Count of Keyword Matches | [optional] 

## Example

```python
from valis.models.legislation_search_text import LegislationSearchText

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationSearchText from a JSON string
legislation_search_text_instance = LegislationSearchText.from_json(json)
# print the JSON string representation of the object
print(LegislationSearchText.to_json())

# convert the object into a dict
legislation_search_text_dict = legislation_search_text_instance.to_dict()
# create an instance of LegislationSearchText from a dict
legislation_search_text_from_dict = LegislationSearchText.from_dict(legislation_search_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


