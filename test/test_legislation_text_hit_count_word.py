# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.legislation_text_hit_count_word import LegislationTextHitCountWord

class TestLegislationTextHitCountWord(unittest.TestCase):
    """LegislationTextHitCountWord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegislationTextHitCountWord:
        """Test LegislationTextHitCountWord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegislationTextHitCountWord`
        """
        model = LegislationTextHitCountWord()
        if include_optional:
            return LegislationTextHitCountWord(
                hitword = ''
            )
        else:
            return LegislationTextHitCountWord(
        )
        """

    def testLegislationTextHitCountWord(self):
        """Test LegislationTextHitCountWord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
