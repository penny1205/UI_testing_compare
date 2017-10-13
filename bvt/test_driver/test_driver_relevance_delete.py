#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.file.fileutil import FileUtil
from interface.driver.driver_relevance_delete import DriverRelevanceDelete
from interface.driver.driver_relevance_select import DriverRelevanceSelect
from bvt.common.create_driver import CreateDriver

class TestDriverRelevanceDelete(unittest.TestCase):
    '''删除关联关系'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverRelevanceDelete START ###########################')
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
        self.logger.info('############################ TestDriverRelevanceDelete END ############################')
        pass

    def test_driver_relevance_delete_success(self):
        '''删除外请车关联关系'''
        driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile).json()['content']['dataList']
        if driver_list != None:
            for driver in driver_list:
                if str(driver['loginId']) == self.loginId:
                    response = DriverRelevanceDelete().driver_relevance_delete(id=driver['tmsDriverId'])
                    self.logger.info('删除外请车关联关系返回状态码：{0}'.format(response))
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(response.json()['code'], 0)
                    self.logger.info('删除外请车关联关系返回的结果是：{0}'.format(response.json()))
        else:
            self.logger.error('Please check the results of the driver for empty!')


if __name__ == '__main__':
    unittest.main()