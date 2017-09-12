#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class WayBillDetailGet(object):
    '''
    获取运单详情
    /api/tms/wayBill/getWayBillDetail
    '''
    def __init__(self):
        self.logger = Log()
        config = ReadYaml( project_path + '/config/config.yaml').getValue()
        self.url = "https://{0}:{1}{2}/api/tms/wayBill/getWayBillDetail".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.token = config['tms_api_token']
        self.headers = {
            'Content - Type': 'multipart/form-data',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token}


    def waybill_detail_get(self,wayBillId=''):
        '''获取运单详情'''
        payload = {'wayBillId': wayBillId}
        request = HttpClient().post_form(self.url,payload,self.headers)
        response = request.json()
        if response['code'] == 0:
            return response['content']
        else:
            self.logger.info('/payment/tmsConfirmWayBill return status code error:{0}'.format(response))