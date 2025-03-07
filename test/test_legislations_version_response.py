# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.legislations_version_response import LegislationsVersionResponse

class TestLegislationsVersionResponse(unittest.TestCase):
    """LegislationsVersionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegislationsVersionResponse:
        """Test LegislationsVersionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegislationsVersionResponse`
        """
        model = LegislationsVersionResponse()
        if include_optional:
            return LegislationsVersionResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.legislation_version_response.LegislationVersionResponse(
                        legislation_id = 56, 
                        legislation_number = '', 
                        chamber_code = '', 
                        session_id = 56, 
                        legislation_text_id = 56, 
                        draft_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        document_code = '', 
                        description = '', 
                        sponsor = '', 
                        ld_number = '', 
                        legislation_version_id = 56, 
                        version = '', 
                        is_public = True, 
                        is_active = True, 
                        pdf_file = [
                            valis.models.file.File(
                                legislation_text_id = 56, 
                                text_format_id = 56, 
                                text_format = '', 
                                file_url = '', )
                            ], 
                        html_file = [
                            valis.models.file.File(
                                legislation_text_id = 56, 
                                text_format_id = 56, 
                                text_format = '', 
                                file_url = '', )
                            ], 
                        link_file = [
                            
                            ], 
                        impact_file = [
                            
                            ], 
                        text_disposition_id = 56, 
                        text_disposition = '', )
                    ],
                search_criteria = ''
            )
        else:
            return LegislationsVersionResponse(
        )
        """

    def testLegislationsVersionResponse(self):
        """Test LegislationsVersionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
