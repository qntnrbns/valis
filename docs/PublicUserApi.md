# valis.PublicUserApi

All URIs are relative to *https://lis.virginia.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_createpublicuserasync_post**](PublicUserApi.md#api_createpublicuserasync_post) | **POST** /api/createpublicuserasync | Registers a User
[**api_registerpublicuserasync_post**](PublicUserApi.md#api_registerpublicuserasync_post) | **POST** /api/registerpublicuserasync | Initial registration of a User
[**api_requestresetuserpasswordasync_post**](PublicUserApi.md#api_requestresetuserpasswordasync_post) | **POST** /api/requestresetuserpasswordasync | Requests a Password Reset via email
[**api_resetuserpasswordasync_post**](PublicUserApi.md#api_resetuserpasswordasync_post) | **POST** /api/resetuserpasswordasync | Resets a user password


# **api_createpublicuserasync_post**
> CreateUserResponse api_createpublicuserasync_post(create_public_user_request, web_api_key=web_api_key)

Registers a User

### Example


```python
import valis
from valis.models.create_public_user_request import CreatePublicUserRequest
from valis.models.create_user_response import CreateUserResponse
from valis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lis.virginia.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = valis.Configuration(
    host = "https://lis.virginia.gov"
)


# Enter a context with an instance of the API client
with valis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = valis.PublicUserApi(api_client)
    create_public_user_request = valis.CreatePublicUserRequest() # CreatePublicUserRequest | CreatePublicUserRequest
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Registers a User
        api_response = api_instance.api_createpublicuserasync_post(create_public_user_request, web_api_key=web_api_key)
        print("The response of PublicUserApi->api_createpublicuserasync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicUserApi->api_createpublicuserasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_public_user_request** | [**CreatePublicUserRequest**](CreatePublicUserRequest.md)| CreatePublicUserRequest | 
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_registerpublicuserasync_post**
> api_registerpublicuserasync_post(email_address, web_api_key=web_api_key)

Initial registration of a User

### Example


```python
import valis
from valis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lis.virginia.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = valis.Configuration(
    host = "https://lis.virginia.gov"
)


# Enter a context with an instance of the API client
with valis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = valis.PublicUserApi(api_client)
    email_address = 'email_address_example' # str | emailAddress
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Initial registration of a User
        api_instance.api_registerpublicuserasync_post(email_address, web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling PublicUserApi->api_registerpublicuserasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| emailAddress | 
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_requestresetuserpasswordasync_post**
> api_requestresetuserpasswordasync_post(email_address, web_api_key=web_api_key)

Requests a Password Reset via email

### Example


```python
import valis
from valis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lis.virginia.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = valis.Configuration(
    host = "https://lis.virginia.gov"
)


# Enter a context with an instance of the API client
with valis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = valis.PublicUserApi(api_client)
    email_address = 'email_address_example' # str | emailAddress
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Requests a Password Reset via email
        api_instance.api_requestresetuserpasswordasync_post(email_address, web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling PublicUserApi->api_requestresetuserpasswordasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| emailAddress | 
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_resetuserpasswordasync_post**
> api_resetuserpasswordasync_post(user_information_request, web_api_key=web_api_key)

Resets a user password

### Example


```python
import valis
from valis.models.user_information_request import UserInformationRequest
from valis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lis.virginia.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = valis.Configuration(
    host = "https://lis.virginia.gov"
)


# Enter a context with an instance of the API client
with valis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = valis.PublicUserApi(api_client)
    user_information_request = valis.UserInformationRequest() # UserInformationRequest | userInformationRequest
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Resets a user password
        api_instance.api_resetuserpasswordasync_post(user_information_request, web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling PublicUserApi->api_resetuserpasswordasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_information_request** | [**UserInformationRequest**](UserInformationRequest.md)| userInformationRequest | 
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**202** | Success |  -  |
**204** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

