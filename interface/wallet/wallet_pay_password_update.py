#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletPayPasswordUpdate(object):
    '''
    支付密码修改
    /api/tms/wallet/paypwdModify
    '''
    __slots__ = ('__walletPatPasswordUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletPatPasswordUpdateApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/paypwdModify'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_pay_password_update(self,pwdPay='',pwdPayNew=''):
         '''支付密码修改'''
         try:
             payload = {
                 'pwdPay': pwdPay,         # 原支付密码(6)
                 'pwdPayNew':pwdPayNew     # 新支付密码
             }
             response = HttpClient().post_json(self.__walletPatPasswordUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None