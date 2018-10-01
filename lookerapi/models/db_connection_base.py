# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DBConnectionBase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, dialect=None, snippets=None, can=None):
        """
        DBConnectionBase - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'dialect': 'Dialect',
            'snippets': 'list[Snippet]',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'name': 'name',
            'dialect': 'dialect',
            'snippets': 'snippets',
            'can': 'can'
        }

        self._name = name
        self._dialect = dialect
        self._snippets = snippets
        self._can = can

    @property
    def name(self):
        """
        Gets the name of this DBConnectionBase.
        Name of the connection. Also used as the unique identifier

        :return: The name of this DBConnectionBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DBConnectionBase.
        Name of the connection. Also used as the unique identifier

        :param name: The name of this DBConnectionBase.
        :type: str
        """

        self._name = name

    @property
    def dialect(self):
        """
        Gets the dialect of this DBConnectionBase.
        (Read-only) SQL Dialect details

        :return: The dialect of this DBConnectionBase.
        :rtype: Dialect
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """
        Sets the dialect of this DBConnectionBase.
        (Read-only) SQL Dialect details

        :param dialect: The dialect of this DBConnectionBase.
        :type: Dialect
        """

        self._dialect = dialect

    @property
    def snippets(self):
        """
        Gets the snippets of this DBConnectionBase.
        SQL Runner snippets for this connection

        :return: The snippets of this DBConnectionBase.
        :rtype: list[Snippet]
        """
        return self._snippets

    @snippets.setter
    def snippets(self, snippets):
        """
        Sets the snippets of this DBConnectionBase.
        SQL Runner snippets for this connection

        :param snippets: The snippets of this DBConnectionBase.
        :type: list[Snippet]
        """

        self._snippets = snippets

    @property
    def can(self):
        """
        Gets the can of this DBConnectionBase.
        Operations the current user is able to perform on this object

        :return: The can of this DBConnectionBase.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this DBConnectionBase.
        Operations the current user is able to perform on this object

        :param can: The can of this DBConnectionBase.
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DBConnectionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other