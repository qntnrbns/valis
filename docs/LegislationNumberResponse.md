# LegislationNumberResponse

Legislation Number Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_number** | **str** | LegislationNumber | [optional] 

## Example

```python
from valis.models.legislation_number_response import LegislationNumberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationNumberResponse from a JSON string
legislation_number_response_instance = LegislationNumberResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationNumberResponse.to_json())

# convert the object into a dict
legislation_number_response_dict = legislation_number_response_instance.to_dict()
# create an instance of LegislationNumberResponse from a dict
legislation_number_response_from_dict = LegislationNumberResponse.from_dict(legislation_number_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


