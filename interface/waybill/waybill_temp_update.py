#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillTempUpdate(object):
    '''
    根据ID修改临时运单
    /api/tms/tmpWayBill/updateTmpWayBillById
    '''
    __slots__ = ('__wayBillTempUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempUpdateApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/updateTmpWayBillById'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_update(self,wayBillId='',carType='',applyDate='',projects='',projectId='',supplierName='',
                            name='',idNo='',mobile='',carNo='',carLength='',carModel='',
                            sendProvince='',sendCity='',sendDistrict='',arriveProvince='',arriveCity='',arriveDistrict='',
                            income='',feeAmt='',cash='',oilFee='',destAmt='',retAmt='',hasReceipt='',content='',
                            cargoName='',cargoWeight='',cargoVolume='',cargoNumberOfCases='',cargoWorth='',insuranceCosts='',
                            handlingFee='',deliveryFee='',oilCardDeposit='',otherFee='',upWayBillId='',oilCardNo='',
                            vehicleIdNo='',driverCardNo='',depositBank='', accountName=''):
         '''根据ID修改临时运单'''
         try:

             payload = {
                 'id': wayBillId,                        #ID，由后端查询得出，页面不显示；非必填，不填返回该运单不存在
                 'carType': carType,                     # 车型：1:公司车、2：外请车，值只有1,2； 必填
                 'projects': projects,                   # 项目，字符长度20；  必填
                 'projectId': projectId,                 # 项目ID，必填
                 'supplierName': supplierName,           # 供应商，非必填
                 'applyDate': applyDate,                 #用车日期，日期格式为（yyyy-MM-dd）必填
                 'name': name,                           #司机姓名，客户手动输入，长度10； 必填
                 'idNo': idNo,                           # 身份证号，必须为15或者18位字符； 非必填
                 'mobile': mobile,                       #司机手机号，必须为11位数字； 必填
                 'carNo': carNo,                         #车牌号，长度为7位； 必填
                 'carLength':carLength,                  #车长，[4.2,6.8,7.6,9.6,12.5,13.,15.,16,17.5,21,其他]非必填
                 'carModel':carModel,                    #车型，[XIANG_SHI_CHE,GAO_LAN_CHE,PING_BAN_CHE,GAO_DI_BAN_CHE,LENG_CANG_CHE,DA_JIAN_CHE,QI_TA],非必填
                 'sendProvince': sendProvince,           # 出发省，省市联动控件输入 必填
                 'sendCity': sendCity,                   # 出发城市，省市联动控件输入  必填
                 'sendDistrict': sendDistrict,           # 发车区县，省市联动控件输入  非必填
                 'arriveProvince': arriveProvince,       # 到达省，省市联动控件输入 必填
                 'arriveCity': arriveCity,               # 到达城市，省市联动控件输入  必填
                 'arriveDistrict': arriveDistrict,       # 到达区县，省市联动控件输入  非必填
                 'income': income,                       # 发车收入，无小数或小数为2位数字；  非必填
                 'feeAmt': feeAmt,                       # 总金额，无小数或小数为2位数字；  必填
                 'cash': cash,                           # 预付款，无小数或小数为2位数字；  非必填
                 'oilFee': oilFee,                       # 油费，无小数或小数为2位数字；  非必填
                 'destAmt': destAmt,                     # 到付金额，无小数或小数为2位数字；  非必填
                 'retAmt': retAmt,                       # 尾款，无小数或小数为2位数字；   非必填
                 'hasReceipt': hasReceipt,  # 是否有回单 1有 0没有，值只有0,1；  非必填
                 'content': content,                     # 备注，长度为50；   非必填
                 #自定义配置字段
                 'cargoName':cargoName,                  #货物名称，（根据或者配置显示 是否必填）
                 'cargoWeight':cargoWeight,              #货物重量，（根据或者配置显示 是否必填）
                 'cargoVolume':cargoVolume,              #货物体积，（根据或者配置显示 是否必填）
                 'cargoNumberOfCases':cargoNumberOfCases,#货物件数，（根据或者配置显示 是否必填）
                 'cargoWorth':cargoWorth,                #货物价值，（根据或者配置显示 是否必填）
                 'insuranceCosts':insuranceCosts,        #投保费用，（根据或者配置显示 是否必填）
                 'upWayBillId':upWayBillId,              #订单号，（根据或者配置显示 是否必填）
                 'oilCardNo':oilCardNo,                  #油卡卡号，（根据或者配置显示 是否必填）
                 'handlingFee':handlingFee,              #装卸费，（根据或者配置显示）
                 'deliveryFee':deliveryFee,              #送货费，（根据或者配置显示）
                 'oilCardDeposit':oilCardDeposit,        #油卡押金，（根据或者配置显示）
                 'otherFee':otherFee,                    #其他费用，（根据或者配置显示）
                 'vehicleIdNo':vehicleIdNo,              #车架号，（根据或者配置显示 是否必填）
                 'driverCardNo':driverCardNo,            #司机银行卡号，（根据或者配置显示 是否必填）
                 'depositBank': depositBank,
                 'accountName': accountName,
             }
             response = HttpClient().post_json(self.__wayBillTempUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None
