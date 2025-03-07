# UserInformationRequest

User Information request containing random hash, submitted email address and expiration date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashed_word** | **str** | hash of a random word | [optional] 
**email_address** | **str** | email address submitted for registration | [optional] 
**expiration_date** | **datetime** | when this registration cache object should expire | [optional] 

## Example

```python
from valis.models.user_information_request import UserInformationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserInformationRequest from a JSON string
user_information_request_instance = UserInformationRequest.from_json(json)
# print the JSON string representation of the object
print(UserInformationRequest.to_json())

# convert the object into a dict
user_information_request_dict = user_information_request_instance.to_dict()
# create an instance of UserInformationRequest from a dict
user_information_request_from_dict = UserInformationRequest.from_dict(user_information_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


