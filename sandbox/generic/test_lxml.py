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

from lxml import etree

prefix_0 = "_0"
namespace_0 = "http://idempiere.org/ADInterface/1_0"
prefix_soapenv = "soapenv"
namespace_soapenv = "http://schemas.xmlsoap.org/soap/envelope/"

attribute_xmlns = "xmlns"
namespace_xmlns = "http://www.w3.org/2000/xmlns/"

url = 'http://localhost:8031/ADInterface/services/ModelADService'
urls = 'https://localhost:8431/ADInterface/services/ModelADService'
headers = {'user-agent': 'my-app/0.0.1', 'content-type': 'text/xml; charset=UTF-8'}

root = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope",
                     nsmap={prefix_0: namespace_0, prefix_soapenv: namespace_soapenv})
root.append(etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Header"))
body = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Body")
root.append(body)
body.append(etree.Element("{http://idempiere.org/ADInterface/1_0}createData"))
body.set('hi','hello')
print(etree.tostring(root, pretty_print=True))

root2 = etree.parse("../../documents/CreateBPartnerTest_request.xml")
print(etree.tostring(root2, pretty_print=True))
