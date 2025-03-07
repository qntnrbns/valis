# PublicCommitteeResponse

Information for public Committee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Committee name | 
**committee_number** | **str** | Committee number (e.g. S12) | 
**chamber_code** | **str** | Chamber code (H/S) for which committee belongs | 
**session_code** | **str** | Session code (e.g. 20181) | [optional] 
**twitter_handle** | **str** | Twitter username/handle | [optional] 
**twitter_email** | **str** | Twitter email address | [optional] 
**parent_committee_id** | **int** | Unique Identifier for Parent Committee | [optional] 
**service_end_date** | **datetime** | End date of Service for this Committee | [optional] 
**service_begin_date** | **datetime** | Begin date of Service for this Committee | [optional] 
**effective_begin_date** | **datetime** | Effective begin date | [optional] 
**effective_end_date** | **datetime** | Effective ending date | [optional] 
**abbreviation** | **str** | Committee abbreviation | [optional] 
**description** | **str** | Committee description | [optional] 
**meeting_note** | **str** | Committee meeting note | [optional] 
**pending_change** | **bool** | Are there any pending changes? | [optional] 
**sub_pending_change** | **bool** | Are there any pending changes for Subcommittee? | [optional] 
**is_public** | **bool** | Is this public? | [optional] 
**agenda_url** | **str** | Agenda link for committees and subcommittees | [optional] 
**committee_id** | **int** | Unique identifier for Committee | [optional] 
**committee_files** | [**List[PublicCommitteeFileResponse]**](PublicCommitteeFileResponse.md) | List of Committee Files | [optional] 

## Example

```python
from valis.models.public_committee_response import PublicCommitteeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCommitteeResponse from a JSON string
public_committee_response_instance = PublicCommitteeResponse.from_json(json)
# print the JSON string representation of the object
print(PublicCommitteeResponse.to_json())

# convert the object into a dict
public_committee_response_dict = public_committee_response_instance.to_dict()
# create an instance of PublicCommitteeResponse from a dict
public_committee_response_from_dict = PublicCommitteeResponse.from_dict(public_committee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


