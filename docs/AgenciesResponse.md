# AgenciesResponse

Response object containing a list of LIS agencies (using AgencyResponse)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[AgencyResponse]**](AgencyResponse.md) | list of agencies | [optional] 

## Example

```python
from valis.models.agencies_response import AgenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgenciesResponse from a JSON string
agencies_response_instance = AgenciesResponse.from_json(json)
# print the JSON string representation of the object
print(AgenciesResponse.to_json())

# convert the object into a dict
agencies_response_dict = agencies_response_instance.to_dict()
# create an instance of AgenciesResponse from a dict
agencies_response_from_dict = AgenciesResponse.from_dict(agencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


