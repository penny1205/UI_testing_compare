#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillReceiptGet(object):
    '''
    获取回单详情
    /payment/getReceiptMsg
    '''
    __slots__ = ('__wayBillReceiptGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillReceiptGetApiUrl = 'http://{0}:{1}{2}/payment/getReceiptMsg'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.__head_dict = {
            # 'content-type': "application/json",
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_receipt_get(self,wayBillId=''):
         '''回单确认'''
         try:
             payload ={
                 'id': wayBillId,
                       }
             response = HttpClient().get(self.__wayBillReceiptGetApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None