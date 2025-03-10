# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.text_dispositions_response import TextDispositionsResponse

class TestTextDispositionsResponse(unittest.TestCase):
    """TextDispositionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextDispositionsResponse:
        """Test TextDispositionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextDispositionsResponse`
        """
        model = TextDispositionsResponse()
        if include_optional:
            return TextDispositionsResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.text_disposition_response.TextDispositionResponse(
                        text_disposition_id = 56, 
                        name = '', )
                    ]
            )
        else:
            return TextDispositionsResponse(
        )
        """

    def testTextDispositionsResponse(self):
        """Test TextDispositionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
