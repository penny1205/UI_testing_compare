#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class CustomerUpdate(object):
    '''
    客户资料修改
    /api/tms/customer/updateTmsCustomer
    '''
    __slots__ = ('__customerUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__customerUpdateApiUrl = "https://{0}:{1}{2}/api/tms/customer/updateTmsCustomer".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def customer_update(self,customerId='',updateType='',customerName='',customerCode='',phone ='',customerDeveloper=''):
         '''客户资料修改'''
         try:
             payload ={
                 'customerId':customerId,
                 'updateType':updateType,
                 'customerName': customerName,
                 'customerCode': customerCode,
                 'phone': phone,
                 'customerDeveloper': customerDeveloper,
             }
             response = HttpClient().post_form(self.__customerUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None