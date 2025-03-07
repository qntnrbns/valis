# PublicOrganizationsResponse

Request and Response object containing a list of LIS organizations (using PublicOrganizationResponse)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicOrganizationResponse]**](PublicOrganizationResponse.md) | list of organizations | [optional] 

## Example

```python
from valis.models.public_organizations_response import PublicOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicOrganizationsResponse from a JSON string
public_organizations_response_instance = PublicOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicOrganizationsResponse.to_json())

# convert the object into a dict
public_organizations_response_dict = public_organizations_response_instance.to_dict()
# create an instance of PublicOrganizationsResponse from a dict
public_organizations_response_from_dict = PublicOrganizationsResponse.from_dict(public_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


