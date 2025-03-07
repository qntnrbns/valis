# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.meeting_rooms_response import MeetingRoomsResponse

class TestMeetingRoomsResponse(unittest.TestCase):
    """MeetingRoomsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeetingRoomsResponse:
        """Test MeetingRoomsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MeetingRoomsResponse`
        """
        model = MeetingRoomsResponse()
        if include_optional:
            return MeetingRoomsResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.meeting_room_response.MeetingRoomResponse(
                        vote_room_id = 56, 
                        description = '', 
                        room_number = '', 
                        seat_count = 56, 
                        chamber_code = '', )
                    ]
            )
        else:
            return MeetingRoomsResponse(
        )
        """

    def testMeetingRoomsResponse(self):
        """Test MeetingRoomsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
