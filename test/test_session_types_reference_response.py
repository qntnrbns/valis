# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.session_types_reference_response import SessionTypesReferenceResponse

class TestSessionTypesReferenceResponse(unittest.TestCase):
    """SessionTypesReferenceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SessionTypesReferenceResponse:
        """Test SessionTypesReferenceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SessionTypesReferenceResponse`
        """
        model = SessionTypesReferenceResponse()
        if include_optional:
            return SessionTypesReferenceResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.session_type_reference_response.SessionTypeReferenceResponse(
                        name = '', 
                        id = 56, )
                    ]
            )
        else:
            return SessionTypesReferenceResponse(
        )
        """

    def testSessionTypesReferenceResponse(self):
        """Test SessionTypesReferenceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
