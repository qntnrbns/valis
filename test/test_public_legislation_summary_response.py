# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_legislation_summary_response import PublicLegislationSummaryResponse

class TestPublicLegislationSummaryResponse(unittest.TestCase):
    """PublicLegislationSummaryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicLegislationSummaryResponse:
        """Test PublicLegislationSummaryResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicLegislationSummaryResponse`
        """
        model = PublicLegislationSummaryResponse()
        if include_optional:
            return PublicLegislationSummaryResponse(
                legislation_number = '',
                summary = '',
                document_code = '',
                ld_number = '',
                summary_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_version_id = 56,
                is_public = True,
                is_active = True,
                legislation_id = 56,
                session_id = 56,
                legislation_summary_id = 56,
                summary_version = ''
            )
        else:
            return PublicLegislationSummaryResponse(
        )
        """

    def testPublicLegislationSummaryResponse(self):
        """Test PublicLegislationSummaryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
