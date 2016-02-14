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


class LogEntry100LogEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LogEntry100LogEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'odata_context': 'Odata400Context',
            'odata_id': 'Odata400Id',
            'odata_type': 'Odata400Type',
            'created': 'datetime',
            'description': 'ResourceDescription',
            'entry_code': 'LogEntry100LogEntryCode',
            'entry_type': 'LogEntry100LogEntryType',
            'id': 'ResourceId',
            'links': 'LogEntry100LogEntryLinks',
            'message': 'str',
            'message_args': 'list[str]',
            'message_id': 'str',
            'name': 'ResourceName',
            'oem': 'ResourceOem',
            'sensor_type': 'LogEntry100SensorType',
            'severity': 'LogEntry100EventSeverity'
        }

        self.attribute_map = {
            'odata_context': '@odata.context',
            'odata_id': '@odata.id',
            'odata_type': '@odata.type',
            'created': 'Created',
            'description': 'Description',
            'entry_code': 'EntryCode',
            'entry_type': 'EntryType',
            'id': 'Id',
            'links': 'Links',
            'message': 'Message',
            'message_args': 'MessageArgs',
            'message_id': 'MessageId',
            'name': 'Name',
            'oem': 'Oem',
            'sensor_type': 'SensorType',
            'severity': 'Severity'
        }

        self._odata_context = None
        self._odata_id = None
        self._odata_type = None
        self._created = None
        self._description = None
        self._entry_code = None
        self._entry_type = None
        self._id = None
        self._links = None
        self._message = None
        self._message_args = None
        self._message_id = None
        self._name = None
        self._oem = None
        self._sensor_type = None
        self._severity = None

    @property
    def odata_context(self):
        """
        Gets the odata_context of this LogEntry100LogEntry.


        :return: The odata_context of this LogEntry100LogEntry.
        :rtype: Odata400Context
        """
        return self._odata_context

    @odata_context.setter
    def odata_context(self, odata_context):
        """
        Sets the odata_context of this LogEntry100LogEntry.


        :param odata_context: The odata_context of this LogEntry100LogEntry.
        :type: Odata400Context
        """
        self._odata_context = odata_context

    @property
    def odata_id(self):
        """
        Gets the odata_id of this LogEntry100LogEntry.


        :return: The odata_id of this LogEntry100LogEntry.
        :rtype: Odata400Id
        """
        return self._odata_id

    @odata_id.setter
    def odata_id(self, odata_id):
        """
        Sets the odata_id of this LogEntry100LogEntry.


        :param odata_id: The odata_id of this LogEntry100LogEntry.
        :type: Odata400Id
        """
        self._odata_id = odata_id

    @property
    def odata_type(self):
        """
        Gets the odata_type of this LogEntry100LogEntry.


        :return: The odata_type of this LogEntry100LogEntry.
        :rtype: Odata400Type
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self, odata_type):
        """
        Sets the odata_type of this LogEntry100LogEntry.


        :param odata_type: The odata_type of this LogEntry100LogEntry.
        :type: Odata400Type
        """
        self._odata_type = odata_type

    @property
    def created(self):
        """
        Gets the created of this LogEntry100LogEntry.
        The time the log entry was created.

        :return: The created of this LogEntry100LogEntry.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this LogEntry100LogEntry.
        The time the log entry was created.

        :param created: The created of this LogEntry100LogEntry.
        :type: datetime
        """
        self._created = created

    @property
    def description(self):
        """
        Gets the description of this LogEntry100LogEntry.


        :return: The description of this LogEntry100LogEntry.
        :rtype: ResourceDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogEntry100LogEntry.


        :param description: The description of this LogEntry100LogEntry.
        :type: ResourceDescription
        """
        self._description = description

    @property
    def entry_code(self):
        """
        Gets the entry_code of this LogEntry100LogEntry.
        If the EntryType is SEL, this will have the entry code for the log entry.

        :return: The entry_code of this LogEntry100LogEntry.
        :rtype: LogEntry100LogEntryCode
        """
        return self._entry_code

    @entry_code.setter
    def entry_code(self, entry_code):
        """
        Sets the entry_code of this LogEntry100LogEntry.
        If the EntryType is SEL, this will have the entry code for the log entry.

        :param entry_code: The entry_code of this LogEntry100LogEntry.
        :type: LogEntry100LogEntryCode
        """
        self._entry_code = entry_code

    @property
    def entry_type(self):
        """
        Gets the entry_type of this LogEntry100LogEntry.
        his is the type of log entry.

        :return: The entry_type of this LogEntry100LogEntry.
        :rtype: LogEntry100LogEntryType
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """
        Sets the entry_type of this LogEntry100LogEntry.
        his is the type of log entry.

        :param entry_type: The entry_type of this LogEntry100LogEntry.
        :type: LogEntry100LogEntryType
        """
        self._entry_type = entry_type

    @property
    def id(self):
        """
        Gets the id of this LogEntry100LogEntry.


        :return: The id of this LogEntry100LogEntry.
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogEntry100LogEntry.


        :param id: The id of this LogEntry100LogEntry.
        :type: ResourceId
        """
        self._id = id

    @property
    def links(self):
        """
        Gets the links of this LogEntry100LogEntry.


        :return: The links of this LogEntry100LogEntry.
        :rtype: LogEntry100LogEntryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this LogEntry100LogEntry.


        :param links: The links of this LogEntry100LogEntry.
        :type: LogEntry100LogEntryLinks
        """
        self._links = links

    @property
    def message(self):
        """
        Gets the message of this LogEntry100LogEntry.
        This property decodes from EntryType:  If it is Event then it is a message string.  Otherwise, it is SEL or Oem specific.  In most cases, this will be the actual Log Entry.

        :return: The message of this LogEntry100LogEntry.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this LogEntry100LogEntry.
        This property decodes from EntryType:  If it is Event then it is a message string.  Otherwise, it is SEL or Oem specific.  In most cases, this will be the actual Log Entry.

        :param message: The message of this LogEntry100LogEntry.
        :type: str
        """
        self._message = message

    @property
    def message_args(self):
        """
        Gets the message_args of this LogEntry100LogEntry.
        The values of this property shall be any arguments for the message.

        :return: The message_args of this LogEntry100LogEntry.
        :rtype: list[str]
        """
        return self._message_args

    @message_args.setter
    def message_args(self, message_args):
        """
        Sets the message_args of this LogEntry100LogEntry.
        The values of this property shall be any arguments for the message.

        :param message_args: The message_args of this LogEntry100LogEntry.
        :type: list[str]
        """
        self._message_args = message_args

    @property
    def message_id(self):
        """
        Gets the message_id of this LogEntry100LogEntry.
        This property decodes from EntryType:  If it is Event then it is a message id.  Otherwise, it is SEL or Oem specific.  This value is only used for registries - for more information, see the specification.

        :return: The message_id of this LogEntry100LogEntry.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this LogEntry100LogEntry.
        This property decodes from EntryType:  If it is Event then it is a message id.  Otherwise, it is SEL or Oem specific.  This value is only used for registries - for more information, see the specification.

        :param message_id: The message_id of this LogEntry100LogEntry.
        :type: str
        """
        self._message_id = message_id

    @property
    def name(self):
        """
        Gets the name of this LogEntry100LogEntry.


        :return: The name of this LogEntry100LogEntry.
        :rtype: ResourceName
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogEntry100LogEntry.


        :param name: The name of this LogEntry100LogEntry.
        :type: ResourceName
        """
        self._name = name

    @property
    def oem(self):
        """
        Gets the oem of this LogEntry100LogEntry.
        This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections.

        :return: The oem of this LogEntry100LogEntry.
        :rtype: ResourceOem
        """
        return self._oem

    @oem.setter
    def oem(self, oem):
        """
        Sets the oem of this LogEntry100LogEntry.
        This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections.

        :param oem: The oem of this LogEntry100LogEntry.
        :type: ResourceOem
        """
        self._oem = oem

    @property
    def sensor_type(self):
        """
        Gets the sensor_type of this LogEntry100LogEntry.
        If the EntryType is SEL, this will have the sensor type that the log entry pertains to.

        :return: The sensor_type of this LogEntry100LogEntry.
        :rtype: LogEntry100SensorType
        """
        return self._sensor_type

    @sensor_type.setter
    def sensor_type(self, sensor_type):
        """
        Sets the sensor_type of this LogEntry100LogEntry.
        If the EntryType is SEL, this will have the sensor type that the log entry pertains to.

        :param sensor_type: The sensor_type of this LogEntry100LogEntry.
        :type: LogEntry100SensorType
        """
        self._sensor_type = sensor_type

    @property
    def severity(self):
        """
        Gets the severity of this LogEntry100LogEntry.
        This is the severity of the log entry.

        :return: The severity of this LogEntry100LogEntry.
        :rtype: LogEntry100EventSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this LogEntry100LogEntry.
        This is the severity of the log entry.

        :param severity: The severity of this LogEntry100LogEntry.
        :type: LogEntry100EventSeverity
        """
        self._severity = severity

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

