# VoteTypes

List of Vote Types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[VoteType]**](VoteType.md) | List of Vote Types | [optional] 

## Example

```python
from valis.models.vote_types import VoteTypes

# TODO update the JSON string below
json = "{}"
# create an instance of VoteTypes from a JSON string
vote_types_instance = VoteTypes.from_json(json)
# print the JSON string representation of the object
print(VoteTypes.to_json())

# convert the object into a dict
vote_types_dict = vote_types_instance.to_dict()
# create an instance of VoteTypes from a dict
vote_types_from_dict = VoteTypes.from_dict(vote_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


