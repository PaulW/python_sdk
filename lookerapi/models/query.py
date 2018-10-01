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


class Query(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, model=None, view=None, fields=None, pivots=None, fill_fields=None, filters=None, filter_expression=None, sorts=None, limit=None, column_limit=None, total=None, row_total=None, runtime=None, vis_config=None, filter_config=None, visible_ui_sections=None, slug=None, dynamic_fields=None, client_id=None, share_url=None, expanded_share_url=None, url=None, query_timezone=None, has_table_calculations=None, can=None):
        """
        Query - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'model': 'str',
            'view': 'str',
            'fields': 'list[str]',
            'pivots': 'list[str]',
            'fill_fields': 'list[str]',
            'filters': 'dict(str, str)',
            'filter_expression': 'str',
            'sorts': 'list[str]',
            'limit': 'str',
            'column_limit': 'str',
            'total': 'bool',
            'row_total': 'str',
            'runtime': 'float',
            'vis_config': 'dict(str, str)',
            'filter_config': 'dict(str, str)',
            'visible_ui_sections': 'str',
            'slug': 'str',
            'dynamic_fields': 'list[str]',
            'client_id': 'str',
            'share_url': 'str',
            'expanded_share_url': 'str',
            'url': 'str',
            'query_timezone': 'str',
            'has_table_calculations': 'bool',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'model': 'model',
            'view': 'view',
            'fields': 'fields',
            'pivots': 'pivots',
            'fill_fields': 'fill_fields',
            'filters': 'filters',
            'filter_expression': 'filter_expression',
            'sorts': 'sorts',
            'limit': 'limit',
            'column_limit': 'column_limit',
            'total': 'total',
            'row_total': 'row_total',
            'runtime': 'runtime',
            'vis_config': 'vis_config',
            'filter_config': 'filter_config',
            'visible_ui_sections': 'visible_ui_sections',
            'slug': 'slug',
            'dynamic_fields': 'dynamic_fields',
            'client_id': 'client_id',
            'share_url': 'share_url',
            'expanded_share_url': 'expanded_share_url',
            'url': 'url',
            'query_timezone': 'query_timezone',
            'has_table_calculations': 'has_table_calculations',
            'can': 'can'
        }

        self._id = id
        self._model = model
        self._view = view
        self._fields = fields
        self._pivots = pivots
        self._fill_fields = fill_fields
        self._filters = filters
        self._filter_expression = filter_expression
        self._sorts = sorts
        self._limit = limit
        self._column_limit = column_limit
        self._total = total
        self._row_total = row_total
        self._runtime = runtime
        self._vis_config = vis_config
        self._filter_config = filter_config
        self._visible_ui_sections = visible_ui_sections
        self._slug = slug
        self._dynamic_fields = dynamic_fields
        self._client_id = client_id
        self._share_url = share_url
        self._expanded_share_url = expanded_share_url
        self._url = url
        self._query_timezone = query_timezone
        self._has_table_calculations = has_table_calculations
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this Query.
        Unique Id

        :return: The id of this Query.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Query.
        Unique Id

        :param id: The id of this Query.
        :type: int
        """

        self._id = id

    @property
    def model(self):
        """
        Gets the model of this Query.
        Model

        :return: The model of this Query.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Query.
        Model

        :param model: The model of this Query.
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")

        self._model = model

    @property
    def view(self):
        """
        Gets the view of this Query.
        View

        :return: The view of this Query.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this Query.
        View

        :param view: The view of this Query.
        :type: str
        """
        if view is None:
            raise ValueError("Invalid value for `view`, must not be `None`")

        self._view = view

    @property
    def fields(self):
        """
        Gets the fields of this Query.
        Fields

        :return: The fields of this Query.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this Query.
        Fields

        :param fields: The fields of this Query.
        :type: list[str]
        """

        self._fields = fields

    @property
    def pivots(self):
        """
        Gets the pivots of this Query.
        Pivots

        :return: The pivots of this Query.
        :rtype: list[str]
        """
        return self._pivots

    @pivots.setter
    def pivots(self, pivots):
        """
        Sets the pivots of this Query.
        Pivots

        :param pivots: The pivots of this Query.
        :type: list[str]
        """

        self._pivots = pivots

    @property
    def fill_fields(self):
        """
        Gets the fill_fields of this Query.
        Fill Fields

        :return: The fill_fields of this Query.
        :rtype: list[str]
        """
        return self._fill_fields

    @fill_fields.setter
    def fill_fields(self, fill_fields):
        """
        Sets the fill_fields of this Query.
        Fill Fields

        :param fill_fields: The fill_fields of this Query.
        :type: list[str]
        """

        self._fill_fields = fill_fields

    @property
    def filters(self):
        """
        Gets the filters of this Query.
        Filters

        :return: The filters of this Query.
        :rtype: dict(str, str)
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this Query.
        Filters

        :param filters: The filters of this Query.
        :type: dict(str, str)
        """

        self._filters = filters

    @property
    def filter_expression(self):
        """
        Gets the filter_expression of this Query.
        Filter Expression

        :return: The filter_expression of this Query.
        :rtype: str
        """
        return self._filter_expression

    @filter_expression.setter
    def filter_expression(self, filter_expression):
        """
        Sets the filter_expression of this Query.
        Filter Expression

        :param filter_expression: The filter_expression of this Query.
        :type: str
        """

        self._filter_expression = filter_expression

    @property
    def sorts(self):
        """
        Gets the sorts of this Query.
        Sorting for the query results. Use the format [\"view.field\", ...] to sort on fields in ascending order. Use the format [\"view.field desc\", ...] to sort on fields in descending order. Use [\"__UNSORTED__\"] to disable sorting entirely. Empty sorts [] will trigger a default sort.

        :return: The sorts of this Query.
        :rtype: list[str]
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """
        Sets the sorts of this Query.
        Sorting for the query results. Use the format [\"view.field\", ...] to sort on fields in ascending order. Use the format [\"view.field desc\", ...] to sort on fields in descending order. Use [\"__UNSORTED__\"] to disable sorting entirely. Empty sorts [] will trigger a default sort.

        :param sorts: The sorts of this Query.
        :type: list[str]
        """

        self._sorts = sorts

    @property
    def limit(self):
        """
        Gets the limit of this Query.
        Limit

        :return: The limit of this Query.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this Query.
        Limit

        :param limit: The limit of this Query.
        :type: str
        """

        self._limit = limit

    @property
    def column_limit(self):
        """
        Gets the column_limit of this Query.
        Column Limit

        :return: The column_limit of this Query.
        :rtype: str
        """
        return self._column_limit

    @column_limit.setter
    def column_limit(self, column_limit):
        """
        Sets the column_limit of this Query.
        Column Limit

        :param column_limit: The column_limit of this Query.
        :type: str
        """

        self._column_limit = column_limit

    @property
    def total(self):
        """
        Gets the total of this Query.
        Total

        :return: The total of this Query.
        :rtype: bool
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this Query.
        Total

        :param total: The total of this Query.
        :type: bool
        """

        self._total = total

    @property
    def row_total(self):
        """
        Gets the row_total of this Query.
        Raw Total

        :return: The row_total of this Query.
        :rtype: str
        """
        return self._row_total

    @row_total.setter
    def row_total(self, row_total):
        """
        Sets the row_total of this Query.
        Raw Total

        :param row_total: The row_total of this Query.
        :type: str
        """

        self._row_total = row_total

    @property
    def runtime(self):
        """
        Gets the runtime of this Query.
        Runtime

        :return: The runtime of this Query.
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this Query.
        Runtime

        :param runtime: The runtime of this Query.
        :type: float
        """

        self._runtime = runtime

    @property
    def vis_config(self):
        """
        Gets the vis_config of this Query.
        Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A \"type\" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.

        :return: The vis_config of this Query.
        :rtype: dict(str, str)
        """
        return self._vis_config

    @vis_config.setter
    def vis_config(self, vis_config):
        """
        Sets the vis_config of this Query.
        Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A \"type\" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.

        :param vis_config: The vis_config of this Query.
        :type: dict(str, str)
        """

        self._vis_config = vis_config

    @property
    def filter_config(self):
        """
        Gets the filter_config of this Query.
        The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over \"filters\". When creating a query or modifying an existing query, \"filter_config\" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.

        :return: The filter_config of this Query.
        :rtype: dict(str, str)
        """
        return self._filter_config

    @filter_config.setter
    def filter_config(self, filter_config):
        """
        Sets the filter_config of this Query.
        The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over \"filters\". When creating a query or modifying an existing query, \"filter_config\" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.

        :param filter_config: The filter_config of this Query.
        :type: dict(str, str)
        """

        self._filter_config = filter_config

    @property
    def visible_ui_sections(self):
        """
        Gets the visible_ui_sections of this Query.
        Visible UI Sections

        :return: The visible_ui_sections of this Query.
        :rtype: str
        """
        return self._visible_ui_sections

    @visible_ui_sections.setter
    def visible_ui_sections(self, visible_ui_sections):
        """
        Sets the visible_ui_sections of this Query.
        Visible UI Sections

        :param visible_ui_sections: The visible_ui_sections of this Query.
        :type: str
        """

        self._visible_ui_sections = visible_ui_sections

    @property
    def slug(self):
        """
        Gets the slug of this Query.
        Slug

        :return: The slug of this Query.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this Query.
        Slug

        :param slug: The slug of this Query.
        :type: str
        """

        self._slug = slug

    @property
    def dynamic_fields(self):
        """
        Gets the dynamic_fields of this Query.
        Dynamic Fields

        :return: The dynamic_fields of this Query.
        :rtype: list[str]
        """
        return self._dynamic_fields

    @dynamic_fields.setter
    def dynamic_fields(self, dynamic_fields):
        """
        Sets the dynamic_fields of this Query.
        Dynamic Fields

        :param dynamic_fields: The dynamic_fields of this Query.
        :type: list[str]
        """

        self._dynamic_fields = dynamic_fields

    @property
    def client_id(self):
        """
        Gets the client_id of this Query.
        Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.

        :return: The client_id of this Query.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this Query.
        Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.

        :param client_id: The client_id of this Query.
        :type: str
        """

        self._client_id = client_id

    @property
    def share_url(self):
        """
        Gets the share_url of this Query.
        Share Url

        :return: The share_url of this Query.
        :rtype: str
        """
        return self._share_url

    @share_url.setter
    def share_url(self, share_url):
        """
        Sets the share_url of this Query.
        Share Url

        :param share_url: The share_url of this Query.
        :type: str
        """

        self._share_url = share_url

    @property
    def expanded_share_url(self):
        """
        Gets the expanded_share_url of this Query.
        Expanded Share Url

        :return: The expanded_share_url of this Query.
        :rtype: str
        """
        return self._expanded_share_url

    @expanded_share_url.setter
    def expanded_share_url(self, expanded_share_url):
        """
        Sets the expanded_share_url of this Query.
        Expanded Share Url

        :param expanded_share_url: The expanded_share_url of this Query.
        :type: str
        """

        self._expanded_share_url = expanded_share_url

    @property
    def url(self):
        """
        Gets the url of this Query.
        Expanded Url

        :return: The url of this Query.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Query.
        Expanded Url

        :param url: The url of this Query.
        :type: str
        """

        self._url = url

    @property
    def query_timezone(self):
        """
        Gets the query_timezone of this Query.
        Query Timezone

        :return: The query_timezone of this Query.
        :rtype: str
        """
        return self._query_timezone

    @query_timezone.setter
    def query_timezone(self, query_timezone):
        """
        Sets the query_timezone of this Query.
        Query Timezone

        :param query_timezone: The query_timezone of this Query.
        :type: str
        """

        self._query_timezone = query_timezone

    @property
    def has_table_calculations(self):
        """
        Gets the has_table_calculations of this Query.
        Has Table Calculations

        :return: The has_table_calculations of this Query.
        :rtype: bool
        """
        return self._has_table_calculations

    @has_table_calculations.setter
    def has_table_calculations(self, has_table_calculations):
        """
        Sets the has_table_calculations of this Query.
        Has Table Calculations

        :param has_table_calculations: The has_table_calculations of this Query.
        :type: bool
        """

        self._has_table_calculations = has_table_calculations

    @property
    def can(self):
        """
        Gets the can of this Query.
        Operations the current user is able to perform on this object

        :return: The can of this Query.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Query.
        Operations the current user is able to perform on this object

        :param can: The can of this Query.
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
        if not isinstance(other, Query):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
