#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class WayBillSelect(object):
    '''
    运单查询
    /api/tms/wayBill/wayBillList
    '''
    def __init__(self):
        self.logger = Log()
        config = ReadYaml(project_path + '/config/config.yaml').getValue()
        self.url = "http://{0}:{1}{2}/api/tms/wayBill/wayBillList".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.token = config['token']
        self.YD_OAUTH = config['YD_OAUTH']
        self.headers = {
            'Content - Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token,
            'yd_oauth': self.YD_OAUTH
        }

    def waybill_select(self,currentPage='1',rows='10',billStatus='',name='', mobile='',carType='2',carNo='',
                       sendCity='',arriveCity='',applyDateFirst='',applyDateLast='',shipperInsertTimeFirst='',
                       shipperInsertTimeLast='',needAccount='false',normalCondition='',searchStatus='false'):
         '''查询运单'''
         payload ={
             'currentPage': currentPage,
             'rows': rows,
             'billStatus': billStatus,#运单状态,W：待发车，Y：运输中，C：已完成,D:到达确认，H：回单确认，Q：运单取消
             'name': name,
             'mobile':mobile,
             'carType': carType,
             'carNo': carNo,
             'sendCity': sendCity,
             'arriveCity': arriveCity,
             'applyDateFirst': applyDateFirst, #用车日期
             'applyDateLast': applyDateLast,
             'shipperInsertTimeFirst':shipperInsertTimeFirst, #制单日期
             "shipperInsertTimeLast":shipperInsertTimeLast,
             'needAccount': needAccount, #是否需要手动定位次数字段，true需要，false不需要
             'normalCondition':normalCondition,
             'searchStatus': searchStatus #查询方式：true:普通查询，false:高级查询

         }
         request = HttpClient().get(self.url,payload,self.headers)
         response = request.json()
         if response['code'] == 0:
             return response['content']['dataList']
         else:
             self.logger.info('/api/tms/wayBill/wayBillList return status code error:{0}'.format(response))
