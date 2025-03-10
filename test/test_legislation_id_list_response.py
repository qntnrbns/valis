# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.legislation_id_list_response import LegislationIdListResponse

class TestLegislationIdListResponse(unittest.TestCase):
    """LegislationIdListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegislationIdListResponse:
        """Test LegislationIdListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegislationIdListResponse`
        """
        model = LegislationIdListResponse()
        if include_optional:
            return LegislationIdListResponse(
                legislation_id = 56,
                legislation_status_id = 56,
                legislation_number = '',
                session_id = 56,
                session_code = 56,
                search_text = [
                    valis.models.legislation_search_text.LegislationSearchText(
                        legislation_text_id = 56, 
                        description = '', 
                        document_code = '', 
                        count_matches = 56, )
                    ]
            )
        else:
            return LegislationIdListResponse(
        )
        """

    def testLegislationIdListResponse(self):
        """Test LegislationIdListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
