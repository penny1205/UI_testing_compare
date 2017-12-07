#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class SupplierSelect(object):
    '''
    查询供应商信息列表
    /api/tms/supplier/listSuppliers
    '''
    __slots__ = ('__supplierSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__supplierSelectApiUrl = "https://{0}:{1}{2}/api/tms/supplier/listSuppliers".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def supplier_select(self,currentPage='1',rows='10',name='',type='',contactPersonMobile =''):
         '''供应商信息列表'''
         try:
             payload ={
             'currentPage': currentPage,
             'rows': rows,
             'name': name,
             'type': type,
             'contactPersonMobile': contactPersonMobile,
             }
             response = HttpClient().get(self.__supplierSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('供应商信息列表发生异常:{0}'.format(e))
             return None