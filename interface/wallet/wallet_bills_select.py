#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletBillsSelect(object):
    '''
    交易记录查询
    /api/tms/wallet/listPayment
    '''
    __slots__ = ('__walletBillsSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletBillsSelectApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/listPayment'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_bills_select(self,currentPage='1',rows='10',type='',startAmount='',endAmount='',startDateStr='',endDateStr=''):
         '''交易记录查询'''
         try:
             payload = {
                 'currentPage': currentPage,
                 'rows': rows,
                 'type': type,
                 'startAmount': startAmount,
                 'endAmount': endAmount,
                 'startDateStr': startDateStr,
                 'endDateStr': endDateStr,
             }
             response = HttpClient().get(self.__walletBillsSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None