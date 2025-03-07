# ChamberStatisticResponse

Response object containing chamber statistics information. If no valid response   could be obtained, Success boolean will be false and additional information can be found   in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chamber_code** | **str** | Chamber Code | [optional] 
**legislation_type_code** | **str** | Legislation Type Code (B/J/R) | [optional] 
**introduced** | **int** | number of legislation introduced | [optional] 
**passed_house** | **int** | number of legislation passed in the House of Delegates | [optional] 
**passed_senate** | **int** | number of legislation passed in the Senate | [optional] 
**passed** | **int** | number of legislation passed | [optional] 
**pending** | **int** | number of legislation pending | [optional] 
**incorporated** | **int** | number of legislation incorporated | [optional] 
**failed** | **int** | number of legislation failed | [optional] 
**approved** | **int** | number of legislation approved | [optional] 
**veto** | **int** | number of legislation vetoed | [optional] 
**awaiting_gov_action** | **int** | number of legislation awaiting Governor&#39;s action | [optional] 
**continued_from_last_session** | **int** | number of legislation that was continued from last session | [optional] 
**continued_to_next_session** | **int** | number of legislation that is continued to next session | [optional] 

## Example

```python
from valis.models.chamber_statistic_response import ChamberStatisticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChamberStatisticResponse from a JSON string
chamber_statistic_response_instance = ChamberStatisticResponse.from_json(json)
# print the JSON string representation of the object
print(ChamberStatisticResponse.to_json())

# convert the object into a dict
chamber_statistic_response_dict = chamber_statistic_response_instance.to_dict()
# create an instance of ChamberStatisticResponse from a dict
chamber_statistic_response_from_dict = ChamberStatisticResponse.from_dict(chamber_statistic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


