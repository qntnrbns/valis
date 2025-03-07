# ChamberTypeReferenceResponse

Information for a Chamber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**name** | **str** | Chamber name | [optional] 

## Example

```python
from valis.models.chamber_type_reference_response import ChamberTypeReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChamberTypeReferenceResponse from a JSON string
chamber_type_reference_response_instance = ChamberTypeReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ChamberTypeReferenceResponse.to_json())

# convert the object into a dict
chamber_type_reference_response_dict = chamber_type_reference_response_instance.to_dict()
# create an instance of ChamberTypeReferenceResponse from a dict
chamber_type_reference_response_from_dict = ChamberTypeReferenceResponse.from_dict(chamber_type_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


