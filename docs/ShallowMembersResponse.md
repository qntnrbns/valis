# ShallowMembersResponse

List of shallow members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ShallowMemberResponse]**](ShallowMemberResponse.md) | List of shallow members | [optional] 

## Example

```python
from valis.models.shallow_members_response import ShallowMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShallowMembersResponse from a JSON string
shallow_members_response_instance = ShallowMembersResponse.from_json(json)
# print the JSON string representation of the object
print(ShallowMembersResponse.to_json())

# convert the object into a dict
shallow_members_response_dict = shallow_members_response_instance.to_dict()
# create an instance of ShallowMembersResponse from a dict
shallow_members_response_from_dict = ShallowMembersResponse.from_dict(shallow_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


