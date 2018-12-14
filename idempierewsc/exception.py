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


class WebServiceException(Exception):
    def __init__(self, message, cause=None):
        if cause:
            super(WebServiceException, self).__init__(u'{message}, caused by: {cause}'.format(
                message=message, 
                cause=repr(cause)
            ))
        else:
            super(WebServiceException, self).__init__(message)

        self.cause = cause

class WebServiceTimeoutException(Exception):
    def __init__(self, message, cause=None):
        if cause:
            super(WebServiceTimeoutException, self).__init__(u'{message}, caused by: {cause}'.format(
                message=message, 
                cause=repr(cause)
            ))
        else:
            super(WebServiceTimeoutException, self).__init__(message)
        
        self.cause = cause
