# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.key_word import KeyWord

class TestKeyWord(unittest.TestCase):
    """KeyWord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyWord:
        """Test KeyWord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyWord`
        """
        model = KeyWord()
        if include_optional:
            return KeyWord(
                keyword = '',
                operator = '',
                keywords = [
                    valis.models.key_word.KeyWord(
                        keyword = '', 
                        operator = '', )
                    ]
            )
        else:
            return KeyWord(
        )
        """

    def testKeyWord(self):
        """Test KeyWord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
