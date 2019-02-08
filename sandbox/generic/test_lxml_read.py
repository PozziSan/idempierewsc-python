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

# root = etree.parse("../../documents/QueryBPartnerTest_response.xml")
root = etree.parse("../../documents/StandardResponseError_Example.xml")
fault = etree.parse("../../documents/Fault_response.xml")
print(etree.tostring(root, pretty_print=True))
print(etree.tostring(fault, pretty_print=True))


def check_fault(xml):
    for element in xml.iter():
        temp_tag = element.tag.rsplit('}', 1)[-1]
        temp_text = element.text
        if temp_tag in ('Fault',):
            continue
        print(temp_tag)
        print(temp_text)


def find_elements_0(root, name):
    return root.findall('.//{%s}%s' % (namespace_0, name))


# CHECK FAULT
for element in fault.iter():
    temp_tag = element.tag.rsplit('}', 1)[-1]
    if temp_tag in ('Envelope', 'Body'):
        continue

    if temp_tag in ('Fault',):
        check_fault(element)
        break

print("")

for element in root.iter():
    temp_tag = element.tag.rsplit('}', 1)[-1]
    if temp_tag in ('Envelope', 'Body'):
        continue

    print(find_elements_0(element, 'StandardResponse')[0].get('RecordIDe'))
    break
