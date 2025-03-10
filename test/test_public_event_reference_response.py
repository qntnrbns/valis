# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_event_reference_response import PublicEventReferenceResponse

class TestPublicEventReferenceResponse(unittest.TestCase):
    """PublicEventReferenceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicEventReferenceResponse:
        """Test PublicEventReferenceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicEventReferenceResponse`
        """
        model = PublicEventReferenceResponse()
        if include_optional:
            return PublicEventReferenceResponse(
                event_reference_id = 56,
                reference_text = '',
                reference_id = 56,
                legislation_event_id = 56,
                action_reference_type_id = 56,
                action_reference_type = '',
                sequence = 56
            )
        else:
            return PublicEventReferenceResponse(
        )
        """

    def testPublicEventReferenceResponse(self):
        """Test PublicEventReferenceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
