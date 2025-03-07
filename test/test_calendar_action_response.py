# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.calendar_action_response import CalendarActionResponse

class TestCalendarActionResponse(unittest.TestCase):
    """CalendarActionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CalendarActionResponse:
        """Test CalendarActionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CalendarActionResponse`
        """
        model = CalendarActionResponse()
        if include_optional:
            return CalendarActionResponse(
                calendar_action_id = 56,
                vote_description = '',
                description = '',
                event_code = '',
                chamber_code = '',
                category_code = '',
                calendar_category_type_id = 56,
                legislation_chamber_code = '',
                is_passed = True,
                in_preview = True,
                action_references = [
                    valis.models.calendar_action_reference_response.CalendarActionReferenceResponse(
                        action_reference_id = 56, 
                        is_mandatory = True, 
                        sequence = 56, 
                        reference_text = '', 
                        calendar_action_id = 56, 
                        action_reference_type_id = 56, 
                        action_reference_type = '', )
                    ]
            )
        else:
            return CalendarActionResponse(
                calendar_action_id = 56,
                vote_description = '',
                description = '',
        )
        """

    def testCalendarActionResponse(self):
        """Test CalendarActionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
