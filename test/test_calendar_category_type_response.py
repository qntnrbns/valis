# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.calendar_category_type_response import CalendarCategoryTypeResponse

class TestCalendarCategoryTypeResponse(unittest.TestCase):
    """CalendarCategoryTypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CalendarCategoryTypeResponse:
        """Test CalendarCategoryTypeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CalendarCategoryTypeResponse`
        """
        model = CalendarCategoryTypeResponse()
        if include_optional:
            return CalendarCategoryTypeResponse(
                clerks_copy = True,
                calendar_category_type_id = 56,
                category_code = '',
                description = '',
                plural_description = '',
                sequence = 56,
                chamber_code = '',
                calendar_type_id = 56,
                category_type_id = 56,
                category_type = '',
                display_type = True,
                legislation_type_code = '',
                legislation_chamber_code = '',
                is_legislation_category = True,
                is_print = True
            )
        else:
            return CalendarCategoryTypeResponse(
                calendar_category_type_id = 56,
                category_code = '',
                description = '',
                sequence = 56,
                calendar_type_id = 56,
                category_type_id = 56,
                is_legislation_category = True,
        )
        """

    def testCalendarCategoryTypeResponse(self):
        """Test CalendarCategoryTypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
