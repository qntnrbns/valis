# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.impact_file import ImpactFile

class TestImpactFile(unittest.TestCase):
    """ImpactFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImpactFile:
        """Test ImpactFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImpactFile`
        """
        model = ImpactFile()
        if include_optional:
            return ImpactFile(
                legislation_text_id = 56,
                text_format_id = 56,
                text_format = '',
                file_url = '',
                reference_number = '',
                session_id = 56,
                description = ''
            )
        else:
            return ImpactFile(
        )
        """

    def testImpactFile(self):
        """Test ImpactFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
