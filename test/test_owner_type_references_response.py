# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.owner_type_references_response import OwnerTypeReferencesResponse

class TestOwnerTypeReferencesResponse(unittest.TestCase):
    """OwnerTypeReferencesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OwnerTypeReferencesResponse:
        """Test OwnerTypeReferencesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OwnerTypeReferencesResponse`
        """
        model = OwnerTypeReferencesResponse()
        if include_optional:
            return OwnerTypeReferencesResponse(
                success = True,
                failure_message = '',
                cache_key_name = '',
                list_items = [
                    valis.models.owner_type_reference_response.OwnerTypeReferenceResponse(
                        owner_type_id = 56, 
                        owner_type = '', )
                    ]
            )
        else:
            return OwnerTypeReferencesResponse(
        )
        """

    def testOwnerTypeReferencesResponse(self):
        """Test OwnerTypeReferencesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
