# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.amendment_item import AmendmentItem

class TestAmendmentItem(unittest.TestCase):
    """AmendmentItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AmendmentItem:
        """Test AmendmentItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AmendmentItem`
        """
        model = AmendmentItem()
        if include_optional:
            return AmendmentItem(
                sponsor = valis.models.sponsor.Sponsor(
                    name = '', 
                    class_name = '', ),
                line = '',
                line_number = 56,
                line_class_name = '',
                item_order = 56,
                item_condition = '',
                amendment_changes = [
                    valis.models.amendment_change.AmendmentChange(
                        class_name = '', 
                        amendment_actions = [
                            valis.models.amendment_action.AmendmentAction(
                                text_class_name = '', 
                                action = '', 
                                text = '', )
                            ], )
                    ]
            )
        else:
            return AmendmentItem(
        )
        """

    def testAmendmentItem(self):
        """Test AmendmentItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
