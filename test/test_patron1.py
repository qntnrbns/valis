# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.patron1 import Patron1

class TestPatron1(unittest.TestCase):
    """Patron1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Patron1:
        """Test Patron1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Patron1`
        """
        model = Patron1()
        if include_optional:
            return Patron1(
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
                by_request = True
            )
        else:
            return Patron1(
        )
        """

    def testPatron1(self):
        """Test Patron1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
