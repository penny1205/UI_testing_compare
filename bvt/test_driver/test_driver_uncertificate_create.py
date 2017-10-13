#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_uncertificate_create import DriverUnCertificateCreate
from interface.driver.driver_relevance_select import DriverRelevanceSelect

class TestDriverUnCertificateCreate(unittest.TestCase):
    '''新增未认证的外请车'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestDriverUnCertificateCreate START ########################')
        self.mobile = DataUtil().createmoble()
        self.idNo = DataUtil().genneratorIdNo()
        self.carNo = DataUtil().genneratorCarNo()
        self.carLength = DataUtil().genneratorCarLength()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
        self.photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
        self.photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
        self.photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'

    def tearDown(self):
        self.logger.info('######################### TestDriverUnCertificateCreate END #########################')
        pass


    def test_driver_unCertificate_create_success(self):
        '''新增未认证的外请车'''
        response = DriverUnCertificateCreate().driver_unCertificate_create('孙师傅', self.mobile, self.idNo,
                                                self.photoIdFront, self.photoIdReserve,self.photoDriverCard,
                                                self.photoTransPort,self.carNo, self.carLength, self.carModel, '10')
        self.logger.info('新增未认证的外请车返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('新增未认证的外请车的手机号是：{0}，返回结果是：{1}'.format(self.mobile, response.json()))
        driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile).json()['content']['dataList']
        if driver_list != None:
            L = []
            for driver in driver_list:
                L.append(str(driver['tmsDriverId']))
            self.assertIn(response.json()['content'], L, 'The unCertificated driver created fail!')
        else:
            self.logger.error('Please check the results of the driver for empty!')

if __name__ == '__main__':
    unittest.main()