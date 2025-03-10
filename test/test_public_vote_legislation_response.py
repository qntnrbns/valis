# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_vote_legislation_response import PublicVoteLegislationResponse

class TestPublicVoteLegislationResponse(unittest.TestCase):
    """PublicVoteLegislationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicVoteLegislationResponse:
        """Test PublicVoteLegislationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicVoteLegislationResponse`
        """
        model = PublicVoteLegislationResponse()
        if include_optional:
            return PublicVoteLegislationResponse(
                vote_legislation_id = 56,
                legislation_id = 56,
                legislation_number = '',
                description = '',
                vote_number = '',
                minutes_entry_id = 56,
                vote_items = [
                    valis.models.vote_item_response.VoteItemResponse(
                        ld_number = '', 
                        legislation_version_id = 56, 
                        legislation_version = '', 
                        legislation_text_id = 56, 
                        document_code = '', 
                        description = '', 
                        committee_id = 56, )
                    ]
            )
        else:
            return PublicVoteLegislationResponse(
        )
        """

    def testPublicVoteLegislationResponse(self):
        """Test PublicVoteLegislationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
