#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class CustomerGet(object):
    '''
    获取客户详情
    /api/tms/customer/getTmsCustomer
    '''
    __slots__ = ('__CustomerGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__CustomerGetApiUrl = "https://{0}:{1}{2}/api/tms/customer/getTmsCustomer".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def customer_get(self,customerId=''):
         '''获取客户详情'''
         try:
             payload ={
                 'customerId': customerId,
             }
             response = HttpClient().get(self.__CustomerGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('获取客户详情发生异常:{0}'.format(e))
             return None