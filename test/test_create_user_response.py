# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.create_user_response import CreateUserResponse

class TestCreateUserResponse(unittest.TestCase):
    """CreateUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUserResponse:
        """Test CreateUserResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUserResponse`
        """
        model = CreateUserResponse()
        if include_optional:
            return CreateUserResponse(
                user_profile_id = 56,
                login_id = '',
                password = ''
            )
        else:
            return CreateUserResponse(
        )
        """

    def testCreateUserResponse(self):
        """Test CreateUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
