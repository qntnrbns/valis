# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.models.authentication_response import AuthenticationResponse

class TestAuthenticationResponse(unittest.TestCase):
    """AuthenticationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticationResponse:
        """Test AuthenticationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticationResponse`
        """
        model = AuthenticationResponse()
        if include_optional:
            return AuthenticationResponse(
                email_address = '',
                last_name = '',
                first_name = '',
                unique_id = '',
                groups = '',
                access_token = '',
                graph_token = '',
                refresh_token = '',
                access_token_lifetime = 56,
                claims = valis.models.group_roles_response.GroupRolesResponse(
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
                    failure_message = '', ),
                success = True,
                failure_message = '',
                cache_key_name = '',
                is_password_temporary_or_expired = True
            )
        else:
            return AuthenticationResponse(
        )
        """

    def testAuthenticationResponse(self):
        """Test AuthenticationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
