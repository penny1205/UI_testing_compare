#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_get import DriverGet
from bvt.common.create_driver import CreateDriver

class TestDriverGet(unittest.TestCase):
    '''获取外请车详细信息'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverGet START ###########################')
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
        self.logger.info('############################ TestDriverGet END ############################')

    def test_driver_get_success(self):
        '''获取外请车详细信息'''
        response = DriverGet().driver_get(loginId=self.loginId)
        self.logger.info('获取外请车详细信息返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取外请车详细信息返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()