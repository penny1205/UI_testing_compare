#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletBillsUpdate(object):
    '''
    修改交易状态
    /api/tms/wallet/updateSerialNumber
    '''
    __slots__ = ('__walletBillsSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletBillsSelectApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/updateSerialNumber'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_bills_update(self,serialNumber='',type=''):
         '''修改交易状态'''
         try:
             payload = {
                 'serialNumber': serialNumber,
                 'type': type,
             }
             response = HttpClient().post_form(self.__walletBillsSelectApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None