# PublicLegislationSummariesResponse

listing of all legislative summaries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicLegislationSummaryResponse]**](PublicLegislationSummaryResponse.md) | list of persons | [optional] 
**search_criteria** | **str** | Search JSON used to product these results | [optional] 

## Example

```python
from valis.models.public_legislation_summaries_response import PublicLegislationSummariesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicLegislationSummariesResponse from a JSON string
public_legislation_summaries_response_instance = PublicLegislationSummariesResponse.from_json(json)
# print the JSON string representation of the object
print(PublicLegislationSummariesResponse.to_json())

# convert the object into a dict
public_legislation_summaries_response_dict = public_legislation_summaries_response_instance.to_dict()
# create an instance of PublicLegislationSummariesResponse from a dict
public_legislation_summaries_response_from_dict = PublicLegislationSummariesResponse.from_dict(public_legislation_summaries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


