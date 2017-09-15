#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillArrivalConfirm(object):
    '''
    到达确认
    /payment/confirmWayComplete
    '''
    __slots__ = ('__arrivalConfirmWayBillApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__arrivalConfirmWayBillApiUrl = 'http://{0}:{1}{2}/payment/confirmWayComplete'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.__head_dict = {
            # 'content-type': "application/json",
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_arrival_confirm(self,wayBillId='',destAmt='',destMemo='',lastAmt='',lastMemo=''):
         '''到达确认'''
         try:
             payload ={'billId': wayBillId,
                       'destAmt': destAmt,
                       'destMemo': destMemo,
                       'lastAmt':lastAmt,
                       'lastMemo':lastMemo
                       }
             response = HttpClient().post_json(self.__arrivalConfirmWayBillApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None