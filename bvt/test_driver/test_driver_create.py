#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import random
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_relevance_select import DriverRelevanceSelect
from bvt.common.create_driver import CreateDriver

class TestDriverCreate(unittest.TestCase):
    '''新增外请车'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverCreate START ###########################')
        self.mobile = DataUtil().createmoble()
        self.idNo = DataUtil().genneratorIdNo()
        self.carNo = DataUtil().genneratorCarNo()
        self.carLength = DataUtil().genneratorCarLength()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
        self.photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
        self.photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
        self.photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'
        mobile_certificate = ['13077327043','18301771383','15000422980']
        self.mobile_certificate = random.sample(mobile_certificate, 1)[0]

    def tearDown(self):
        self.logger.info('############################ TestDriverCreate END ############################')
        pass


    def test_driver_create_success(self):
        '''新增外请车'''
        loginId = CreateDriver().create_driver('孙师傅', self.mobile, self.idNo, self.photoIdFront, self.photoIdReserve,
                                                self.photoDriverCard,self.photoTransPort,
                                                self.carNo, self.carLength, self.carModel, '10')[0]
        driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile).json()['content']['dataList']
        if driver_list != None:
            L = []
            for driver in driver_list:
                L.append(str(driver['loginId']))
            self.assertIn(loginId, L, 'Driver created fail!')
        else:
            self.logger.error('Driver created fail')

    def test_certificate_driver_create_success(self):
        '''新增已认证外请车 '''
        loginId = CreateDriver().create_driver('黄师傅', self.mobile_certificate, self.idNo, self.photoIdFront,
                                               self.photoIdReserve,self.photoDriverCard, self.photoTransPort,
                                               self.carNo, self.carLength, self.carModel, '10')[0]
        driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile_certificate).json()['content'][
            'dataList']
        if driver_list != None:
            L = []
            for driver in driver_list:
                L.append(str(driver['loginId']))
            self.assertIn(loginId, L, 'Driver created fail!')
        else:
            self.logger.error('Please check the results of the driver for empty!')


if __name__ == '__main__':
    unittest.main()