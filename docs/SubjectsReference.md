# SubjectsReference

List of Subject References

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[SubjectReference]**](SubjectReference.md) | list of subjects references | [optional] 

## Example

```python
from valis.models.subjects_reference import SubjectsReference

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectsReference from a JSON string
subjects_reference_instance = SubjectsReference.from_json(json)
# print the JSON string representation of the object
print(SubjectsReference.to_json())

# convert the object into a dict
subjects_reference_dict = subjects_reference_instance.to_dict()
# create an instance of SubjectsReference from a dict
subjects_reference_from_dict = SubjectsReference.from_dict(subjects_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


