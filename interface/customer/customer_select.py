#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class CustomerSelect(object):
    '''
    查询客户列表
    /api/tms/customer/listTmsCustomers
    '''
    __slots__ = ('__customerSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__customerSelectApiUrl = "https://{0}:{1}{2}/api/tms/customer/listTmsCustomers".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def customer_select(self,currentPage='1',rows='10',customerName ='',startTime='',endTime='',customerStatus=''):
         '''查询客户列表'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'customerName': customerName,
                 'startTime':startTime,
                 'endTime':endTime,
                 'customerStatus':customerStatus  # 客户合作状态，int， 0-全部，1-合作中，2-停止合作，必填
             }
             response = HttpClient().get(self.__customerSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None