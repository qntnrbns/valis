# PublicPersonResponse

Public Response object containing LIS person information. If no valid response   could be obtained, Success boolean will be false and additional information can be found   in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **int** | Person unique identifier | [optional] 
**full_name** | **str** | Full Name | [optional] 
**first_name** | **str** | First Name | [optional] 
**middle_name** | **str** | Middle Name or Initial | [optional] 
**last_name** | **str** | Last Name | [optional] 
**prefix** | **str** | Prefix like Mr, Mrs or Sir | [optional] 
**suffix** | **str** | Suffix like Sr.or Jr. | [optional] 
**alternate_name** | **str** | Alternate Name | [optional] 
**creation_date** | **datetime** | Creation Date | [optional] 

## Example

```python
from valis.models.public_person_response import PublicPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPersonResponse from a JSON string
public_person_response_instance = PublicPersonResponse.from_json(json)
# print the JSON string representation of the object
print(PublicPersonResponse.to_json())

# convert the object into a dict
public_person_response_dict = public_person_response_instance.to_dict()
# create an instance of PublicPersonResponse from a dict
public_person_response_from_dict = PublicPersonResponse.from_dict(public_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


