# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.committee_statistic_response import CommitteeStatisticResponse

class TestCommitteeStatisticResponse(unittest.TestCase):
    """CommitteeStatisticResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommitteeStatisticResponse:
        """Test CommitteeStatisticResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitteeStatisticResponse`
        """
        model = CommitteeStatisticResponse()
        if include_optional:
            return CommitteeStatisticResponse(
                committee_id = 56,
                committee_number = '',
                committee_name = '',
                h_referred = 56,
                s_referred = 56,
                hin_committee = 56,
                sin_committee = 56,
                hin_sub_committee = 56,
                sin_sub_committee = 56,
                h_reported = 56,
                s_reported = 56,
                h_incorporated = 56,
                s_incorporated = 56,
                h_continued = 56,
                s_continued = 56,
                h_continued_from = 56,
                s_continued_from = 56,
                h_failed = 56,
                s_failed = 56
            )
        else:
            return CommitteeStatisticResponse(
        )
        """

    def testCommitteeStatisticResponse(self):
        """Test CommitteeStatisticResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
