# AuthenticationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Email Address (\&quot;UserPrincipalName\&quot;) | [optional] 
**last_name** | **str** | First Name (\&quot;GivenName\&quot;) | [optional] 
**first_name** | **str** | Last Name (\&quot;Surname\&quot;) | [optional] 
**unique_id** | **str** | Active Directory unique identifier (\&quot;Id\&quot;) | [optional] 
**groups** | **str** | list of groups the user is part of | [optional] 
**access_token** | **str** | JWT access token created by LIS to contain the the user group claims | [optional] 
**graph_token** | **str** | JWT access token issued by Graph API when successfully logged in | [optional] 
**refresh_token** | **str** | JWT refresh token which can be used to obtain new access tokens | [optional] 
**access_token_lifetime** | **int** | Access Token Lifetime in seconds - returned when successfully logged in | [optional] 
**claims** | [**GroupRolesResponse**](GroupRolesResponse.md) |  | [optional] 
**success** | **bool** | is this response valid? (true&#x3D;success, false&#x3D;unsuccessful) | [optional] 
**failure_message** | **str** | message describing why this response was not successful | [optional] 
**cache_key_name** | **str** | Cache Key Name for GetResponses | [optional] 
**is_password_temporary_or_expired** | **bool** | Boolean flags password if it&#39;s temporary or expired | [optional] 

## Example

```python
from valis.models.authentication_response import AuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationResponse from a JSON string
authentication_response_instance = AuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationResponse.to_json())

# convert the object into a dict
authentication_response_dict = authentication_response_instance.to_dict()
# create an instance of AuthenticationResponse from a dict
authentication_response_from_dict = AuthenticationResponse.from_dict(authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


