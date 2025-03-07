# LegislationIdListResponse

Information for Legislation ID Search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | Unique identifier for Legislation | [optional] 
**legislation_status_id** | **int** | Unique Identifier for Legislation Event Status | [optional] 
**legislation_number** | **str** | Legislation number | [optional] 
**session_id** | **int** | unique identifier for Session | [optional] 
**session_code** | **int** | Session code (e.g. 20181) | [optional] 
**search_text** | [**List[LegislationSearchText]**](LegislationSearchText.md) | List of Search Text (contains version results) | [optional] 

## Example

```python
from valis.models.legislation_id_list_response import LegislationIdListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationIdListResponse from a JSON string
legislation_id_list_response_instance = LegislationIdListResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationIdListResponse.to_json())

# convert the object into a dict
legislation_id_list_response_dict = legislation_id_list_response_instance.to_dict()
# create an instance of LegislationIdListResponse from a dict
legislation_id_list_response_from_dict = LegislationIdListResponse.from_dict(legislation_id_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


