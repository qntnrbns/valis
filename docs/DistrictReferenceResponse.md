# DistrictReferenceResponse

Information for a District

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**district_id** | **int** | Unique identifier for this District | [optional] 
**title** | **str** | District title | [optional] 
**description** | **str** | District description | [optional] 

## Example

```python
from valis.models.district_reference_response import DistrictReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictReferenceResponse from a JSON string
district_reference_response_instance = DistrictReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(DistrictReferenceResponse.to_json())

# convert the object into a dict
district_reference_response_dict = district_reference_response_instance.to_dict()
# create an instance of DistrictReferenceResponse from a dict
district_reference_response_from_dict = DistrictReferenceResponse.from_dict(district_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


