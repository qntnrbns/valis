# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.shallow_minute_book_response import ShallowMinuteBookResponse

class TestShallowMinuteBookResponse(unittest.TestCase):
    """ShallowMinuteBookResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShallowMinuteBookResponse:
        """Test ShallowMinuteBookResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShallowMinuteBookResponse`
        """
        model = ShallowMinuteBookResponse()
        if include_optional:
            return ShallowMinuteBookResponse(
                vote_room_id = 56,
                session_name = '',
                session_code = '',
                session_id = 56,
                committee_id = 56,
                committee_name = '',
                chamber_code = '0',
                minutes_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                minutes_number = 56,
                minutes_status_id = 56,
                minutes_status = '',
                minutes_book_id = 56,
                status = '',
                pending_change = True,
                minutes_calendars = [
                    valis.models.public_minutes_calendar.PublicMinutesCalendar(
                        minutes_book_id = 56, 
                        calendar_id = 56, 
                        calendar_number = 56, 
                        description = '', 
                        minutes_status_id = 56, 
                        calendar_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = '', 
                        status_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                minutes_files = [
                    valis.models.public_minutes_file.PublicMinutesFile(
                        minutes_book_id = 56, 
                        file_url = '', 
                        text_format_id = 56, 
                        is_active = True, 
                        minutes_file_id = 56, )
                    ]
            )
        else:
            return ShallowMinuteBookResponse(
                session_id = 56,
                chamber_code = '0',
                minutes_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testShallowMinuteBookResponse(self):
        """Test ShallowMinuteBookResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
