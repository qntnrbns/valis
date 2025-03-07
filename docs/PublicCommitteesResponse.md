# PublicCommitteesResponse

List of Public Committees

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicCommitteeResponse]**](PublicCommitteeResponse.md) | List of Public Committees | [optional] 

## Example

```python
from valis.models.public_committees_response import PublicCommitteesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCommitteesResponse from a JSON string
public_committees_response_instance = PublicCommitteesResponse.from_json(json)
# print the JSON string representation of the object
print(PublicCommitteesResponse.to_json())

# convert the object into a dict
public_committees_response_dict = public_committees_response_instance.to_dict()
# create an instance of PublicCommitteesResponse from a dict
public_committees_response_from_dict = PublicCommitteesResponse.from_dict(public_committees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


