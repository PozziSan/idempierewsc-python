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

from enum import Enum


class WebServiceDefinition(Enum):
    """
    WebService Type Definition
    """
    ModelADService = 'ModelADService'
    compositeInterface = 'compositeInterface'


class WebServiceMethod(Enum):
    """
    WebService Method
    """
    runProcess = 'runProcess'
    createData = 'createData'
    createUpdateData = 'createUpdateData'
    deleteData = 'deleteData'
    getList = 'getList'
    queryData = 'queryData'
    readData = 'readData'
    setDocAction = 'setDocAction'
    updateData = 'updateData'
    compositeOperation = 'compositeOperation'


class WebServiceResponseModel(Enum):
    """
    Response Model
    """
    StandardResponse = 'StandardResponse'
    RunProcessResponse = 'RunProcessResponse'
    WindowTabDataResponse = 'WindowTabDataResponse'
    CompositeResponse = 'CompositeResponse'


class WebServiceResponseStatus(Enum):
    """
    Response Status
    """
    Error = 'Error'
    Successful = 'Successful'
    Unsuccessful = 'Unsuccessful'


class WebServiceRequestModel(Enum):
    """
    Request Model
    """
    ModelCRUDRequest = 'ModelCRUDRequest'
    ModelGetListRequest = 'ModelGetListRequest'
    ModelRunProcessRequest = 'ModelRunProcessRequest'
    ModelSetDocActionRequest = 'ModelSetDocActionRequest'
    CompositeRequest = 'CompositeRequest'


class ModelCRUDAction(Enum):
    """
    ModelCRUD Action Values
    """
    Read = 'Read'
    Create = 'Create'
    CreateUpdate = 'CreateUpdate'
    Delete = 'Delete'
    Update = 'Update'


class DocAction(Enum):
    """
    iDempiere Document Action Values
    """
    Complete = 'CO'
    WaitComplete = 'WC'
    Approve = 'AP'
    Reject = 'RJ'
    Post = 'PO'
    Void = 'VO'
    Close = 'CL'
    ReverseCorrect = 'RC'
    ReverseAccrual = 'RA'
    ReActivate = 'RE'
    NoneAction = '--'
    Prepare = 'PR'
    Unlock = 'XL'
    Invalidate = 'IN'
    ReOpen = 'OP'


class DocStatus(Enum):
    """
    iDempiere Document Status Values
    """
    Drafted = 'DR'
    Completed = 'CO'
    Approved = 'AP'
    Invalid = 'IN'
    NotApproved = 'NA'
    Voided = 'VO'
    Reversed = 'RE'
    Closed = 'CL'
    Unknown = '??'
    InProgress = 'IP'
    WaitingPayment = 'WP'
    WaitingConfirmation = 'WC'


class Language(Enum):
    """
    iDempiere Language Values
    """
    ar_AE = 'ar_AE'
    ar_BH = 'ar_BH'
    ar_DZ = 'ar_DZ'
    ar_EG = 'ar_EG'
    ar_IQ = 'ar_IQ'
    ar_JO = 'ar_JO'
    ar_KW = 'ar_KW'
    ar_LB = 'ar_LB'
    ar_LY = 'ar_LY'
    ar_MA = 'ar_MA'
    ar_OM = 'ar_OM'
    ar_QA = 'ar_QA'
    ar_SA = 'ar_SA'
    ar_SD = 'ar_SD'
    ar_SY = 'ar_SY'
    ar_TN = 'ar_TN'
    ar_YE = 'ar_YE'
    be_BY = 'be_BY'
    bg_BG = 'bg_BG'
    ca_ES = 'ca_ES'
    cs_CZ = 'cs_CZ'
    da_DK = 'da_DK'
    de_AT = 'de_AT'
    de_CH = 'de_CH'
    de_DE = 'de_DE'
    de_LU = 'de_LU'
    el_CY = 'el_CY'
    el_GR = 'el_GR'
    en_AU = 'en_AU'
    en_CA = 'en_CA'
    en_GB = 'en_GB'
    en_IE = 'en_IE'
    en_IN = 'en_IN'
    en_MT = 'en_MT'
    en_NZ = 'en_NZ'
    en_PH = 'en_PH'
    en_SG = 'en_SG'
    en_US = 'en_US'
    en_ZA = 'en_ZA'
    es_AR = 'es_AR'
    es_BO = 'es_BO'
    es_CL = 'es_CL'
    es_CO = 'es_CO'
    es_CR = 'es_CR'
    es_DO = 'es_DO'
    es_EC = 'es_EC'
    es_ES = 'es_ES'
    es_GT = 'es_GT'
    es_HN = 'es_HN'
    es_MX = 'es_MX'
    es_NI = 'es_NI'
    es_PA = 'es_PA'
    es_PE = 'es_PE'
    es_PR = 'es_PR'
    es_PY = 'es_PY'
    es_SV = 'es_SV'
    es_US = 'es_US'
    es_UY = 'es_UY'
    es_VE = 'es_VE'
    et_EE = 'et_EE'
    fa_IR = 'fa_IR'
    fi_FI = 'fi_FI'
    fr_BE = 'fr_BE'
    fr_CA = 'fr_CA'
    fr_CH = 'fr_CH'
    fr_FR = 'fr_FR'
    fr_LU = 'fr_LU'
    ga_IE = 'ga_IE'
    hi_IN = 'hi_IN'
    hr_HR = 'hr_HR'
    hu_HU = 'hu_HU'
    in_ID = 'in_ID'
    is_IS = 'is_IS'
    it_CH = 'it_CH'
    it_IT = 'it_IT'
    iw_IL = 'iw_IL'
    ja_JP = 'ja_JP'
    ko_KR = 'ko_KR'
    lt_LT = 'lt_LT'
    lv_LV = 'lv_LV'
    mk_MK = 'mk_MK'
    ms_MY = 'ms_MY'
    mt_MT = 'mt_MT'
    nl_BE = 'nl_BE'
    nl_NL = 'nl_NL'
    no_NO = 'no_NO'
    pl_PL = 'pl_PL'
    pt_BR = 'pt_BR'
    pt_PT = 'pt_PT'
    ro_RO = 'ro_RO'
    ru_RU = 'ru_RU'
    sh_YU = 'sh_YU'
    sk_SK = 'sk_SK'
    sl_SI = 'sl_SI'
    sq_AL = 'sq_AL'
    sr_BA = 'sr_BA'
    sr_CS = 'sr_CS'
    sr_ME = 'sr_ME'
    sr_RS = 'sr_RS'
    sr_YU = 'sr_YU'
    sv_SE = 'sv_SE'
    th_TH = 'th_TH'
    tr_TR = 'tr_TR'
    uk_UA = 'uk_UA'
    vi_VN = 'vi_VN'
    zh_CN = 'zh_CN'
    zh_HK = 'zh_HK'
    zh_SG = 'zh_SG'
    zh_TW = 'zh_TW'
