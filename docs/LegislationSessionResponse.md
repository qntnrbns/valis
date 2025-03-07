# LegislationSessionResponse

LegislationSessionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | Legislation unique identifier | [optional] 
**legislation_number** | **str** | Legislation Number (Unique for each Biennial) | [optional] 
**description** | **str** | Legislation Description/Catchline | [optional] 
**chamber_code** | **str** | Chamber Code | [optional] 
**legislation_type_code** | **str** | Legislation Type Code | [optional] 
**legislation_key** | **int** | Legislation Key (Numerical Part of the Legislation Number) | [optional] 
**legislation_status** | **str** | Legislative Status | [optional] 
**patrons** | [**List[Patron]**](Patron.md) | List of Patrons on the associated Legislation | [optional] 

## Example

```python
from valis.models.legislation_session_response import LegislationSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationSessionResponse from a JSON string
legislation_session_response_instance = LegislationSessionResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationSessionResponse.to_json())

# convert the object into a dict
legislation_session_response_dict = legislation_session_response_instance.to_dict()
# create an instance of LegislationSessionResponse from a dict
legislation_session_response_from_dict = LegislationSessionResponse.from_dict(legislation_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


