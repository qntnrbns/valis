# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_vote_member_response import PublicVoteMemberResponse

class TestPublicVoteMemberResponse(unittest.TestCase):
    """PublicVoteMemberResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicVoteMemberResponse:
        """Test PublicVoteMemberResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicVoteMemberResponse`
        """
        model = PublicVoteMemberResponse()
        if include_optional:
            return PublicVoteMemberResponse(
                vote_member_id = 56,
                member_id = 56,
                member_display_name = '',
                patron_display_name = '',
                member_number = '',
                response_code = '0',
                vote_statement = '',
                voting_sequence = 56
            )
        else:
            return PublicVoteMemberResponse(
        )
        """

    def testPublicVoteMemberResponse(self):
        """Test PublicVoteMemberResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
