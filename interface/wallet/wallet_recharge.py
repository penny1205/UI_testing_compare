#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletRecharge(object):
    '''
    钱包充值申请
    /api/tms/wallet/recharge
    '''
    __slots__ = ('__walletRechargeApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletRechargeApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/recharge'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_recharge(self,moneyOrder=''):
         '''钱包充值申请'''
         try:
             payload = {
                 'moneyOrder': moneyOrder, # 充值金额
             }
             response = HttpClient().post_form(self.__walletRechargeApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None