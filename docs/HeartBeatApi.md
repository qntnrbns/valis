# valis.HeartBeatApi

All URIs are relative to *https://lis.virginia.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#api_heartbeat_heartbeatasync_get) | **GET** /api/heartbeat/heartbeatasync | Checks service health
[**authentication_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#authentication_api_heartbeat_heartbeatasync_get) | **GET** /Authentication/api/heartbeat/heartbeatasync | Checks service health
[**calendar_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#calendar_api_heartbeat_heartbeatasync_get) | **GET** /Calendar/api/heartbeat/heartbeatasync | Checks service health
[**committee_legislation_referral_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#committee_legislation_referral_api_heartbeat_heartbeatasync_get) | **GET** /CommitteeLegislationReferral/api/heartbeat/heartbeatasync | Checks service health
[**communication_file_generation_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#communication_file_generation_api_heartbeat_heartbeatasync_get) | **GET** /CommunicationFileGeneration/api/heartbeat/heartbeatasync | Checks service health
[**contact_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#contact_api_heartbeat_heartbeatasync_get) | **GET** /Contact/api/heartbeat/heartbeatasync | Checks service health
[**legislation_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_api_heartbeat_heartbeatasync_get) | **GET** /Legislation/api/heartbeat/heartbeatasync | Checks service health
[**legislation_by_member_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_by_member_api_heartbeat_heartbeatasync_get) | **GET** /LegislationByMember/api/heartbeat/heartbeatasync | Checks service health
[**legislation_collections_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_collections_api_heartbeat_heartbeatasync_get) | **GET** /LegislationCollections/api/heartbeat/heartbeatasync | Checks service health
[**legislation_communications_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_communications_api_heartbeat_heartbeatasync_get) | **GET** /LegislationCommunications/api/heartbeat/heartbeatasync | Checks service health
[**legislation_event_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_event_api_heartbeat_heartbeatasync_get) | **GET** /LegislationEvent/api/heartbeat/heartbeatasync | Checks service health
[**legislation_file_generation_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_file_generation_api_heartbeat_heartbeatasync_get) | **GET** /LegislationFileGeneration/api/heartbeat/heartbeatasync | Checks service health
[**legislation_patron_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_patron_api_heartbeat_heartbeatasync_get) | **GET** /LegislationPatron/api/heartbeat/heartbeatasync | Checks service health
[**legislation_subject_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_subject_api_heartbeat_heartbeatasync_get) | **GET** /LegislationSubject/api/heartbeat/heartbeatasync | Checks service health
[**legislation_summary_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_summary_api_heartbeat_heartbeatasync_get) | **GET** /LegislationSummary/api/heartbeat/heartbeatasync | Checks service health
[**legislation_text_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_text_api_heartbeat_heartbeatasync_get) | **GET** /LegislationText/api/heartbeat/heartbeatasync | Checks service health
[**legislation_version_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#legislation_version_api_heartbeat_heartbeatasync_get) | **GET** /LegislationVersion/api/heartbeat/heartbeatasync | Checks service health
[**member_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#member_api_heartbeat_heartbeatasync_get) | **GET** /Member/api/heartbeat/heartbeatasync | Checks service health
[**member_vote_search_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#member_vote_search_api_heartbeat_heartbeatasync_get) | **GET** /MemberVoteSearch/api/heartbeat/heartbeatasync | Checks service health
[**members_by_committee_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#members_by_committee_api_heartbeat_heartbeatasync_get) | **GET** /MembersByCommittee/api/heartbeat/heartbeatasync | Checks service health
[**minutes_book_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#minutes_book_api_heartbeat_heartbeatasync_get) | **GET** /MinutesBook/api/heartbeat/heartbeatasync | Checks service health
[**organization_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#organization_api_heartbeat_heartbeatasync_get) | **GET** /Organization/api/heartbeat/heartbeatasync | Checks service health
[**partner_authentication_api_heartbeat_heartbeatasync_get**](HeartBeatApi.md#partner_authentication_api_heartbeat_heartbeatasync_get) | **GET** /PartnerAuthentication/api/heartbeat/heartbeatasync | Checks service health


# **api_heartbeat_heartbeatasync_get**
> api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_api_heartbeat_heartbeatasync_get**
> authentication_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.authentication_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->authentication_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_api_heartbeat_heartbeatasync_get**
> calendar_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.calendar_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->calendar_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_legislation_referral_api_heartbeat_heartbeatasync_get**
> committee_legislation_referral_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.committee_legislation_referral_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->committee_legislation_referral_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **communication_file_generation_api_heartbeat_heartbeatasync_get**
> communication_file_generation_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.communication_file_generation_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->communication_file_generation_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_api_heartbeat_heartbeatasync_get**
> contact_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.contact_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->contact_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_api_heartbeat_heartbeatasync_get**
> legislation_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_by_member_api_heartbeat_heartbeatasync_get**
> legislation_by_member_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_by_member_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_by_member_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_collections_api_heartbeat_heartbeatasync_get**
> legislation_collections_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_collections_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_collections_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_communications_api_heartbeat_heartbeatasync_get**
> legislation_communications_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_communications_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_communications_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_event_api_heartbeat_heartbeatasync_get**
> legislation_event_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_event_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_event_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_file_generation_api_heartbeat_heartbeatasync_get**
> legislation_file_generation_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_file_generation_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_file_generation_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_patron_api_heartbeat_heartbeatasync_get**
> legislation_patron_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_patron_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_patron_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_subject_api_heartbeat_heartbeatasync_get**
> legislation_subject_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_subject_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_subject_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_summary_api_heartbeat_heartbeatasync_get**
> legislation_summary_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_summary_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_summary_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_text_api_heartbeat_heartbeatasync_get**
> legislation_text_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_text_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_text_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legislation_version_api_heartbeat_heartbeatasync_get**
> legislation_version_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.legislation_version_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->legislation_version_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_api_heartbeat_heartbeatasync_get**
> member_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.member_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->member_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_vote_search_api_heartbeat_heartbeatasync_get**
> member_vote_search_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.member_vote_search_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->member_vote_search_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_by_committee_api_heartbeat_heartbeatasync_get**
> members_by_committee_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.members_by_committee_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->members_by_committee_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minutes_book_api_heartbeat_heartbeatasync_get**
> minutes_book_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.minutes_book_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->minutes_book_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_api_heartbeat_heartbeatasync_get**
> organization_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Checks service health
        api_instance.organization_api_heartbeat_heartbeatasync_get(web_api_key=web_api_key)
    except Exception as e:
        print("Exception when calling HeartBeatApi->organization_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_api_key** | **str**| Partner WebAPIKey | [optional] 

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_authentication_api_heartbeat_heartbeatasync_get**
> partner_authentication_api_heartbeat_heartbeatasync_get()

Checks service health

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
    api_instance = valis.HeartBeatApi(api_client)

    try:
        # Checks service health
        api_instance.partner_authentication_api_heartbeat_heartbeatasync_get()
    except Exception as e:
        print("Exception when calling HeartBeatApi->partner_authentication_api_heartbeat_heartbeatasync_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

