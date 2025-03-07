# ChamberStatisticsResponse

list of chamber statistics (using ChamberStatisticResponse). If no valid response could be   obtained, Success boolean will be false and additional information can be found in FailureMessage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ChamberStatisticResponse]**](ChamberStatisticResponse.md) | committee statistics list | [optional] 

## Example

```python
from valis.models.chamber_statistics_response import ChamberStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChamberStatisticsResponse from a JSON string
chamber_statistics_response_instance = ChamberStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(ChamberStatisticsResponse.to_json())

# convert the object into a dict
chamber_statistics_response_dict = chamber_statistics_response_instance.to_dict()
# create an instance of ChamberStatisticsResponse from a dict
chamber_statistics_response_from_dict = ChamberStatisticsResponse.from_dict(chamber_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


