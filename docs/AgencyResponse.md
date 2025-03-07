# AgencyResponse

Public Agency Response object containing LIS agency information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **int** | Identity unique identifier | [optional] 
**agency_name** | **str** | Agency Name (e.g. Auditor of Public Accounts) | [optional] 
**abbreviation** | **str** | Agency Abbreviation (e.g. APA) | [optional] 
**agency_number** | **str** | Agency Number (e.g. 133) | [optional] 
**branch** | **str** | Branch of Government (e.g. Legislative/Education) | [optional] 

## Example

```python
from valis.models.agency_response import AgencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyResponse from a JSON string
agency_response_instance = AgencyResponse.from_json(json)
# print the JSON string representation of the object
print(AgencyResponse.to_json())

# convert the object into a dict
agency_response_dict = agency_response_instance.to_dict()
# create an instance of AgencyResponse from a dict
agency_response_from_dict = AgencyResponse.from_dict(agency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


