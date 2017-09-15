#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.waybill.waybill_create import WayBillCreate
from interface.waybill.waybill_select import WayBillSelect
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.project.project_select import ProjectSelect
from interface.driver.mycar_select import MyCarSelect
from interface.driver.mydriver_select import MyDriverSelect
from interface.driver.driver_select import DriverSelect
from interface.driver.supplier_select import SupplierSelect


class CreateWayBill(object):
    '''我要录单'''

    def __init__(self):
        self.logger = Log()

    def create_waybill(self,carType,applyDate,sendProvince,sendCity,arriveProvince,arriveCity,
                       income,totalAmt,preAmt,oilAmt,destAmt,lastAmt,hasReceipt,content,source,
                       cargoName,cargoWeight,cargoVolume,cargoNumberOfCases,cargoWorth,insuranceCosts):
        '''我要录单'''

        # 获取项目列表
        project_list = ProjectSelect().driver_select(rows='1000').json()['content']['dataList']
        if project_list == []:
            self.project['projectId'] = '0'
            self.project['projectName'] = '其他'
        else:
            self.project = random.sample(project_list, 1)[0]
            self.logger.info('选择的项目是: {0}'.format(self.project))

        # 获取供应商列表
        supplier_list = SupplierSelect().supplier_select(rows='1000').json()['content']['dataList']
        if supplier_list == []:
            self.supplier['name'] = None
            self.supplier['supplierId'] = None
        else:
            self.supplier = random.sample(supplier_list, 1)[0]
            self.logger.info('选择的供应商是: {0}'.format(self.supplier))

        try:
            if carType == '1':
               #公司车
               # 获取我的司机
               my_car_list = MyCarSelect().my_car_select(rows='1000').json()['content']['dataList']
               if my_car_list == []:
                   self.my_car = None
                   self.logger.info('My car list is empty')
               else:
                   self.my_car = random.sample(my_car_list, 1)[0]
                   self.logger.info('选择的司机是: {0}'.format(self.my_car))

               # 获取我的车辆
               my_driver_list = MyDriverSelect().my_driver_select(rows='1000').json()['content']['dataList']
               if my_driver_list == []:
                   self.my_driver = None
                   self.logger.info('My driver list is empty')
               else:
                   self.my_driver = random.sample(my_driver_list, 1)[0]
                   self.logger.info('选择的车辆是: {0}'.format(self.my_driver))

               if ((self.my_driver != None) and (self.my_car != None)):
                   self.waybill = WayBillCreate().waybill_create(
                       carType=carType, applyDate=applyDate, projects=self.project['projectName'],
                       projectId=self.project['projectId'],
                       realName=self.my_driver['name'], idNo=self.my_driver['idNo'],
                       mobile=self.my_driver['mobile'], carNo=self.my_car['carNo'],
                       sendProvince=sendProvince, sendCity=sendCity, arriveProvince=arriveProvince,
                       arriveCity=arriveCity,
                       income=income, totalAmt=totalAmt, preAmt=preAmt, oilAmt=oilAmt, destAmt=destAmt, lastAmt=lastAmt,
                       hasReceipt=hasReceipt,
                       supplierName=self.supplier['name'], supplierId=self.supplier['supplierId'], content=content,
                       source=source,
                       cargoName=cargoName, cargoWeight=cargoWeight, cargoVolume=cargoVolume,
                       cargoNumberOfCases=cargoNumberOfCases, cargoWorth=cargoWorth, insuranceCosts=insuranceCosts
                   ).json()['content']

                   # 判断手机号是否存在未发车的订单
                   if self.waybill == None:
                       # 【发车确认】按手机号查询订单，获取该订单号调用发车确认接口
                       waybill = WayBillSelect().waybill_select(billStatus='W', normalCondition=self.my_driver['mobile'],
                                                                searchStatus=True).json()['content']['dataList']
                       WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
                       self.waybill = WayBillCreate().waybill_create(
                           carType=carType, applyDate=applyDate, projects=self.project['projectName'],
                           projectId=self.project['projectId'],
                           realName=self.my_driver['name'], idNo=self.my_driver['idNo'],
                           mobile=self.my_driver['mobile'], carNo=self.my_car['carNo'],
                           sendProvince=sendProvince, sendCity=sendCity, arriveProvince=arriveProvince,
                           arriveCity=arriveCity,
                           income=income, totalAmt=totalAmt, preAmt=preAmt, oilAmt=oilAmt, destAmt=destAmt,
                           lastAmt=lastAmt,
                           hasReceipt=hasReceipt,
                           supplierName=self.supplier['name'], supplierId=self.supplier['supplierId'], content=content,
                           source=source,
                           cargoName=cargoName, cargoWeight=cargoWeight, cargoVolume=cargoVolume,
                           cargoNumberOfCases=cargoNumberOfCases, cargoWorth=cargoWorth, insuranceCosts=insuranceCosts
                       ).json()['content']
                       return self.waybill, self.my_driver['mobile'],self.my_driver['name'],\
                              self.my_driver['idNo'],self.my_car['carNo']
                   else:
                       return self.waybill, self.my_driver['mobile'],self.my_driver['name'],\
                              self.my_driver['idNo'],self.my_car['carNo']

            elif carType == '2':
                #外请车
                # 获取我的外请车列表
                driver_list = DriverSelect().driver_select(rows='1000').json()['content']['dataList']
                if driver_list == []:
                    self.driver = None
                    self.logger.info('My outside driver list is empty')
                else:
                    self.driver = random.sample(driver_list, 1)[0]
                    self.logger.info('选择的外请车是: {0}'.format(self.driver))

                if self.driver !=None:
                    self.waybill = WayBillCreate().waybill_create(
                        carType=carType, applyDate=applyDate, projects=self.project['projectName'],
                        projectId=self.project['projectId'],
                        loginId=self.driver['loginId'], realName=self.driver['name'], idNo=self.driver['idNo'],
                        mobile=self.driver['mobile'], carNo=self.driver['carNo'],
                        sendProvince=sendProvince, sendCity=sendCity, arriveProvince=arriveProvince,
                        arriveCity=arriveCity,
                        income=income, totalAmt=totalAmt, preAmt=preAmt, oilAmt=oilAmt, destAmt=destAmt,
                        lastAmt=lastAmt, hasReceipt=hasReceipt,
                        supplierName=self.supplier['name'], supplierId=self.supplier['supplierId'], content=content,
                        source=source,
                        cargoName=cargoName, cargoWeight=cargoWeight, cargoVolume=cargoVolume,
                        cargoNumberOfCases=cargoNumberOfCases, cargoWorth=cargoWorth, insuranceCosts=insuranceCosts
                    ).json()['content']

                    # 判断手机号是否存在未发车的订单
                    if self.waybill == None:
                        # 【发车确认】按手机号查询订单，获取该订单号调用发车确认接口
                        waybill = WayBillSelect().waybill_select(billStatus='W', normalCondition=self.driver['mobile'],
                                                                 searchStatus=True).json()['content']['dataList']
                        WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
                        self.waybill = WayBillCreate().waybill_create(
                            carType=carType, applyDate=applyDate, projects=self.project['projectName'],
                            projectId=self.project['projectId'],
                            loginId=self.driver['loginId'], realName=self.driver['name'], idNo=self.driver['idNo'],
                            mobile=self.driver['mobile'], carNo=self.driver['carNo'],
                            sendProvince=sendProvince, sendCity=sendCity, arriveProvince=arriveProvince,
                            arriveCity=arriveCity,
                            income=income, totalAmt=totalAmt, preAmt=preAmt, oilAmt=oilAmt, destAmt=destAmt,
                            lastAmt=lastAmt, hasReceipt=hasReceipt,
                            supplierName=self.supplier['name'], supplierId=self.supplier['supplierId'], content=content,
                            source=source,
                            cargoName=cargoName, cargoWeight=cargoWeight, cargoVolume=cargoVolume,
                            cargoNumberOfCases=cargoNumberOfCases, cargoWorth=cargoWorth, insuranceCosts=insuranceCosts
                        ).json()['content']
                        return self.waybill,self.driver['mobile'],self.driver['name'],\
                               self.driver['idNo'],self.driver['carNo'],
                    else:
                        return self.waybill,self.driver['mobile'],self.driver['name'],\
                               self.driver['idNo'],self.driver['carNo'],
            else:
                self.logger.error('外请车类型错误: {0}'.format(carType))
                return None,None
        except Exception:
            return None