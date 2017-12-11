#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.line.line_delete import LineDelete
from bvt.common.create_line import CreateLine

class TestLineDelete(unittest.TestCase):
    '''删除线路'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineDelete START ###########################')
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.sendDistrict = ''
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'
        self.arriveDistrict = ''
        self.stationAProvince= '上海'
        self.stationACity = '上海'
        self.stationADistrict = ''
        self.stationBProvince = ''
        self.stationBCity = ''
        self.stationBDistrict = ''
        self.arriveTime ='10'
        self.Id = CreateLine().create_line(self.sendProvince,self.sendCity,self.sendDistrict,self.arriveProvince,
                                      self.arriveCity,self.arriveDistrict,self.stationAProvince,self.stationACity,
                                      self.stationADistrict,self.stationBProvince,self.stationBCity,
                                      self.stationBDistrict,self.arriveTime)[0]
        self.logger.info('新增线路Id是：{0}'.format(self.Id))

    def tearDown(self):
        self.logger.info('############################ TestLineDelete END ############################')


    def test_line_delete_success(self):
        '''删除线路'''
        response = LineDelete().line_delete(self.Id)
        self.logger.info('删除线路返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('删除线路返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()