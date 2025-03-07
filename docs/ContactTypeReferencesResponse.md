# ContactTypeReferencesResponse

Request and Response object containing a list of LIS contact references (using ContactReferenceResponse). If no valid response could be obtained, Success boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[ContactTypeReferenceResponse]**](ContactTypeReferenceResponse.md) | list of contact references | [optional] 

## Example

```python
from valis.models.contact_type_references_response import ContactTypeReferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTypeReferencesResponse from a JSON string
contact_type_references_response_instance = ContactTypeReferencesResponse.from_json(json)
# print the JSON string representation of the object
print(ContactTypeReferencesResponse.to_json())

# convert the object into a dict
contact_type_references_response_dict = contact_type_references_response_instance.to_dict()
# create an instance of ContactTypeReferencesResponse from a dict
contact_type_references_response_from_dict = ContactTypeReferencesResponse.from_dict(contact_type_references_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


