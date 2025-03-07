# DocketFilePartnerGetResponse

Docket File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_file_id** | **int** | Database Unique Identifier for Files | [optional] 
**calendar_id** | **int** | Database Unique Identifier for Calendar/Docket/Agenda | [optional] 
**file_url** | **str** | File URL | [optional] 
**text_format_id** | **int** | Unique Identifier for Text format ID | 
**is_generated** | **bool** | File Generated | [optional] 
**is_public** | **bool** | File Public | [optional] 
**is_active** | **bool** | File Active | [optional] 
**modification_date** | **datetime** | last modification date, needed to control updates | [optional] 

## Example

```python
from valis.models.docket_file_partner_get_response import DocketFilePartnerGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketFilePartnerGetResponse from a JSON string
docket_file_partner_get_response_instance = DocketFilePartnerGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketFilePartnerGetResponse.to_json())

# convert the object into a dict
docket_file_partner_get_response_dict = docket_file_partner_get_response_instance.to_dict()
# create an instance of DocketFilePartnerGetResponse from a dict
docket_file_partner_get_response_from_dict = DocketFilePartnerGetResponse.from_dict(docket_file_partner_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


