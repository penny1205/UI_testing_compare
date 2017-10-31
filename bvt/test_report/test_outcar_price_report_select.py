#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from interface.report.outcar_price_report_select import OutCarPriceReportSelect

class TestOutCarPriceReportSelect(unittest.TestCase):
    '''外请车价监控报表查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestOutCarPriceReportSelect START ########################')
        self.startDate = time.strftime('%Y-%m-%d', time.localtime(time.time() - 2592000))
        self.endDate = time.strftime('%Y-%m-%d')
        self.dataType = random.choice(['week','day','month'])

    def tearDown(self):
        self.logger.info('######################## TestOutCarPriceReportSelect END #########################')


    def test_outCar_price_report_select_success(self):
        '''外请车价监控报表查询'''
        response = OutCarPriceReportSelect().outCar_price_report_select(startDate=self.startDate,endDate=self.endDate,
                                                            sendCity='杭州',arriveCity='合肥',dataType=self.dataType)
        self.logger.info('外请车价监控报表查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('外请车价监控报表查询返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()