#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletWithdrawStatusGet(object):
    '''
    获取钱包提现状态
    /api/tms/wallet/getCashOutStatus
    '''
    __slots__ = ('__walletWithdrawApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletWithdrawApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/getCashOutStatus'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_withdraw_status_get(self):
         '''获取钱包提现状态'''
         try:
             response = HttpClient().get(self.__walletWithdrawApiUrl,self.__head_dict)
             return response
         except Exception:
             return None