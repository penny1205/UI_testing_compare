#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_relevance_update import DriverRelevanceUpdate
from interface.driver.driver_relevance_select import DriverRelevanceSelect
from bvt.common.create_driver import CreateDriver

class TestDriverRelevanceUpdate(unittest.TestCase):
    '''修改未认证的外请车'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverRelevanceUpdate START ###########################')
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
        self.logger.info('############################ TestDriverRelevanceUpdate END ############################')

    def test_driver_relevance_Update_mobile_success(self):
        '''修改未认证的外请车的手机号'''
        driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile).json()['content']['dataList']
        if driver_list != []:
            for driver in driver_list:
                if driver['loginId'] == self.loginId and driver['certificate'] == 'N':
                    self.mobile_update = DataUtil().createmoble()
                    response = DriverRelevanceUpdate().driver_relevance_update(self.loginId, '孙师傅', self.mobile_update,
                                                                               self.idNo,self.photoIdFront,
                                                                               self.photoIdReserve,self.photoDriverCard,
                                                                               self.photoTransPort,self.carNo,
                                                                               self.carLength,self.carModel, '10')
                    self.logger.info('修改未认证的外请车的手机号返回状态码：{0}'.format(response))
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(response.json()['code'], 0)
                    self.logger.info('将手机号由{0}修改为{1}，修改未认证的外请车的手机号返回结果是：{2}'.format(
                        self.mobile, self.mobile_update,response.json()))
        else:
            self.logger.error('Please check the results of the driver for empty!')

if __name__ == '__main__':
    unittest.main()