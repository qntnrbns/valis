# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.district_reference_response import DistrictReferenceResponse

class TestDistrictReferenceResponse(unittest.TestCase):
    """DistrictReferenceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DistrictReferenceResponse:
        """Test DistrictReferenceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DistrictReferenceResponse`
        """
        model = DistrictReferenceResponse()
        if include_optional:
            return DistrictReferenceResponse(
                chamber_code = '0',
                district_id = 56,
                title = '',
                description = ''
            )
        else:
            return DistrictReferenceResponse(
        )
        """

    def testDistrictReferenceResponse(self):
        """Test DistrictReferenceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
