# AdvancedSearch

Information for performing a Legislation search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_control_id** | **int** | Unique identifier for Event Control | [optional] 
**start_date** | **datetime** | Start Date associated with status dropdown | [optional] 
**end_date** | **datetime** | End Date associated with status dropdown | [optional] 
**event_start_date** | **datetime** | End Event Date, associated with Event Control dropdown | [optional] 
**event_end_date** | **datetime** | Start Event Date, associated with Event Control dropdown | [optional] 
**introduction_date** | **datetime** |  | [optional] 
**legislation_title** | **str** |  | [optional] 
**description** | **str** | Bill description | [optional] 
**chambercode** | **str** | Chamber code (H/S) | [optional] 
**legislation_status_id** | **int** | Unique identifier for Legislation Status | [optional] 
**legislation_category_id** | **int** | Unique identifier for Legislation Category | [optional] 
**committee_id** | **int** | Unique identifier for Committee | [optional] 
**session_id** | **int** | Unique identifier for Session | [optional] 
**session_code** | **int** | Session code (e.g. 20181) | [optional] 
**legislation_event_type_id** | **int** | Unique identifier for Legislation Event Type | [optional] 
**summary_length** | **int** | Limitation on summary length | [optional] 
**patron_types** | **List[int]** | List of Patron Types | [optional] 
**member_id** | **int** | Unique identifier for Member | [optional] 
**subject_index_id** | **int** | Unique identifier for Subject Index | [optional] 
**most_frequent** | **bool** | Return most frequently accessed bills? | [optional] 
**is_pending** | **bool** | Return pending bills? | [optional] 
**keyword_expression** | **str** | Keyword search - supports operators and parentheses | [optional] 
**keyword_location** | **str** | Where to perform the Keyword search (Summary/Bill Text) | [optional] 
**keyword_summary_version_id** | **int** | Unique identifier of Keyword Summary Version | [optional] 
**keyword_legislation_version_id** | **int** | Unique identifier of Keyword Legislation Version | [optional] 
**keyword_use_global_session_search** | **bool** | Should the keyword search search across all sessions? | [optional] 
**skip_legislation_text_calls** | **bool** | Skip searching legislation text? | [optional] 
**current_status** | **bool** | Search by only the current bill status? | [optional] 
**keywords** | [**List[KeyWord]**](KeyWord.md) | List of KeyWord search objects | [optional] 
**exclude_failed** | **bool** |  | [optional] 
**chapter_number** | **str** | Chapter Number | [optional] 
**legislation_numbers** | [**List[LegislationNumberResponse]**](LegislationNumberResponse.md) | List of Legislative Numbers | [optional] 
**legislation_ids** | [**List[LegislationID]**](LegislationID.md) | List of Legislation IDs | [optional] 

## Example

```python
from valis.models.advanced_search import AdvancedSearch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedSearch from a JSON string
advanced_search_instance = AdvancedSearch.from_json(json)
# print the JSON string representation of the object
print(AdvancedSearch.to_json())

# convert the object into a dict
advanced_search_dict = advanced_search_instance.to_dict()
# create an instance of AdvancedSearch from a dict
advanced_search_from_dict = AdvancedSearch.from_dict(advanced_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


