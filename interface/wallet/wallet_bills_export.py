#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class WalletBillsExport(object):
    '''
    交易记录导出
    /api/tms/wallet/exportPaymentList
    '''
    __slots__ = ('__walletBillsExportApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__walletBillsExportApiUrl = 'https://{0}:{1}{2}/api/tms/wallet/exportPaymentExcel'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def wallet_bills_export(self,type='',startAmount='',endAmount='',startDateStr='',endDateStr=''):
         '''交易记录导出'''
         try:
             payload = {
                 'type': type,
                 'startAmount': startAmount,   #查询的起始金额
                 'endAmount': endAmount,       #查询的结束金额
                 'startDateStr': startDateStr, #开始时间
                 'endDateStr': endDateStr,     #结束时间
             }
             response = HttpClient().post_json(self.__walletBillsExportApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None