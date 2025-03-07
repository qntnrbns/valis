# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.legislation_amendment_response import LegislationAmendmentResponse

class TestLegislationAmendmentResponse(unittest.TestCase):
    """LegislationAmendmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegislationAmendmentResponse:
        """Test LegislationAmendmentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegislationAmendmentResponse`
        """
        model = LegislationAmendmentResponse()
        if include_optional:
            return LegislationAmendmentResponse(
                session_id = 56,
                session_code = '',
                legislation_class_id = 56,
                legislation_number = '',
                description = '',
                legislation_title = '',
                offered_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                introduction_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                chamber_code = '',
                legislation_type_code = '',
                full_number = '',
                legislation_status_id = 56,
                legislation_id = 56,
                legislation_key = 56,
                legislation_status = '',
                legislation_summary = '',
                legislation_text_id = 56,
                effective_type = '',
                effective_type_id = 56,
                pending_change = True,
                summary_version = '',
                session_name = '',
                committee_name = '',
                committee_id = 56,
                parent_committee_name = '',
                committee_number = '',
                amendments = [
                    valis.models.amendment_response.AmendmentResponse(
                        legislation_id = 56, 
                        legislation_text_id = 56, 
                        legislation_version_id = 56, 
                        legislation_version = '', 
                        text_disposition_id = 56, 
                        text_disposition = '', 
                        is_active = True, 
                        is_public = True, 
                        document_code = '', 
                        chamber_code = '', 
                        description = '', 
                        ld_number = '', 
                        version_date = '', )
                    ],
                patrons = [
                    valis.models.legislation_patron.LegislationPatron(
                        legislation_id = 56, 
                        legislation_text_id = 56, 
                        chamber_code = '', 
                        member_id = 56, 
                        member_number = '', 
                        patron_type_id = 56, 
                        name = '', 
                        display_name = '', 
                        member_display_name = '', 
                        patron_display_name = '', 
                        sequence = 56, 
                        by_request = True, )
                    ]
            )
        else:
            return LegislationAmendmentResponse(
        )
        """

    def testLegislationAmendmentResponse(self):
        """Test LegislationAmendmentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
