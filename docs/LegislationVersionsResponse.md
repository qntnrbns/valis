# LegislationVersionsResponse

list of legislation versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[LegislationVersionResponse1]**](LegislationVersionResponse1.md) | list of versions | [optional] 

## Example

```python
from valis.models.legislation_versions_response import LegislationVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationVersionsResponse from a JSON string
legislation_versions_response_instance = LegislationVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationVersionsResponse.to_json())

# convert the object into a dict
legislation_versions_response_dict = legislation_versions_response_instance.to_dict()
# create an instance of LegislationVersionsResponse from a dict
legislation_versions_response_from_dict = LegislationVersionsResponse.from_dict(legislation_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


