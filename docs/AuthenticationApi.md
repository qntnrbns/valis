# valis.AuthenticationApi

All URIs are relative to *https://lis.virginia.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_api_authenticationheartbeatasync_get**](AuthenticationApi.md#authentication_api_authenticationheartbeatasync_get) | **GET** /Authentication/api/authenticationheartbeatasync | Gets telemetry on service health
[**authentication_api_changepasswordasync_put**](AuthenticationApi.md#authentication_api_changepasswordasync_put) | **PUT** /Authentication/api/changepasswordasync | Changes your password
[**authentication_api_getaccesstokenasync_post**](AuthenticationApi.md#authentication_api_getaccesstokenasync_post) | **POST** /Authentication/api/getaccesstokenasync | Get Access Token
[**authentication_api_loginasync_post**](AuthenticationApi.md#authentication_api_loginasync_post) | **POST** /Authentication/api/loginasync | Makes a request to login
[**authentication_api_refreshaccesstokenasync_post**](AuthenticationApi.md#authentication_api_refreshaccesstokenasync_post) | **POST** /Authentication/api/refreshaccesstokenasync | Refreshes the access token


# **authentication_api_authenticationheartbeatasync_get**
> HeartBeatPublicModel authentication_api_authenticationheartbeatasync_get(web_api_key=web_api_key)

Gets telemetry on service health

### Example


```python
import valis
from valis.models.heart_beat_public_model import HeartBeatPublicModel
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
    api_instance = valis.AuthenticationApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Gets telemetry on service health
        api_response = api_instance.authentication_api_authenticationheartbeatasync_get(web_api_key=web_api_key)
        print("The response of AuthenticationApi->authentication_api_authenticationheartbeatasync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_api_authenticationheartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

[**HeartBeatPublicModel**](HeartBeatPublicModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_api_changepasswordasync_put**
> AuthenticationResponse authentication_api_changepasswordasync_put(username, password, newpassword, web_api_key=web_api_key)

Changes your password

### Example


```python
import valis
from valis.models.authentication_response import AuthenticationResponse
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
    api_instance = valis.AuthenticationApi(api_client)
    username = 'username_example' # str | username (email address format)
    password = 'password_example' # str | existing password
    newpassword = 'newpassword_example' # str | new password
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Changes your password
        api_response = api_instance.authentication_api_changepasswordasync_put(username, password, newpassword, web_api_key=web_api_key)
        print("The response of AuthenticationApi->authentication_api_changepasswordasync_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_api_changepasswordasync_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username (email address format) | 
 **password** | **str**| existing password | 
 **newpassword** | **str**| new password | 
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_api_getaccesstokenasync_post**
> AuthenticationResponse authentication_api_getaccesstokenasync_post(access_token, expiresin=expiresin, web_api_key=web_api_key)

Get Access Token

### Example


```python
import valis
from valis.models.authentication_response import AuthenticationResponse
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
    api_instance = valis.AuthenticationApi(api_client)
    access_token = 'access_token_example' # str | 
    expiresin = 56 # int |  (optional)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Get Access Token
        api_response = api_instance.authentication_api_getaccesstokenasync_post(access_token, expiresin=expiresin, web_api_key=web_api_key)
        print("The response of AuthenticationApi->authentication_api_getaccesstokenasync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_api_getaccesstokenasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **expiresin** | **int**|  | [optional] 
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_api_loginasync_post**
> AuthenticationResponse authentication_api_loginasync_post(web_api_key=web_api_key, login_request=login_request)

Makes a request to login

### Example


```python
import valis
from valis.models.authentication_response import AuthenticationResponse
from valis.models.login_request import LoginRequest
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
    api_instance = valis.AuthenticationApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)
    login_request = valis.LoginRequest() # LoginRequest | LoginRequest (optional)

    try:
        # Makes a request to login
        api_response = api_instance.authentication_api_loginasync_post(web_api_key=web_api_key, login_request=login_request)
        print("The response of AuthenticationApi->authentication_api_loginasync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_api_loginasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 
 **login_request** | [**LoginRequest**](LoginRequest.md)| LoginRequest | [optional] 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_api_refreshaccesstokenasync_post**
> AuthenticationResponse authentication_api_refreshaccesstokenasync_post(web_api_key=web_api_key)

Refreshes the access token

### Example


```python
import valis
from valis.models.authentication_response import AuthenticationResponse
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
    api_instance = valis.AuthenticationApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Refreshes the access token
        api_response = api_instance.authentication_api_refreshaccesstokenasync_post(web_api_key=web_api_key)
        print("The response of AuthenticationApi->authentication_api_refreshaccesstokenasync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_api_refreshaccesstokenasync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

