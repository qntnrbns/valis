# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.legislation_text_response import LegislationTextResponse

class TestLegislationTextResponse(unittest.TestCase):
    """LegislationTextResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegislationTextResponse:
        """Test LegislationTextResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegislationTextResponse`
        """
        model = LegislationTextResponse()
        if include_optional:
            return LegislationTextResponse(
                legislation_id = 56,
                legislation_number = '',
                description = '',
                session_id = 56,
                legislation_text_id = 56,
                draft_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                document_code = '',
                ld_number = '',
                legislation_version_id = 56,
                version = '',
                is_public = True,
                is_complete = True,
                governors_request = True,
                pdf_file = [
                    valis.models.pdf_file.PDFFile(
                        legislation_text_id = 56, 
                        text_format_id = 56, 
                        text_format = '', 
                        file_url = '', 
                        reference_number = '', 
                        session_id = 56, 
                        description = '', 
                        page_count = 56, )
                    ],
                html_file = [
                    valis.models.html_file.HTMLFile(
                        legislation_text_id = 56, 
                        text_format_id = 56, 
                        text_format = '', 
                        file_url = '', 
                        reference_number = '', 
                        session_id = 56, 
                        description = '', )
                    ],
                impact_file = [
                    valis.models.impact_file.ImpactFile(
                        legislation_text_id = 56, 
                        text_format_id = 56, 
                        text_format = '', 
                        file_url = '', 
                        reference_number = '', 
                        session_id = 56, 
                        description = '', )
                    ],
                link_file = [
                    valis.models.link_file.LinkFile(
                        legislation_text_id = 56, 
                        text_format_id = 56, 
                        text_format = '', 
                        file_url = '', 
                        reference_number = '', 
                        session_id = 56, 
                        description = '', )
                    ],
                is_emergency = True,
                is_reprint = True,
                text_disposition_id = 56
            )
        else:
            return LegislationTextResponse(
        )
        """

    def testLegislationTextResponse(self):
        """Test LegislationTextResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
