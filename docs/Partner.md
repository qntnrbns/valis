# Partner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **int** |  | [optional] 
**identity_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**last_connect_date** | **datetime** |  | [optional] 
**eula_date** | **datetime** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**success** | **bool** |  | [optional] 
**failure_message** | **str** |  | [optional] 

## Example

```python
from valis.models.partner import Partner

# TODO update the JSON string below
json = "{}"
# create an instance of Partner from a JSON string
partner_instance = Partner.from_json(json)
# print the JSON string representation of the object
print(Partner.to_json())

# convert the object into a dict
partner_dict = partner_instance.to_dict()
# create an instance of Partner from a dict
partner_from_dict = Partner.from_dict(partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


