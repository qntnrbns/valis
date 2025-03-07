# ConferenceLegislationsList

conference legislation list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ConferenceLegislationList]**](ConferenceLegislationList.md) | list of conference legislation | [optional] 

## Example

```python
from valis.models.conference_legislations_list import ConferenceLegislationsList

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceLegislationsList from a JSON string
conference_legislations_list_instance = ConferenceLegislationsList.from_json(json)
# print the JSON string representation of the object
print(ConferenceLegislationsList.to_json())

# convert the object into a dict
conference_legislations_list_dict = conference_legislations_list_instance.to_dict()
# create an instance of ConferenceLegislationsList from a dict
conference_legislations_list_from_dict = ConferenceLegislationsList.from_dict(conference_legislations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


