# CreatePublicUserRequest

Response for registering a new Public User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashed_word** | **str** | Registration hash | 
**first_name** | **str** | User&#39;s first name | [optional] 
**last_name** | **str** | User&#39;s last name | [optional] 
**password** | **str** | Password | 

## Example

```python
from valis.models.create_public_user_request import CreatePublicUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePublicUserRequest from a JSON string
create_public_user_request_instance = CreatePublicUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePublicUserRequest.to_json())

# convert the object into a dict
create_public_user_request_dict = create_public_user_request_instance.to_dict()
# create an instance of CreatePublicUserRequest from a dict
create_public_user_request_from_dict = CreatePublicUserRequest.from_dict(create_public_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


