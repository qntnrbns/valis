# MemberStatusTypesReferenceResponse

List of Member Status Types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[MemberStatusTypeReferenceResponse]**](MemberStatusTypeReferenceResponse.md) | list of Member Status Types | [optional] 

## Example

```python
from valis.models.member_status_types_reference_response import MemberStatusTypesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberStatusTypesReferenceResponse from a JSON string
member_status_types_reference_response_instance = MemberStatusTypesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(MemberStatusTypesReferenceResponse.to_json())

# convert the object into a dict
member_status_types_reference_response_dict = member_status_types_reference_response_instance.to_dict()
# create an instance of MemberStatusTypesReferenceResponse from a dict
member_status_types_reference_response_from_dict = MemberStatusTypesReferenceResponse.from_dict(member_status_types_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


