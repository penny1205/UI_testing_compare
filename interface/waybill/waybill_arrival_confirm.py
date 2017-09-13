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
            'token': config['tms_api_token']
        }

    def waybill_arrival_confirm(self,wayBillId='',destAmt='',destMemo=''):
         '''到达确认'''
         try:
             payload ={'billId': wayBillId, 'destAmt': destAmt, 'destMemo': destMemo}
             request = HttpClient().post_form(self.__arrivalConfirmWayBillApiUrl,payload,self.__head_dict)
             response = request.json()
             return response
         except Exception:
             return None
         # if response['code'] == 0:
         #     return True
         # else:
         #     self.logger.info('/payment/confirmWayComplete return status code error:{0}'.format(response))