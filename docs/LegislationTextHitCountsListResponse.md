# LegislationTextHitCountsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**hit_counts** | [**List[LegislationTextHitCountListResponse]**](LegislationTextHitCountListResponse.md) |  | [optional] 

## Example

```python
from valis.models.legislation_text_hit_counts_list_response import LegislationTextHitCountsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextHitCountsListResponse from a JSON string
legislation_text_hit_counts_list_response_instance = LegislationTextHitCountsListResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextHitCountsListResponse.to_json())

# convert the object into a dict
legislation_text_hit_counts_list_response_dict = legislation_text_hit_counts_list_response_instance.to_dict()
# create an instance of LegislationTextHitCountsListResponse from a dict
legislation_text_hit_counts_list_response_from_dict = LegislationTextHitCountsListResponse.from_dict(legislation_text_hit_counts_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


