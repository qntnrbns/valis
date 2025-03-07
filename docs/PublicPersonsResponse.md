# PublicPersonsResponse

Public Request and Response object containing a list of LIS persons (using PersonResponse). If no valid response could be   obtained, Success boolean will be false and additional information can be found in the FailureMessage string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is this a successful response? | [optional] 
**failure_message** | **str** | Details if this response failed | [optional] 
**cache_key_name** | **str** | CacheKey name | [optional] 
**list_items** | [**List[PublicPersonResponse]**](PublicPersonResponse.md) | list of persons | [optional] 

## Example

```python
from valis.models.public_persons_response import PublicPersonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPersonsResponse from a JSON string
public_persons_response_instance = PublicPersonsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicPersonsResponse.to_json())

# convert the object into a dict
public_persons_response_dict = public_persons_response_instance.to_dict()
# create an instance of PublicPersonsResponse from a dict
public_persons_response_from_dict = PublicPersonsResponse.from_dict(public_persons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


