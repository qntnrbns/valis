# MembersByCommitteeSearchResponse

Search list of Members by Committee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[MemberByCommitteeSearchResponse]**](MemberByCommitteeSearchResponse.md) | Search list of Members by Committee | [optional] 

## Example

```python
from valis.models.members_by_committee_search_response import MembersByCommitteeSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembersByCommitteeSearchResponse from a JSON string
members_by_committee_search_response_instance = MembersByCommitteeSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MembersByCommitteeSearchResponse.to_json())

# convert the object into a dict
members_by_committee_search_response_dict = members_by_committee_search_response_instance.to_dict()
# create an instance of MembersByCommitteeSearchResponse from a dict
members_by_committee_search_response_from_dict = MembersByCommitteeSearchResponse.from_dict(members_by_committee_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


