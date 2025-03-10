# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_personnel_response import PublicPersonnelResponse

class TestPublicPersonnelResponse(unittest.TestCase):
    """PublicPersonnelResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicPersonnelResponse:
        """Test PublicPersonnelResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicPersonnelResponse`
        """
        model = PublicPersonnelResponse()
        if include_optional:
            return PublicPersonnelResponse(
                staff_id = 56,
                affiliation_id = 56,
                staff_role_type_id = 56,
                identity_id = 56,
                organization_name = '',
                full_name = '',
                phone_number = '',
                email_address = '',
                sequence = 56,
                is_public = True,
                effective_begin_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                effective_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PublicPersonnelResponse(
        )
        """

    def testPublicPersonnelResponse(self):
        """Test PublicPersonnelResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
