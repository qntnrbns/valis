# CommitteeActionsResponse

List of Committee Actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[CommitteeActionResponse]**](CommitteeActionResponse.md) | List of Committee Actions | [optional] 

## Example

```python
from valis.models.committee_actions_response import CommitteeActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeActionsResponse from a JSON string
committee_actions_response_instance = CommitteeActionsResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteeActionsResponse.to_json())

# convert the object into a dict
committee_actions_response_dict = committee_actions_response_instance.to_dict()
# create an instance of CommitteeActionsResponse from a dict
committee_actions_response_from_dict = CommitteeActionsResponse.from_dict(committee_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


