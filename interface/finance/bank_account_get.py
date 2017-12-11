#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class BankAccountGet(object):
    '''
    根据partnerNo获取开户行信息
    /api/tms/loan/getCardInfo
    '''
    __slots__ = ('__loanDeleteApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__loanDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/loan/getCardInfo'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def bank_account_get(self):
         '''根据partnerNo获取开户行信息'''
         try:
             payload ={
                 'partnerNo': self.partnerNo,
             }
             response = HttpClient().get(self.__loanDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据partnerNo获取开户行信息发生异常:{0}'.format(e))
             return None