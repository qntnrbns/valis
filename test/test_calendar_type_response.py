# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.calendar_type_response import CalendarTypeResponse

class TestCalendarTypeResponse(unittest.TestCase):
    """CalendarTypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CalendarTypeResponse:
        """Test CalendarTypeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CalendarTypeResponse`
        """
        model = CalendarTypeResponse()
        if include_optional:
            return CalendarTypeResponse(
                name = '',
                id = 56
            )
        else:
            return CalendarTypeResponse(
        )
        """

    def testCalendarTypeResponse(self):
        """Test CalendarTypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
