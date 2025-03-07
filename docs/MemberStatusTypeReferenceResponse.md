# MemberStatusTypeReferenceResponse

Information for a Member Status Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_status_id** | **int** | Unique identifier for Member Status | [optional] 
**name** | **str** | Member Status name | [optional] 

## Example

```python
from valis.models.member_status_type_reference_response import MemberStatusTypeReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberStatusTypeReferenceResponse from a JSON string
member_status_type_reference_response_instance = MemberStatusTypeReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(MemberStatusTypeReferenceResponse.to_json())

# convert the object into a dict
member_status_type_reference_response_dict = member_status_type_reference_response_instance.to_dict()
# create an instance of MemberStatusTypeReferenceResponse from a dict
member_status_type_reference_response_from_dict = MemberStatusTypeReferenceResponse.from_dict(member_status_type_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


