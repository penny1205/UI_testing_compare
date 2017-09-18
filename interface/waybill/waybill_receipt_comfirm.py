#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillReceiptConfirm(object):
    '''
    回单确认
    /app/payment/confirmReceipt
    '''
    __slots__ = ('__wayBillReceiptConfirmApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillReceiptConfirmApiUrl = 'http://{0}:{1}{2}/payment/confirmReceipt'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.__head_dict = {
            # 'content-type': "application/json",
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_receipt_confirm(self,wayBillId='',lastAmt='',lastMemo='',shipperMemo=''):
         '''回单确认'''
         try:
             payload ={
                 'wayBillId': wayBillId,
                 'shipperMemo': shipperMemo,
                 'lastAmt':lastAmt,
                 'lastMemo':lastMemo
                       }
             response = HttpClient().post_json(self.__wayBillReceiptConfirmApiUrl,payload,self.__head_dict)
             print(response.json())
             return response
         except Exception:
             return None