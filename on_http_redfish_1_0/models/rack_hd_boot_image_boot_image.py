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


class RackHDBootImageBootImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RackHDBootImageBootImage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'root_ssh_key': 'str',
            'domain': 'str',
            'users': 'list[RackHDBootImageUsers]',
            'hostname': 'str',
            'os_name': 'str',
            'repo': 'str',
            'version': 'str',
            'network_devices': 'list[RackHDBootImageNetworkDevice]',
            'root_password': 'str',
            'dns_servers': 'list[str]',
            'install_disk': 'str'
        }

        self.attribute_map = {
            'root_ssh_key': 'rootSshKey',
            'domain': 'domain',
            'users': 'users',
            'hostname': 'hostname',
            'os_name': 'osName',
            'repo': 'repo',
            'version': 'version',
            'network_devices': 'networkDevices',
            'root_password': 'rootPassword',
            'dns_servers': 'dnsServers',
            'install_disk': 'installDisk'
        }

        self._root_ssh_key = None
        self._domain = None
        self._users = None
        self._hostname = None
        self._os_name = None
        self._repo = None
        self._version = None
        self._network_devices = None
        self._root_password = None
        self._dns_servers = None
        self._install_disk = None

    @property
    def root_ssh_key(self):
        """
        Gets the root_ssh_key of this RackHDBootImageBootImage.
        This is the SshKey for the OS root account.

        :return: The root_ssh_key of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._root_ssh_key

    @root_ssh_key.setter
    def root_ssh_key(self, root_ssh_key):
        """
        Sets the root_ssh_key of this RackHDBootImageBootImage.
        This is the SshKey for the OS root account.

        :param root_ssh_key: The root_ssh_key of this RackHDBootImageBootImage.
        :type: str
        """
        self._root_ssh_key = root_ssh_key

    @property
    def domain(self):
        """
        Gets the domain of this RackHDBootImageBootImage.
        This is the domain for the target OS

        :return: The domain of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this RackHDBootImageBootImage.
        This is the domain for the target OS

        :param domain: The domain of this RackHDBootImageBootImage.
        :type: str
        """
        self._domain = domain

    @property
    def users(self):
        """
        Gets the users of this RackHDBootImageBootImage.
        This is a list of user account information that will created after OS installation

        :return: The users of this RackHDBootImageBootImage.
        :rtype: list[RackHDBootImageUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this RackHDBootImageBootImage.
        This is a list of user account information that will created after OS installation

        :param users: The users of this RackHDBootImageBootImage.
        :type: list[RackHDBootImageUsers]
        """
        self._users = users

    @property
    def hostname(self):
        """
        Gets the hostname of this RackHDBootImageBootImage.
        The hostname for target OS.

        :return: The hostname of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this RackHDBootImageBootImage.
        The hostname for target OS.

        :param hostname: The hostname of this RackHDBootImageBootImage.
        :type: str
        """
        self._hostname = hostname

    @property
    def os_name(self):
        """
        Gets the os_name of this RackHDBootImageBootImage.
        Name of the target OS to be installed

        :return: The os_name of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this RackHDBootImageBootImage.
        Name of the target OS to be installed

        :param os_name: The os_name of this RackHDBootImageBootImage.
        :type: str
        """
        allowed_values = ["CentOS", "CentOS+KVM", "ESXi", "RHEL", "RHEL+KVM"]
        if os_name not in allowed_values:
            raise ValueError(
                "Invalid value for `os_name`, must be one of {0}"
                .format(allowed_values)
            )
        self._os_name = os_name

    @property
    def repo(self):
        """
        Gets the repo of this RackHDBootImageBootImage.
        The external OS repository address, currently only supports HTTP

        :return: The repo of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """
        Sets the repo of this RackHDBootImageBootImage.
        The external OS repository address, currently only supports HTTP

        :param repo: The repo of this RackHDBootImageBootImage.
        :type: str
        """
        self._repo = repo

    @property
    def version(self):
        """
        Gets the version of this RackHDBootImageBootImage.
        The version number of target OS that needs to install.

        :return: The version of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this RackHDBootImageBootImage.
        The version number of target OS that needs to install.

        :param version: The version of this RackHDBootImageBootImage.
        :type: str
        """
        self._version = version

    @property
    def network_devices(self):
        """
        Gets the network_devices of this RackHDBootImageBootImage.
        List of device names and static IP settings for network devices after OS installation.

        :return: The network_devices of this RackHDBootImageBootImage.
        :rtype: list[RackHDBootImageNetworkDevice]
        """
        return self._network_devices

    @network_devices.setter
    def network_devices(self, network_devices):
        """
        Sets the network_devices of this RackHDBootImageBootImage.
        List of device names and static IP settings for network devices after OS installation.

        :param network_devices: The network_devices of this RackHDBootImageBootImage.
        :type: list[RackHDBootImageNetworkDevice]
        """
        self._network_devices = network_devices

    @property
    def root_password(self):
        """
        Gets the root_password of this RackHDBootImageBootImage.
        The password for the OS root account.

        :return: The root_password of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        """
        Sets the root_password of this RackHDBootImageBootImage.
        The password for the OS root account.

        :param root_password: The root_password of this RackHDBootImageBootImage.
        :type: str
        """
        self._root_password = root_password

    @property
    def dns_servers(self):
        """
        Gets the dns_servers of this RackHDBootImageBootImage.
        This is a list of Domain Name Servers.

        :return: The dns_servers of this RackHDBootImageBootImage.
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """
        Sets the dns_servers of this RackHDBootImageBootImage.
        This is a list of Domain Name Servers.

        :param dns_servers: The dns_servers of this RackHDBootImageBootImage.
        :type: list[str]
        """
        self._dns_servers = dns_servers

    @property
    def install_disk(self):
        """
        Gets the install_disk of this RackHDBootImageBootImage.


        :return: The install_disk of this RackHDBootImageBootImage.
        :rtype: str
        """
        return self._install_disk

    @install_disk.setter
    def install_disk(self, install_disk):
        """
        Sets the install_disk of this RackHDBootImageBootImage.


        :param install_disk: The install_disk of this RackHDBootImageBootImage.
        :type: str
        """
        self._install_disk = install_disk

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

