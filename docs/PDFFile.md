# PDFFile

PDF File object representing storage in Azure Blob Storage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legislation_text_id** | **int** | unique identifier of LegislationText | [optional] 
**text_format_id** | **int** | unique identifier of TextFormat | [optional] 
**text_format** | **str** | Text Format (e.g. PDF) | [optional] 
**file_url** | **str** | Azure Blob Storage URL | [optional] 
**reference_number** | **str** | Reference Number | [optional] 
**session_id** | **int** | internal SessionID | [optional] 
**description** | **str** | Description | [optional] 
**page_count** | **int** | Page count for a particular bill pdf | [optional] 

## Example

```python
from valis.models.pdf_file import PDFFile

# TODO update the JSON string below
json = "{}"
# create an instance of PDFFile from a JSON string
pdf_file_instance = PDFFile.from_json(json)
# print the JSON string representation of the object
print(PDFFile.to_json())

# convert the object into a dict
pdf_file_dict = pdf_file_instance.to_dict()
# create an instance of PDFFile from a dict
pdf_file_from_dict = PDFFile.from_dict(pdf_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


