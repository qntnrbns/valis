# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.text_disposition_response import TextDispositionResponse

class TestTextDispositionResponse(unittest.TestCase):
    """TextDispositionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextDispositionResponse:
        """Test TextDispositionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextDispositionResponse`
        """
        model = TextDispositionResponse()
        if include_optional:
            return TextDispositionResponse(
                text_disposition_id = 56,
                name = ''
            )
        else:
            return TextDispositionResponse(
        )
        """

    def testTextDispositionResponse(self):
        """Test TextDispositionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
