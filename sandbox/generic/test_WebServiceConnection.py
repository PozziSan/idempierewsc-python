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
Contributor: @pozzisan <pedropozzif@gmail.com>
"""

from idempierewsc.net import WebServiceConnection

url = 'http://dev11.devcoffee.com.br/ADInterface/services/ModelADService'
urls = 'https://localhost:8431/ADInterface/services/ModelADService'


def test_xml():
    test_file = open('../documents/ReadBPartnerTest_request.xml', 'r')
    return test_file.read()


wsc = WebServiceConnection()
wsc.url = url
wsc.attempts = 3
try:
    response = wsc.send_request(test_xml())
except Exception as e:
    print('Error', str(e))
else:
    wsc.print_xml_response()
finally:
    print(wsc.attempts_request)
    print(wsc.time_request)
    print(wsc.response_status)
