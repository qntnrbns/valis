# LegislationTextHitCountListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_id** | **int** |  | [optional] 
**hit_count** | **int** |  | [optional] 

## Example

```python
from valis.models.legislation_text_hit_count_list_response import LegislationTextHitCountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationTextHitCountListResponse from a JSON string
legislation_text_hit_count_list_response_instance = LegislationTextHitCountListResponse.from_json(json)
# print the JSON string representation of the object
print(LegislationTextHitCountListResponse.to_json())

# convert the object into a dict
legislation_text_hit_count_list_response_dict = legislation_text_hit_count_list_response_instance.to_dict()
# create an instance of LegislationTextHitCountListResponse from a dict
legislation_text_hit_count_list_response_from_dict = LegislationTextHitCountListResponse.from_dict(legislation_text_hit_count_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


