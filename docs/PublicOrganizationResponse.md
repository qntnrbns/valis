# PublicOrganizationResponse

Public Response object containing LIS organization information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **int** | Identity unique identifier | [optional] 
**name** | **str** | Organization Name | 

## Example

```python
from valis.models.public_organization_response import PublicOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicOrganizationResponse from a JSON string
public_organization_response_instance = PublicOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(PublicOrganizationResponse.to_json())

# convert the object into a dict
public_organization_response_dict = public_organization_response_instance.to_dict()
# create an instance of PublicOrganizationResponse from a dict
public_organization_response_from_dict = PublicOrganizationResponse.from_dict(public_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


