# MemberPatronTypesResponse

List of Member Patron Types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[MemberPatronTypeResponse]**](MemberPatronTypeResponse.md) | list of member patron types | [optional] 

## Example

```python
from valis.models.member_patron_types_response import MemberPatronTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPatronTypesResponse from a JSON string
member_patron_types_response_instance = MemberPatronTypesResponse.from_json(json)
# print the JSON string representation of the object
print(MemberPatronTypesResponse.to_json())

# convert the object into a dict
member_patron_types_response_dict = member_patron_types_response_instance.to_dict()
# create an instance of MemberPatronTypesResponse from a dict
member_patron_types_response_from_dict = MemberPatronTypesResponse.from_dict(member_patron_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


