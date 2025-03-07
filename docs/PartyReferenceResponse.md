# PartyReferenceResponse

Information for Political Party

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_code** | **str** | Unique identifer for Political Party | [optional] 
**name** | **str** | Political Party name | [optional] 

## Example

```python
from valis.models.party_reference_response import PartyReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartyReferenceResponse from a JSON string
party_reference_response_instance = PartyReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(PartyReferenceResponse.to_json())

# convert the object into a dict
party_reference_response_dict = party_reference_response_instance.to_dict()
# create an instance of PartyReferenceResponse from a dict
party_reference_response_from_dict = PartyReferenceResponse.from_dict(party_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


