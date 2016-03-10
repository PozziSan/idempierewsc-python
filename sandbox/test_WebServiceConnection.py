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

from idempierewsc.net import WebServiceConnection

url = 'http://localhost:8031/ADInterface/services/ModelADService'
urls = 'https://localhost:8431/ADInterface/services/ModelADService'


def test_xml():
    test_file = open('../documents/QueryBPartnerTest_request.xml', 'r')
    return test_file.read()


request = test_xml()
print('Request:\n' + request)

wsc = WebServiceConnection()
wsc.url = urls
wsc.attempts = 3
try:
    response = wsc.send_request(request)
except Exception as e:
    print('Error'+e.message)
else:
    wsc.print_xml_response()
finally:
    print(wsc.attempts_request)
    print(wsc.time_request)
    print(wsc.response_status)
