# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.public_communications_list import PublicCommunicationsList

class TestPublicCommunicationsList(unittest.TestCase):
    """PublicCommunicationsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicCommunicationsList:
        """Test PublicCommunicationsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicCommunicationsList`
        """
        model = PublicCommunicationsList()
        if include_optional:
            return PublicCommunicationsList(
                communication_id = 56,
                communication_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                communication_number = 56,
                reference_number = '',
                is_public = True,
                communication_type_id = 56,
                communication_type = '',
                chamber_code = '0',
                session_id = 56,
                show_signature_note = True,
                communication_files = [
                    valis.models.public_communication_file.PublicCommunicationFile(
                        communication_file_id = 56, 
                        communication_id = 56, 
                        file_url = '', 
                        text_format_id = 56, 
                        is_generated = True, 
                        is_public = True, 
                        is_active = True, )
                    ]
            )
        else:
            return PublicCommunicationsList(
        )
        """

    def testPublicCommunicationsList(self):
        """Test PublicCommunicationsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
