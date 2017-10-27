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
from interface.driver.driver_bank_VIN_get import DriverBankVINGet
from bvt.common.create_project import CreateProject
from bvt.common.create_driver import CreateDriver


class CreateWayBill(object):
    '''我要录单'''

    def __init__(self):
        self.logger = Log()

    def create_waybill(self, carType, applyDate, photoAirWay,
                       sendProvince, sendCity, sendDistrict, arriveProvince, arriveCity, arriveDistrict,
                       income, totalAmt, preAmt, oilAmt, destAmt, lastAmt, hasReceipt, content, source,
                       cargoName, cargoWeight, cargoVolume, cargoNumberOfCases, cargoWorth, insuranceCosts,
                       handlingFee, deliveryFee, oilCardDeposit, otherFee, upWayBillId, oilCardNo, vehicleIdNo,
                       driverCardNo,depositBank, accountName,
                       projectName, startTime, endTime, customerName, customerCode, phone, customerDeveloper,  # 新建项目
                       name, mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard, photoTransPort, carNo,
                       carLength, carModel, carLoad,  # 新建外请车
                       ):

        '''我要录单'''

        # 选择项目
        project_list = ProjectSelect().project_select(rows='1000',projectStatus='1').json()['content']['dataList']
        if project_list == []:
            projectId = CreateProject().create_project(projectName,startTime,endTime,customerName,customerCode,phone,
                                                       customerDeveloper)
            self.project = {'projectId':projectId, 'projectName':projectName}
            self.logger.info('新建的项目是: {0}'.format(self.project))
        else:
            self.project = random.sample(project_list, 1)[0]
            self.logger.info('选择的项目是: {0}'.format(self.project))

        # 选择供应商
        supplier_list = SupplierSelect().supplier_select(rows='1000').json()['content']['dataList']
        if supplier_list == []:
            self.supplier = {'name':None,'supplierId':None}
        else:
            self.supplier = random.sample(supplier_list, 1)[0]
            self.logger.info('选择的供应商是: {0}'.format(self.supplier))

        #创建运单
        try:
            #选择公司车
            if carType == '1':
               # 选择司机
               my_car_list = MyCarSelect().my_car_select(rows='1000').json()['content']['dataList']
               if my_car_list == []:
                   self.my_car = None
                   self.logger.info('My car list is empty')
               else:
                   self.my_car = random.sample(my_car_list, 1)[0]
                   self.logger.info('选择的司机是: {0}'.format(self.my_car))
               # 选择车辆
               my_driver_list = MyDriverSelect().my_driver_select(rows='1000').json()['content']['dataList']
               if my_driver_list == []:
                   self.my_driver = None
                   self.logger.info('My driver list is empty')
               else:
                   self.my_driver = random.sample(my_driver_list, 1)[0]
                   self.logger.info('选择的车辆是: {0}'.format(self.my_driver))

               if ((self.my_driver != None) and (self.my_car != None)):
                   response = WayBillCreate().waybill_create(carType,applyDate,
                                                                 self.project['projectName'],self.project['projectId'],
                                                                 self.supplier['name'], self.supplier['supplierId'],
                                                                 self.my_driver['name'],self.my_driver['idNo'],
                                                                 self.my_driver['mobile'],self.my_car['carNo'],
                                                                 self.my_car['carLength'],self.my_car['carModel'],
                                                                 photoAirWay,'',sendProvince, sendCity, sendDistrict,
                                                                 arriveProvince, arriveCity, arriveDistrict,
                                                                 income, totalAmt, preAmt, oilAmt, destAmt, lastAmt,
                                                                 hasReceipt,content,source,
                                                                 cargoName, cargoWeight, cargoVolume,
                                                                 cargoNumberOfCases, cargoWorth, insuranceCosts,
                                                                 handlingFee, deliveryFee, oilCardDeposit,
                                                                 otherFee, upWayBillId, oilCardNo,vehicleIdNo,
                                                                 driverCardNo,depositBank,accountName,
                                                                 )

                   if  response.json()['code'] == 0:
                       return response.json()['content'], self.my_driver['mobile'], self.my_driver['name'],\
                              self.my_driver['idNo'], self.my_car['carNo'], self.my_car['carLength'], \
                              self.my_car['carModel'], self.project['projectName'], self.project['projectId'],\
                              self.supplier['name'], self.supplier['supplierId']
                   elif response.json()['code'] == 9040104 and response.json()['msg']== \
                           '此手机号已有未确认的订单,不可重复提交，请发车确认后再录单':
                       waybill = WayBillSelect().waybill_select(billStatus='W',
                                                                normalCondition=self.my_driver['mobile'],
                                                                searchStatus=True).json()['content']['dataList']
                       WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
                       self.waybillId =  WayBillCreate().waybill_create(carType,applyDate,
                                                                 self.project['projectName'],self.project['projectId'],
                                                                 self.supplier['name'], self.supplier['supplierId'],
                                                                 self.my_driver['name'],self.my_driver['idNo'],
                                                                 self.my_driver['mobile'],self.my_car['carNo'],
                                                                 self.my_car['carLength'],self.my_car['carModel'],
                                                                 photoAirWay,'',sendProvince, sendCity, sendDistrict,
                                                                 arriveProvince, arriveCity, arriveDistrict,
                                                                 income, totalAmt, preAmt, oilAmt, destAmt, lastAmt,
                                                                 hasReceipt,content,source,
                                                                 cargoName, cargoWeight, cargoVolume,
                                                                 cargoNumberOfCases, cargoWorth, insuranceCosts,
                                                                 handlingFee, deliveryFee, oilCardDeposit,
                                                                 otherFee, upWayBillId, oilCardNo,vehicleIdNo,
                                                                 driverCardNo,depositBank,accountName,
                                                                 ).json()['content']
                       return self.waybillId, self.my_driver['mobile'], self.my_driver['name'],\
                              self.my_driver['idNo'], self.my_car['carNo'], self.my_car['carLength'], \
                              self.my_car['carModel'], self.project['projectName'], self.project['projectId'],\
                              self.supplier['name'], self.supplier['supplierId']
                   else:
                       self.logger.info("Failed to create the public waybill module")
                       return None, None, None, None, None,None,None,None,None,None,None

            elif carType == '2':
                # 选择外请车
                driver_list = DriverSelect().driver_select().json()['content']
                if driver_list == []:
                    loginId, Id = CreateDriver().create_driver(name, mobile, idNo, photoIdFront, photoIdReserve,
                                                               photoDriverCard,
                                                               photoTransPort, carNo, carLength, carModel, carLoad)
                    self.driver = {'loginId': loginId, 'name': name, 'idNo': idNo, 'mobile': mobile, 'carNo': carNo,
                                   'carLength': carLength, 'carModel': carModel}
                else:
                    self.driver = random.sample(driver_list, 1)[0]
                    self.logger.info('选择的外请车是: {0}'.format(self.driver))

                #获取银行卡号和车架号
                driver_info = DriverBankVINGet().driver_bank_VIN_get(mobile).json()['content']

                response = WayBillCreate().waybill_create(carType, applyDate,
                                                          self.project['projectName'], self.project['projectId'],
                                                          self.supplier['name'], self.supplier['supplierId'],
                                                          self.driver['name'], self.driver['idNo'],
                                                          self.driver['mobile'], self.driver['carNo'],
                                                          self.driver['carLength'], self.driver['carModel'],
                                                          photoAirWay, self.driver['loginId'],
                                                          sendProvince, sendCity, sendDistrict,
                                                          arriveProvince, arriveCity, arriveDistrict,
                                                          income, totalAmt, preAmt, oilAmt, destAmt, lastAmt,
                                                          hasReceipt, content, source,
                                                          cargoName, cargoWeight, cargoVolume,
                                                          cargoNumberOfCases, cargoWorth, insuranceCosts,
                                                          handlingFee, deliveryFee, oilCardDeposit,
                                                          otherFee, upWayBillId, oilCardNo, driver_info['vehicleIdNo'],
                                                          driver_info['cardNo'],driver_info['driverCardBank'],
                                                          driver_info['accountName'],
                                                          )
                if response.json()['code'] == 0:
                    return response.json()['content'], self.driver['mobile'],self.driver['name'],\
                           self.driver['idNo'],self.driver['carNo'],self.driver['carLength'], self.driver['carModel'],\
                           self.project['projectName'], self.project['projectId'], \
                           self.supplier['name'], self.supplier['supplierId']

                elif response.json()['code'] == 9040104 and response.json()['msg'] ==\
                        '此手机号已有未确认的订单,不可重复提交，请发车确认后再录单':
                    waybill = WayBillSelect().waybill_select(billStatus='W',
                                                             normalCondition=self.driver['mobile'],
                                                             searchStatus=True).json()['content']['dataList']
                    WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
                    self.waybillId = WayBillCreate().waybill_create(carType, applyDate,
                                                          self.project['projectName'], self.project['projectId'],
                                                          self.supplier['name'], self.supplier['supplierId'],
                                                          self.driver['name'], self.driver['idNo'],
                                                          self.driver['mobile'], self.driver['carNo'],
                                                          self.driver['carLength'], self.driver['carModel'],
                                                          photoAirWay, self.driver['loginId'],
                                                          sendProvince, sendCity, sendDistrict,
                                                          arriveProvince, arriveCity, arriveDistrict,
                                                          income, totalAmt, preAmt, oilAmt, destAmt, lastAmt,
                                                          hasReceipt, content, source,
                                                          cargoName, cargoWeight, cargoVolume,
                                                          cargoNumberOfCases, cargoWorth, insuranceCosts,
                                                          handlingFee, deliveryFee, oilCardDeposit,
                                                          otherFee, upWayBillId, oilCardNo, driver_info['vehicleIdNo'],
                                                          driver_info['cardNo'],driver_info['driverCardBank'],
                                                          driver_info['accountName'],
                                                          ).json()['content']
                    return self.waybillId, self.driver['mobile'],self.driver['name'],\
                           self.driver['idNo'],self.driver['carNo'],self.driver['carLength'], self.driver['carModel'],\
                           self.project['projectName'], self.project['projectId'], \
                           self.supplier['name'], self.supplier['supplierId']
                else:
                    self.logger.info("Failed to create the public waybill module")
                    return None, None, None, None, None, None, None, None, None, None, None
            else:
                self.logger.error('外请车类型错误: {0}'.format(carType))
                return None, None, None, None, None, None, None, None, None, None, None
        except Exception:
            return None