#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class SupplierGet(object):
    '''
    查询供应商详情
    /api/tms/supplier/getSupplier
    '''
    __slots__ = ('__supplierCreateApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__supplierCreateApiUrl = "https://{0}:{1}{2}/api/tms/supplier/getSupplier".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def supplier_get(self,supplierId=''):
         '''查询供应商详情'''
         try:
             payload ={
                 'supplierId': supplierId,
             }
             response = HttpClient().get(self.__supplierCreateApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None