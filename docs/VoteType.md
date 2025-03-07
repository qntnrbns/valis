# VoteType

Information for a Vote Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Description/Name of the ID | [optional] 
**id** | **int** | Unique identifier for Vote Type | [optional] 

## Example

```python
from valis.models.vote_type import VoteType

# TODO update the JSON string below
json = "{}"
# create an instance of VoteType from a JSON string
vote_type_instance = VoteType.from_json(json)
# print the JSON string representation of the object
print(VoteType.to_json())

# convert the object into a dict
vote_type_dict = vote_type_instance.to_dict()
# create an instance of VoteType from a dict
vote_type_from_dict = VoteType.from_dict(vote_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


