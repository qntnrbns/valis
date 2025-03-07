# SponsorTypeResponse

Sponsor type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Body that can sponsor a Legislation Text (House/Senate/Conference/Governor) | [optional] 
**sponsor_type_id** | **int** | unique identifier for sponsor type (e.g. 1&#x3D;House of Delegates, 2&#x3D;Senate, 3&#x3D;Committee, 4&#x3D;Member, etc) | [optional] 

## Example

```python
from valis.models.sponsor_type_response import SponsorTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorTypeResponse from a JSON string
sponsor_type_response_instance = SponsorTypeResponse.from_json(json)
# print the JSON string representation of the object
print(SponsorTypeResponse.to_json())

# convert the object into a dict
sponsor_type_response_dict = sponsor_type_response_instance.to_dict()
# create an instance of SponsorTypeResponse from a dict
sponsor_type_response_from_dict = SponsorTypeResponse.from_dict(sponsor_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


