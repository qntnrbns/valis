# DistrictsReferenceResponse

List of Districts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[DistrictReferenceResponse]**](DistrictReferenceResponse.md) | List of Districts | [optional] 

## Example

```python
from valis.models.districts_reference_response import DistrictsReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictsReferenceResponse from a JSON string
districts_reference_response_instance = DistrictsReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(DistrictsReferenceResponse.to_json())

# convert the object into a dict
districts_reference_response_dict = districts_reference_response_instance.to_dict()
# create an instance of DistrictsReferenceResponse from a dict
districts_reference_response_from_dict = DistrictsReferenceResponse.from_dict(districts_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


