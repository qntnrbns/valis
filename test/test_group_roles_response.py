# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.group_roles_response import GroupRolesResponse

class TestGroupRolesResponse(unittest.TestCase):
    """GroupRolesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupRolesResponse:
        """Test GroupRolesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupRolesResponse`
        """
        model = GroupRolesResponse()
        if include_optional:
            return GroupRolesResponse(
                roles = [
                    valis.models.role_response.RoleResponse(
                        role_id = 56, 
                        role_name = '', 
                        scope = '', 
                        resource = '', 
                        component = '', 
                        action = '', 
                        modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                success = True,
                failure_message = ''
            )
        else:
            return GroupRolesResponse(
        )
        """

    def testGroupRolesResponse(self):
        """Test GroupRolesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
