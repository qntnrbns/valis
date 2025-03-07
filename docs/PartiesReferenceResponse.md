# PartiesReferenceResponse

List of Political Parties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PartyReferenceResponse]**](PartyReferenceResponse.md) | list of Politcal Parties | [optional] 

## Example

```python
from valis.models.parties_reference_response import PartiesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartiesReferenceResponse from a JSON string
parties_reference_response_instance = PartiesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(PartiesReferenceResponse.to_json())

# convert the object into a dict
parties_reference_response_dict = parties_reference_response_instance.to_dict()
# create an instance of PartiesReferenceResponse from a dict
parties_reference_response_from_dict = PartiesReferenceResponse.from_dict(parties_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


