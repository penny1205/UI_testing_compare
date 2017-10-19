#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_relevance_select import DriverRelevanceSelect
from bvt.common.create_driver import CreateDriver

class TestDriverRelevanceSelect(unittest.TestCase):
    '''我的外请车列表,查询结果是已关联的外请车'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverRelevanceSelect START ###########################')
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
        self.logger.info('############################ TestDriverRelevanceSelect END ############################')
        pass

    def test_driver_relevance_select_mobile_success(self):
        '''按手机号查询已关联的外请车'''
        response = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile)
        self.logger.info('按手机号查询已关联的外请车返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的手机号是：{0}，查询结果是：{1}'.format(self.mobile, response.json()))
        driver_list = response.json()['content']['dataList']
        if driver_list != []:
            L = []
            for driver in driver_list:
                L.append(str(driver['loginId']))
            self.assertIn(self.loginId, L, 'Driver selected fail!')
        else:
            self.logger.error( 'Driver selected fail!')

    def test_driver_relevance_select_carNo_success(self):
        '''按车牌号查询已关联的外请车'''
        response = DriverRelevanceSelect().driver_relevance_select(carNo=self.carNo)
        self.logger.info('按车牌号查询已关联的外请车返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的车牌号是：{0}，查询结果是：{1}'.format(self.mobile, response.json()))
        driver_list = response.json()['content']['dataList']
        if driver_list != []:
            L = []
            for driver in driver_list:
                L.append(str(driver['loginId']))
            self.assertIn(self.loginId, L, 'Driver selected fail!')
        else:
            self.logger.error('Please check the results of the driver for empty!')

if __name__ == '__main__':
    unittest.main()