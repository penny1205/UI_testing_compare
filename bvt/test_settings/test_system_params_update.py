#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.settings.system_params_settings_update import SystemParamsSettingsUpdate

class TestSystemParamsUpdate(unittest.TestCase):
    '''更新系统属性配置信息'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSystemParamsUpdate START ###########################')


    def tearDown(self):
        self.logger.info('############################ TestSystemParamsUpdate END ############################')


    # def test_system_params_update_init_success(self):
    #     '''更新系统属性配置信息'''
    #     response = SystemParamsSettingsUpdate().system_params_settings_update(True,True,True,True,True,True,True,True,
    #                                                                           True,True,True,True,True,True,True,True,
    #                                                                           True, True, True, True, True, True, True,
    #                                                                           True, True, True, True, True)
    #     self.logger.info('更新系统属性配置信息返回状态码：{0}'.format(response))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['code'], 0)
    #     self.logger.info('更新系统属性配置信息返回结果是：{0}'.format(response.json()))
    #

    def test_system_params_update_success(self):
        '''更新系统属性配置信息'''
        cargoParamsSet = '{"hasCargoName":true,"cargoNameRequired":true,"hasCargoWeight":true,"cargoWeightRequired":true,"hasCargoVolume":true,"cargoVolumeRequired":true,"hasCargoNumberOfCases":true,"cargoNumberRequired":true,"hasCargocargoWorth":true,"cargoWorthRequired":true,"hasInsuranceCosts":true,"insuranceCostsRequired":true,"hasUpWayBillId":true,"upWayBillIdRequired":true,"hasOilCardNo":true,"oilCardNoRequired":true}'
        userDefinedFee = '{"hasHandlingFee":true,"hasDeliveryFee":true,"hasOilCardDeposit":true,"hasOtherFee":true}'
        carParamsSet = '{"hasDriverCardNo":true,"driverCardNoRequired":true,"hasVehicleIdNo":true,"vehicleIdNoRequired":true}'
        userDefinedFunction = '{"authTodelWayBill":true}'
        response = SystemParamsSettingsUpdate().system_params_settings_update(cargoParamsSet,userDefinedFee,
                                                                              carParamsSet,userDefinedFunction)
        self.logger.info('更新系统属性配置信息返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('更新系统属性配置信息返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()