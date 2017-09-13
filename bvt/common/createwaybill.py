#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.waybill.waybill_create import WayBillCreate
from interface.waybill.waybill_select import WayBillSelect
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.project.project_select import ProjectSelect
from interface.driver.driver_select import DriverSelect
from interface.driver.supplier_select import SupplierSelect


class CreateWayBill(object):
    '''我要录单'''

    def __init__(self):
        self.logger = Log()

    def create_waybill(self,carType,applyDate,partnerNo,source,sendProvince,sendCity,arriveProvince,arriveCity,
                       income,totalAmt,preAmt,oilAmt,destAmt,lastAmt,hasReceipt,
                       cargoName,content,cargoWeight,cargoVolume,cargoNumberOfCases,cargoWorth,insuranceCosts):
        '''我要录单  外请车'''

        #获取项目列表
        project_list = ProjectSelect().driver_select(rows='1000')['content']['dataList']
        if project_list == None:
            self.project['projectId'] = '0'
            self.project['projectName'] = '其他'
        else:
            self.project = random.sample(project_list, 1)[0]

        #获取供应商列表
        supplier_list = SupplierSelect().supplier_select(rows='1000')['content']['dataList']
        if supplier_list == None:
            self.supplier['name'] = None
            self.supplier['supplierId'] = None
        else:
            self.supplier = random.sample(supplier_list, 1)[0]
        #获取我的外请车列表
        driver_list = DriverSelect().driver_select(rows='1000', partnerNo=partnerNo)['content']['dataList']
        if driver_list == None:
            self.logger.info('My outside driver list is empty')
        else:
            # 选择一个外请车
            self.driver = random.sample(driver_list, 1)[0]
            self.logger.info('选择的司机是: {0}'.format(self.driver))
            self.waybill = WayBillCreate().waybill_create(
                carType=carType,applyDate=applyDate,projects=self.project['projectName'],projectId= self.project['projectId'],
                partnerNo=partnerNo, loginId=self.driver['loginId'],source=source,
                realName=self.driver['name'],idNo=self.driver['idNo'],mobile=self.driver['mobile'],carNo=self.driver['carNo'],
                sendProvince=sendProvince,sendCity=sendCity,arriveProvince=arriveProvince,arriveCity=arriveCity,
                income=income,totalAmt=totalAmt,preAmt=preAmt,oilAmt=oilAmt,destAmt=destAmt,lastAmt=lastAmt,hasReceipt=hasReceipt,
                supplierName=self.supplier['name'],supplierId=self.supplier['supplierId'],content=content,
                cargoName=cargoName,cargoWeight=cargoWeight,cargoVolume=cargoVolume,
                cargoNumberOfCases=cargoNumberOfCases,cargoWorth=cargoWorth,insuranceCosts=insuranceCosts
            )

        #判断手机号是否存在未发车的订单
        if self.waybill == None :
            #【发车确认】按手机号查询订单，获取该订单号调用发车确认接口
            waybill = WayBillSelect().waybill_select(billStatus='W', normalCondition=self.driver['mobile'],
                                                     searchStatus=True)['content']['dataList']
            WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
            self.waybill = WayBillCreate().waybill_create(
                carType=carType, applyDate=applyDate, projects=self.project['projectName'],projectId=self.project['projectId'],
                partnerNo=partnerNo, loginId=self.driver['loginId'], source=source,
                realName=self.driver['name'], idNo=self.driver['idNo'], mobile=self.driver['mobile'],carNo=self.driver['carNo'],
                sendProvince=sendProvince, sendCity=sendCity, arriveProvince=arriveProvince, arriveCity=arriveCity,
                income=income, totalAmt=totalAmt, preAmt=preAmt, oilAmt=oilAmt, destAmt=destAmt, lastAmt=lastAmt,hasReceipt=hasReceipt,
                supplierName=self.supplier['supplierName'], supplierId=self.project['projectName'], content=content,
                cargoName=cargoName,cargoWeight=cargoWeight, cargoVolume=cargoVolume,
                cargoNumberOfCases=cargoNumberOfCases,cargoWorth=cargoWorth, insuranceCosts=insuranceCosts
            )

            return self.waybill['content'],self.driver['mobile']
        else:
            return self.waybill['content'],self.driver['mobile']