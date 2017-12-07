#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class SupplierCreate(object):
    '''
    新增供应商
    /api/tms/supplier/createSupplier
    '''
    __slots__ = ('__supplierCreateApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__supplierCreateApiUrl = "https://{0}:{1}{2}/api/tms/supplier/createSupplier".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def supplier_create(self,name='',type='',contactPersonName='',contactPersonMobile ='',contactPersonIdNo='',
                        contactPersonIdCardPhoto='',businessLicencePhoto='',businessPermitPhoto='',
                        taxRegistrationCertificatePhoto='',contractPhoto=''):
         '''新增供应商'''
         try:
             payload ={
                 'name': name,
                 'type': type,
                 'contactPersonName': contactPersonName,
                 'contactPersonMobile': contactPersonMobile,
                 'contactPersonIdNo': contactPersonIdNo,
                 'contactPersonIdCardPhoto': contactPersonIdCardPhoto,
                 'businessLicencePhoto':businessLicencePhoto,
                 'businessPermitPhoto':businessPermitPhoto,
                 'taxRegistrationCertificatePhoto': taxRegistrationCertificatePhoto,
                 'contractPhoto':contractPhoto,
             }
             response = HttpClient().post_json(self.__supplierCreateApiUrl,payload,self.__head_dict)
             print(response.request.body)
             return response
         except Exception as e:
             Log().error('新增供应商发生异常:{0}'.format(e))
             return None