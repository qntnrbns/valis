# MembersContactInformationSearchResponse

List of Member Contact Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[MemberContactInformationSearchResponse]**](MemberContactInformationSearchResponse.md) | List of Member Contact Information | [optional] 

## Example

```python
from valis.models.members_contact_information_search_response import MembersContactInformationSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembersContactInformationSearchResponse from a JSON string
members_contact_information_search_response_instance = MembersContactInformationSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MembersContactInformationSearchResponse.to_json())

# convert the object into a dict
members_contact_information_search_response_dict = members_contact_information_search_response_instance.to_dict()
# create an instance of MembersContactInformationSearchResponse from a dict
members_contact_information_search_response_from_dict = MembersContactInformationSearchResponse.from_dict(members_contact_information_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


