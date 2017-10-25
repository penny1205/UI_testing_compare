#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class LoanDelete(object):
    '''
    根据ID删除数据
    /api/tms/loan/deleteById
    '''
    __slots__ = ('__loanDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__loanDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/loan/deleteById'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def loan_delete(self,Id=''):
         '''根据ID删除数据'''
         try:
             payload ={
                 'id': Id,
             }
             response = HttpClient().get(self.__loanDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None