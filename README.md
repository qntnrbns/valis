# valis

A Package for exploring the VA LIS API

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/qntnrbns/valis.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/qntnrbns/valis.git`)

Then import the package:
```python
import valis
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import valis
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = valis.AuthenticationApi(api_client)
    web_api_key = 'web_api_key_example' # str | Partner WebAPIKey (optional)

    try:
        # Gets telemetry on service health
        api_response = api_instance.authentication_api_authenticationheartbeatasync_get(web_api_key=web_api_key)
        print("The response of AuthenticationApi->authentication_api_authenticationheartbeatasync_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->authentication_api_authenticationheartbeatasync_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://lis.virginia.gov*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**authentication_api_authenticationheartbeatasync_get**](docs/AuthenticationApi.md#authentication_api_authenticationheartbeatasync_get) | **GET** /Authentication/api/authenticationheartbeatasync | Gets telemetry on service health
*AuthenticationApi* | [**authentication_api_changepasswordasync_put**](docs/AuthenticationApi.md#authentication_api_changepasswordasync_put) | **PUT** /Authentication/api/changepasswordasync | Changes your password
*AuthenticationApi* | [**authentication_api_getaccesstokenasync_post**](docs/AuthenticationApi.md#authentication_api_getaccesstokenasync_post) | **POST** /Authentication/api/getaccesstokenasync | Get Access Token
*AuthenticationApi* | [**authentication_api_loginasync_post**](docs/AuthenticationApi.md#authentication_api_loginasync_post) | **POST** /Authentication/api/loginasync | Makes a request to login
*AuthenticationApi* | [**authentication_api_refreshaccesstokenasync_post**](docs/AuthenticationApi.md#authentication_api_refreshaccesstokenasync_post) | **POST** /Authentication/api/refreshaccesstokenasync | Refreshes the access token
*HeartBeatApi* | [**api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#api_heartbeat_heartbeatasync_get) | **GET** /api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**authentication_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#authentication_api_heartbeat_heartbeatasync_get) | **GET** /Authentication/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**calendar_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#calendar_api_heartbeat_heartbeatasync_get) | **GET** /Calendar/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**committee_legislation_referral_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#committee_legislation_referral_api_heartbeat_heartbeatasync_get) | **GET** /CommitteeLegislationReferral/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**communication_file_generation_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#communication_file_generation_api_heartbeat_heartbeatasync_get) | **GET** /CommunicationFileGeneration/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**contact_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#contact_api_heartbeat_heartbeatasync_get) | **GET** /Contact/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_api_heartbeat_heartbeatasync_get) | **GET** /Legislation/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_by_member_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_by_member_api_heartbeat_heartbeatasync_get) | **GET** /LegislationByMember/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_collections_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_collections_api_heartbeat_heartbeatasync_get) | **GET** /LegislationCollections/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_communications_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_communications_api_heartbeat_heartbeatasync_get) | **GET** /LegislationCommunications/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_event_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_event_api_heartbeat_heartbeatasync_get) | **GET** /LegislationEvent/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_file_generation_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_file_generation_api_heartbeat_heartbeatasync_get) | **GET** /LegislationFileGeneration/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_patron_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_patron_api_heartbeat_heartbeatasync_get) | **GET** /LegislationPatron/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_subject_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_subject_api_heartbeat_heartbeatasync_get) | **GET** /LegislationSubject/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_summary_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_summary_api_heartbeat_heartbeatasync_get) | **GET** /LegislationSummary/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_text_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_text_api_heartbeat_heartbeatasync_get) | **GET** /LegislationText/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**legislation_version_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#legislation_version_api_heartbeat_heartbeatasync_get) | **GET** /LegislationVersion/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**member_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#member_api_heartbeat_heartbeatasync_get) | **GET** /Member/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**member_vote_search_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#member_vote_search_api_heartbeat_heartbeatasync_get) | **GET** /MemberVoteSearch/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**members_by_committee_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#members_by_committee_api_heartbeat_heartbeatasync_get) | **GET** /MembersByCommittee/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**minutes_book_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#minutes_book_api_heartbeat_heartbeatasync_get) | **GET** /MinutesBook/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**organization_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#organization_api_heartbeat_heartbeatasync_get) | **GET** /Organization/api/heartbeat/heartbeatasync | Checks service health
*HeartBeatApi* | [**partner_authentication_api_heartbeat_heartbeatasync_get**](docs/HeartBeatApi.md#partner_authentication_api_heartbeat_heartbeatasync_get) | **GET** /PartnerAuthentication/api/heartbeat/heartbeatasync | Checks service health
*PublicActionsApi* | [**api_clearpubliccache_get**](docs/PublicActionsApi.md#api_clearpubliccache_get) | **GET** /api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**api_getchamberstatisticsasync_get**](docs/PublicActionsApi.md#api_getchamberstatisticsasync_get) | **GET** /api/getchamberstatisticsasync | Gets Chamber Statistics by session
*PublicActionsApi* | [**api_getclerkpersonnellistasync_get**](docs/PublicActionsApi.md#api_getclerkpersonnellistasync_get) | **GET** /api/getclerkpersonnellistasync | Gets a list of Committee Clerks (Personnel)
*PublicActionsApi* | [**api_getcommitteebyidasync_get**](docs/PublicActionsApi.md#api_getcommitteebyidasync_get) | **GET** /api/getcommitteebyidasync | Gets a committee by unique identifier
*PublicActionsApi* | [**api_getcommitteelistasync_get**](docs/PublicActionsApi.md#api_getcommitteelistasync_get) | **GET** /api/getcommitteelistasync | Gets a shallow list of Committees
*PublicActionsApi* | [**api_getcommitteestatisticsasync_get**](docs/PublicActionsApi.md#api_getcommitteestatisticsasync_get) | **GET** /api/getcommitteestatisticsasync | Gets Committee Statistics by session and chamber
*PublicActionsApi* | [**api_getdefaultsessionasync_get**](docs/PublicActionsApi.md#api_getdefaultsessionasync_get) | **GET** /api/getdefaultsessionasync | Gets a list of Sessions marked as default
*PublicActionsApi* | [**api_getmeetingroomsreferenceasync_get**](docs/PublicActionsApi.md#api_getmeetingroomsreferenceasync_get) | **GET** /api/getmeetingroomsreferenceasync | Gets a list of Meeting Rooms by Chamber Code
*PublicActionsApi* | [**api_getpersonbyidasync_identity_id_get**](docs/PublicActionsApi.md#api_getpersonbyidasync_identity_id_get) | **GET** /api/getpersonbyidasync/{identityId} | Gets a list of Persons by unique identifier
*PublicActionsApi* | [**api_getpersonlistasync_get**](docs/PublicActionsApi.md#api_getpersonlistasync_get) | **GET** /api/getpersonlistasync | Gets a list of Persons
*PublicActionsApi* | [**api_getpersonnellistasync_get**](docs/PublicActionsApi.md#api_getpersonnellistasync_get) | **GET** /api/getpersonnellistasync | Gets a list of Committee Staff (Personnel)
*PublicActionsApi* | [**api_getreferencesasync_get**](docs/PublicActionsApi.md#api_getreferencesasync_get) | **GET** /api/getreferencesasync | Gets a list of Personnel
*PublicActionsApi* | [**api_getschedulelistasync_get**](docs/PublicActionsApi.md#api_getschedulelistasync_get) | **GET** /api/getschedulelistasync | Gets a list of Meetings for non Docket and Calendar related items
*PublicActionsApi* | [**api_getscheduletypesreferenceasync_get**](docs/PublicActionsApi.md#api_getscheduletypesreferenceasync_get) | **GET** /api/getscheduletypesreferenceasync | Gets a list of Schedule Types
*PublicActionsApi* | [**api_getsessionbycodeasync_session_code_get**](docs/PublicActionsApi.md#api_getsessionbycodeasync_session_code_get) | **GET** /api/getsessionbycodeasync/{sessionCode} | Gets a list of Sessions by session code
*PublicActionsApi* | [**api_getsessionbyidasync_session_id_get**](docs/PublicActionsApi.md#api_getsessionbyidasync_session_id_get) | **GET** /api/getsessionbyidasync/{sessionId} | Get a list of Session by unique identifier
*PublicActionsApi* | [**api_getsessioneventtypereferencesasync_get**](docs/PublicActionsApi.md#api_getsessioneventtypereferencesasync_get) | **GET** /api/getsessioneventtypereferencesasync | Gets a list of Session Event Types
*PublicActionsApi* | [**api_getsessionlistasync_get**](docs/PublicActionsApi.md#api_getsessionlistasync_get) | **GET** /api/getsessionlistasync | Gets a list of Sessions
*PublicActionsApi* | [**api_getsessionsbyyearasync_year_get**](docs/PublicActionsApi.md#api_getsessionsbyyearasync_year_get) | **GET** /api/getsessionsbyyearasync/{year} | Gets a list of Sessions for a specific year
*PublicActionsApi* | [**api_getsessionshallowlistasync_get**](docs/PublicActionsApi.md#api_getsessionshallowlistasync_get) | **GET** /api/getsessionshallowlistasync | Gets a shallow list of Sessions
*PublicActionsApi* | [**api_getsessiontypereferencesasync_get**](docs/PublicActionsApi.md#api_getsessiontypereferencesasync_get) | **GET** /api/getsessiontypereferencesasync | Gets a list of Session Types
*PublicActionsApi* | [**api_getshallowvoteasync_get**](docs/PublicActionsApi.md#api_getshallowvoteasync_get) | **GET** /api/getshallowvoteasync | Gets a list of Shallow Votes
*PublicActionsApi* | [**api_getstaffpersonnellistasync_get**](docs/PublicActionsApi.md#api_getstaffpersonnellistasync_get) | **GET** /api/getstaffpersonnellistasync | Gets a list of Committee DLS Staff (Personnel)
*PublicActionsApi* | [**api_getstaffroletypesasync_get**](docs/PublicActionsApi.md#api_getstaffroletypesasync_get) | **GET** /api/getstaffroletypesasync | Gets a list of Staff Role Types
*PublicActionsApi* | [**api_getvotebyidasync_get**](docs/PublicActionsApi.md#api_getvotebyidasync_get) | **GET** /api/getvotebyidasync | Gets a Public Vote
*PublicActionsApi* | [**api_getvotelinksasync_get**](docs/PublicActionsApi.md#api_getvotelinksasync_get) | **GET** /api/getvotelinksasync | Gets a list of Vote Links for a given unique identifier
*PublicActionsApi* | [**api_getvotetypereferencesasync_get**](docs/PublicActionsApi.md#api_getvotetypereferencesasync_get) | **GET** /api/getvotetypereferencesasync | Gets a list of Vote Types
*PublicActionsApi* | [**api_heartbeatasync_get**](docs/PublicActionsApi.md#api_heartbeatasync_get) | **GET** /api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**api_previewvcalfileasync_get**](docs/PublicActionsApi.md#api_previewvcalfileasync_get) | **GET** /api/previewvcalfileasync | Generates vCal file for Meetings
*PublicActionsApi* | [**calendar_api_clearpubliccache_get**](docs/PublicActionsApi.md#calendar_api_clearpubliccache_get) | **GET** /Calendar/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**calendar_api_getcalendaractionsreferenceasync_get**](docs/PublicActionsApi.md#calendar_api_getcalendaractionsreferenceasync_get) | **GET** /Calendar/api/getcalendaractionsreferenceasync | Gets a List of Calendar Actions
*PublicActionsApi* | [**calendar_api_getcalendarcategorytypesreferenceasync_get**](docs/PublicActionsApi.md#calendar_api_getcalendarcategorytypesreferenceasync_get) | **GET** /Calendar/api/getcalendarcategorytypesreferenceasync | Gets a List of Calendar Categories
*PublicActionsApi* | [**calendar_api_getcalendarlistasync_get**](docs/PublicActionsApi.md#calendar_api_getcalendarlistasync_get) | **GET** /Calendar/api/getcalendarlistasync | Gets a List of Calendars
*PublicActionsApi* | [**calendar_api_getcalendarsbyidasync_get**](docs/PublicActionsApi.md#calendar_api_getcalendarsbyidasync_get) | **GET** /Calendar/api/getcalendarsbyidasync | Gets a List of Public Calendar using unique identifier
*PublicActionsApi* | [**calendar_api_getcalendartypesreferenceasync_get**](docs/PublicActionsApi.md#calendar_api_getcalendartypesreferenceasync_get) | **GET** /Calendar/api/getcalendartypesreferenceasync | Gets a List of Calendar Types
*PublicActionsApi* | [**calendar_api_getcategorytypesreferenceasync_get**](docs/PublicActionsApi.md#calendar_api_getcategorytypesreferenceasync_get) | **GET** /Calendar/api/getcategorytypesreferenceasync | Gets a List of Calendar Category Types
*PublicActionsApi* | [**calendar_api_getdocketlistasync_get**](docs/PublicActionsApi.md#calendar_api_getdocketlistasync_get) | **GET** /Calendar/api/getdocketlistasync | Gets a List of Dockets
*PublicActionsApi* | [**calendar_api_getdocketlistbycommitteenumberasync_get**](docs/PublicActionsApi.md#calendar_api_getdocketlistbycommitteenumberasync_get) | **GET** /Calendar/api/getdocketlistbycommitteenumberasync | Get a List of Dockets by Session Code, Committee Number and Chamber Code  Only Show Public Dockets
*PublicActionsApi* | [**calendar_api_getdocketsbyidasync_get**](docs/PublicActionsApi.md#calendar_api_getdocketsbyidasync_get) | **GET** /Calendar/api/getdocketsbyidasync | Gets a List of Public Dockets using unique identifier
*PublicActionsApi* | [**calendar_api_heartbeatasync_get**](docs/PublicActionsApi.md#calendar_api_heartbeatasync_get) | **GET** /Calendar/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**committee_api_getcommitteesasync_get**](docs/PublicActionsApi.md#committee_api_getcommitteesasync_get) | **GET** /Committee/api/getcommitteesasync | Gets a list of Committees
*PublicActionsApi* | [**committee_legislation_referral_api_clearpubliccache_get**](docs/PublicActionsApi.md#committee_legislation_referral_api_clearpubliccache_get) | **GET** /CommitteeLegislationReferral/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**committee_legislation_referral_api_getcommitteeactionreferencesasync_get**](docs/PublicActionsApi.md#committee_legislation_referral_api_getcommitteeactionreferencesasync_get) | **GET** /CommitteeLegislationReferral/api/getcommitteeactionreferencesasync | Gets a list of Committee Actions
*PublicActionsApi* | [**committee_legislation_referral_api_heartbeatasync_get**](docs/PublicActionsApi.md#committee_legislation_referral_api_heartbeatasync_get) | **GET** /CommitteeLegislationReferral/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**communication_file_generation_api_heartbeatasync_get**](docs/PublicActionsApi.md#communication_file_generation_api_heartbeatasync_get) | **GET** /CommunicationFileGeneration/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**contact_api_clearpubliccache_get**](docs/PublicActionsApi.md#contact_api_clearpubliccache_get) | **GET** /Contact/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**contact_api_getcontactbyidasync_contact_information_id_get**](docs/PublicActionsApi.md#contact_api_getcontactbyidasync_contact_information_id_get) | **GET** /Contact/api/getcontactbyidasync/{contactInformationId} | Gets a list of Contacts by unique identifier
*PublicActionsApi* | [**contact_api_getcontactlistasync_get**](docs/PublicActionsApi.md#contact_api_getcontactlistasync_get) | **GET** /Contact/api/getcontactlistasync | Get a list of LIS Contacts using unique identifier
*PublicActionsApi* | [**contact_api_getcontactsbycontacttypeidasync_contact_type_id_get**](docs/PublicActionsApi.md#contact_api_getcontactsbycontacttypeidasync_contact_type_id_get) | **GET** /Contact/api/getcontactsbycontacttypeidasync/{contactTypeID} | Gets a list of Contacts by a contact type
*PublicActionsApi* | [**contact_api_getcontactsbyownerasync_get**](docs/PublicActionsApi.md#contact_api_getcontactsbyownerasync_get) | **GET** /Contact/api/getcontactsbyownerasync | Gets a list of Contacts by Owner
*PublicActionsApi* | [**contact_api_getcontactsbystatusasync_status_get**](docs/PublicActionsApi.md#contact_api_getcontactsbystatusasync_status_get) | **GET** /Contact/api/getcontactsbystatusasync/{status} | Gets a list of Contacts by status
*PublicActionsApi* | [**contact_api_getcontacttypereferencesasync_get**](docs/PublicActionsApi.md#contact_api_getcontacttypereferencesasync_get) | **GET** /Contact/api/getcontacttypereferencesasync | Gets a list of Contact Types
*PublicActionsApi* | [**contact_api_getownertypereferencesasync_get**](docs/PublicActionsApi.md#contact_api_getownertypereferencesasync_get) | **GET** /Contact/api/getownertypereferencesasync | Gets a list of Owner Types
*PublicActionsApi* | [**contact_api_heartbeatasync_get**](docs/PublicActionsApi.md#contact_api_heartbeatasync_get) | **GET** /Contact/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_api_clearpubliccache_get) | **GET** /Legislation/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_api_getconferencelegislationlistasync_get**](docs/PublicActionsApi.md#legislation_api_getconferencelegislationlistasync_get) | **GET** /Legislation/api/getconferencelegislationlistasync | Gets a list of Conference Legislation
*PublicActionsApi* | [**legislation_api_getlegislationamendmentlistasync_get**](docs/PublicActionsApi.md#legislation_api_getlegislationamendmentlistasync_get) | **GET** /Legislation/api/getlegislationamendmentlistasync | Gets a list of Public Legislation with Amendments by Session
*PublicActionsApi* | [**legislation_api_getlegislationbyidasync_legislation_id_get**](docs/PublicActionsApi.md#legislation_api_getlegislationbyidasync_legislation_id_get) | **GET** /Legislation/api/getlegislationbyidasync/{legislationID} | Gets a list of Public Legislation using unique identifier
*PublicActionsApi* | [**legislation_api_getlegislationbylegislationidsasync_post**](docs/PublicActionsApi.md#legislation_api_getlegislationbylegislationidsasync_post) | **POST** /Legislation/api/getlegislationbylegislationidsasync | Gets a list of Legislation based on set of Legislation IDs
*PublicActionsApi* | [**legislation_api_getlegislationidslistasync_post**](docs/PublicActionsApi.md#legislation_api_getlegislationidslistasync_post) | **POST** /Legislation/api/getlegislationidslistasync | Gets a list of Legislation IDs
*PublicActionsApi* | [**legislation_api_getlegislationlistasync_post**](docs/PublicActionsApi.md#legislation_api_getlegislationlistasync_post) | **POST** /Legislation/api/getlegislationlistasync | Gets a list of Public Legislation
*PublicActionsApi* | [**legislation_api_getlegislationsessionlistasync_get**](docs/PublicActionsApi.md#legislation_api_getlegislationsessionlistasync_get) | **GET** /Legislation/api/getlegislationsessionlistasync | Gets a list of Public Legislation by Session
*PublicActionsApi* | [**legislation_api_getlegislationstatuslistasync_get**](docs/PublicActionsApi.md#legislation_api_getlegislationstatuslistasync_get) | **GET** /Legislation/api/getlegislationstatuslistasync | Gets a list of Legislation Statuses
*PublicActionsApi* | [**legislation_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_api_heartbeatasync_get) | **GET** /Legislation/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_by_member_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_by_member_api_clearpubliccache_get) | **GET** /LegislationByMember/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_by_member_api_getmemberlegislationlistasync_get**](docs/PublicActionsApi.md#legislation_by_member_api_getmemberlegislationlistasync_get) | **GET** /LegislationByMember/api/getmemberlegislationlistasync | Gets a list of Member Legislation
*PublicActionsApi* | [**legislation_by_member_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_by_member_api_heartbeatasync_get) | **GET** /LegislationByMember/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_collections_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_collections_api_heartbeatasync_get) | **GET** /LegislationCollections/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_communications_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_communications_api_clearpubliccache_get) | **GET** /LegislationCommunications/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_communications_api_getcommunicationcategoryreferencesasync_get**](docs/PublicActionsApi.md#legislation_communications_api_getcommunicationcategoryreferencesasync_get) | **GET** /LegislationCommunications/api/getcommunicationcategoryreferencesasync | Gets a list of Legislation Communication Categories
*PublicActionsApi* | [**legislation_communications_api_getlegislationcommunicationsbloburlasync_get**](docs/PublicActionsApi.md#legislation_communications_api_getlegislationcommunicationsbloburlasync_get) | **GET** /LegislationCommunications/api/getlegislationcommunicationsbloburlasync | Gets a Legislation Communication Files
*PublicActionsApi* | [**legislation_communications_api_getlegislationcommunicationsbyidasync_get**](docs/PublicActionsApi.md#legislation_communications_api_getlegislationcommunicationsbyidasync_get) | **GET** /LegislationCommunications/api/getlegislationcommunicationsbyidasync | Gets a Legislation Communication
*PublicActionsApi* | [**legislation_communications_api_getlegislationcommunicationslistasync_get**](docs/PublicActionsApi.md#legislation_communications_api_getlegislationcommunicationslistasync_get) | **GET** /LegislationCommunications/api/getlegislationcommunicationslistasync | Gets a list of Legislation Communications
*PublicActionsApi* | [**legislation_communications_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_communications_api_heartbeatasync_get) | **GET** /LegislationCommunications/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_event_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_event_api_clearpubliccache_get) | **GET** /LegislationEvent/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_event_api_getactortypereferencesasync_get**](docs/PublicActionsApi.md#legislation_event_api_getactortypereferencesasync_get) | **GET** /LegislationEvent/api/getactortypereferencesasync | Gets a list of Actor Types
*PublicActionsApi* | [**legislation_event_api_getlegislationeventbyidasync_legislation_event_id_get**](docs/PublicActionsApi.md#legislation_event_api_getlegislationeventbyidasync_legislation_event_id_get) | **GET** /LegislationEvent/api/getlegislationeventbyidasync/{legislationEventID} | Gets a list of Legislation Events by unique identifier
*PublicActionsApi* | [**legislation_event_api_getlegislationeventbylegislationidasync_get**](docs/PublicActionsApi.md#legislation_event_api_getlegislationeventbylegislationidasync_get) | **GET** /LegislationEvent/api/getlegislationeventbylegislationidasync | Gets a list of Legislation Events by Legislation
*PublicActionsApi* | [**legislation_event_api_getlegislationeventtypereferencesasync_get**](docs/PublicActionsApi.md#legislation_event_api_getlegislationeventtypereferencesasync_get) | **GET** /LegislationEvent/api/getlegislationeventtypereferencesasync | Gets a list of Legislation Event Types
*PublicActionsApi* | [**legislation_event_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_event_api_heartbeatasync_get) | **GET** /LegislationEvent/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_file_generation_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_file_generation_api_heartbeatasync_get) | **GET** /LegislationFileGeneration/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_patron_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_patron_api_clearpubliccache_get) | **GET** /LegislationPatron/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_patron_api_getlegislationpatronlistasync_get**](docs/PublicActionsApi.md#legislation_patron_api_getlegislationpatronlistasync_get) | **GET** /LegislationPatron/api/getlegislationpatronlistasync | Gets a List of Legislation Patrons
*PublicActionsApi* | [**legislation_patron_api_getlegislationpatronsbyidasync_legislation_id_get**](docs/PublicActionsApi.md#legislation_patron_api_getlegislationpatronsbyidasync_legislation_id_get) | **GET** /LegislationPatron/api/getlegislationpatronsbyidasync/{legislationID} | Gets a list of Patrons using legislation unique identifier
*PublicActionsApi* | [**legislation_patron_api_getmemberpatrontypelistasync_get**](docs/PublicActionsApi.md#legislation_patron_api_getmemberpatrontypelistasync_get) | **GET** /LegislationPatron/api/getmemberpatrontypelistasync | Gets a List of Member Patron Types
*PublicActionsApi* | [**legislation_patron_api_getpatronroletypelistasync_get**](docs/PublicActionsApi.md#legislation_patron_api_getpatronroletypelistasync_get) | **GET** /LegislationPatron/api/getpatronroletypelistasync | Gets a list of Patron Role Types
*PublicActionsApi* | [**legislation_patron_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_patron_api_heartbeatasync_get) | **GET** /LegislationPatron/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_subject_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_subject_api_clearpubliccache_get) | **GET** /LegislationSubject/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_subject_api_getsubjectreferencesasync_get**](docs/PublicActionsApi.md#legislation_subject_api_getsubjectreferencesasync_get) | **GET** /LegislationSubject/api/getsubjectreferencesasync | Gets a list of Subject References by Session
*PublicActionsApi* | [**legislation_subject_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_subject_api_heartbeatasync_get) | **GET** /LegislationSubject/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_summary_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_summary_api_clearpubliccache_get) | **GET** /LegislationSummary/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_summary_api_getlegislationsummarylistasync_get**](docs/PublicActionsApi.md#legislation_summary_api_getlegislationsummarylistasync_get) | **GET** /LegislationSummary/api/getlegislationsummarylistasync | Gets a list of Legislation Summaries
*PublicActionsApi* | [**legislation_summary_api_getsummaryversionsreferenceasync_get**](docs/PublicActionsApi.md#legislation_summary_api_getsummaryversionsreferenceasync_get) | **GET** /LegislationSummary/api/getsummaryversionsreferenceasync | Gets a list of Summary Versions
*PublicActionsApi* | [**legislation_summary_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_summary_api_heartbeatasync_get) | **GET** /LegislationSummary/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_text_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_text_api_clearpubliccache_get) | **GET** /LegislationText/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_text_api_getdrafttextbylegislationtextidasync_get**](docs/PublicActionsApi.md#legislation_text_api_getdrafttextbylegislationtextidasync_get) | **GET** /LegislationText/api/getdrafttextbylegislationtextidasync | Gets Legislation Draft Text by unique identifier
*PublicActionsApi* | [**legislation_text_api_getlegislationhtmlcontentasync_get**](docs/PublicActionsApi.md#legislation_text_api_getlegislationhtmlcontentasync_get) | **GET** /LegislationText/api/getlegislationhtmlcontentasync | Returns HTML with highlights
*PublicActionsApi* | [**legislation_text_api_getlegislationtextactionlistasync_get**](docs/PublicActionsApi.md#legislation_text_api_getlegislationtextactionlistasync_get) | **GET** /LegislationText/api/getlegislationtextactionlistasync | Gets a list of Legislation Text Actions
*PublicActionsApi* | [**legislation_text_api_getlegislationtextbyidasync_get**](docs/PublicActionsApi.md#legislation_text_api_getlegislationtextbyidasync_get) | **GET** /LegislationText/api/getlegislationtextbyidasync | Get a list of Legislation Text by unique identifier
*PublicActionsApi* | [**legislation_text_api_getlegislationtextlistasync_get**](docs/PublicActionsApi.md#legislation_text_api_getlegislationtextlistasync_get) | **GET** /LegislationText/api/getlegislationtextlistasync | Gets a list of Legislation Text
*PublicActionsApi* | [**legislation_text_api_getlegislationtextshitcountsasync_post**](docs/PublicActionsApi.md#legislation_text_api_getlegislationtextshitcountsasync_post) | **POST** /LegislationText/api/getlegislationtextshitcountsasync | Gets a list of hit counts in legislation texts based on set of Legislation Text IDs and keywords
*PublicActionsApi* | [**legislation_text_api_getlegislationversionlistasync_get**](docs/PublicActionsApi.md#legislation_text_api_getlegislationversionlistasync_get) | **GET** /LegislationText/api/getlegislationversionlistasync | Gets a list of Legislation Versions
*PublicActionsApi* | [**legislation_text_api_getpdfasync_get**](docs/PublicActionsApi.md#legislation_text_api_getpdfasync_get) | **GET** /LegislationText/api/getpdfasync | Returns PDF for either Legislation or an Impact Statement by reference number
*PublicActionsApi* | [**legislation_text_api_getsponsortypelistasync_get**](docs/PublicActionsApi.md#legislation_text_api_getsponsortypelistasync_get) | **GET** /LegislationText/api/getsponsortypelistasync | Gets a list of Sponsor Types
*PublicActionsApi* | [**legislation_text_api_gettextdispositionsreferenceasync_get**](docs/PublicActionsApi.md#legislation_text_api_gettextdispositionsreferenceasync_get) | **GET** /LegislationText/api/gettextdispositionsreferenceasync | Gets a list of Text Dispositions
*PublicActionsApi* | [**legislation_text_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_text_api_heartbeatasync_get) | **GET** /LegislationText/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**legislation_version_api_clearpubliccache_get**](docs/PublicActionsApi.md#legislation_version_api_clearpubliccache_get) | **GET** /LegislationVersion/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**legislation_version_api_getlegislationversionbybillnumberasync_get**](docs/PublicActionsApi.md#legislation_version_api_getlegislationversionbybillnumberasync_get) | **GET** /LegislationVersion/api/getlegislationversionbybillnumberasync | Gets LIS Legislation Version for a particular Bill Number and a particular session)
*PublicActionsApi* | [**legislation_version_api_getlegislationversionbylegislationidasync_get**](docs/PublicActionsApi.md#legislation_version_api_getlegislationversionbylegislationidasync_get) | **GET** /LegislationVersion/api/getlegislationversionbylegislationidasync | Gets LIS Legislation Version for a particular LegislationID or LegislationIDs (multiple)
*PublicActionsApi* | [**legislation_version_api_heartbeatasync_get**](docs/PublicActionsApi.md#legislation_version_api_heartbeatasync_get) | **GET** /LegislationVersion/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**member_api_clearpubliccache_get**](docs/PublicActionsApi.md#member_api_clearpubliccache_get) | **GET** /Member/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**member_api_getactivemembersasync_get**](docs/PublicActionsApi.md#member_api_getactivemembersasync_get) | **GET** /Member/api/getactivemembersasync | Gets a list of active Members
*PublicActionsApi* | [**member_api_getchambertypereferencesasync_get**](docs/PublicActionsApi.md#member_api_getchambertypereferencesasync_get) | **GET** /Member/api/getchambertypereferencesasync | Gets a list of Chambers
*PublicActionsApi* | [**member_api_getcommitteeslistasync_get**](docs/PublicActionsApi.md#member_api_getcommitteeslistasync_get) | **GET** /Member/api/getcommitteeslistasync | Gets a list of Committees by Member
*PublicActionsApi* | [**member_api_getdistrictreferencesasync_get**](docs/PublicActionsApi.md#member_api_getdistrictreferencesasync_get) | **GET** /Member/api/getdistrictreferencesasync | Gets a list of Districts
*PublicActionsApi* | [**member_api_getmemberbyidasync_get**](docs/PublicActionsApi.md#member_api_getmemberbyidasync_get) | **GET** /Member/api/getmemberbyidasync | Gets a Member by unique identifier
*PublicActionsApi* | [**member_api_getmemberlistasync_get**](docs/PublicActionsApi.md#member_api_getmemberlistasync_get) | **GET** /Member/api/getmemberlistasync | Gets a shallow list of Members
*PublicActionsApi* | [**member_api_getmembersasync_get**](docs/PublicActionsApi.md#member_api_getmembersasync_get) | **GET** /Member/api/getmembersasync | Gets a list of Members
*PublicActionsApi* | [**member_api_getmemberscontactinformationlistasync_get**](docs/PublicActionsApi.md#member_api_getmemberscontactinformationlistasync_get) | **GET** /Member/api/getmemberscontactinformationlistasync | Gets a list of Member Contact Information
*PublicActionsApi* | [**member_api_getmemberstatustypereferencesasync_get**](docs/PublicActionsApi.md#member_api_getmemberstatustypereferencesasync_get) | **GET** /Member/api/getmemberstatustypereferencesasync | Gets a list of Member Status Types
*PublicActionsApi* | [**member_api_getownertypereferencesasync_get**](docs/PublicActionsApi.md#member_api_getownertypereferencesasync_get) | **GET** /Member/api/getownertypereferencesasync | Gets a list of Owner Types
*PublicActionsApi* | [**member_api_getpartyreferencesasync_get**](docs/PublicActionsApi.md#member_api_getpartyreferencesasync_get) | **GET** /Member/api/getpartyreferencesasync | Gets a list of Political Parties
*PublicActionsApi* | [**member_api_heartbeatasync_get**](docs/PublicActionsApi.md#member_api_heartbeatasync_get) | **GET** /Member/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**member_vote_search_api_clearpubliccache_get**](docs/PublicActionsApi.md#member_vote_search_api_clearpubliccache_get) | **GET** /MemberVoteSearch/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**member_vote_search_api_getmembervotelistasync_get**](docs/PublicActionsApi.md#member_vote_search_api_getmembervotelistasync_get) | **GET** /MemberVoteSearch/api/getmembervotelistasync | Gets a list of Member Votes
*PublicActionsApi* | [**member_vote_search_api_heartbeatasync_get**](docs/PublicActionsApi.md#member_vote_search_api_heartbeatasync_get) | **GET** /MemberVoteSearch/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**members_by_committee_api_clearpubliccache_get**](docs/PublicActionsApi.md#members_by_committee_api_clearpubliccache_get) | **GET** /MembersByCommittee/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**members_by_committee_api_getcommitteememberslistasync_get**](docs/PublicActionsApi.md#members_by_committee_api_getcommitteememberslistasync_get) | **GET** /MembersByCommittee/api/getcommitteememberslistasync | Gets a list of Committee Members
*PublicActionsApi* | [**members_by_committee_api_getcommitteememberslisttextasync_get**](docs/PublicActionsApi.md#members_by_committee_api_getcommitteememberslisttextasync_get) | **GET** /MembersByCommittee/api/getcommitteememberslisttextasync | Gets a list of Committee Members in text format
*PublicActionsApi* | [**members_by_committee_api_getcommitteerolesasync_get**](docs/PublicActionsApi.md#members_by_committee_api_getcommitteerolesasync_get) | **GET** /MembersByCommittee/api/getcommitteerolesasync | Gets a list of Committee Roles
*PublicActionsApi* | [**members_by_committee_api_heartbeatasync_get**](docs/PublicActionsApi.md#members_by_committee_api_heartbeatasync_get) | **GET** /MembersByCommittee/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**minutes_book_api_clearpubliccache_get**](docs/PublicActionsApi.md#minutes_book_api_clearpubliccache_get) | **GET** /MinutesBook/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**minutes_book_api_getactionreferencetypelistasync_get**](docs/PublicActionsApi.md#minutes_book_api_getactionreferencetypelistasync_get) | **GET** /MinutesBook/api/getactionreferencetypelistasync | Gets a list of Action Reference Types
*PublicActionsApi* | [**minutes_book_api_getminutesbookasync_get**](docs/PublicActionsApi.md#minutes_book_api_getminutesbookasync_get) | **GET** /MinutesBook/api/getminutesbookasync | Gets a list of MinutesBooks by unique identifier
*PublicActionsApi* | [**minutes_book_api_getminutesbookinteractivecalendarasync_get**](docs/PublicActionsApi.md#minutes_book_api_getminutesbookinteractivecalendarasync_get) | **GET** /MinutesBook/api/getminutesbookinteractivecalendarasync | Gets a list of MinutesBooks for Interactive Calendar
*PublicActionsApi* | [**minutes_book_api_getpublishedminutesbooklistasync_get**](docs/PublicActionsApi.md#minutes_book_api_getpublishedminutesbooklistasync_get) | **GET** /MinutesBook/api/getpublishedminutesbooklistasync | Gets a shallow list of MinutesBooks
*PublicActionsApi* | [**minutes_book_api_heartbeatasync_get**](docs/PublicActionsApi.md#minutes_book_api_heartbeatasync_get) | **GET** /MinutesBook/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**organization_api_clearpubliccache_get**](docs/PublicActionsApi.md#organization_api_clearpubliccache_get) | **GET** /Organization/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**organization_api_getagencyreferencesasync_get**](docs/PublicActionsApi.md#organization_api_getagencyreferencesasync_get) | **GET** /Organization/api/getagencyreferencesasync | Gets a list of Owner Types
*PublicActionsApi* | [**organization_api_getorganizationbyidasync_organization_id_get**](docs/PublicActionsApi.md#organization_api_getorganizationbyidasync_organization_id_get) | **GET** /Organization/api/getorganizationbyidasync/{organizationId} | Gets a list of Organizations by unique identifier
*PublicActionsApi* | [**organization_api_getorganizationlistasync_get**](docs/PublicActionsApi.md#organization_api_getorganizationlistasync_get) | **GET** /Organization/api/getorganizationlistasync | Gets a list of Organizations
*PublicActionsApi* | [**organization_api_heartbeatasync_get**](docs/PublicActionsApi.md#organization_api_heartbeatasync_get) | **GET** /Organization/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**partner_authentication_api_checkpartnerkeyasync_api_key_get**](docs/PublicActionsApi.md#partner_authentication_api_checkpartnerkeyasync_api_key_get) | **GET** /PartnerAuthentication/api/checkpartnerkeyasync/{apiKey} | Checks a Partner API key
*PublicActionsApi* | [**partner_authentication_api_clearpubliccache_get**](docs/PublicActionsApi.md#partner_authentication_api_clearpubliccache_get) | **GET** /PartnerAuthentication/api/clearpubliccache | Clear all cache for this controller
*PublicActionsApi* | [**partner_authentication_api_completepartnerregistrationasync_post**](docs/PublicActionsApi.md#partner_authentication_api_completepartnerregistrationasync_post) | **POST** /PartnerAuthentication/api/completepartnerregistrationasync | Registers a Partner - step 2
*PublicActionsApi* | [**partner_authentication_api_heartbeatasync_get**](docs/PublicActionsApi.md#partner_authentication_api_heartbeatasync_get) | **GET** /PartnerAuthentication/api/heartbeatasync | Gets telemetry on service health
*PublicActionsApi* | [**partner_authentication_api_registerpartnerasync_post**](docs/PublicActionsApi.md#partner_authentication_api_registerpartnerasync_post) | **POST** /PartnerAuthentication/api/registerpartnerasync | Registers a Partner - step 1
*PublicUserApi* | [**api_createpublicuserasync_post**](docs/PublicUserApi.md#api_createpublicuserasync_post) | **POST** /api/createpublicuserasync | Registers a User
*PublicUserApi* | [**api_registerpublicuserasync_post**](docs/PublicUserApi.md#api_registerpublicuserasync_post) | **POST** /api/registerpublicuserasync | Initial registration of a User
*PublicUserApi* | [**api_requestresetuserpasswordasync_post**](docs/PublicUserApi.md#api_requestresetuserpasswordasync_post) | **POST** /api/requestresetuserpasswordasync | Requests a Password Reset via email
*PublicUserApi* | [**api_resetuserpasswordasync_post**](docs/PublicUserApi.md#api_resetuserpasswordasync_post) | **POST** /api/resetuserpasswordasync | Resets a user password


## Documentation For Models

 - [ActionReferenceTypeList](docs/ActionReferenceTypeList.md)
 - [ActionReferenceTypesList](docs/ActionReferenceTypesList.md)
 - [ActorTypeReferenceResponse](docs/ActorTypeReferenceResponse.md)
 - [ActorTypesReferenceResponse](docs/ActorTypesReferenceResponse.md)
 - [AdvancedSearch](docs/AdvancedSearch.md)
 - [AgenciesResponse](docs/AgenciesResponse.md)
 - [AgencyResponse](docs/AgencyResponse.md)
 - [AgendaItemPublicGetResponse](docs/AgendaItemPublicGetResponse.md)
 - [AgendaPublicGetResponse](docs/AgendaPublicGetResponse.md)
 - [AmendmentAction](docs/AmendmentAction.md)
 - [AmendmentChange](docs/AmendmentChange.md)
 - [AmendmentItem](docs/AmendmentItem.md)
 - [AmendmentResponse](docs/AmendmentResponse.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [CalendarActionReferenceResponse](docs/CalendarActionReferenceResponse.md)
 - [CalendarActionResponse](docs/CalendarActionResponse.md)
 - [CalendarCategoryPublicGetResponse](docs/CalendarCategoryPublicGetResponse.md)
 - [CalendarCategoryTypeResponse](docs/CalendarCategoryTypeResponse.md)
 - [CalendarCategoryTypesResponse](docs/CalendarCategoryTypesResponse.md)
 - [CalendarCommentPublicGetResponse](docs/CalendarCommentPublicGetResponse.md)
 - [CalendarDisplayPublicGetResponse](docs/CalendarDisplayPublicGetResponse.md)
 - [CalendarFileBaseModel](docs/CalendarFileBaseModel.md)
 - [CalendarFilePublicGetResponse](docs/CalendarFilePublicGetResponse.md)
 - [CalendarPublicGetResponse](docs/CalendarPublicGetResponse.md)
 - [CalendarPublicListGetResponse](docs/CalendarPublicListGetResponse.md)
 - [CalendarTypeResponse](docs/CalendarTypeResponse.md)
 - [CalendarTypesResponse](docs/CalendarTypesResponse.md)
 - [CalendarsPublicGetResponse](docs/CalendarsPublicGetResponse.md)
 - [CalendarsPublicListGetResponse](docs/CalendarsPublicListGetResponse.md)
 - [CategoryTypeResponse](docs/CategoryTypeResponse.md)
 - [CategoryTypesResponse](docs/CategoryTypesResponse.md)
 - [ChamberStatisticResponse](docs/ChamberStatisticResponse.md)
 - [ChamberStatisticsResponse](docs/ChamberStatisticsResponse.md)
 - [ChamberTypeReferenceResponse](docs/ChamberTypeReferenceResponse.md)
 - [ChamberTypesReferenceResponse](docs/ChamberTypesReferenceResponse.md)
 - [CommitteeActionResponse](docs/CommitteeActionResponse.md)
 - [CommitteeActionsResponse](docs/CommitteeActionsResponse.md)
 - [CommitteeByMemberResponse](docs/CommitteeByMemberResponse.md)
 - [CommitteeMemberPartnerGetResponse](docs/CommitteeMemberPartnerGetResponse.md)
 - [CommitteeRoleReference](docs/CommitteeRoleReference.md)
 - [CommitteeRolesReference](docs/CommitteeRolesReference.md)
 - [CommitteeStatisticResponse](docs/CommitteeStatisticResponse.md)
 - [CommitteeStatisticsResponse](docs/CommitteeStatisticsResponse.md)
 - [CommitteesByMemberSearchResponse](docs/CommitteesByMemberSearchResponse.md)
 - [CommunicationCategoryTypeReference](docs/CommunicationCategoryTypeReference.md)
 - [CommunicationCategoryTypesReference](docs/CommunicationCategoryTypesReference.md)
 - [ConferenceLegislationList](docs/ConferenceLegislationList.md)
 - [ConferenceLegislationsList](docs/ConferenceLegislationsList.md)
 - [ContactPublicGetResponse](docs/ContactPublicGetResponse.md)
 - [ContactResponse](docs/ContactResponse.md)
 - [ContactTypeReferenceResponse](docs/ContactTypeReferenceResponse.md)
 - [ContactTypeReferencesResponse](docs/ContactTypeReferencesResponse.md)
 - [ContactsPublicGetResponse](docs/ContactsPublicGetResponse.md)
 - [CreatePartnerRequest](docs/CreatePartnerRequest.md)
 - [CreatePublicUserRequest](docs/CreatePublicUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [DistrictReferenceResponse](docs/DistrictReferenceResponse.md)
 - [DistrictsReferenceResponse](docs/DistrictsReferenceResponse.md)
 - [DocketCategoryPublicGetResponse](docs/DocketCategoryPublicGetResponse.md)
 - [DocketFilePartnerGetResponse](docs/DocketFilePartnerGetResponse.md)
 - [DocketFilePublicGetResponse](docs/DocketFilePublicGetResponse.md)
 - [DocketItemPublicGetResponse](docs/DocketItemPublicGetResponse.md)
 - [DocketPublicListGetResponse](docs/DocketPublicListGetResponse.md)
 - [DocketWithSchedulePublicGetResponse](docs/DocketWithSchedulePublicGetResponse.md)
 - [DocketsPublicListGetResponse](docs/DocketsPublicListGetResponse.md)
 - [DocketsWithSchedulesPublicGetResponse](docs/DocketsWithSchedulesPublicGetResponse.md)
 - [File](docs/File.md)
 - [GroupRolesResponse](docs/GroupRolesResponse.md)
 - [HTMLFile](docs/HTMLFile.md)
 - [HeartBeatPublicModel](docs/HeartBeatPublicModel.md)
 - [ImpactFile](docs/ImpactFile.md)
 - [JSONFile](docs/JSONFile.md)
 - [KeyWord](docs/KeyWord.md)
 - [Legislation](docs/Legislation.md)
 - [LegislationAmendmentResponse](docs/LegislationAmendmentResponse.md)
 - [LegislationAmendmentsResponse](docs/LegislationAmendmentsResponse.md)
 - [LegislationEventTypeReferenceResponse](docs/LegislationEventTypeReferenceResponse.md)
 - [LegislationEventTypesReferenceResponse](docs/LegislationEventTypesReferenceResponse.md)
 - [LegislationID](docs/LegislationID.md)
 - [LegislationIdListResponse](docs/LegislationIdListResponse.md)
 - [LegislationIdsListResponse](docs/LegislationIdsListResponse.md)
 - [LegislationNumberResponse](docs/LegislationNumberResponse.md)
 - [LegislationPatron](docs/LegislationPatron.md)
 - [LegislationPatronsResponse](docs/LegislationPatronsResponse.md)
 - [LegislationReferencesResponse](docs/LegislationReferencesResponse.md)
 - [LegislationResponse](docs/LegislationResponse.md)
 - [LegislationSearchText](docs/LegislationSearchText.md)
 - [LegislationSessionResponse](docs/LegislationSessionResponse.md)
 - [LegislationTextActionResponse](docs/LegislationTextActionResponse.md)
 - [LegislationTextActionsList](docs/LegislationTextActionsList.md)
 - [LegislationTextDraftResponse](docs/LegislationTextDraftResponse.md)
 - [LegislationTextDraftsResponse](docs/LegislationTextDraftsResponse.md)
 - [LegislationTextGetResponse](docs/LegislationTextGetResponse.md)
 - [LegislationTextHitCountDocument](docs/LegislationTextHitCountDocument.md)
 - [LegislationTextHitCountListResponse](docs/LegislationTextHitCountListResponse.md)
 - [LegislationTextHitCountSearch](docs/LegislationTextHitCountSearch.md)
 - [LegislationTextHitCountWord](docs/LegislationTextHitCountWord.md)
 - [LegislationTextHitCountsListResponse](docs/LegislationTextHitCountsListResponse.md)
 - [LegislationTextResponse](docs/LegislationTextResponse.md)
 - [LegislationTextsResponse](docs/LegislationTextsResponse.md)
 - [LegislationVersionResponse](docs/LegislationVersionResponse.md)
 - [LegislationVersionResponse1](docs/LegislationVersionResponse1.md)
 - [LegislationVersionsResponse](docs/LegislationVersionsResponse.md)
 - [LegislationsReferencesResponse](docs/LegislationsReferencesResponse.md)
 - [LegislationsResponse](docs/LegislationsResponse.md)
 - [LegislationsSessionResponse](docs/LegislationsSessionResponse.md)
 - [LegislationsTextGetResponse](docs/LegislationsTextGetResponse.md)
 - [LegislationsVersionResponse](docs/LegislationsVersionResponse.md)
 - [LinkFile](docs/LinkFile.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [MeetingRoomResponse](docs/MeetingRoomResponse.md)
 - [MeetingRoomsResponse](docs/MeetingRoomsResponse.md)
 - [MemberByCommitteeSearchResponse](docs/MemberByCommitteeSearchResponse.md)
 - [MemberContactInformationSearchResponse](docs/MemberContactInformationSearchResponse.md)
 - [MemberPatronTypeResponse](docs/MemberPatronTypeResponse.md)
 - [MemberPatronTypesResponse](docs/MemberPatronTypesResponse.md)
 - [MemberStatusTypeReferenceResponse](docs/MemberStatusTypeReferenceResponse.md)
 - [MemberStatusTypesReferenceResponse](docs/MemberStatusTypesReferenceResponse.md)
 - [MemberVoteSearchResponse](docs/MemberVoteSearchResponse.md)
 - [MembersByCommitteeSearchResponse](docs/MembersByCommitteeSearchResponse.md)
 - [MembersContactInformationSearchResponse](docs/MembersContactInformationSearchResponse.md)
 - [MembersVoteSearchResponse](docs/MembersVoteSearchResponse.md)
 - [OwnerTypeReferenceResponse](docs/OwnerTypeReferenceResponse.md)
 - [OwnerTypeReferenceResponse1](docs/OwnerTypeReferenceResponse1.md)
 - [OwnerTypeReferencesResponse](docs/OwnerTypeReferencesResponse.md)
 - [OwnerTypesReferenceResponse](docs/OwnerTypesReferenceResponse.md)
 - [PDFFile](docs/PDFFile.md)
 - [PartiesReferenceResponse](docs/PartiesReferenceResponse.md)
 - [Partner](docs/Partner.md)
 - [PartyReferenceResponse](docs/PartyReferenceResponse.md)
 - [Patron](docs/Patron.md)
 - [Patron1](docs/Patron1.md)
 - [PatronBaseModel](docs/PatronBaseModel.md)
 - [PatronLegislationListResponse](docs/PatronLegislationListResponse.md)
 - [PatronPartnerGetResponse](docs/PatronPartnerGetResponse.md)
 - [PatronRoleReference](docs/PatronRoleReference.md)
 - [PatronRolesReference](docs/PatronRolesReference.md)
 - [PatronsLegislationListResponse](docs/PatronsLegislationListResponse.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [PublicActivityReference](docs/PublicActivityReference.md)
 - [PublicCommitteeFileResponse](docs/PublicCommitteeFileResponse.md)
 - [PublicCommitteeResponse](docs/PublicCommitteeResponse.md)
 - [PublicCommitteesResponse](docs/PublicCommitteesResponse.md)
 - [PublicCommunicationFile](docs/PublicCommunicationFile.md)
 - [PublicCommunicationsList](docs/PublicCommunicationsList.md)
 - [PublicEventReferenceResponse](docs/PublicEventReferenceResponse.md)
 - [PublicGetCommunicationCategoryResponse](docs/PublicGetCommunicationCategoryResponse.md)
 - [PublicGetCommunicationFilesResponse](docs/PublicGetCommunicationFilesResponse.md)
 - [PublicGetCommunicationLegislationResponse](docs/PublicGetCommunicationLegislationResponse.md)
 - [PublicGetCommunicationResponse](docs/PublicGetCommunicationResponse.md)
 - [PublicGetCommunicationsResponse](docs/PublicGetCommunicationsResponse.md)
 - [PublicLegislationEventResponse](docs/PublicLegislationEventResponse.md)
 - [PublicLegislationEventsResponse](docs/PublicLegislationEventsResponse.md)
 - [PublicLegislationSummariesResponse](docs/PublicLegislationSummariesResponse.md)
 - [PublicLegislationSummaryResponse](docs/PublicLegislationSummaryResponse.md)
 - [PublicMemberResponse](docs/PublicMemberResponse.md)
 - [PublicMembersResponse](docs/PublicMembersResponse.md)
 - [PublicMinutesActivity](docs/PublicMinutesActivity.md)
 - [PublicMinutesBook](docs/PublicMinutesBook.md)
 - [PublicMinutesBooks](docs/PublicMinutesBooks.md)
 - [PublicMinutesCalendar](docs/PublicMinutesCalendar.md)
 - [PublicMinutesCategory](docs/PublicMinutesCategory.md)
 - [PublicMinutesEntry](docs/PublicMinutesEntry.md)
 - [PublicMinutesFile](docs/PublicMinutesFile.md)
 - [PublicMinutesSummary](docs/PublicMinutesSummary.md)
 - [PublicOrganizationResponse](docs/PublicOrganizationResponse.md)
 - [PublicOrganizationsResponse](docs/PublicOrganizationsResponse.md)
 - [PublicPersonResponse](docs/PublicPersonResponse.md)
 - [PublicPersonnelResponse](docs/PublicPersonnelResponse.md)
 - [PublicPersonnelsResponse](docs/PublicPersonnelsResponse.md)
 - [PublicPersonsResponse](docs/PublicPersonsResponse.md)
 - [PublicScheduleResponse](docs/PublicScheduleResponse.md)
 - [PublicSchedulesResponse](docs/PublicSchedulesResponse.md)
 - [PublicShallowVoteResponse](docs/PublicShallowVoteResponse.md)
 - [PublicShallowVotesResponse](docs/PublicShallowVotesResponse.md)
 - [PublicVoteFile](docs/PublicVoteFile.md)
 - [PublicVoteLegislationResponse](docs/PublicVoteLegislationResponse.md)
 - [PublicVoteMemberResponse](docs/PublicVoteMemberResponse.md)
 - [PublicVoteResponse](docs/PublicVoteResponse.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [ScheduleTypeResponse](docs/ScheduleTypeResponse.md)
 - [ScheduleTypesResponse](docs/ScheduleTypesResponse.md)
 - [SessionEventPublicGetResponse](docs/SessionEventPublicGetResponse.md)
 - [SessionEventTypeReferenceResponse](docs/SessionEventTypeReferenceResponse.md)
 - [SessionEventTypesReferenceResponse](docs/SessionEventTypesReferenceResponse.md)
 - [SessionPublicGetResponse](docs/SessionPublicGetResponse.md)
 - [SessionResponse](docs/SessionResponse.md)
 - [SessionShallowPublicGetResponse](docs/SessionShallowPublicGetResponse.md)
 - [SessionTypeReferenceResponse](docs/SessionTypeReferenceResponse.md)
 - [SessionTypesReferenceResponse](docs/SessionTypesReferenceResponse.md)
 - [SessionsPublicGetResponse](docs/SessionsPublicGetResponse.md)
 - [SessionsShallowPublicGetResponse](docs/SessionsShallowPublicGetResponse.md)
 - [ShallowMemberResponse](docs/ShallowMemberResponse.md)
 - [ShallowMembersResponse](docs/ShallowMembersResponse.md)
 - [ShallowMinuteBookResponse](docs/ShallowMinuteBookResponse.md)
 - [ShallowMinutesBooksResponse](docs/ShallowMinutesBooksResponse.md)
 - [Sponsor](docs/Sponsor.md)
 - [SponsorTypeResponse](docs/SponsorTypeResponse.md)
 - [SponsorTypesResponse](docs/SponsorTypesResponse.md)
 - [StaffPartnerGetResponse](docs/StaffPartnerGetResponse.md)
 - [StaffRoleType](docs/StaffRoleType.md)
 - [StaffRoleTypes](docs/StaffRoleTypes.md)
 - [SubjectReference](docs/SubjectReference.md)
 - [SubjectsReference](docs/SubjectsReference.md)
 - [SummaryVersionResponse](docs/SummaryVersionResponse.md)
 - [SummaryVersionsResponse](docs/SummaryVersionsResponse.md)
 - [TextDispositionResponse](docs/TextDispositionResponse.md)
 - [TextDispositionsResponse](docs/TextDispositionsResponse.md)
 - [UserInformationRequest](docs/UserInformationRequest.md)
 - [VoteItemResponse](docs/VoteItemResponse.md)
 - [VoteLinkResponse](docs/VoteLinkResponse.md)
 - [VoteLinksResponse](docs/VoteLinksResponse.md)
 - [VoteMemberPublicGetResponse](docs/VoteMemberPublicGetResponse.md)
 - [VoteResultResponse](docs/VoteResultResponse.md)
 - [VoteType](docs/VoteType.md)
 - [VoteTypes](docs/VoteTypes.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




