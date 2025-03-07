# PublicGetCommunicationResponse

Information for Public Get Communication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_date** | **datetime** | Communication date | [optional] 
**communication_number** | **int** | Communication # | [optional] 
**reference_number** | **str** | Reference # | [optional] 
**is_public** | **bool** | Is this public? | [optional] 
**communication_type_id** | **int** | Unique identifier for Communication Type | [optional] 
**communication_type** | **str** | Communication Type | [optional] 
**committee_id** | **int** | Unique identifier for Committee | [optional] 
**committee_name** | **str** | Committee Name | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**session_id** | **int** | Unique identifier for Session | [optional] 
**document_code** | **str** | Document Code | [optional] 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**show_signature_note** | **bool** | Show Signature Note | [optional] 
**communication_id** | **int** | Unique identifier for Communication | [optional] 
**communication_categories** | [**List[PublicGetCommunicationCategoryResponse]**](PublicGetCommunicationCategoryResponse.md) | List of Communication Categories | [optional] 
**communication_files** | [**List[PublicCommunicationFile]**](PublicCommunicationFile.md) | List of Communication Files | [optional] 

## Example

```python
from valis.models.public_get_communication_response import PublicGetCommunicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicGetCommunicationResponse from a JSON string
public_get_communication_response_instance = PublicGetCommunicationResponse.from_json(json)
# print the JSON string representation of the object
print(PublicGetCommunicationResponse.to_json())

# convert the object into a dict
public_get_communication_response_dict = public_get_communication_response_instance.to_dict()
# create an instance of PublicGetCommunicationResponse from a dict
public_get_communication_response_from_dict = PublicGetCommunicationResponse.from_dict(public_get_communication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


