#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DriverCreate(object):
    '''
    新增外请车
    /api/tms/driver/createTmsAppDriver/all
    '''
    def __init__(self):
        self.logger = Log()

        config = ReadYaml( project_path + '/config/config.yaml').getValue()
        self.url = 'https://{0}:{1}{2}/api/tms/driver/createTmsAppDriver/all'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.token = config['tms_api_token']
        self.headers = {
            'Content - Type': 'multipart/form-data',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token
        }

    def driver_create(self):
        '''新增外请车'''
        payload = {
            'name' : 'penny',
            'mobile' : '13077327047',
            'idNo' : '110605199001011551',
            'carNo' : '京A00000',
            'carLength' : '17.5',
            'carModel' : 'XIANG_SHI_CHE',
            'carLoad' : '20'
        }
        request = HttpClient().post_form(self.url,payload,self.headers)
        response = request.json()
        if response['code'] == 0:
            return response['content']['dataList']
        else:
            self.logger.info(' /api/tms/driver/createTmsAppDriver/all return status code error:{0}'.format(response))

if __name__ == '__main__':
    driver_list = DriverCreate().driver_create()
    print(driver_list)