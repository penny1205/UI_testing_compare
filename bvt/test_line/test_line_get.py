#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from interface.line.line_get import LineGet
from bvt.common.create_line import CreateLine

class TestLineGet(unittest.TestCase):
    '''根据ID获取线路'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineGet START ###########################')
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'
        self.Id = CreateLine().create_line(self.sendProvince, self.sendCity, self.arriveProvince, self.arriveCity, '5',
                                           '德邦空运', self.startTime, self.endTime, '德邦', 'DB201710200001',
                                           '13801011213', '黄经理')[0]

    def tearDown(self):
        self.logger.info('############################ TestLineGet END ############################')


    def test_line_get_success(self):
        '''根据ID获取线路'''
        response = LineGet().line_get(self.Id)
        self.logger.info('根据ID获取线路返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('根据ID获取线路返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()