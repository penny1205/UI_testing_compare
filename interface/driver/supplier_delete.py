#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class SupplierDelete(object):
    '''
    删除供应商信息
    /api/tms/supplier/deleteSupplier
    '''
    __slots__ = ('__supplierDeleteApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__supplierDeleteApiUrl = "https://{0}:{1}{2}/api/tms/supplier/deleteSupplier".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def supplier_delete(self,supplierId=''):
         '''删除供应商信息'''
         try:
             payload ={
                 'supplierId': supplierId,
             }
             response = HttpClient().post_form(self.__supplierDeleteApiUrl,payload,self.__head_dict)
             return response
         except Exception as e:
             Log().error('删除供应商信息发生异常:{0}'.format(e))
             return None