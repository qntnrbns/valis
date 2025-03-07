# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.contact_response import ContactResponse

class TestContactResponse(unittest.TestCase):
    """ContactResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactResponse:
        """Test ContactResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactResponse`
        """
        model = ContactResponse()
        if include_optional:
            return ContactResponse(
                contact_information_id = 56,
                owner_id = 56,
                contact_type_id = 56,
                contact_type = '',
                address1 = '',
                address2 = '',
                address3 = '',
                city = '',
                state_code = '',
                zip_code = '',
                phone_number = '',
                email_address = '',
                is_active = True,
                is_public = True
            )
        else:
            return ContactResponse(
        )
        """

    def testContactResponse(self):
        """Test ContactResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
