# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.role_api import RoleApi


class TestRoleApi(unittest.TestCase):
    """ RoleApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.role_api.RoleApi()

    def tearDown(self):
        pass

    def test_all_model_sets(self):
        """
        Test case for all_model_sets

        Get All Model Sets
        """
        pass

    def test_all_permission_sets(self):
        """
        Test case for all_permission_sets

        Get All Permission Sets
        """
        pass

    def test_all_permissions(self):
        """
        Test case for all_permissions

        Get All Permissions
        """
        pass

    def test_all_roles(self):
        """
        Test case for all_roles

        Get All Roles
        """
        pass

    def test_create_model_set(self):
        """
        Test case for create_model_set

        Create Model Set
        """
        pass

    def test_create_permission_set(self):
        """
        Test case for create_permission_set

        Create Permission Set
        """
        pass

    def test_create_role(self):
        """
        Test case for create_role

        Create Role
        """
        pass

    def test_delete_model_set(self):
        """
        Test case for delete_model_set

        Delete Model Set
        """
        pass

    def test_delete_permission_set(self):
        """
        Test case for delete_permission_set

        Delete Permission Set
        """
        pass

    def test_delete_role(self):
        """
        Test case for delete_role

        Delete Role
        """
        pass

    def test_model_set(self):
        """
        Test case for model_set

        Get Model Set
        """
        pass

    def test_permission_set(self):
        """
        Test case for permission_set

        Get Permission Set
        """
        pass

    def test_role(self):
        """
        Test case for role

        Get Role
        """
        pass

    def test_role_groups(self):
        """
        Test case for role_groups

        Get Role Groups
        """
        pass

    def test_role_users(self):
        """
        Test case for role_users

        Get Role Users
        """
        pass

    def test_set_role_groups(self):
        """
        Test case for set_role_groups

        Update Role Groups
        """
        pass

    def test_set_role_users(self):
        """
        Test case for set_role_users

        Update Role Users
        """
        pass

    def test_update_model_set(self):
        """
        Test case for update_model_set

        Update Model Set
        """
        pass

    def test_update_permission_set(self):
        """
        Test case for update_permission_set

        Update Permission Set
        """
        pass

    def test_update_role(self):
        """
        Test case for update_role

        Update Role
        """
        pass


if __name__ == '__main__':
    unittest.main()
