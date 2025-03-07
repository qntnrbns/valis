# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_shallow_vote_response import PublicShallowVoteResponse

class TestPublicShallowVoteResponse(unittest.TestCase):
    """PublicShallowVoteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicShallowVoteResponse:
        """Test PublicShallowVoteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicShallowVoteResponse`
        """
        model = PublicShallowVoteResponse()
        if include_optional:
            return PublicShallowVoteResponse(
                vote_id = 56,
                chamber_code = '0',
                committee_id = 56,
                committee_name = '',
                legislation_number = '',
                reference_id = 56,
                reference_number = '',
                vote_number = '',
                is_voice = True,
                is_block = True,
                is_public = True,
                session_id = 56,
                session_code = '',
                vote_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sequence = 56,
                vote_type_id = 56,
                vote_type = '',
                batch_number = '',
                description = '',
                vote_tally = '',
                vote_room_id = 56,
                room_description = '',
                event_code = '',
                vote_action_description = '',
                vote_action_id = 56,
                vote_classification_id = 56,
                refer_to_committee_id = 56,
                refer_to_committee_number = '',
                classification_name = ''
            )
        else:
            return PublicShallowVoteResponse(
                vote_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testPublicShallowVoteResponse(self):
        """Test PublicShallowVoteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
