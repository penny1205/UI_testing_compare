#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import os
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
from util.config.yaml.readyaml import ReadYaml
from interface.waybill.waybill_create import WayBillCreate
from interface.waybill.waybill_select import WayBillSelect
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_temp_import import WayBillTempImport
from interface.project.project_select import ProjectSelect
from interface.driver.mycar_select import MyCarSelect
from interface.driver.mydriver_select import MyDriverSelect
from interface.driver.driver_mobile_select import DriverMobileSelect
from interface.driver.driver_select import DriverSelect
from interface.driver.supplier_select import SupplierSelect
from interface.driver.driver_bank_VIN_get import DriverBankVINGet
from bvt.common.create_project import CreateProject
from bvt.common.create_supplier import CreateSupplier
from bvt.common.create_driver import CreateDriver
from bvt.common.create_mydriver import CreateMyDriver
from bvt.common.create_mycar import CreateMyCar



class CreateWayBill(object):
    '''我要录单'''
    def __init__(self):
        self.logger = Log()

    @staticmethod
    def my_print(msg):
        logger = Log()
        logger.info(msg)

    # 选择项目
    @staticmethod
    def project_choice(projectName='德邦物流', customerName='德邦集团', customerCode='DB20171101100',
                       phone='13077327043' , customerDeveloper='张经理'):
        project_list = ProjectSelect().project_select(rows='1000', projectStatus='1').json()['content']['dataList']
        if project_list == []:
            startTime = time.strftime('%Y-%m-%d')
            endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 2592000))
            projectId = CreateProject().create_project(projectName, startTime, endTime, customerName, customerCode,
                                                       phone,customerDeveloper)
            project = {'projectId': projectId, 'projectName': projectName}
            CreateWayBill.my_print('新建的项目名称是: {0}'.format(project['projectName']))
        else:
            project = random.sample(project_list, 1)[0]
            CreateWayBill.my_print('选择的项目名称是: {0}'.format(project['projectName']))
        return project

    # 选择指定项目
    @staticmethod
    def project_one_choice(projectName, startTime, endTime, customerName, customerCode, phone , customerDeveloper):
        project_list = ProjectSelect().project_select(rows='1000', projectStatus='1').json()['content']['dataList']
        if project_list != []:
            L = []
            for project in project_list:
                if project['projectName'] == projectName:
                    L.append(project['projectName'])
                    return project
            if len(L) == 0:
                projectId = CreateProject().create_project(projectName, startTime, endTime, customerName, customerCode,
                                                           phone,customerDeveloper)
                project = {'projectId': projectId, 'projectName': projectName}
                return project
        else:
            projectId = CreateProject().create_project(projectName, startTime, endTime, customerName,customerCode,
                                                       phone, customerDeveloper)
            project = {'projectId': projectId, 'projectName': projectName}
            return project

    #选择供应商
    @staticmethod
    def supplier_choice( name='哇哈哈', type='1', contactPersonName='李经理'):
        supplier_list = SupplierSelect().supplier_select(rows='1000').json()['content']['dataList']
        if supplier_list == []:
            contactPersonMobile = DataUtil().createmoble()
            contactPersonIdNo = DataUtil().genneratorIdNo()
            contactPersonIdCardPhoto = "http://yudian.ufile.ucloud.com.cn/18d4d203-3712-43c7-93d9-9b791aa4806d.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=CGRGouKFXGdBh3aI4+gK+nA5XmU="
            businessLicencePhoto = "http://yudian.ufile.ucloud.com.cn/9503b68e-6e0b-40df-b30f-c7af545da878.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=42hC+hmiXMNbRIoR8H4wipW0SI8="
            businessPermitPhoto = "http://yudian.ufile.ucloud.com.cn/8539002d-b90f-4a1a-b19c-22b2135cbf6b.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=hwTz+Pk8yffBXUwEbgSsoVU9QT4="
            taxRegistrationCertificatePhoto = "http://yudian.ufile.ucloud.com.cn/b117b5e1-e4d5-47f6-8e81-50bb344c3896.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=4+YLofibFNAqF1PhOFoNSqu4CN4="
            contractPhoto = "http://yudian.ufile.ucloud.com.cn/b2098698-56e7-425e-9186-61dbb966310a.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=IknyOZi+hHvHpyajfp8HI3aANqA="
            supplierId = CreateSupplier().create_supplier(name,type,contactPersonName,contactPersonMobile,contactPersonIdNo,
                        contactPersonIdCardPhoto,businessLicencePhoto,businessPermitPhoto,
                        taxRegistrationCertificatePhoto,contractPhoto)
            supplier = {'name': name, 'supplierId': supplierId}
            CreateWayBill.my_print('新建的供应商名称是: {0}'.format(supplier['supplier']))
        else:
            supplier = random.sample(supplier_list, 1)[0]
            CreateWayBill.my_print('选择的供应商名称是: {0}'.format(supplier['supplier']))
        return supplier

    # 选择司机
    @staticmethod
    def driver_choice( name = '王师傅'):
        driver_list = MyDriverSelect().my_driver_select(rows='1000').json()['content']['dataList']
        if driver_list == []:
            mobile = DataUtil().createmoble()
            idNo = DataUtil().genneratorIdNo()
            photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
            frontIdCard = 'http://yudian.ufile.ucloud.com.cn/df03e2a2-6751-488e-9f1f-ec60a1da49fa.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=b3XzoIcs67/0D6ZExdG0fWbjUzc='
            backIdCard = 'http://yudian.ufile.ucloud.com.cn/4acb87e0-8c0d-44a9-a1b3-b8cb7ca103d1.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=XfbOAUgpkjIe1FJU/hxiMqfsWno='
            CreateMyDriver().create_my_driver(mobile,name,idNo,photoDriverCard,frontIdCard,backIdCard)
            driver = {'name': name, 'idNo': idNo, 'mobile': mobile,}
            CreateWayBill.my_print('新建的司机手机号是: {0}'.format(driver['mobile']))
        else:
            driver = random.sample(driver_list, 1)[0]
            CreateWayBill.my_print('选择的司机手机号是: {0}'.format(driver['mobile']))
        return driver

    # 选择车辆
    @staticmethod
    def car_choice(carLoad='10',carAge='',carBrand='长城'):
        car_list = MyCarSelect().my_car_select(rows='1000').json()['content']['dataList']
        if car_list == []:
            carNo = DataUtil().genneratorCarNo()
            carModel = DataUtil().genneratorCarTypeInfo()
            carLength = DataUtil().genneratorCarLength()
            buycarTime = time.strftime('%Y-%m-%d')
            photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
            photoCar = 'http://yudian.ufile.ucloud.com.cn/69eec140-f95d-4af7-9aaf-c57b8442d799.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=bPzioEVJ8i4E3iXi+Yx7KQSeHvw='
            CreateMyCar().create_my_car(carNo,carModel,carLength,carLoad,carAge,buycarTime,carBrand,photoDriverCard,photoCar)
            car = { 'carNo': carNo, 'carLength': carLength, 'carModel': carModel}
            CreateWayBill.my_print('新建的车牌号是: {0}'.format(car['carNo']))
        else:
            car = random.sample(car_list, 1)[0]
            CreateWayBill.my_print('选择的车牌号是: {0}'.format(car['carNo']))
        return car

    #选择外请车
    @staticmethod
    def outCar_choice(name='张三三',carLoad='10'):
        outCar_list = DriverSelect().driver_select().json()['content']
        if outCar_list == []:
            mobile = DataUtil().createmoble()
            idNo = DataUtil().genneratorIdNo()
            carNo = DataUtil().genneratorCarNo()
            carLength = DataUtil().genneratorCarLength()
            carModel = DataUtil().genneratorCarTypeInfo()
            photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
            photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
            photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
            photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'
            loginId, Id = CreateDriver().create_driver(name, mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard,
                                                       photoTransPort, carNo, carLength, carModel, carLoad)
            outCar = {'loginId': loginId, 'name': name, 'idNo': idNo, 'mobile': mobile, 'carNo': carNo,
                           'carLength': carLength, 'carModel': carModel}
        else:
            outCar = random.sample(outCar_list, 1)[0]
            CreateWayBill.my_print('选择的外请车车牌号是: {0}'.format(outCar['carNo']))
        return outCar

    #创建运单
    def create_waybill(self,carType, applyDate, photoAirWay,sendProvince, sendCity, sendDistrict,arriveProvince,
            arriveCity, arriveDistrict,income, totalAmt, preAmt, oilAmt, destAmt, lastAmt,hasReceipt, content, source,
            cargoName, cargoWeight, cargoVolume,cargoNumberOfCases, cargoWorth, insuranceCosts, handlingFee, deliveryFee,
            oilCardDeposit,otherFee, upWayBillId, oilCardNo, vehicleIdNo,driverCardNo, depositBank, accountName):
        try:
            project = CreateWayBill().project_choice()
            supplier = CreateWayBill().supplier_choice()
            if carType == '1':
                car = CreateWayBill.car_choice()
                driver = CreateWayBill.driver_choice()
                response = WayBillCreate().waybill_create(carType, applyDate, project['projectName'], project['projectId'],
                                                      supplier['name'], supplier['supplierId'], driver['name'],
                                                      driver['idNo'], driver['mobile'], car['carNo'], car['carLength'],
                                                      car['carModel'], photoAirWay, '', sendProvince, sendCity,
                                                      sendDistrict, arriveProvince, arriveCity, arriveDistrict, income,
                                                      totalAmt, preAmt, oilAmt, destAmt, lastAmt, hasReceipt, content,
                                                      source, cargoName, cargoWeight, cargoVolume, cargoNumberOfCases,
                                                      cargoWorth, insuranceCosts, handlingFee, deliveryFee,
                                                      oilCardDeposit, otherFee, upWayBillId, oilCardNo, '','', '', '')
                if response.json()['code'] == 0:
                    return response.json()['content'],driver['mobile'],driver['name'],driver['idNo'],car['carNo'],\
                           car['carLength'],car['carModel'],project['projectName'],project['projectId'],\
                           supplier['name'], supplier['supplierId']

                elif response.json()['code'] == 9040104 and response.json()['msg'] == \
                        '此手机号已有未确认的订单,不可重复提交，请发车确认后再录单':
                    waybill = WayBillSelect().waybill_select(billStatus='W', normalCondition=driver['mobile'],
                                                             searchStatus=True).json()['content']['dataList']
                    WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
                    waybillId = WayBillCreate().waybill_create(carType, applyDate, project['projectName'],
                                                               project['projectId'],supplier['name'],
                                                               supplier['supplierId'], driver['name'],
                                                      driver['idNo'], driver['mobile'], car['carNo'], car['carLength'],
                                                      car['carModel'], photoAirWay, '', sendProvince, sendCity,
                                                      sendDistrict, arriveProvince, arriveCity, arriveDistrict, income,
                                                      totalAmt, preAmt, oilAmt, destAmt, lastAmt, hasReceipt, content,
                                                      source, cargoName, cargoWeight, cargoVolume, cargoNumberOfCases,
                                                      cargoWorth, insuranceCosts, handlingFee, deliveryFee,
                                                      oilCardDeposit, otherFee, upWayBillId, oilCardNo, '','', '', ''
                                                               ).json()['content']
                    return waybillId,driver['mobile'],driver['mobile'],driver['name'],driver['idNo'],car['carNo'],\
                           car['carLength'],car['carModel'],project['projectName'],project['projectId'],\
                           supplier['name'],supplier['supplierId']

                else:
                    self.logger.info("创建运单公共模块失败!")
                    return None, None, None, None, None, None, None, None, None, None, None

            elif  carType == '2':
                outCar = CreateWayBill().outCar_choice()
                driver_info = DriverBankVINGet().driver_bank_VIN_get(outCar['mobile'], ).json()['content']
                response = WayBillCreate().waybill_create(carType, applyDate, project['projectName'], project['projectId'],
                                                      supplier['name'], supplier['supplierId'], outCar['name'],
                                                      outCar['idNo'], outCar['mobile'], outCar['carNo'],
                                                      outCar['carLength'], outCar['carModel'], photoAirWay,
                                                      outCar['loginId'], sendProvince, sendCity, sendDistrict,
                                                      arriveProvince, arriveCity, arriveDistrict, income, totalAmt,
                                                      preAmt, oilAmt, destAmt, lastAmt, hasReceipt, content, source,
                                                      cargoName, cargoWeight, cargoVolume, cargoNumberOfCases,
                                                      cargoWorth, insuranceCosts, handlingFee, deliveryFee,
                                                      oilCardDeposit, otherFee, upWayBillId, oilCardNo,
                                                      driver_info['vehicleIdNo'], driver_info['cardNo'],
                                                      driver_info['driverCardBank'],driver_info['accountName'])
                if response.json()['code'] == 0:
                    return response.json()['content'],outCar['mobile'],outCar['name'],outCar['idNo'],outCar['carNo'],\
                           outCar['carLength'],outCar['carModel'],project['projectName'], project['projectId'],\
                           supplier['name'], supplier['supplierId']

                elif response.json()['code'] == 9040104 and response.json()['msg'] ==\
                          '此手机号已有未确认的订单,不可重复提交，请发车确认后再录单':
                    waybill = WayBillSelect().waybill_select(billStatus='W',normalCondition=outCar['mobile'],
                                                             searchStatus=True).json()['content']['dataList']
                    WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
                    waybillId = WayBillCreate().waybill_create(carType, applyDate, project['projectName'],
                                                           project['projectId'],supplier['name'],supplier['supplierId'],
                                                           outCar['name'],outCar['idNo'], outCar['mobile'], outCar['carNo'],
                                                           outCar['carLength'], outCar['carModel'], photoAirWay,
                                                           outCar['loginId'], sendProvince, sendCity, sendDistrict,
                                                           arriveProvince, arriveCity, arriveDistrict, income, totalAmt,
                                                           preAmt, oilAmt, destAmt, lastAmt, hasReceipt, content, source,
                                                           cargoName, cargoWeight, cargoVolume, cargoNumberOfCases,
                                                           cargoWorth, insuranceCosts, handlingFee, deliveryFee,
                                                           oilCardDeposit, otherFee, upWayBillId, oilCardNo,
                                                           driver_info['vehicleIdNo'], driver_info['cardNo'],
                                                           driver_info['driverCardBank'],driver_info['accountName']
                                                           ).json()['content']
                    return waybillId, outCar['mobile'],outCar['name'],outCar['idNo'],outCar['carNo'],outCar['carLength'],\
                           outCar['carModel'],project['projectName'], project['projectId'],supplier['name'], \
                           supplier['supplierId']
                else:
                    self.logger.info("Failed to create the public waybill module")
                    return None, None, None, None, None, None, None, None, None, None, None
            else:
                self.logger.error('外请车类型错误: {0}'.format(carType))
                return None, None, None, None, None, None, None, None, None, None, None
        except Exception:
            self.logger.error('新增运单发生异常:{0}'.format(Exception))
            return None

    def create_waybill_register(self, handlingFee='', deliveryFee='', oilCardDeposit='', otherFee=''):
        """ 使用已认证司机新建运单 """
        applyDate = time.strftime('%Y-%m-%d')
        project = CreateWayBill().project_choice()
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        mobile_certificate = config['mobile_certificate']
        self.mobile_certificate = random.sample(mobile_certificate, 1)[0]
        # 获取认证司机的信息
        try:
            driver = DriverMobileSelect().driver_mobile_select(self.mobile_certificate).json()
            self.logger.info('获取已认证司机信息：{0}'.format(driver))
            driver = driver['content'][0]
        except Exception as error:
            print(error)
            self.logger.info('获取认证司机信息失败,错误信息：{0}'.format(error))
            return None
        # 查询认证司机是否有待发车状态的运单并处理
        waybill = WayBillSelect().waybill_select(billStatus='W',normalCondition=driver['mobile'],
                                                 searchStatus='true').json()['content']['dataList']
        if waybill:
            WayBillDepartureConfirm().waybill_departure_confirm(waybill[0]['id'])
        try:
            response = WayBillCreate().waybill_create(applyDate=applyDate, sendCity='天津', sendProvince='天津',
                                                      arriveCity='北京', arriveProvince='北京', totalAmt='0.05',
                                                      preAmt='0.01', oilAmt='0.01', destAmt='0.01', lastAmt='0.01',
                                                      projectId=project['projectId'], projects=project['projectName'],
                                                      carType='2', carNo=driver['carNo'], realName=driver['name'],
                                                      carLength=driver['carLength'], carModel=driver['carModel'],
                                                      mobile=driver['mobile'], hasReceipt='1', handlingFee=handlingFee,
                                                      deliveryFee=deliveryFee, oilCardDeposit=oilCardDeposit,
                                                      otherFee=otherFee)
            self.logger.info('新建运单返回信息：{}'.format(response.json()))
            return response
        except Exception as e:
            self.logger.error('新增运单发生异常:{0}'.format(e))
            return None

    def create_temp_waybill(self, file, projectName, customerName, customerCode,
                            phone='130773271234', customerDeveloper='张经理'):
        '''批量录单 导入运单'''
        startTime = time.strftime('%Y-%m-%d')
        endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 2592000))
        try:
            project = self.project_one_choice(projectName, startTime, endTime, customerName, customerCode, phone,
                                              customerDeveloper)
            response = WayBillTempImport().waybill_temp_import(file)
            if response.json()['code'] == 0:
                temp_waybillId = response.json()['content']
                return temp_waybillId
            else:
                self.logger.error('批量导入运单报错:{0}'.format(response.json()))
                return None
        except Exception as e:
            self.logger.error('批量导入运单发生异常:{0}'.format(e))
            return None


if __name__ == "__main__":
    i = 0
    # while i < 21:
    test = CreateWayBill().create_waybill_register()
    print(test.json())
        # i += 1

