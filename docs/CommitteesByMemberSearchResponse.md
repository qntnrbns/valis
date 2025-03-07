# CommitteesByMemberSearchResponse

List of committees associated to a member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CommitteeByMemberResponse]**](CommitteeByMemberResponse.md) | List of committees associated to a member | [optional] 

## Example

```python
from valis.models.committees_by_member_search_response import CommitteesByMemberSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteesByMemberSearchResponse from a JSON string
committees_by_member_search_response_instance = CommitteesByMemberSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteesByMemberSearchResponse.to_json())

# convert the object into a dict
committees_by_member_search_response_dict = committees_by_member_search_response_instance.to_dict()
# create an instance of CommitteesByMemberSearchResponse from a dict
committees_by_member_search_response_from_dict = CommitteesByMemberSearchResponse.from_dict(committees_by_member_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


