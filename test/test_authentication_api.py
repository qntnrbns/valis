# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from valis.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_authentication_api_authenticationheartbeatasync_get(self) -> None:
        """Test case for authentication_api_authenticationheartbeatasync_get

        Gets telemetry on service health
        """
        pass

    def test_authentication_api_changepasswordasync_put(self) -> None:
        """Test case for authentication_api_changepasswordasync_put

        Changes your password
        """
        pass

    def test_authentication_api_getaccesstokenasync_post(self) -> None:
        """Test case for authentication_api_getaccesstokenasync_post

        Get Access Token
        """
        pass

    def test_authentication_api_loginasync_post(self) -> None:
        """Test case for authentication_api_loginasync_post

        Makes a request to login
        """
        pass

    def test_authentication_api_refreshaccesstokenasync_post(self) -> None:
        """Test case for authentication_api_refreshaccesstokenasync_post

        Refreshes the access token
        """
        pass


if __name__ == '__main__':
    unittest.main()
