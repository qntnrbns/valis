# SubjectReference

Subject Reference Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_index_id** | **int** | subject unique identifier | [optional] 
**subject** | **str** | subject name/description | [optional] 
**subject_number** | **str** | subject number | [optional] 

## Example

```python
from valis.models.subject_reference import SubjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectReference from a JSON string
subject_reference_instance = SubjectReference.from_json(json)
# print the JSON string representation of the object
print(SubjectReference.to_json())

# convert the object into a dict
subject_reference_dict = subject_reference_instance.to_dict()
# create an instance of SubjectReference from a dict
subject_reference_from_dict = SubjectReference.from_dict(subject_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


