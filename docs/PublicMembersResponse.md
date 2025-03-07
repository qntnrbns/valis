# PublicMembersResponse

List of Public Members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicMemberResponse]**](PublicMemberResponse.md) | list of Public Members | [optional] 

## Example

```python
from valis.models.public_members_response import PublicMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMembersResponse from a JSON string
public_members_response_instance = PublicMembersResponse.from_json(json)
# print the JSON string representation of the object
print(PublicMembersResponse.to_json())

# convert the object into a dict
public_members_response_dict = public_members_response_instance.to_dict()
# create an instance of PublicMembersResponse from a dict
public_members_response_from_dict = PublicMembersResponse.from_dict(public_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


