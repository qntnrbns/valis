# ChamberTypesReferenceResponse

List of Chambers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ChamberTypeReferenceResponse]**](ChamberTypeReferenceResponse.md) | List of Chambers | [optional] 

## Example

```python
from valis.models.chamber_types_reference_response import ChamberTypesReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChamberTypesReferenceResponse from a JSON string
chamber_types_reference_response_instance = ChamberTypesReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ChamberTypesReferenceResponse.to_json())

# convert the object into a dict
chamber_types_reference_response_dict = chamber_types_reference_response_instance.to_dict()
# create an instance of ChamberTypesReferenceResponse from a dict
chamber_types_reference_response_from_dict = ChamberTypesReferenceResponse.from_dict(chamber_types_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


