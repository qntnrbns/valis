# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.member_patron_type_response import MemberPatronTypeResponse

class TestMemberPatronTypeResponse(unittest.TestCase):
    """MemberPatronTypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberPatronTypeResponse:
        """Test MemberPatronTypeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberPatronTypeResponse`
        """
        model = MemberPatronTypeResponse()
        if include_optional:
            return MemberPatronTypeResponse(
                patron_type_id = 56,
                name = '',
                display_name = ''
            )
        else:
            return MemberPatronTypeResponse(
        )
        """

    def testMemberPatronTypeResponse(self):
        """Test MemberPatronTypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
