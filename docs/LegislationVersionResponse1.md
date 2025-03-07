# LegislationVersionResponse1

Different types of versions for legislation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_version_id** | **int** | unique identifier of the LegislationVersion | [optional] 
**name** | **str** | name of the LegislationVersion | [optional] 
**version_code** | **str** | code for the LegislationVersion | [optional] 
**legislation_status_id** | **int** | ID for what legislation status this version correlates to | [optional] 
**suffix** | **str** | The suffix that is added to the end of the legislation number on the printed legislation text | [optional] 
**authoring_label** | **str** | legislation version label for authoring purposes | [optional] 

## Example

```python
from valis.models.legislation_version_response1 import LegislationVersionResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationVersionResponse1 from a JSON string
legislation_version_response1_instance = LegislationVersionResponse1.from_json(json)
# print the JSON string representation of the object
print(LegislationVersionResponse1.to_json())

# convert the object into a dict
legislation_version_response1_dict = legislation_version_response1_instance.to_dict()
# create an instance of LegislationVersionResponse1 from a dict
legislation_version_response1_from_dict = LegislationVersionResponse1.from_dict(legislation_version_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


