# DocketFilePublicGetResponse

Docket Files

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

## Example

```python
from valis.models.docket_file_public_get_response import DocketFilePublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketFilePublicGetResponse from a JSON string
docket_file_public_get_response_instance = DocketFilePublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketFilePublicGetResponse.to_json())

# convert the object into a dict
docket_file_public_get_response_dict = docket_file_public_get_response_instance.to_dict()
# create an instance of DocketFilePublicGetResponse from a dict
docket_file_public_get_response_from_dict = DocketFilePublicGetResponse.from_dict(docket_file_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


