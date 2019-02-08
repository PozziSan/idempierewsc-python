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

from idempierewsc.request import CreateDataRequest
from idempierewsc.base import LoginRequest
from idempierewsc.enums import WebServiceResponseStatus
from idempierewsc.net import WebServiceConnection
from idempierewsc.base import Field
import traceback
import random

url = 'http://dev11.devcoffee.com.br/'
urls = 'https://teste.brerp.com.br/'
login = LoginRequest()
login.client_id = 11
login.org_id = 0
login.role_id = 102
login.password = 'superuser @ brerp.com.br'
login.user = 'caio_udiseen'

ws = CreateDataRequest()
ws.web_service_type = 'CreateBPartnerTest'
ws.login = login

ws.data_row = [
    Field('Name', 'Chicão de Negócios'), 
    Field('Value', 
    str(random.randint(1000000, 10000000))),
    Field('TaxID', '987654321')
]

wsc = WebServiceConnection()
wsc.url = url
wsc.attempts = 3
wsc.app_name = 'Test from python'

try:
    response = wsc.send_request(ws)
    wsc.print_xml_request()
    wsc.print_xml_response()

    if response.status == WebServiceResponseStatus.Error:
        print('Error: ', esponse.error_message)
    else:
        print('RecordID: ', str(response.record_id))
        for field in response.output_fields:
            print('{}: {}'.format(
                str(field.column),
                str(field.value)
            ))
        print('-' * 45)
        print('Web Service Type: ', ws.web_service_type)
        print('Attempts: ', str(wsc.attempts_request))
        print('Time: ', str(wsc.time_request))
except:
    traceback.print_exc()
