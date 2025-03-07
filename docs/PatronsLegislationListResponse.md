# PatronsLegislationListResponse

patron legislation list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PatronLegislationListResponse]**](PatronLegislationListResponse.md) | list of patron legislation | [optional] 

## Example

```python
from valis.models.patrons_legislation_list_response import PatronsLegislationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatronsLegislationListResponse from a JSON string
patrons_legislation_list_response_instance = PatronsLegislationListResponse.from_json(json)
# print the JSON string representation of the object
print(PatronsLegislationListResponse.to_json())

# convert the object into a dict
patrons_legislation_list_response_dict = patrons_legislation_list_response_instance.to_dict()
# create an instance of PatronsLegislationListResponse from a dict
patrons_legislation_list_response_from_dict = PatronsLegislationListResponse.from_dict(patrons_legislation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


