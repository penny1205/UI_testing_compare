#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class WayBillCreate(object):
    '''
    新增运单
    /api/tms/wayBill/createWayBill
    '''
    def __init__(self):
        self.logger = Log()
        config = ReadYaml( project_path + '/config/config.yaml').getValue()
        self.url = 'https://{0}:{1}{2}/api/tms/wayBill/createWayBill'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.token = config['tms_api_token']
        self.YD_OAUTH = config['tms_api_YD_OAUTH']
        self.headers = {
            'Content-Type': 'multipart/form-data',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token,
            'YD_OAUTH': self.YD_OAUTH
        }

    def waybill_create(self,carType='',applyDate='',projects='',projectId='',partnerNo='', loginId='',source='',
                       realName='',idNo='',mobile='',carNo='',
                       sendProvince='',sendCity='',arriveProvince='',arriveCity='',
                       income='',totalAmt='',preAmt='',oilAmt='',destAmt='',lastAmt='',hasReceipt='',
                       supplierName='',supplierId='',content='',
                       cargoWeight='',cargoVolume='',cargoNumberOfCases='',cargoWorth='',insuranceCosts='',cargoName=''
                      ):
        '''新增运单'''
        #用表单来传数据
        files = {
            'carType': (None, carType),
            'applyDate': (None, applyDate),
            'projects': (None, projects),
            'projectId': (None, projectId),
            'partnerNo': (None, partnerNo),
            'loginId': (None, loginId),
            'source': (None, source),
            #车辆信息
            'realName': (None, realName),
            'idNo':(None,idNo),
            'mobile':(None,mobile),
            'carNo':(None,carNo),
            #线路
            'sendProvince':(None,sendProvince),
            'sendCity': (None, sendCity),
            'arriveProvince':(None,arriveProvince),
            'arriveCity':(None,arriveCity),
            #金额
            'income': (None, income),
            'totalAmt':(None,totalAmt),
            'preAmt':(None,preAmt),
            'oilAmt':(None,oilAmt),
            'destAmt':(None,destAmt),
            'lastAmt':(None,lastAmt),
            'hasReceipt': (None, hasReceipt),
            'supplierName': (None, supplierName),  # 供应商
            'supplierId': (None, supplierId),
            'content':(None,content),#备注
            #货物信息
            'cargoWeight':(None,cargoWeight),
            'cargoVolume':(None,cargoVolume),
            'cargoNumberOfCases':(None,cargoNumberOfCases),
            'cargoWorth':(None,cargoWorth),
            'insuranceCosts':(None,insuranceCosts),
            'cargoName':(None,cargoName)
        }

        request = HttpClient().post_multipart(self.url,files,self.headers)
        response = request.json()
        if response['code'] == 0:
            return response['content']
        else:
            if response['msg'] == '此手机号已有未确认的订单,不可重复提交':
                return response['content']
            else:
                self.logger.info('/api/tms/wayBill/createWayBill return status code error:{0}'.format(response))

