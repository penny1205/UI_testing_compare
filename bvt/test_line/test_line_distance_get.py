#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.line.line_distance_get import LineDistanceGet

class TestLineDistanceGet(unittest.TestCase):
    '''根据出发城市和到达城市计算两地的距离'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineDistanceGet START ###########################')
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'

    def tearDown(self):
        self.logger.info('############################ TestLineDistanceGet END ############################')


    def test_line_distance_get_success(self):
        '''根据出发城市和到达城市计算两地的距离'''
        response = LineDistanceGet().line_get(self.sendCity,self.arriveCity,self.sendProvince + self.sendCity,
                                              self.arriveProvince + self.arriveCity)
        self.logger.info('根据出发城市和到达城市计算两地的距离返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('根据出发城市和到达城市计算两地的距离返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()