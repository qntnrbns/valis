# PublicPersonnelResponse

Information for Public Personnel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staff_id** | **int** | Unique identifier for Staff | [optional] 
**affiliation_id** | **int** | Unique identifier for Committee | [optional] 
**staff_role_type_id** | **int** | Unique identifier for Staff Role Type | [optional] 
**identity_id** | **int** | Unique identifier for Identity (associated person) | [optional] 
**organization_name** | **str** | Organization Name | [optional] 
**full_name** | **str** | Person&#39;s name | [optional] 
**phone_number** | **str** | Person&#39;s phone number | [optional] 
**email_address** | **str** | Email address | [optional] 
**sequence** | **int** | Sequence | [optional] 
**is_public** | **bool** | is this public? | [optional] 
**effective_begin_date** | **datetime** | Effective begin date for this assignment | [optional] 
**effective_end_date** | **datetime** | Effective End date for this assignment | [optional] 

## Example

```python
from valis.models.public_personnel_response import PublicPersonnelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPersonnelResponse from a JSON string
public_personnel_response_instance = PublicPersonnelResponse.from_json(json)
# print the JSON string representation of the object
print(PublicPersonnelResponse.to_json())

# convert the object into a dict
public_personnel_response_dict = public_personnel_response_instance.to_dict()
# create an instance of PublicPersonnelResponse from a dict
public_personnel_response_from_dict = PublicPersonnelResponse.from_dict(public_personnel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


