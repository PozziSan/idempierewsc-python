# -*- encoding: utf-8 -*-
"""
Copyright (c) 2016 Saúl Piña <sauljabin@gmail.com>.

Contributor: Pedro Pozzi Ferreira - @pozzisan <pedropozzif@gmail.com>

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

from idempierewsc.base import LoginRequest
from idempierewsc.base import Operation
from idempierewsc.base import Field
from idempierewsc.request import CreateDataRequest
from idempierewsc.request import CompositeOperationRequest
from idempierewsc.enums import WebServiceResponseStatus
from idempierewsc.net import WebServiceConnection
from random import randint

import traceback

url = 'http://dev04.devcoffee.com.br'
urls = 'https://test.idempiere.org'

# CREATE LOGIN
login = LoginRequest()
login.client_id = 11
login.org_id = 0
login.role_id = 102
login.password = 'pp_brerp'
login.user = 'superuser @ brerp.com.br'

# CREATE WEBSERVICE FOR IMAGE
path_image = '/home/pedro/Documentos/Workspace/PozziSan/idempierewsc/documents/idempiere-logo.png'

ws1 = CreateDataRequest()
ws1.web_service_type = 'CreateImageTest'
ws1.data_row.append(Field('Name', path_image))
ws1.data_row.append(Field('Description', 'Test Create BPartner and Logo'))

# CREATE BINARY FIELD
binary_field = Field('BinaryData')
with open(path_image, 'rb') as file:
    binary_field.set_byte_value(file.read())
ws1.data_row.append(binary_field)

# CREATE WEBSERVICE FOR BPARTNER
ws2 = CreateDataRequest()
ws2.web_service_type = 'CreateBPartnerTest'
ws2.data_row.append(Field('Name', 'Chicão de Negócios'))
ws2.data_row.append(Field('Value', randint(1000000, 10000000)))
# ws2.data_row.append(Field('TaxID', '987654321'))
ws2.data_row.append(Field('Logo_ID', '@AD_Image.AD_Image_ID'))

# CREATE COMPOSITE
ws0 = CompositeOperationRequest()
ws0.login = login
ws0.operations.append(Operation(ws1))
ws0.operations.append(Operation(ws2))
ws0.web_service_type = 'CompositeBPartnerTest'

# CREATE CONNECTION
wsc = WebServiceConnection()
wsc.url = urls
wsc.attempts = 3
wsc.app_name = 'Test from python'

# SEND CONNECTION
try:
    response = wsc.send_request(ws0)
    wsc.print_xml_request()
    wsc.print_xml_response()

# GET THE RESPONSE
    if response.status == WebServiceResponseStatus.Error:
        print('Error: ', response.error_message)
    else:
        print('Response: ', str(response.web_service_response_model()))
        for res in response.responses:
            print('Response: ', str(res.web_service_response_model()))
        print('-' * 45)
        print('Web Service Type: ', ws0.web_service_type)
        print('Attempts: ', str(wsc.attempts_request))
        print('Time: ', str(wsc.time_request))
except:
    traceback.print_exc()
