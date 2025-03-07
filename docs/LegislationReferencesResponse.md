# LegislationReferencesResponse

Information for a Legislation Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_status_id** | **int** | Unique Identifier for Legislation Status | [optional] 
**name** | **str** | Legislation Status Common Name | [optional] 
**display_name** | **str** | Legislation Status Display Name | [optional] 
**legislation_version_id** | **int** | Unique Identifier for Legislation Version | [optional] 

## Example

```python
from valis.models.legislation_references_response import LegislationReferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationReferencesResponse from a JSON string
legislation_references_response_instance = LegislationReferencesResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationReferencesResponse.to_json())

# convert the object into a dict
legislation_references_response_dict = legislation_references_response_instance.to_dict()
# create an instance of LegislationReferencesResponse from a dict
legislation_references_response_from_dict = LegislationReferencesResponse.from_dict(legislation_references_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


