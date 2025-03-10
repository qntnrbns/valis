# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.dockets_with_schedules_public_get_response import DocketsWithSchedulesPublicGetResponse

class TestDocketsWithSchedulesPublicGetResponse(unittest.TestCase):
    """DocketsWithSchedulesPublicGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocketsWithSchedulesPublicGetResponse:
        """Test DocketsWithSchedulesPublicGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocketsWithSchedulesPublicGetResponse`
        """
        model = DocketsWithSchedulesPublicGetResponse()
        if include_optional:
            return DocketsWithSchedulesPublicGetResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.docket_with_schedule_public_get_response.DocketWithSchedulePublicGetResponse(
                        docket_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        meeting_time = '', 
                        docket_number = 56, 
                        description = '', 
                        is_public = True, 
                        docket_type_id = 56, 
                        docket_type = '', 
                        chamber_code = '', 
                        session_id = 56, 
                        session_code = '', 
                        vote_room_id = 56, 
                        comments = '', 
                        committee_id = 56, 
                        committee_name = '', 
                        parent_committee_name = '', 
                        pending_change = True, 
                        reference_number = '', 
                        is_proforma = True, 
                        deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        docket_id = 56, 
                        calendar_display = [
                            valis.models.calendar_display_public_get_response.CalendarDisplayPublicGetResponse(
                                display_column = '', 
                                is_displayed = True, )
                            ], 
                        committee_member = [
                            valis.models.committee_member_partner_get_response.CommitteeMemberPartnerGetResponse(
                                committee_member_id = 56, 
                                committee_id = 56, 
                                committee_number = '', 
                                member_id = 56, 
                                member_number = '', 
                                member_display_name = '', 
                                patron_display_name = '', 
                                party_code = '', 
                                voting_sequence = 56, 
                                display_sequence = 56, 
                                committee_role_id = 56, 
                                title = '', 
                                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                is_public = True, )
                            ], 
                        staff = [
                            valis.models.staff_partner_get_response.StaffPartnerGetResponse(
                                staff_id = 56, 
                                affiliation_id = 56, 
                                staff_role_type_id = 56, 
                                identity_id = 56, 
                                full_name = '', 
                                sequence = 56, 
                                is_public = True, 
                                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        docket_categories = [
                            valis.models.docket_category_public_get_response.DocketCategoryPublicGetResponse(
                                calendar_id = 56, 
                                calendar_category_type_id = 56, 
                                category_code = '', 
                                category_type = '', 
                                description = '', 
                                plural_description = '', 
                                sequence = 56, 
                                display_type = True, 
                                is_legislation_category = True, 
                                is_print = True, 
                                calendar_category_id = 56, 
                                docket_items = [
                                    valis.models.docket_item_public_get_response.DocketItemPublicGetResponse(
                                        sequence = 56, 
                                        docket_id = 56, 
                                        category_type = '', 
                                        docket_category_id = 56, 
                                        category_code = '', 
                                        description = '', 
                                        legislation_id = 56, 
                                        legislation_number = '', 
                                        legislation_description = '', 
                                        ld_number = '', 
                                        summary = '', 
                                        draft_title = '', 
                                        is_active = True, 
                                        calendar_category_template_id = 56, 
                                        communication_id = 56, 
                                        committee_id = 56, 
                                        candidate_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        docket_item_id = 56, 
                                        patrons = [
                                            valis.models.patron_partner_get_response.PatronPartnerGetResponse(
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
                                            ], )
                                    ], )
                            ], 
                        docket_files = [
                            valis.models.docket_file_partner_get_response.DocketFilePartnerGetResponse(
                                calendar_file_id = 56, 
                                calendar_id = 56, 
                                file_url = '', 
                                text_format_id = 56, 
                                is_generated = True, 
                                is_public = True, 
                                is_active = True, 
                                modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        schedules = [
                            valis.models.public_schedule_response.PublicScheduleResponse(
                                display_sequence = 56, 
                                owner_id = 56, 
                                owner_name = '', 
                                schedule_type_id = 56, 
                                schedule_type = '', 
                                vote_room_id = 56, 
                                room_description = '', 
                                schedule_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                schedule_time = '', 
                                comments = '', 
                                is_cancelled = True, 
                                is_public = True, 
                                link_url = '', 
                                schedule_id = 56, 
                                version_sequence = 56, )
                            ], )
                    ]
            )
        else:
            return DocketsWithSchedulesPublicGetResponse(
        )
        """

    def testDocketsWithSchedulesPublicGetResponse(self):
        """Test DocketsWithSchedulesPublicGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
