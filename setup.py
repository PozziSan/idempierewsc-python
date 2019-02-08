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

from distutils.core import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


requirements = parse_requirements('requirements.txt', session=False)

setup(
        name='idempierewsc',
        version='1.0.1',
        packages=['idempierewsc'],
        url='https://github.com/PozziSan/idempierewsc-python',
        license='LGPL 3',
        author='Saúl Piña',
        author_email='sauljabin@gmail.com',
        description='iDempiere Web Service Client',
        install_requires=[str(ir.req) for ir in requirements]
)
