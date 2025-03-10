# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_get_communication_legislation_response import PublicGetCommunicationLegislationResponse

class TestPublicGetCommunicationLegislationResponse(unittest.TestCase):
    """PublicGetCommunicationLegislationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicGetCommunicationLegislationResponse:
        """Test PublicGetCommunicationLegislationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicGetCommunicationLegislationResponse`
        """
        model = PublicGetCommunicationLegislationResponse()
        if include_optional:
            return PublicGetCommunicationLegislationResponse(
                communication_category_id = 56,
                legislation_id = 56,
                legislation_number = '',
                legislation_key = 56,
                legislation_description = '',
                is_active = True,
                legislation_text_id = 56,
                committee_referred_name = '',
                event_code = '',
                document_code = '',
                ld_number = '',
                draft_title = '',
                vote_id = 56,
                vote_number = '',
                suffix = '',
                effective_type_id = 56,
                effective_type = '',
                is_candidate = True,
                communication_legislation_id = 56,
                patrons = [
                    valis.models.patron_1.Patron_1(
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
                        by_request = True, )
                    ]
            )
        else:
            return PublicGetCommunicationLegislationResponse(
        )
        """

    def testPublicGetCommunicationLegislationResponse(self):
        """Test PublicGetCommunicationLegislationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
