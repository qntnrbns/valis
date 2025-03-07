# DocketWithSchedulePublicGetResponse

Docket Public Get Response with potential list of Schedule Responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docket_date** | **datetime** | Docket(Committee Calendar) Date | 
**meeting_time** | **str** | Meeting Time | [optional] 
**docket_number** | **int** | Docket(Committee Calendar) Number | [optional] 
**description** | **str** | Docket(Committee Calendar) Description | [optional] 
**is_public** | **bool** | Is Docket(Committee Calendar) for Public Consumption | [optional] 
**docket_type_id** | **int** | Docket(Committee Calendar) Type ID | [optional] 
**docket_type** | **str** | Docket Type | 
**chamber_code** | **str** | Chamber Code is always defaulted to S for Senate | [optional] 
**session_id** | **int** | Session ID | 
**session_code** | **str** | Session Code | [optional] 
**vote_room_id** | **int** | Vote Room ID | [optional] 
**comments** | **str** | Meeting Notes/Comments | [optional] 
**committee_id** | **int** | Committee ID | 
**committee_name** | **str** | Committee Name | [optional] 
**parent_committee_name** | **str** | Parent Committee Name | [optional] 
**pending_change** | **bool** | Pending Change to Docket | [optional] 
**reference_number** | **str** | Reference Number used for External Reference to Docket | [optional] 
**is_proforma** | **bool** | IsProforma to Calendar | [optional] 
**deletion_date** | **datetime** | Docket(Committee Calendar) Deletion Date | [optional] 
**docket_id** | **int** | Docket unique identifier | 
**calendar_display** | [**List[CalendarDisplayPublicGetResponse]**](CalendarDisplayPublicGetResponse.md) | Listing of Calendar Displays | [optional] 
**committee_member** | [**List[CommitteeMemberPartnerGetResponse]**](CommitteeMemberPartnerGetResponse.md) | Listing of Committee Members | [optional] 
**staff** | [**List[StaffPartnerGetResponse]**](StaffPartnerGetResponse.md) | Listing of Staff | [optional] 
**docket_categories** | [**List[DocketCategoryPublicGetResponse]**](DocketCategoryPublicGetResponse.md) | Listing of Calendar Categories | [optional] 
**docket_files** | [**List[DocketFilePartnerGetResponse]**](DocketFilePartnerGetResponse.md) | Listing of Docket Files | [optional] 
**schedules** | [**List[PublicScheduleResponse]**](PublicScheduleResponse.md) | Schedules | [optional] 

## Example

```python
from valis.models.docket_with_schedule_public_get_response import DocketWithSchedulePublicGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocketWithSchedulePublicGetResponse from a JSON string
docket_with_schedule_public_get_response_instance = DocketWithSchedulePublicGetResponse.from_json(json)
# print the JSON string representation of the object
print(DocketWithSchedulePublicGetResponse.to_json())

# convert the object into a dict
docket_with_schedule_public_get_response_dict = docket_with_schedule_public_get_response_instance.to_dict()
# create an instance of DocketWithSchedulePublicGetResponse from a dict
docket_with_schedule_public_get_response_from_dict = DocketWithSchedulePublicGetResponse.from_dict(docket_with_schedule_public_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


