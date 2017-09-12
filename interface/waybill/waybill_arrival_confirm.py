#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class WayBillArrivalConfirm(object):
    '''
    到达确认
    /payment/confirmWayComplete
    '''
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(project_path + '/config/config.yaml').getValue()
        self.url = 'http://{0}:{1}{2}/payment/confirmWayComplete'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.token = config['tms_api_token']
        self.headers = {
            'Content - Type': 'multipart/form-data',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token
        }

    def waybill_arrival_confirm(self,wayBillId='',destAmt='',destMemo=''):
         '''到达确认'''
         payload ={'billId': wayBillId, 'destAmt': destAmt, 'destMemo': destMemo}
         request = HttpClient().post_form(self.url,payload,self.headers)
         response = request.json()
         if response['code'] == 0:
             return True
         else:
             self.logger.info('/payment/confirmWayComplete return status code error:{0}'.format(response))