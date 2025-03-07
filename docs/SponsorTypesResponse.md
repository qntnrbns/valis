# SponsorTypesResponse

list of sponsor types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[SponsorTypeResponse]**](SponsorTypeResponse.md) | list of sponsor types | [optional] 

## Example

```python
from valis.models.sponsor_types_response import SponsorTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorTypesResponse from a JSON string
sponsor_types_response_instance = SponsorTypesResponse.from_json(json)
# print the JSON string representation of the object
print(SponsorTypesResponse.to_json())

# convert the object into a dict
sponsor_types_response_dict = sponsor_types_response_instance.to_dict()
# create an instance of SponsorTypesResponse from a dict
sponsor_types_response_from_dict = SponsorTypesResponse.from_dict(sponsor_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


