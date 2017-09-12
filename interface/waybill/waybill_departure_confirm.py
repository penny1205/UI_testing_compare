#__author__ = 'pan'
# -*- coding:utf-8 -*-
import json
import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class WayBillDepartureConfirm(object):
    '''
    发车确认
    /payment/tmsConfirmWayBill
    '''
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(project_path + '/config/config.yaml').getValue()
        self.url = 'http://{0}:{1}{2}/payment/tmsConfirmWayBill'.format(
            config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.token = config['tms_api_token']
        self.YD_OAUTH = config['tms_api_YD_OAUTH']
        self.headers = {
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token,
            'yd_oauth': self.YD_OAUTH
        }

    def waybill_departure_confirm(self,billId=''):
        '''发车确认'''
        payload ={
            'billId':billId
        }
        request = HttpClient().post_json(self.url,payload,self.headers)
        response = request.json()
        if response['code'] == 0:
            return True
        else:
            self.logger.info('/payment/tmsConfirmWayBill return status code error:{0}'.format(response))

if __name__ == '__main__':
    WayBillDepartureConfirm().waybill_departure_confirm('23166')
