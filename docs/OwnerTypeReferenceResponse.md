# OwnerTypeReferenceResponse

Response object containing LIS Owner Type reference information. If no valid response   could be obtained, Success boolean will be false and additional information can be found   in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_type_id** | **int** | Owner Type unique identifier | [optional] 
**owner_type** | **str** | Owner Type Name or Description | [optional] 

## Example

```python
from valis.models.owner_type_reference_response import OwnerTypeReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerTypeReferenceResponse from a JSON string
owner_type_reference_response_instance = OwnerTypeReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(OwnerTypeReferenceResponse.to_json())

# convert the object into a dict
owner_type_reference_response_dict = owner_type_reference_response_instance.to_dict()
# create an instance of OwnerTypeReferenceResponse from a dict
owner_type_reference_response_from_dict = OwnerTypeReferenceResponse.from_dict(owner_type_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


