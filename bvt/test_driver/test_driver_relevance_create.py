#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from interface.driver.driver_relevance_create import DriverRelevanceCreate
from interface.driver.driver_relevance_delete import DriverRelevanceDelete
from interface.driver.driver_relevance_select import DriverRelevanceSelect
from interface.driver.driver_mobile_select import DriverMobileSelect

class TestDriverRelevanceCreate(unittest.TestCase):
    '''关联外请车'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDriverRelevanceCreate START ###########################')
        mobile_certificate = ['13077327043', '18301771383', '15000422980']
        self.mobile_certificate = random.sample(mobile_certificate, 1)[0]


    def tearDown(self):
        self.logger.info('############################ TestDriverRelevanceCreate END ############################')
        pass

    def test_driver_relevance_create_success(self):
        '''关联外请车'''
        driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=self.mobile_certificate).json()['content'][
            'dataList']
        if driver_list != None:
            for driver in driver_list:
                DriverRelevanceDelete().driver_relevance_delete(id=driver['tmsDriverId'])
        driver_certificate_list = DriverMobileSelect().driver_mobile_select(mobile=self.mobile_certificate).json()[
            'content']
        if len(driver_certificate_list) != 1:
            self.logger.error('同一个已认证手机号不是只有一个外请车信息')
        response = DriverRelevanceCreate().driver_relevance_create(driver_certificate_list[0]['loginId'])
        self.logger.info('关联外请车返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('关联外请车的手机号是：{0},返回的结果是：{1}'.format(self.mobile_certificate,response.json()))



if __name__ == '__main__':
    unittest.main()