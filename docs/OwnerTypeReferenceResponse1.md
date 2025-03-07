# OwnerTypeReferenceResponse1

Information for an Owner Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_type_id** | **str** | Unique identifier for Owner Type | [optional] 
**owner_type** | **str** | Owner Type | [optional] 

## Example

```python
from valis.models.owner_type_reference_response1 import OwnerTypeReferenceResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerTypeReferenceResponse1 from a JSON string
owner_type_reference_response1_instance = OwnerTypeReferenceResponse1.from_json(json)
# print the JSON string representation of the object
print(OwnerTypeReferenceResponse1.to_json())

# convert the object into a dict
owner_type_reference_response1_dict = owner_type_reference_response1_instance.to_dict()
# create an instance of OwnerTypeReferenceResponse1 from a dict
owner_type_reference_response1_from_dict = OwnerTypeReferenceResponse1.from_dict(owner_type_reference_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


