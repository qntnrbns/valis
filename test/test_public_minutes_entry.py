# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_minutes_entry import PublicMinutesEntry

class TestPublicMinutesEntry(unittest.TestCase):
    """PublicMinutesEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicMinutesEntry:
        """Test PublicMinutesEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicMinutesEntry`
        """
        model = PublicMinutesEntry()
        if include_optional:
            return PublicMinutesEntry(
                minutes_category_id = 56,
                sequence = 56,
                legislation_id = 56,
                legislation_number = '',
                legislation_description = '',
                agenda_id = 56,
                entry_text = '',
                communication_id = 56,
                legislation_chamber_code = '',
                communication_reference_number = '',
                is_public = True,
                communication_chamber_code = '',
                communication_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                communication_number = 56,
                is_oob = True,
                release_to_preview = True,
                minutes_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                minutes_entry_id = 56,
                minutes_activities = [
                    valis.models.public_minutes_activity.PublicMinutesActivity(
                        minutes_entry_id = 56, 
                        description = '', 
                        sequence = 56, 
                        calendar_action_id = 56, 
                        action_description = '', 
                        committee_complete = True, 
                        vote_id = 56, 
                        deletion_date = '', 
                        is_public = True, 
                        is_passed = True, 
                        in_preview = True, 
                        minutes_activity_id = 56, 
                        activity_references = [
                            valis.models.public_activity_reference.PublicActivityReference(
                                reference_text = '', 
                                reference_id = 56, 
                                minutes_activity_id = 56, 
                                action_reference_type_id = 56, 
                                action_reference_type = '', 
                                sequence = 56, )
                            ], )
                    ],
                minutes_summaries = [
                    valis.models.public_minutes_summary.PublicMinutesSummary(
                        minutes_entry_id = 56, 
                        minutes_summary = '', )
                    ]
            )
        else:
            return PublicMinutesEntry(
        )
        """

    def testPublicMinutesEntry(self):
        """Test PublicMinutesEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
