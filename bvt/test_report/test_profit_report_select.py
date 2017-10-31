#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from interface.report.profit_report_select import ProfitReportSelect

class TestProfitReportSelect(unittest.TestCase):
    '''利润报表信息列表查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestProfitReportSelect START ########################')
        self.sendDateStart = time.strftime('%Y-%m-%d', time.localtime(time.time() - 2592000))
        self.sendDateEnd = time.strftime('%Y-%m-%d')

    def tearDown(self):
        self.logger.info('######################## TestProfitReportSelect END #########################')


    def test_profit_report_select_success(self):
        '''利润报表信息列表查询'''
        response = ProfitReportSelect().profit_report_select(sendDateStart=self.sendDateStart,sendDateEnd=self.sendDateEnd)
        self.logger.info('利润报表信息列表查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('利润报表信息列表查询返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()