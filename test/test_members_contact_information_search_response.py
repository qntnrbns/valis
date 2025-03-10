# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.members_contact_information_search_response import MembersContactInformationSearchResponse

class TestMembersContactInformationSearchResponse(unittest.TestCase):
    """MembersContactInformationSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MembersContactInformationSearchResponse:
        """Test MembersContactInformationSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MembersContactInformationSearchResponse`
        """
        model = MembersContactInformationSearchResponse()
        if include_optional:
            return MembersContactInformationSearchResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.member_contact_information_search_response.MemberContactInformationSearchResponse(
                        member_id = 56, 
                        identity_id = 56, 
                        member_number = '', 
                        full_name = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        member_display_name = '', 
                        room_number = '', 
                        is_public = True, 
                        gab_phone_number = '', 
                        gab_email_address = '', 
                        chamber_code = '0', 
                        chamber = '', 
                        party_code = '0', 
                        party_name = '', 
                        district_id = 56, 
                        district_name = '', 
                        member_status_id = 56, 
                        member_status = '', 
                        service_begin_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_end_reason = '', 
                        contact_information = [
                            valis.models.contact_response.ContactResponse(
                                contact_information_id = 56, 
                                owner_id = 56, 
                                contact_type_id = 56, 
                                contact_type = '', 
                                address1 = '', 
                                address2 = '', 
                                address3 = '', 
                                city = '', 
                                state_code = '', 
                                zip_code = '', 
                                phone_number = '', 
                                email_address = '', 
                                is_active = True, 
                                is_public = True, )
                            ], )
                    ]
            )
        else:
            return MembersContactInformationSearchResponse(
        )
        """

    def testMembersContactInformationSearchResponse(self):
        """Test MembersContactInformationSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
