# PublicCommunicationsList

List of Public Communication Files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_id** | **int** | Unique identifier for Communication | [optional] 
**communication_date** | **datetime** | Communication date | [optional] 
**communication_number** | **int** | Communication Number | [optional] 
**reference_number** | **str** | Reference Number | [optional] 
**is_public** | **bool** | Is this Communication public? | [optional] 
**communication_type_id** | **int** | Unique identifier for Communication Type | [optional] 
**communication_type** | **str** | Communication Type name | [optional] 
**chamber_code** | **str** | Chamber code (H/S) | [optional] 
**session_id** | **int** | Unique identifier for Session | [optional] 
**show_signature_note** | **bool** | Show Signature Note | [optional] 
**communication_files** | [**List[PublicCommunicationFile]**](PublicCommunicationFile.md) | List of Public Communication Files | [optional] 

## Example

```python
from valis.models.public_communications_list import PublicCommunicationsList

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCommunicationsList from a JSON string
public_communications_list_instance = PublicCommunicationsList.from_json(json)
# print the JSON string representation of the object
print(PublicCommunicationsList.to_json())

# convert the object into a dict
public_communications_list_dict = public_communications_list_instance.to_dict()
# create an instance of PublicCommunicationsList from a dict
public_communications_list_from_dict = PublicCommunicationsList.from_dict(public_communications_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


