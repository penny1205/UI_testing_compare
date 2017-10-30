#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletWithdraw(object):
    '''
    钱包提现申请
    /api/tms/wallet/cashOutApply
    '''
    __slots__ = ('__walletWithdrawApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletWithdrawApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/cashOutApply'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_withdraw(self,pwdPay='',moneyOrder=''):
         '''钱包提现申请'''
         try:
             payload = {
                 'pwdPay': pwdPay,         # 用户支付密码(6)
                 'moneyOrder':moneyOrder   # 提现金额 Number(8, 2)
             }
             response = HttpClient().post_form(self.__walletWithdrawApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None