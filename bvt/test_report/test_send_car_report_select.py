#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from interface.report.send_car_report_select import SendCarReportSelect

class TestSendCarReportSelect(unittest.TestCase):
    '''发车综合报表分页查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestSendCarReportSelect START ########################')
        self.sendCarDateStart = time.strftime('%Y-%m-%d', time.localtime(time.time() - 2592000))
        self.sendCarDateEnd = time.strftime('%Y-%m-%d')

    def tearDown(self):
        self.logger.info('######################## TestSendCarReportSelect END #########################')


    def test_send_car_report_select_success(self):
        '''发车综合报表分页查询'''
        response = SendCarReportSelect().send_car_report_select(sendCarDateStart=self.sendCarDateStart,
                                                                sendCarDateEnd=self.sendCarDateEnd)
        self.logger.info('发车综合报表分页查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('发车综合报表分页查询返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()