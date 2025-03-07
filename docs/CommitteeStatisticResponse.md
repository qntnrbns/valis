# CommitteeStatisticResponse

Response object containing committee statistics information. If no valid response   could be obtained, Success boolean will be false and additional information can be found   in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **int** | unique identifier for Committee | [optional] 
**committee_number** | **str** | unique number for Committee | [optional] 
**committee_name** | **str** | name for Committee | [optional] 
**h_referred** | **int** | number of legislation referred to the committee from the House | [optional] 
**s_referred** | **int** | number of legislation referred to the committee from the Senate | [optional] 
**hin_committee** | **int** | number of legislation currently in committee from the House | [optional] 
**sin_committee** | **int** | number of legislation currently in committee from the Senate | [optional] 
**hin_sub_committee** | **int** | number of legislation currently in subcommittee from the House | [optional] 
**sin_sub_committee** | **int** | number of legislation currently in subcommittee from the Senate | [optional] 
**h_reported** | **int** | number of legislation reported out from committee from the House | [optional] 
**s_reported** | **int** | number of legislation reported out from committee from the Senate | [optional] 
**h_incorporated** | **int** | number of legislation incorporated from committee from the House | [optional] 
**s_incorporated** | **int** | number of legislation incorporated from committee from the Senate | [optional] 
**h_continued** | **int** | number of legislation continued from the House | [optional] 
**s_continued** | **int** | number of legislation continued from the Senate | [optional] 
**h_continued_from** | **int** | number of legislation continued from committee from the House | [optional] 
**s_continued_from** | **int** | number of legislation continued from committee from the Senate | [optional] 
**h_failed** | **int** | number of legislation failed from committee from the House | [optional] 
**s_failed** | **int** | number of legislation failed from committee from the Senate | [optional] 

## Example

```python
from valis.models.committee_statistic_response import CommitteeStatisticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeStatisticResponse from a JSON string
committee_statistic_response_instance = CommitteeStatisticResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteeStatisticResponse.to_json())

# convert the object into a dict
committee_statistic_response_dict = committee_statistic_response_instance.to_dict()
# create an instance of CommitteeStatisticResponse from a dict
committee_statistic_response_from_dict = CommitteeStatisticResponse.from_dict(committee_statistic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


