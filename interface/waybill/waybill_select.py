#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillSelect(object):
    '''
    运单查询
    /api/tms/wayBill/wayBillList
    '''
    __slots__ = ('__selectWayBillApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__selectWayBillApiUrl = "https://{0}:{1}{2}/api/tms/wayBill/wayBillList".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_select(self,currentPage='1',rows='10',billStatus='',name='', mobile='',carType='',carNo='',
                       sendCity='',arriveCity='',applyDateFirst='',applyDateLast='',shipperInsertTimeFirst='',
                       shipperInsertTimeLast='',needAccount='false',normalCondition='',searchStatus='false'):
         '''查询运单'''
         try:
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
             response = HttpClient().get(self.__selectWayBillApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('运单查询发生异常:{0}'.format(e))
             return None


if __name__ == '__main__':
    test = WayBillSelect().waybill_select(billStatus='W', normalCondition='18056070532', searchStatus='true')
    print(test.json()['content']['dataList'])




