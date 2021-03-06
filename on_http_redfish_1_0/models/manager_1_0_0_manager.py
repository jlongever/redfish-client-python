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


class Manager100Manager(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Manager100Manager - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'odata_context': 'Odata400Context',
            'odata_id': 'Odata400Id',
            'odata_type': 'Odata400Type',
            'actions': 'Manager100ManagerActions',
            'command_shell': 'Manager100CommandShell',
            'description': 'ResourceDescription',
            'ethernet_interfaces': 'EthernetInterfaceCollectionEthernetInterfaceCollection',
            'graphical_console': 'Manager100GraphicalConsole',
            'id': 'ResourceId',
            'links': 'Manager100ManagerLinks',
            'log_services': 'LogServiceCollectionLogServiceCollection',
            'manager_type': 'Manager100ManagerType',
            'name': 'ResourceName',
            'network_protocol': 'ManagerNetworkProtocol100ManagerNetworkProtocol',
            'oem': 'ResourceOem',
            'redundancy': 'list[RedundancyRedundancy]',
            'redundancyodata_count': 'Odata400Count',
            'redundancyodata_navigation_link': 'Odata400IdRef',
            'serial_console': 'Manager100SerialConsole',
            'serial_interfaces': 'SerialInterfaceCollectionSerialInterfaceCollection',
            'service_entry_point_uuid': 'ResourceUUID',
            'status': 'ResourceStatus',
            'uuid': 'ResourceUUID',
            'virtual_media': 'VirtualMediaCollectionVirtualMediaCollection'
        }

        self.attribute_map = {
            'odata_context': '@odata.context',
            'odata_id': '@odata.id',
            'odata_type': '@odata.type',
            'actions': 'Actions',
            'command_shell': 'CommandShell',
            'description': 'Description',
            'ethernet_interfaces': 'EthernetInterfaces',
            'graphical_console': 'GraphicalConsole',
            'id': 'Id',
            'links': 'Links',
            'log_services': 'LogServices',
            'manager_type': 'ManagerType',
            'name': 'Name',
            'network_protocol': 'NetworkProtocol',
            'oem': 'Oem',
            'redundancy': 'Redundancy',
            'redundancyodata_count': 'Redundancy@odata.count',
            'redundancyodata_navigation_link': 'Redundancy@odata.navigationLink',
            'serial_console': 'SerialConsole',
            'serial_interfaces': 'SerialInterfaces',
            'service_entry_point_uuid': 'ServiceEntryPointUUID',
            'status': 'Status',
            'uuid': 'UUID',
            'virtual_media': 'VirtualMedia'
        }

        self._odata_context = None
        self._odata_id = None
        self._odata_type = None
        self._actions = None
        self._command_shell = None
        self._description = None
        self._ethernet_interfaces = None
        self._graphical_console = None
        self._id = None
        self._links = None
        self._log_services = None
        self._manager_type = None
        self._name = None
        self._network_protocol = None
        self._oem = None
        self._redundancy = None
        self._redundancyodata_count = None
        self._redundancyodata_navigation_link = None
        self._serial_console = None
        self._serial_interfaces = None
        self._service_entry_point_uuid = None
        self._status = None
        self._uuid = None
        self._virtual_media = None

    @property
    def odata_context(self):
        """
        Gets the odata_context of this Manager100Manager.


        :return: The odata_context of this Manager100Manager.
        :rtype: Odata400Context
        """
        return self._odata_context

    @odata_context.setter
    def odata_context(self, odata_context):
        """
        Sets the odata_context of this Manager100Manager.


        :param odata_context: The odata_context of this Manager100Manager.
        :type: Odata400Context
        """
        self._odata_context = odata_context

    @property
    def odata_id(self):
        """
        Gets the odata_id of this Manager100Manager.


        :return: The odata_id of this Manager100Manager.
        :rtype: Odata400Id
        """
        return self._odata_id

    @odata_id.setter
    def odata_id(self, odata_id):
        """
        Sets the odata_id of this Manager100Manager.


        :param odata_id: The odata_id of this Manager100Manager.
        :type: Odata400Id
        """
        self._odata_id = odata_id

    @property
    def odata_type(self):
        """
        Gets the odata_type of this Manager100Manager.


        :return: The odata_type of this Manager100Manager.
        :rtype: Odata400Type
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self, odata_type):
        """
        Sets the odata_type of this Manager100Manager.


        :param odata_type: The odata_type of this Manager100Manager.
        :type: Odata400Type
        """
        self._odata_type = odata_type

    @property
    def actions(self):
        """
        Gets the actions of this Manager100Manager.


        :return: The actions of this Manager100Manager.
        :rtype: Manager100ManagerActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this Manager100Manager.


        :param actions: The actions of this Manager100Manager.
        :type: Manager100ManagerActions
        """
        self._actions = actions

    @property
    def command_shell(self):
        """
        Gets the command_shell of this Manager100Manager.
        Information about the Command Shell service provided by this manager.

        :return: The command_shell of this Manager100Manager.
        :rtype: Manager100CommandShell
        """
        return self._command_shell

    @command_shell.setter
    def command_shell(self, command_shell):
        """
        Sets the command_shell of this Manager100Manager.
        Information about the Command Shell service provided by this manager.

        :param command_shell: The command_shell of this Manager100Manager.
        :type: Manager100CommandShell
        """
        self._command_shell = command_shell

    @property
    def description(self):
        """
        Gets the description of this Manager100Manager.


        :return: The description of this Manager100Manager.
        :rtype: ResourceDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Manager100Manager.


        :param description: The description of this Manager100Manager.
        :type: ResourceDescription
        """
        self._description = description

    @property
    def ethernet_interfaces(self):
        """
        Gets the ethernet_interfaces of this Manager100Manager.
        This is a reference to a collection of NICs that this manager uses for network communication.  It is here that clients will find NIC configuration options and settings.

        :return: The ethernet_interfaces of this Manager100Manager.
        :rtype: EthernetInterfaceCollectionEthernetInterfaceCollection
        """
        return self._ethernet_interfaces

    @ethernet_interfaces.setter
    def ethernet_interfaces(self, ethernet_interfaces):
        """
        Sets the ethernet_interfaces of this Manager100Manager.
        This is a reference to a collection of NICs that this manager uses for network communication.  It is here that clients will find NIC configuration options and settings.

        :param ethernet_interfaces: The ethernet_interfaces of this Manager100Manager.
        :type: EthernetInterfaceCollectionEthernetInterfaceCollection
        """
        self._ethernet_interfaces = ethernet_interfaces

    @property
    def graphical_console(self):
        """
        Gets the graphical_console of this Manager100Manager.
        The value of this property shall contain the information about the Graphical Console (KVM-IP) service of this manager.

        :return: The graphical_console of this Manager100Manager.
        :rtype: Manager100GraphicalConsole
        """
        return self._graphical_console

    @graphical_console.setter
    def graphical_console(self, graphical_console):
        """
        Sets the graphical_console of this Manager100Manager.
        The value of this property shall contain the information about the Graphical Console (KVM-IP) service of this manager.

        :param graphical_console: The graphical_console of this Manager100Manager.
        :type: Manager100GraphicalConsole
        """
        self._graphical_console = graphical_console

    @property
    def id(self):
        """
        Gets the id of this Manager100Manager.


        :return: The id of this Manager100Manager.
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Manager100Manager.


        :param id: The id of this Manager100Manager.
        :type: ResourceId
        """
        self._id = id

    @property
    def links(self):
        """
        Gets the links of this Manager100Manager.


        :return: The links of this Manager100Manager.
        :rtype: Manager100ManagerLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Manager100Manager.


        :param links: The links of this Manager100Manager.
        :type: Manager100ManagerLinks
        """
        self._links = links

    @property
    def log_services(self):
        """
        Gets the log_services of this Manager100Manager.
        This is a reference to a collection of Logs used by the manager.

        :return: The log_services of this Manager100Manager.
        :rtype: LogServiceCollectionLogServiceCollection
        """
        return self._log_services

    @log_services.setter
    def log_services(self, log_services):
        """
        Sets the log_services of this Manager100Manager.
        This is a reference to a collection of Logs used by the manager.

        :param log_services: The log_services of this Manager100Manager.
        :type: LogServiceCollectionLogServiceCollection
        """
        self._log_services = log_services

    @property
    def manager_type(self):
        """
        Gets the manager_type of this Manager100Manager.
        This property represents the type of manager that this resource represents.

        :return: The manager_type of this Manager100Manager.
        :rtype: Manager100ManagerType
        """
        return self._manager_type

    @manager_type.setter
    def manager_type(self, manager_type):
        """
        Sets the manager_type of this Manager100Manager.
        This property represents the type of manager that this resource represents.

        :param manager_type: The manager_type of this Manager100Manager.
        :type: Manager100ManagerType
        """
        self._manager_type = manager_type

    @property
    def name(self):
        """
        Gets the name of this Manager100Manager.


        :return: The name of this Manager100Manager.
        :rtype: ResourceName
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Manager100Manager.


        :param name: The name of this Manager100Manager.
        :type: ResourceName
        """
        self._name = name

    @property
    def network_protocol(self):
        """
        Gets the network_protocol of this Manager100Manager.
        This is a reference to the network services and their settings that the manager controls.  It is here that clients will find network configuration options as well as network services.

        :return: The network_protocol of this Manager100Manager.
        :rtype: ManagerNetworkProtocol100ManagerNetworkProtocol
        """
        return self._network_protocol

    @network_protocol.setter
    def network_protocol(self, network_protocol):
        """
        Sets the network_protocol of this Manager100Manager.
        This is a reference to the network services and their settings that the manager controls.  It is here that clients will find network configuration options as well as network services.

        :param network_protocol: The network_protocol of this Manager100Manager.
        :type: ManagerNetworkProtocol100ManagerNetworkProtocol
        """
        self._network_protocol = network_protocol

    @property
    def oem(self):
        """
        Gets the oem of this Manager100Manager.
        This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections.

        :return: The oem of this Manager100Manager.
        :rtype: ResourceOem
        """
        return self._oem

    @oem.setter
    def oem(self, oem):
        """
        Sets the oem of this Manager100Manager.
        This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections.

        :param oem: The oem of this Manager100Manager.
        :type: ResourceOem
        """
        self._oem = oem

    @property
    def redundancy(self):
        """
        Gets the redundancy of this Manager100Manager.
        Redundancy information for the managers of this system

        :return: The redundancy of this Manager100Manager.
        :rtype: list[RedundancyRedundancy]
        """
        return self._redundancy

    @redundancy.setter
    def redundancy(self, redundancy):
        """
        Sets the redundancy of this Manager100Manager.
        Redundancy information for the managers of this system

        :param redundancy: The redundancy of this Manager100Manager.
        :type: list[RedundancyRedundancy]
        """
        self._redundancy = redundancy

    @property
    def redundancyodata_count(self):
        """
        Gets the redundancyodata_count of this Manager100Manager.


        :return: The redundancyodata_count of this Manager100Manager.
        :rtype: Odata400Count
        """
        return self._redundancyodata_count

    @redundancyodata_count.setter
    def redundancyodata_count(self, redundancyodata_count):
        """
        Sets the redundancyodata_count of this Manager100Manager.


        :param redundancyodata_count: The redundancyodata_count of this Manager100Manager.
        :type: Odata400Count
        """
        self._redundancyodata_count = redundancyodata_count

    @property
    def redundancyodata_navigation_link(self):
        """
        Gets the redundancyodata_navigation_link of this Manager100Manager.


        :return: The redundancyodata_navigation_link of this Manager100Manager.
        :rtype: Odata400IdRef
        """
        return self._redundancyodata_navigation_link

    @redundancyodata_navigation_link.setter
    def redundancyodata_navigation_link(self, redundancyodata_navigation_link):
        """
        Sets the redundancyodata_navigation_link of this Manager100Manager.


        :param redundancyodata_navigation_link: The redundancyodata_navigation_link of this Manager100Manager.
        :type: Odata400IdRef
        """
        self._redundancyodata_navigation_link = redundancyodata_navigation_link

    @property
    def serial_console(self):
        """
        Gets the serial_console of this Manager100Manager.
        Information about the Serial Console service provided by this manager.

        :return: The serial_console of this Manager100Manager.
        :rtype: Manager100SerialConsole
        """
        return self._serial_console

    @serial_console.setter
    def serial_console(self, serial_console):
        """
        Sets the serial_console of this Manager100Manager.
        Information about the Serial Console service provided by this manager.

        :param serial_console: The serial_console of this Manager100Manager.
        :type: Manager100SerialConsole
        """
        self._serial_console = serial_console

    @property
    def serial_interfaces(self):
        """
        Gets the serial_interfaces of this Manager100Manager.
        This is a reference to a collection of serial interfaces that this manager uses for serial and console communication.  It is here that clients will find serial configuration options and settings.

        :return: The serial_interfaces of this Manager100Manager.
        :rtype: SerialInterfaceCollectionSerialInterfaceCollection
        """
        return self._serial_interfaces

    @serial_interfaces.setter
    def serial_interfaces(self, serial_interfaces):
        """
        Sets the serial_interfaces of this Manager100Manager.
        This is a reference to a collection of serial interfaces that this manager uses for serial and console communication.  It is here that clients will find serial configuration options and settings.

        :param serial_interfaces: The serial_interfaces of this Manager100Manager.
        :type: SerialInterfaceCollectionSerialInterfaceCollection
        """
        self._serial_interfaces = serial_interfaces

    @property
    def service_entry_point_uuid(self):
        """
        Gets the service_entry_point_uuid of this Manager100Manager.
        The UUID of the Redfish Service Entry Point provided by this manager

        :return: The service_entry_point_uuid of this Manager100Manager.
        :rtype: ResourceUUID
        """
        return self._service_entry_point_uuid

    @service_entry_point_uuid.setter
    def service_entry_point_uuid(self, service_entry_point_uuid):
        """
        Sets the service_entry_point_uuid of this Manager100Manager.
        The UUID of the Redfish Service Entry Point provided by this manager

        :param service_entry_point_uuid: The service_entry_point_uuid of this Manager100Manager.
        :type: ResourceUUID
        """
        self._service_entry_point_uuid = service_entry_point_uuid

    @property
    def status(self):
        """
        Gets the status of this Manager100Manager.


        :return: The status of this Manager100Manager.
        :rtype: ResourceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Manager100Manager.


        :param status: The status of this Manager100Manager.
        :type: ResourceStatus
        """
        self._status = status

    @property
    def uuid(self):
        """
        Gets the uuid of this Manager100Manager.
        The Universal Unique Identifier (UUID) for this Manager

        :return: The uuid of this Manager100Manager.
        :rtype: ResourceUUID
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this Manager100Manager.
        The Universal Unique Identifier (UUID) for this Manager

        :param uuid: The uuid of this Manager100Manager.
        :type: ResourceUUID
        """
        self._uuid = uuid

    @property
    def virtual_media(self):
        """
        Gets the virtual_media of this Manager100Manager.
        This is a reference to the Virtual Media services for this particular manager.

        :return: The virtual_media of this Manager100Manager.
        :rtype: VirtualMediaCollectionVirtualMediaCollection
        """
        return self._virtual_media

    @virtual_media.setter
    def virtual_media(self, virtual_media):
        """
        Sets the virtual_media of this Manager100Manager.
        This is a reference to the Virtual Media services for this particular manager.

        :param virtual_media: The virtual_media of this Manager100Manager.
        :type: VirtualMediaCollectionVirtualMediaCollection
        """
        self._virtual_media = virtual_media

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

