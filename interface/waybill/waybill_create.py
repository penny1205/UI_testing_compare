#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillCreate(object):
    '''
    新增运单
    /api/tms/wayBill/createWayBill
    '''
    __slots__ = ('__createWayBillApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath()  + '/config/config.yaml').getValue()
        self.__createWayBillApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/createWayBill'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_create(self,carType='',applyDate='',projects='',projectId='',partnerNo='', loginId='',source='',
                       realName='',idNo='',mobile='',carNo='',
                       sendProvince='',sendCity='',arriveProvince='',arriveCity='',
                       income='',totalAmt='',preAmt='',oilAmt='',destAmt='',lastAmt='',hasReceipt='',
                       supplierName='',supplierId='',content='',
                       cargoName='',cargoWeight='',cargoVolume='',cargoNumberOfCases='',cargoWorth='',insuranceCosts=''
                      ):
        '''新增运单'''
        #用表单来传数据
        try:
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
            'cargoName': (None, cargoName),
            'cargoWeight':(None,cargoWeight),
            'cargoVolume':(None,cargoVolume),
            'cargoNumberOfCases':(None,cargoNumberOfCases),
            'cargoWorth':(None,cargoWorth),
            'insuranceCosts':(None,insuranceCosts)
            }

            files2 = {
                'carType': carType,
                'applyDate': applyDate,
                'projects': projects,
                'projectId': projectId,
                'partnerNo': partnerNo,
                'loginId': loginId,
                'source': source,
                # 车辆信息
                'realName': realName,
                'idNo': idNo,
                'mobile': mobile,
                'carNo': carNo,
                # 线路
                'sendProvince': sendProvince,
                'sendCity': sendCity,
                'arriveProvince': arriveProvince,
                'arriveCity': arriveCity,
                # 金额
                'income': income,
                'totalAmt': totalAmt,
                'preAmt': preAmt,
                'oilAmt': oilAmt,
                'destAmt': destAmt,
                'lastAmt': lastAmt,
                'hasReceipt': hasReceipt,
                'supplierName': supplierName,  # 供应商
                'supplierId': supplierId,
                'content': content,  # 备注
                # 货物信息
                'cargoName': cargoName,
                'cargoWeight': cargoWeight,
                'cargoVolume': cargoVolume,
                'cargoNumberOfCases': cargoNumberOfCases,
                'cargoWorth': cargoWorth,
                'insuranceCosts': insuranceCosts
            }

            request = HttpClient().post_multipart(self.__createWayBillApiUrl,files2,self.__head_dict)
            response = request.json()
            return response
        except Exception:
            # return None
            raise
        # if response['code'] == 0:
        #     return response['content']
        # else:
        #     if response['msg'] == '此手机号已有未确认的订单,不可重复提交':
        #         return response['content']
        #     else:
        #         self.logger.info('/api/tms/wayBill/createWayBill return status code error:{0}'.format(response))
