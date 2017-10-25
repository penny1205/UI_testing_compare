#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletInfoGet(object):
    '''
    获取企业钱包信息
    /api/tms/wallet/getWalletInfo
    '''
    __slots__ = ('__loanDeleteApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__loanDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/getWalletInfo'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_info_get(self):
         '''获取企业钱包信息'''
         try:
             payload ={
                 'userId': self.partnerNo,
             }
             response = HttpClient().get(self.__loanDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None