#__author__ = 'pan'
# -*- coding:utf-8 -*-

import requests
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillCreate(object):
    '''
    新增运单
    /api/tms/wayBill/createWayBill
    '''
    __slots__ = ('__createWayBillApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath()  + '/config/config.yaml').getValue()
        self.__createWayBillApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/createWayBill'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_create(self,carType='',applyDate='',projects='',projectId='',
                       realName='',idNo='',mobile='',carNo='', loginId='',
                       sendProvince='',sendCity='',arriveProvince='',arriveCity='',
                       income='',totalAmt='',preAmt='',oilAmt='',destAmt='',lastAmt='',hasReceipt='',
                       supplierName='',supplierId='',content='',source='',
                       cargoName='',cargoWeight='',cargoVolume='',cargoNumberOfCases='',cargoWorth='',insuranceCosts=''
                      ):
        '''新增运单'''
        try:
            # 用表单来传数据
            files = {
                'carType': (None, str(carType)),
                'applyDate': (None, str(applyDate)),
                'projects': (None, str(projects)),
                'projectId': (None, str(projectId)),
                'partnerNo': (None, str(self.partnerNo)),
                'loginId': (None, str(loginId)),
                'source': (None, str(source)),
                #车辆信息
                'realName': (None, str(realName)),
                'idNo':(None,str(idNo)),
                'mobile':(None,str(mobile)),
                'carNo':(None,str(carNo)),
                #线路
                'sendProvince':(None,str(sendProvince)),
                'sendCity': (None, str(sendCity)),
                'arriveProvince':(None,str(arriveProvince)),
                'arriveCity':(None,str(arriveCity)),
                #金额
                'income': (None, str(income)),
                'totalAmt':(None,str(totalAmt)),
                'preAmt':(None,str(preAmt)),
                'oilAmt':(None,str(oilAmt)),
                'destAmt':(None,str(destAmt)),
                'lastAmt':(None,str(lastAmt)),
                'hasReceipt': (None, str(hasReceipt)),
                'supplierName': (None, str(supplierName)),  # 供应商
                'supplierId': (None, str(supplierId)),
                'content':(None,str(content)),#备注
                #货物信息
                'cargoName': (None, str(cargoName)),
                'cargoWeight':(None,str(cargoWeight)),
                'cargoVolume':(None,str(cargoVolume)),
                'cargoNumberOfCases':(None,str(cargoNumberOfCases)),
                'cargoWorth':(None,str(cargoWorth)),
                'insuranceCosts':(None,str(insuranceCosts))
            }

            response = HttpClient().post_multipart(self.__createWayBillApiUrl,files,self.__head_dict)
            return response
        except Exception:
            return None