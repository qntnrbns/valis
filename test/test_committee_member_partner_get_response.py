# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.committee_member_partner_get_response import CommitteeMemberPartnerGetResponse

class TestCommitteeMemberPartnerGetResponse(unittest.TestCase):
    """CommitteeMemberPartnerGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommitteeMemberPartnerGetResponse:
        """Test CommitteeMemberPartnerGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitteeMemberPartnerGetResponse`
        """
        model = CommitteeMemberPartnerGetResponse()
        if include_optional:
            return CommitteeMemberPartnerGetResponse(
                committee_member_id = 56,
                committee_id = 56,
                committee_number = '',
                member_id = 56,
                member_number = '',
                member_display_name = '',
                patron_display_name = '',
                party_code = '',
                voting_sequence = 56,
                display_sequence = 56,
                committee_role_id = 56,
                title = '',
                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_public = True
            )
        else:
            return CommitteeMemberPartnerGetResponse(
        )
        """

    def testCommitteeMemberPartnerGetResponse(self):
        """Test CommitteeMemberPartnerGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
