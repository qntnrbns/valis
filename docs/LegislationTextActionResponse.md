# LegislationTextActionResponse

building element for legislation action list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_action_id** | **int** | unique identifier of the LegislationTextAction | [optional] 
**description** | **str** | Description | [optional] 
**event_code** | **str** | Event Code | [optional] 

## Example

```python
from valis.models.legislation_text_action_response import LegislationTextActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextActionResponse from a JSON string
legislation_text_action_response_instance = LegislationTextActionResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextActionResponse.to_json())

# convert the object into a dict
legislation_text_action_response_dict = legislation_text_action_response_instance.to_dict()
# create an instance of LegislationTextActionResponse from a dict
legislation_text_action_response_from_dict = LegislationTextActionResponse.from_dict(legislation_text_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


