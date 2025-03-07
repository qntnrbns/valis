# LegislationIdsListResponse

List of Legislation IDs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**sort_by** | **str** | Which column to sort legislation by | [optional] 
**delete_all_legislation_cache** | **bool** | Should delete from cache all legislation? | [optional] 
**legislation_ids** | [**List[LegislationIdListResponse]**](LegislationIdListResponse.md) | List of Legislation IDs | [optional] 

## Example

```python
from valis.models.legislation_ids_list_response import LegislationIdsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationIdsListResponse from a JSON string
legislation_ids_list_response_instance = LegislationIdsListResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationIdsListResponse.to_json())

# convert the object into a dict
legislation_ids_list_response_dict = legislation_ids_list_response_instance.to_dict()
# create an instance of LegislationIdsListResponse from a dict
legislation_ids_list_response_from_dict = LegislationIdsListResponse.from_dict(legislation_ids_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


