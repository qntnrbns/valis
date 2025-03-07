# CommitteeStatisticsResponse

list of committee statistics (using CommitteeStatisticResponse). If no valid response could be   obtained, Success boolean will be false and additional information can be found in FailureMessage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CommitteeStatisticResponse]**](CommitteeStatisticResponse.md) | committee statistics list | [optional] 

## Example

```python
from valis.models.committee_statistics_response import CommitteeStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeStatisticsResponse from a JSON string
committee_statistics_response_instance = CommitteeStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteeStatisticsResponse.to_json())

# convert the object into a dict
committee_statistics_response_dict = committee_statistics_response_instance.to_dict()
# create an instance of CommitteeStatisticsResponse from a dict
committee_statistics_response_from_dict = CommitteeStatisticsResponse.from_dict(committee_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


