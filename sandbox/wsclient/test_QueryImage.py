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

from idempierewsc.request import QueryDataRequest
from idempierewsc.base import LoginRequest
from idempierewsc.enums import WebServiceResponseStatus
from idempierewsc.net import WebServiceConnection
import traceback

url = 'http://localhost:8031'
urls = 'https://localhost:8431'

login = LoginRequest()
login.client_id = 11
login.org_id = 0
login.role_id = 102
login.password = 'System'
login.user = 'SuperUser'

query = QueryDataRequest()
query.web_service_type = 'QueryImageTest'
query.offset = 5
query.limit = 1
query.login = login

wsc = WebServiceConnection()
wsc.url = urls
wsc.attempts = 3
wsc.app_name = 'Test from python'

try:
    response = wsc.send_request(query)
    wsc.print_xml_request()
    wsc.print_xml_response()

    if response.status == WebServiceResponseStatus.Error:
        print('Error: ', response.error_message)
    else:
        print('Total Rows: ', str(response.total_rows))
        print('Num rows: ', str(response.num_rows))
        print('Start row: ', str(response.start_row))
        print('')
        for row in response.data_set:
            for field in row:
                print('{}: {}'.format(
                    str(field.column),
                    str(field.value)
                ))
                if str(field.column) == 'BinaryData':
                    with open('newFile.png', 'wb') as file:
                        file.write(field.get_byte_value())
            print('')
        print('-' * 25)
        print('Web Service Type: ', query.web_service_type)
        print('Attempts: ', str(wsc.attempts_request))
        print('Time: ', str(wsc.time_request))
except:
    traceback.print_exc()
