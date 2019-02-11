# -*- encoding: utf-8 -*-
import urllib3
import requests
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


urllib3.disable_warnings()

url = 'http://dev11.devcoffee.com.br/ADInterface/services/ModelADService'
urls = 'https://localhost:8431/ADInterface/services/ModelADService'
headers = {
    'user-agent': 'my-app/0.0.1',
    'content-type': 'text/xml; charset=UTF-8'
}


def test_xml():
    xml = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:_0="http://idempiere.org/ADInterface/1_0">
    <soapenv:Header/>
    <soapenv:Body>
    <_0:queryData>
    <_0:ModelCRUDRequest>
    <_0:ModelCRUD>
    <_0:serviceType>QueryBPartnerTest</_0:serviceType>
    </_0:ModelCRUD>
    <_0:ADLoginRequest>
    <_0:user>superuser @ brerp.com.br</_0:user>
    <_0:pass>pp_brerp</_0:pass>
    <_0:ClientID>11</_0:ClientID>
    <_0:RoleID>102</_0:RoleID>
    </_0:ADLoginRequest>
    </_0:ModelCRUDRequest>
    </_0:queryData>
    </soapenv:Body>
    </soapenv:Envelope>
    """
    return xml


def test_xml_file():
    test_file = open('../../documents/CreateBPartnerTest_request.xml', 'r')
    return test_file.read()


request = test_xml()
print('Request:' + request)

# timeout on seconds
try:
    r = requests.post(url, data=request, headers=headers,
                      verify=False, timeout=2)
except Exception as e:
    print(e)
else:
    print('Status: {}'.format(str(r.status_code)))
    print('Headers: {}'.format(str(r.headers)))
    print('Response: {}'.format(str(r.text)))
