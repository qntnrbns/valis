# CreatePartnerRequest

Create partner request object containing user information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashed_word** | **str** | API Registration URL hash - REQUIRED | 
**contact_name** | **str** | contact name | 
**organization_name** | **str** | organization name | [optional] 
**url** | **str** | URL | [optional] 
**phone** | **str** | Contact Phone | 
**eula_date** | **datetime** | EULA Date | [optional] 

## Example

```python
from valis.models.create_partner_request import CreatePartnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePartnerRequest from a JSON string
create_partner_request_instance = CreatePartnerRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePartnerRequest.to_json())

# convert the object into a dict
create_partner_request_dict = create_partner_request_instance.to_dict()
# create an instance of CreatePartnerRequest from a dict
create_partner_request_from_dict = CreatePartnerRequest.from_dict(create_partner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


