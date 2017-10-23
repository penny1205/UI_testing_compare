#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class CustomerCreate(object):
    '''
    新增客户
   /api/tms/customer/addCustomer
    '''
    __slots__ = ('__CustomerCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__CustomerCreateApiUrl = "https://{0}:{1}{2}/api/tms/customer/addCustomer".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def customer_create(self,customerName='',customerCode='',phone ='',customerDeveloper=''):
         '''新增客户'''
         try:
             payload ={
                 'customerName': customerName,
                 'customerCode': customerCode,
                 'phone': phone,
                 'customerDeveloper': customerDeveloper,
             }
             response = HttpClient().post_json(self.__CustomerCreateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None