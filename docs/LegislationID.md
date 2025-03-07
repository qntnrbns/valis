# LegislationID

Used to separate out legislation IDs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_id** | **int** | LegislationID | [optional] 

## Example

```python
from valis.models.legislation_id import LegislationID

# TODO update the JSON string below
json = "{}"
# create an instance of LegislationID from a JSON string
legislation_id_instance = LegislationID.from_json(json)
# print the JSON string representation of the object
print(LegislationID.to_json())

# convert the object into a dict
legislation_id_dict = legislation_id_instance.to_dict()
# create an instance of LegislationID from a dict
legislation_id_from_dict = LegislationID.from_dict(legislation_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


