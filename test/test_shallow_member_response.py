# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.shallow_member_response import ShallowMemberResponse

class TestShallowMemberResponse(unittest.TestCase):
    """ShallowMemberResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShallowMemberResponse:
        """Test ShallowMemberResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShallowMemberResponse`
        """
        model = ShallowMemberResponse()
        if include_optional:
            return ShallowMemberResponse(
                member_id = 56,
                identity_id = 56,
                session_code = '',
                member_number = '',
                list_display_name = '',
                member_display_name = '',
                patron_display_name = '',
                chamber_code = '0',
                party_code = '0',
                member_status_id = 56,
                member_status = '',
                service_begin_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                service_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                service_end_reason = '',
                gab_phone_number = '',
                gab_email_address = '',
                is_public = True
            )
        else:
            return ShallowMemberResponse(
        )
        """

    def testShallowMemberResponse(self):
        """Test ShallowMemberResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
