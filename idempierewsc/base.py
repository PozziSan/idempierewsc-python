# -*- encoding: utf-8 -*-
"""
Copyright (c) 2016 Saúl Piña <sauljabin@gmail.com>.

This file is part of idempierewsc.

idempierewsc is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

idempierewsc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with idempierewsc.  If not, see <http://www.gnu.org/licenses/>.
"""

from abc import ABCMeta
from abc import abstractmethod
from base64 import b64encode
from base64 import b64decode
from datetime import datetime
from idempierewsc import enums


class LoginRequest(object):
    """
    Class to abstract the iDempiere Web Service Login
    """

    def __init__(self):
        self.user = ''
        self.password = ''
        self.lang = enums.Language.en_US
        self.client_id = 0
        self.role_id = 0
        self.org_id = 0
        self.warehouse_id = 0
        self.stage = 0


class Field(object):
    """
    Class to abstract the iDempiere Web Service Login
    """

    def __init__(self, column='', value=''):
        self.value = value
        self.column = column
        self.type = ''
        self.lval = ''
        self.disp = None
        self.edit = None
        self.error = None
        self.error_val = ''

    def set_byte_value(self, val=None):
        """
        Convert byte to base 64
        :param val: Value to Base 64
        :return: None
        """
        if val:
            self.value = b64encode(val)

    def get_byte_value(self):
        """
        Convert base 64 to byte
        :return: Base64
        """
        if self.value:
            return b64decode(self.value)
        return False

    def get_boolean_value(self):
        """
        Convert value to boolean
        :return: Boolean
        """
        if self.value:
            temp_value = str(self.value).upper()

            if temp_value in ('Y', 'YES'):
                return True

            if temp_value in ('N', 'NO'):
                return False
        return False

    def get_type(self):
        """
        Gets de type of value
        :return: Type of value
        """
        return type(self.value)

    def get_date_value(self):
        """
        Convert the value to Date
        :return: Date
        """
        if self.value:
            temp_value = str(self.value)
            return datetime.strptime(temp_value, '%Y-%m-%d %H:%M:%S')
        return ''

    def get_doc_status_value(self):
        """
        Convert the value to DocStatus
        :return: DocStatus
        """
        if self.value:
            temp_value = str(self.value)
            return enums.DocStatus(temp_value)
        return ''

    def get_doc_action_value(self):
        """
        Convert the value to DocAction
        :return: DocAction
        """
        if self.value:
            temp_value = str(self.value)
            return enums.DocAction(temp_value)
        return ''


class Operation(object):
    """
    Operation For composite operation
    """

    def __init__(self, web_service=None, pre_commit=False, post_commit=False):
        self.web_service = web_service
        self.pre_commit = pre_commit
        self.post_commit = post_commit


class WebServiceResponse(object):
    """
    Class to abstract the iDempiere response
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.error_message = ''
        self.web_service_type = ''
        self.status = enums.WebServiceResponseStatus.Successful

    @abstractmethod
    def web_service_response_model(self):
        pass


class WebServiceRequest(object):
    """
    Class to abstract the iDempiere request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.login = LoginRequest()
        self.web_service_type = ''

    @abstractmethod
    def web_service_response_model(self):
        pass

    @abstractmethod
    def web_service_request_model(self):
        pass

    @abstractmethod
    def web_service_method(self):
        pass

    @abstractmethod
    def web_service_definition(self):
        pass


class ModelCRUDRequest(WebServiceRequest):
    """
    ModelCRUDRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelCRUDRequest, self).__init__()
        self.data_row = []
        self.offset = 0
        self.limit = 0
        self.filter = ''
        self.action = None
        self.record_id = 0
        self.record_id_variable = ''
        self.table_name = ''

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelCRUDRequest


class ModelGetListRequest(WebServiceRequest):
    """
    ModelGetListRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelGetListRequest, self).__init__()
        self.ad_reference_id = 0
        self.filter = ''

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelGetListRequest


class ModelRunProcessRequest(WebServiceRequest):
    """
    ModelRunProcessRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelRunProcessRequest, self).__init__()
        self.param_values = []
        self.doc_action = None
        self.ad_record_id = 0
        self.ad_menu_id = 0
        self.ad_process_id = 0

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelRunProcessRequest


class ModelSetDocActionRequest(WebServiceRequest):
    """
    ModelSetDocActionRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ModelSetDocActionRequest, self).__init__()
        self.table_name = ''
        self.record_id = 0
        self.record_id_variable = ''
        self.doc_action = None

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.ModelSetDocActionRequest


class CompositeRequest(WebServiceRequest):
    """
    CompositeRequest. Web Service Request
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(CompositeRequest, self).__init__()
        self.operations = []

    def web_service_request_model(self):
        return enums.WebServiceRequestModel.CompositeRequest
