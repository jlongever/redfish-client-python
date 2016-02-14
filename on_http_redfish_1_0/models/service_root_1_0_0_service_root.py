# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ServiceRoot100ServiceRoot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ServiceRoot100ServiceRoot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'odata_context': 'Odata400Context',
            'odata_id': 'Odata400Id',
            'odata_type': 'Odata400Type',
            'account_service': 'AccountServiceAccountService',
            'chassis': 'Odata400IdRef',
            'description': 'ResourceDescription',
            'event_service': 'Odata400IdRef',
            'id': 'ResourceId',
            'json_schemas': 'Odata400IdRef',
            'links': 'ServiceRoot100ServiceRootLinks',
            'managers': 'Odata400IdRef',
            'name': 'ResourceName',
            'oem': 'ResourceOem',
            'redfish_version': 'str',
            'registries': 'Odata400IdRef',
            'session_service': 'Odata400IdRef',
            'systems': 'Odata400IdRef',
            'tasks': 'Odata400IdRef',
            'uuid': 'ResourceUUID'
        }

        self.attribute_map = {
            'odata_context': '@odata.context',
            'odata_id': '@odata.id',
            'odata_type': '@odata.type',
            'account_service': 'AccountService',
            'chassis': 'Chassis',
            'description': 'Description',
            'event_service': 'EventService',
            'id': 'Id',
            'json_schemas': 'JsonSchemas',
            'links': 'Links',
            'managers': 'Managers',
            'name': 'Name',
            'oem': 'Oem',
            'redfish_version': 'RedfishVersion',
            'registries': 'Registries',
            'session_service': 'SessionService',
            'systems': 'Systems',
            'tasks': 'Tasks',
            'uuid': 'UUID'
        }

        self._odata_context = None
        self._odata_id = None
        self._odata_type = None
        self._account_service = None
        self._chassis = None
        self._description = None
        self._event_service = None
        self._id = None
        self._json_schemas = None
        self._links = None
        self._managers = None
        self._name = None
        self._oem = None
        self._redfish_version = None
        self._registries = None
        self._session_service = None
        self._systems = None
        self._tasks = None
        self._uuid = None

    @property
    def odata_context(self):
        """
        Gets the odata_context of this ServiceRoot100ServiceRoot.


        :return: The odata_context of this ServiceRoot100ServiceRoot.
        :rtype: Odata400Context
        """
        return self._odata_context

    @odata_context.setter
    def odata_context(self, odata_context):
        """
        Sets the odata_context of this ServiceRoot100ServiceRoot.


        :param odata_context: The odata_context of this ServiceRoot100ServiceRoot.
        :type: Odata400Context
        """
        self._odata_context = odata_context

    @property
    def odata_id(self):
        """
        Gets the odata_id of this ServiceRoot100ServiceRoot.


        :return: The odata_id of this ServiceRoot100ServiceRoot.
        :rtype: Odata400Id
        """
        return self._odata_id

    @odata_id.setter
    def odata_id(self, odata_id):
        """
        Sets the odata_id of this ServiceRoot100ServiceRoot.


        :param odata_id: The odata_id of this ServiceRoot100ServiceRoot.
        :type: Odata400Id
        """
        self._odata_id = odata_id

    @property
    def odata_type(self):
        """
        Gets the odata_type of this ServiceRoot100ServiceRoot.


        :return: The odata_type of this ServiceRoot100ServiceRoot.
        :rtype: Odata400Type
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self, odata_type):
        """
        Sets the odata_type of this ServiceRoot100ServiceRoot.


        :param odata_type: The odata_type of this ServiceRoot100ServiceRoot.
        :type: Odata400Type
        """
        self._odata_type = odata_type

    @property
    def account_service(self):
        """
        Gets the account_service of this ServiceRoot100ServiceRoot.
        This is a link to the Account Service.

        :return: The account_service of this ServiceRoot100ServiceRoot.
        :rtype: AccountServiceAccountService
        """
        return self._account_service

    @account_service.setter
    def account_service(self, account_service):
        """
        Sets the account_service of this ServiceRoot100ServiceRoot.
        This is a link to the Account Service.

        :param account_service: The account_service of this ServiceRoot100ServiceRoot.
        :type: AccountServiceAccountService
        """
        self._account_service = account_service

    @property
    def chassis(self):
        """
        Gets the chassis of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Chassis.

        :return: The chassis of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._chassis

    @chassis.setter
    def chassis(self, chassis):
        """
        Sets the chassis of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Chassis.

        :param chassis: The chassis of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._chassis = chassis

    @property
    def description(self):
        """
        Gets the description of this ServiceRoot100ServiceRoot.


        :return: The description of this ServiceRoot100ServiceRoot.
        :rtype: ResourceDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServiceRoot100ServiceRoot.


        :param description: The description of this ServiceRoot100ServiceRoot.
        :type: ResourceDescription
        """
        self._description = description

    @property
    def event_service(self):
        """
        Gets the event_service of this ServiceRoot100ServiceRoot.
        This is a link to the EventService.

        :return: The event_service of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._event_service

    @event_service.setter
    def event_service(self, event_service):
        """
        Sets the event_service of this ServiceRoot100ServiceRoot.
        This is a link to the EventService.

        :param event_service: The event_service of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._event_service = event_service

    @property
    def id(self):
        """
        Gets the id of this ServiceRoot100ServiceRoot.


        :return: The id of this ServiceRoot100ServiceRoot.
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceRoot100ServiceRoot.


        :param id: The id of this ServiceRoot100ServiceRoot.
        :type: ResourceId
        """
        self._id = id

    @property
    def json_schemas(self):
        """
        Gets the json_schemas of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Json-Schema files.

        :return: The json_schemas of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._json_schemas

    @json_schemas.setter
    def json_schemas(self, json_schemas):
        """
        Sets the json_schemas of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Json-Schema files.

        :param json_schemas: The json_schemas of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._json_schemas = json_schemas

    @property
    def links(self):
        """
        Gets the links of this ServiceRoot100ServiceRoot.


        :return: The links of this ServiceRoot100ServiceRoot.
        :rtype: ServiceRoot100ServiceRootLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this ServiceRoot100ServiceRoot.


        :param links: The links of this ServiceRoot100ServiceRoot.
        :type: ServiceRoot100ServiceRootLinks
        """
        self._links = links

    @property
    def managers(self):
        """
        Gets the managers of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Managers.

        :return: The managers of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._managers

    @managers.setter
    def managers(self, managers):
        """
        Sets the managers of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Managers.

        :param managers: The managers of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._managers = managers

    @property
    def name(self):
        """
        Gets the name of this ServiceRoot100ServiceRoot.


        :return: The name of this ServiceRoot100ServiceRoot.
        :rtype: ResourceName
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceRoot100ServiceRoot.


        :param name: The name of this ServiceRoot100ServiceRoot.
        :type: ResourceName
        """
        self._name = name

    @property
    def oem(self):
        """
        Gets the oem of this ServiceRoot100ServiceRoot.
        This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections.

        :return: The oem of this ServiceRoot100ServiceRoot.
        :rtype: ResourceOem
        """
        return self._oem

    @oem.setter
    def oem(self, oem):
        """
        Sets the oem of this ServiceRoot100ServiceRoot.
        This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections.

        :param oem: The oem of this ServiceRoot100ServiceRoot.
        :type: ResourceOem
        """
        self._oem = oem

    @property
    def redfish_version(self):
        """
        Gets the redfish_version of this ServiceRoot100ServiceRoot.
        The version of the Redfish service

        :return: The redfish_version of this ServiceRoot100ServiceRoot.
        :rtype: str
        """
        return self._redfish_version

    @redfish_version.setter
    def redfish_version(self, redfish_version):
        """
        Sets the redfish_version of this ServiceRoot100ServiceRoot.
        The version of the Redfish service

        :param redfish_version: The redfish_version of this ServiceRoot100ServiceRoot.
        :type: str
        """
        self._redfish_version = redfish_version

    @property
    def registries(self):
        """
        Gets the registries of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Registries.

        :return: The registries of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._registries

    @registries.setter
    def registries(self, registries):
        """
        Sets the registries of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Registries.

        :param registries: The registries of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._registries = registries

    @property
    def session_service(self):
        """
        Gets the session_service of this ServiceRoot100ServiceRoot.
        This is a link to the Sessions Service.

        :return: The session_service of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._session_service

    @session_service.setter
    def session_service(self, session_service):
        """
        Sets the session_service of this ServiceRoot100ServiceRoot.
        This is a link to the Sessions Service.

        :param session_service: The session_service of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._session_service = session_service

    @property
    def systems(self):
        """
        Gets the systems of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Systems.

        :return: The systems of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """
        Sets the systems of this ServiceRoot100ServiceRoot.
        This is a link to a collection of Systems.

        :param systems: The systems of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._systems = systems

    @property
    def tasks(self):
        """
        Gets the tasks of this ServiceRoot100ServiceRoot.
        This is a link to the Task Service.

        :return: The tasks of this ServiceRoot100ServiceRoot.
        :rtype: Odata400IdRef
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this ServiceRoot100ServiceRoot.
        This is a link to the Task Service.

        :param tasks: The tasks of this ServiceRoot100ServiceRoot.
        :type: Odata400IdRef
        """
        self._tasks = tasks

    @property
    def uuid(self):
        """
        Gets the uuid of this ServiceRoot100ServiceRoot.
        Unique identifier for a service instance. When SSDP is used, this value should be an exact match of the UUID value returned in a 200OK from an SSDP M-SEARCH request during discovery.

        :return: The uuid of this ServiceRoot100ServiceRoot.
        :rtype: ResourceUUID
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this ServiceRoot100ServiceRoot.
        Unique identifier for a service instance. When SSDP is used, this value should be an exact match of the UUID value returned in a 200OK from an SSDP M-SEARCH request during discovery.

        :param uuid: The uuid of this ServiceRoot100ServiceRoot.
        :type: ResourceUUID
        """
        self._uuid = uuid

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

