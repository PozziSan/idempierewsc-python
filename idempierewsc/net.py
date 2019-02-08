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

"""
Contributor: @pozzisan
"""
import time
import platform
import idempierewsc
import urllib3

from requests import post
from requests import packages
from requests import codes
from requests import exceptions
from idempierewsc import exception
from idempierewsc import request
from idempierewsc import response
from idempierewsc import base
from lxml import etree


class WebServiceConnection():
    """
    Client class for soap protocol.
    This class send a stream data xml.
    """
    CONTENT_TYPE_HEADER = 'content-type'
    CONTENT_TYPE = 'text/xml; charset=UTF-8'
    USE_AGENT_HEADER = 'user-agent'
    DEFAULT_TIMEOUT = 5000
    DEFAULT_ATTEMPTS = 1
    DEFAULT_ATTEMPTS_TIMEOUT = 500
    ENCODING_UTF_8 = 'UTF-8'

    def __init__(self):
        self.attempts = self.DEFAULT_ATTEMPTS
        self.attempts_timeout = self.DEFAULT_ATTEMPTS_TIMEOUT
        self.timeout = self.DEFAULT_TIMEOUT
        self.app_name = ''
        self.url = ''
        self.time_request = 0
        self.attempts_request = 0
        self.request = None
        self.response_status = ''
        self.xml_request = None
        self.xml_response = None
        self.proxies = {}

    def user_agent(self):
        """
        Gets full user agent
        :return: Full user agent name
        """
        return '{} ({}/{}/{}/{}) {}'.format(
            idempierewsc.name, 
            idempierewsc.component_name,
            idempierewsc.version, 
            "Python",        
            platform.platform(),
            self.app_name
        ).strip()

    def path(self):
        """
        Gets the path of iDempiere web services
        :return:
        """
        if self.request is None:
            return None
        return 'ADInterface/services/{}'.format(self.request.web_service_definition().value)

    def web_service_url(self):
        """
        Build the url for web service
        :return: URL
        """
        if self.path() is None:
            return self.url

        temp_path = self.path().strip('/') if self.path().endswith('/') else self.path()
        temp_url = self.url.strip('/') if self.url.endswith('/') else self.url

        return '{}/{}'.format(
            temp_url, 
            temp_path
        )

    def send_request(self, request):
        """
        Send data request
        :param request: Data request
        :return: Response
        """
        if not self.web_service_url():
            raise exception.WebServiceException('URL must be different than empty or null')

        urllib3.disable_warnings()

        if isinstance(request, idempierewsc.base.WebServiceRequest):
            self.request = request
            factory = idempierewsc.request.RequestFactory()
            self.xml_request = factory.create_request(request)
            data_request = etree.tostring(self.xml_request, encoding=self.ENCODING_UTF_8)
            response_model = request.web_service_response_model()
        else:
            self.request = None
            data_request = request
            response_model = None
            self.xml_request = etree.fromstring(data_request)

        self.attempts_request = 0
        start_time = int(time.time() * 1000.)
        successful = False
        data_response = ''

        while not successful:
            self.attempts_request += 1
            try:
                r = post(
                    self.web_service_url(), 
                    data=data_request,
                    headers={
                        self.CONTENT_TYPE_HEADER: self.CONTENT_TYPE,
                        self.USE_AGENT_HEADER: self.user_agent()
                    },
                    verify=False, 
                    timeout=(float(self.timeout) / 1000.), 
                    proxies=self.proxies
                )

                if r.status_code != codes[200]:
                    r.raise_for_status()

                data_response = r.text
                self.response_status = r.status_code
                successful = True
            except Exception as e:
                if self.attempts_request >= self.attempts:
                    self.time_request = int(time.time() * 1000.) - start_time
                    if isinstance(e, exceptions.ReadTimeout):
                        raise idempierewsc.exception.WebServiceTimeoutException(
                            'Timeout exception, operation has expired {}'.format( 
                                e
                        ))
                    else:
                        raise idempierewsc.exception.WebServiceException(
                            'Error sending request: {}'.format( 
                                e
                        ))
                else:
                    time.sleep(float(self.attempts_timeout) / 1000.)

        self.time_request = int(time.time() * 1000.) - start_time

        self.xml_response = etree.fromstring(data_response)
        factory = idempierewsc.response.ResponseFactory()

        if not response_model:
            return data_response

        return factory.create_response(response_model, self.xml_response)

    def print_xml_request(self):
        """
        Print the request
        :return: None
        """
        st = etree.tostring(self.xml_request, pretty_print=True, encoding=self.ENCODING_UTF_8)
        print(st.decode(self.ENCODING_UTF_8))

    def print_xml_response(self):
        """
        Print the response
        :return: None
        """
        st = etree.tostring(self.xml_response, pretty_print=True, encoding=self.ENCODING_UTF_8)
        print(st.decode(self.ENCODING_UTF_8))

    def save_xml_request(self, file_name):
        """
        Save the request to file
        :param file_name: File to save
        :return: None
        """
        
        with open(file_name, 'w') as save_file:
            save_file.write(etree.tostring(
                self.xml_request, 
                pretty_print=True, 
                encoding=self.ENCODING_UTF_8
                ).decode(
                    self.ENCODING_UTF_8
            ))

    def save_xml_response(self, file_name):
        """
        Save the response to file
        :param file_name: File to save
        :return: None
        """
        with open(file_name, 'w') as save_file:
            save_file.write(
                etree.tostring(
                    self.xml_response, 
                    pretty_print=True, 
                    encoding=self.ENCODING_UTF_8
                ).decode(
                    self.ENCODING_UTF_8
            ))
