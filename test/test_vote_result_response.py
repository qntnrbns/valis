# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.vote_result_response import VoteResultResponse

class TestVoteResultResponse(unittest.TestCase):
    """VoteResultResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VoteResultResponse:
        """Test VoteResultResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VoteResultResponse`
        """
        model = VoteResultResponse()
        if include_optional:
            return VoteResultResponse(
                vote_id = 56,
                chamber_code = '0',
                committee_id = 56,
                committee_name = '',
                vote_number = '',
                session_id = 56,
                vote_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sequence = 56,
                vote_type_id = 56,
                vote_type = '',
                vote_classification_id = 56,
                classification_name = '',
                batch_number = '',
                vote_description = '',
                vote_action_id = 56,
                action_description = '',
                pass_fail = '',
                response_code = '',
                vote_statement = '',
                vote_legislation_id = 56,
                legislation_id = 56,
                legislation_number = '',
                legislation_description = ''
            )
        else:
            return VoteResultResponse(
        )
        """

    def testVoteResultResponse(self):
        """Test VoteResultResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
