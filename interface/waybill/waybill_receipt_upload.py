#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os.path
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillReceiptUpload(object):
    '''
    回单上传
    /app/shipper/uploadReceipt
    '''
    __slots__ = ('__wayBillReceiptUploadApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillReceiptUploadApiUrl = 'http://{0}:{1}{2}/shipper/uploadReceipt'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_receipt_upload(self,wayBillId='',abnormal='',damaged='',losted='',memo='',type='',receipt_0='',receipt_1='',
                               receipt_2='',receipt_3='',receipt_4=''):
         '''到达确认'''
         try:
             # if receipt_0 != None:
             #     receipt_0 = open(receipt_0,'rb')
             #     receipt_name_0 = os.path.basename(receipt_0)
             # else:
             #     receipt_name_0 = None
             #
             # if receipt_1 != None:
             #     receipt_1 = open(receipt_1,'rb')
             #     receipt_name_1 = os.path.basename(receipt_1)
             # else:
             #     receipt_name_1 = None
             #
             # if receipt_2 != None:
             #     receipt_2 = open(receipt_2,'rb')
             #     receipt_name_2 = os.path.basename(receipt_2)
             # else:
             #     receipt_name_2 = None
             #
             # if receipt_3 != None:
             #     receipt_3 = open(receipt_3,'rb')
             #     receipt_name_3 = os.path.basename(receipt_3)
             # else:
             #     receipt_name_3 = None
             #
             # if receipt_4 != None:
             #     receipt_4 = open(receipt_4,'rb')
             #     receipt_name_4 = os.path.basename(receipt_4)
             # else:
             #     receipt_name_4 = None

             payload ={
                  'id': (None, str(wayBillId)),
                  'abnormal': (None, str(abnormal)),
                  'damaged': (None, str(damaged)),
                  'losted': (None, str(losted)),
                  'memo': (None, str(memo)),
                  'type': (None, str(type)),
                  'receipt_0': (os.path.basename(receipt_0), open(receipt_0,'rb')),
                  # 'receipt_0':(receipt_name_0,receipt_0),
                  # 'receipt_1':(receipt_name_1,receipt_1),
                  # 'receipt_2':(receipt_name_2,receipt_2),
                  # 'receipt_3':(receipt_name_3,receipt_3),
                  # 'receipt_4':(receipt_name_4,receipt_4),
                       }

             response = HttpClient().post_multipart(self.__wayBillReceiptUploadApiUrl,payload,self.__head_dict)
             print(response.json())
             return response
         except Exception:
             raise
             # return None