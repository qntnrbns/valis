# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.communication_category_type_reference import CommunicationCategoryTypeReference

class TestCommunicationCategoryTypeReference(unittest.TestCase):
    """CommunicationCategoryTypeReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommunicationCategoryTypeReference:
        """Test CommunicationCategoryTypeReference
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommunicationCategoryTypeReference`
        """
        model = CommunicationCategoryTypeReference()
        if include_optional:
            return CommunicationCategoryTypeReference(
                communication_category_type_id = 56,
                category_code = '',
                description = '',
                plural_description = '',
                chamber_code = '',
                sequence = 56
            )
        else:
            return CommunicationCategoryTypeReference(
        )
        """

    def testCommunicationCategoryTypeReference(self):
        """Test CommunicationCategoryTypeReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
