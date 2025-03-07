# CommitteeActionResponse

CommitteeAction Response Model for getting Committee Action reference list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_action_id** | **int** | Committee Action ID | [optional] 
**description** | **str** | Description of the Action | [optional] 
**event_code** | **str** | EventCode of the Action | [optional] 
**is_complete** | **bool** | IsComplete yes/no | [optional] 

## Example

```python
from valis.models.committee_action_response import CommitteeActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeActionResponse from a JSON string
committee_action_response_instance = CommitteeActionResponse.from_json(json)
# print the JSON string representation of the object
print(CommitteeActionResponse.to_json())

# convert the object into a dict
committee_action_response_dict = committee_action_response_instance.to_dict()
# create an instance of CommitteeActionResponse from a dict
committee_action_response_from_dict = CommitteeActionResponse.from_dict(committee_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


