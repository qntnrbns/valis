# MemberPatronTypeResponse

Member Patron Type for a unique MemberID and Session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patron_type_id** | **int** | patron type id | [optional] 
**name** | **str** | name | [optional] 
**display_name** | **str** | display name | [optional] 

## Example

```python
from valis.models.member_patron_type_response import MemberPatronTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPatronTypeResponse from a JSON string
member_patron_type_response_instance = MemberPatronTypeResponse.from_json(json)
# print the JSON string representation of the object
print(MemberPatronTypeResponse.to_json())

# convert the object into a dict
member_patron_type_response_dict = member_patron_type_response_instance.to_dict()
# create an instance of MemberPatronTypeResponse from a dict
member_patron_type_response_from_dict = MemberPatronTypeResponse.from_dict(member_patron_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


