#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_bank_VIN_get import DriverBankVINGet
from bvt.common.create_driver import CreateDriver

class TestDriverBankVINGet(unittest.TestCase):
    '''根据外请车司机手机号获取银行卡号和车架号'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverBankVINGet START ###########################')
        self.mobile = DataUtil().createmoble()
        self.idNo = DataUtil().genneratorIdNo()
        self.carNo = DataUtil().genneratorCarNo()
        self.carLength = DataUtil().genneratorCarLength()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
        self.photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
        self.photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
        self.photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'
        self.loginId = CreateDriver().create_driver('孙师傅', self.mobile, self.idNo, self.photoIdFront,
                                                    self.photoIdReserve,self.photoDriverCard, self.photoTransPort,
                                                    self.carNo, self.carLength, self.carModel, '10')[0]

    def tearDown(self):
        self.logger.info('############################ TestDriverBankVINGet END ############################')
        pass

    def test_driver_bank_VIN_get_success(self):
        '''根据外请车司机手机号获取银行卡号和车架号'''
        response = DriverBankVINGet().driver_bank_VIN_get(mobile=self.mobile)
        self.logger.info('根据外请车司机手机号获取银行卡号和车架号返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('查询的手机号是：{0}，查询结果是：{1}'.format(self.mobile, response.json()))

if __name__ == '__main__':
    unittest.main()