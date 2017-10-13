#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class SupplierUpdate(object):
    '''
    修改供应商信息
    /api/tms/supplier/updateSupplier
    '''
    __slots__ = ('__supplierUpdateApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__supplierUpdateApiUrl = "https://{0}:{1}{2}/api/tms/supplier/updateSupplier".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def supplier_update(self,supplierId,name='',type='',contactPersonName='',contactPersonMobile ='',contactPersonIdNo='',
                        contactPersonIdCardPhoto='',businessLicencePhoto='',businessPermitPhoto='',
                        taxRegistrationCertificatePhoto='',contractPhoto=''):
         '''修改供应商信息'''
         try:
             payload ={
                 'supplierId':supplierId,
                 'name': name,
                 'type': type,
                 'contactPersonName': contactPersonName,
                 'contactPersonMobile': contactPersonMobile,
                 'contactPersonIdNo': contactPersonIdNo,
                 'contactPersonIdCardPhoto': contactPersonIdCardPhoto,
                 'businessLicencePhoto': businessLicencePhoto,
                 'businessPermitPhoto': businessPermitPhoto,
                 'taxRegistrationCertificatePhoto': taxRegistrationCertificatePhoto,
                 'contractPhoto': contractPhoto,
             }
             response = HttpClient().post_json(self.__supplierUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None