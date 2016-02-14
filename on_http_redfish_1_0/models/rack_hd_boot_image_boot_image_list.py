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


class RackHDBootImageBootImageList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RackHDBootImageBootImageList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'os_name': 'str',
            'odata_type': 'Odata400Type'
        }

        self.attribute_map = {
            'os_name': 'osName',
            'odata_type': '@odata.type'
        }

        self._os_name = None
        self._odata_type = None

    @property
    def os_name(self):
        """
        Gets the os_name of this RackHDBootImageBootImageList.


        :return: The os_name of this RackHDBootImageBootImageList.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this RackHDBootImageBootImageList.


        :param os_name: The os_name of this RackHDBootImageBootImageList.
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
    def odata_type(self):
        """
        Gets the odata_type of this RackHDBootImageBootImageList.


        :return: The odata_type of this RackHDBootImageBootImageList.
        :rtype: Odata400Type
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self, odata_type):
        """
        Sets the odata_type of this RackHDBootImageBootImageList.


        :param odata_type: The odata_type of this RackHDBootImageBootImageList.
        :type: Odata400Type
        """
        self._odata_type = odata_type

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
