#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.line.line_mileage_more_get import LineMileageMoreGet

class TestLineMileageMoreGet(unittest.TestCase):
    '''计算线路中的里程数'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineMileageGet START ###########################')
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'

    def tearDown(self):
        self.logger.info('############################ TestLineMileageGet END ############################')


    def test_line_distance_get_success(self):
        '''计算线路中的里程数'''
        response = LineMileageMoreGet().line_mileage_more_get('安徽','合肥','','上海','上海','','','','','浙江','杭州','')
        self.logger.info('计算线路中的里程数返回状态码：{0}'.format(response))
        self.logger.info('计算线路中的里程数返回结果是：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)


if __name__ == '__main__':
    unittest.main()