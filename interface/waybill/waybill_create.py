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

    def waybill_create(self,carType='',applyDate='',projects='',projectId='',supplierName='',supplierId='',
                       realName='',idNo='',mobile='',carNo='',carLength='',carModel='',photoAirWay='', loginId='',
                       sendProvince='',sendCity='',sendDistrict='',arriveProvince='',arriveCity='',arriveDistrict='',
                       income='',totalAmt='',preAmt='',oilAmt='',destAmt='',lastAmt='',hasReceipt='',content='',source='',
                       cargoName='',cargoWeight='',cargoVolume='',cargoNumberOfCases='',cargoWorth='',insuranceCosts='',
                       handlingFee='',deliveryFee='',oilCardDeposit='',otherFee='',upWayBillId='',oilCardNo='',
                       vehicleIdNo='',driverCardNo='',
                       #depositBank='',accountName='',
                      ):
        '''新增运单'''
        try:
            if photoAirWay != '':
                with open(photoAirWay, 'rb') as f:
                    photoAirWay = f.read()

            files = {
                'carType': (None, str(carType)),
                'applyDate': (None, str(applyDate)),
                'projects': (None, str(projects)),
                'projectId': (None, str(projectId)),
                'supplierName': (None, str(supplierName)),  # 供应商
                'supplierId': (None, str(supplierId)),
                'partnerNo': (None, str(self.partnerNo)),
                'loginId': (None, str(loginId)),
                'source': (None, str(source)),
                #车辆信息
                'realName': (None, str(realName)),
                'idNo':(None,str(idNo)),
                'mobile':(None,str(mobile)),
                'carNo':(None,str(carNo)),
                'carLength': (None, str(carLength)),
                'carModel': (None, str(carModel)),
                'photoAirWay': (None, str(photoAirWay)), # 运单协议照片
                #线路
                'sendProvince':(None,str(sendProvince)),
                'sendCity': (None, str(sendCity)),
                'sendDistrict':  (None, str(sendDistrict)),
                'arriveProvince':(None,str(arriveProvince)),
                'arriveCity':(None,str(arriveCity)),
                'arriveDistrict': (None,str(arriveDistrict)),
                #金额
                'income': (None, str(income)),
                'totalAmt':(None,str(totalAmt)),
                'preAmt':(None,str(preAmt)),
                'oilAmt':(None,str(oilAmt)),
                'destAmt':(None,str(destAmt)),
                'lastAmt':(None,str(lastAmt)),
                'hasReceipt': (None, str(hasReceipt)),
                'content':(None,str(content)),#备注
                #货物信息(拓展属性）
                'cargoName': (None, str(cargoName)),
                'cargoWeight':(None,str(cargoWeight)),
                'cargoVolume':(None,str(cargoVolume)),
                'cargoNumberOfCases':(None,str(cargoNumberOfCases)),
                'cargoWorth':(None,str(cargoWorth)),
                'insuranceCosts':(None,str(insuranceCosts)),
                #拓展属性
                'handlingFee': (None, str(handlingFee)), #/ 装卸费
                'deliveryFee': (None, str(deliveryFee)),# 送货费
                'oilCardDeposit': (None, str(oilCardDeposit)), # 油卡押金
                'otherFee': (None, str(otherFee)), # 其他费用
                'upWayBillId': (None, str(upWayBillId)),  # 订单号
                'oilCardNo': (None, str(oilCardNo)),  # 油卡卡号
                'vehicleIdNo': (None, str(vehicleIdNo)), # 车架号
                'driverCardNo': (None, str(driverCardNo)), # 司机银行卡号
            #    'depositBank': (None, str(depositBank)), # 开户行
            #    'accountName': (None, str(accountName)) # 账户名称
            }
            response = HttpClient().post_multipart(self.__createWayBillApiUrl,files,self.__head_dict)
            return response
        except Exception:
            return None