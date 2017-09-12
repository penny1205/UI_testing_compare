#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DriverSelect(object):
    '''
    我的外请车列表
    /api/tms/driver/listTmsAppDriver
    接口调用：查询外请车、获取外请车列表、录单时按照司机、手机号查询我的外请车
    '''
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(project_path + '/config/config.yaml').getValue()
        self.url = "https://{0}:{1}{2}/api/tms/driver/listTmsAppDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.token = config['tms_api_token']
        self.YD_OAUTH = config['tms_api_YD_OAUTH']
        self.headers = {
            'Content - Type': 'multipart/form-data',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token,
            'YD_OAUTH':  self.YD_OAUTH,
        }

    def driver_select(self,currentPage='',rows='',partnerNo='',mobile ='',name='',carNo=''):
         '''我的外请车列表'''
         payload ={

             'currentPage': currentPage,
             'rows': rows,
             'partnerNo': partnerNo,
             'name': name,
             'mobile': mobile,
             'carNo': carNo
         }
         request = HttpClient().get(self.url,self.headers,payload)
         response = request.json()
         if response['code'] == 0:
             return response['content']['dataList']
         else:
             self.logger.info('/api/tms/driver/listTmsAppDriver return status code error:{0}'.format(response))

if __name__ == '__main__':
    driver_list = DriverSelect().driver_select(currentPage='1', partnerNo='', rows='10')
    print(driver_list)