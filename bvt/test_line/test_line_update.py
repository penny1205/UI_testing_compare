#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from interface.line.line_update import LineUpdate
from bvt.common.create_line import CreateLine

class TestLineUpdate(unittest.TestCase):
    '''修改线路'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineUpdate START ###########################')
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.sendDistrict = ''
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'
        self.arriveDistrict = ''
        self.stationAProvince = '上海'
        self.stationACity = '上海'
        self.stationADistrict = ''
        self.stationBProvince = ''
        self.stationBCity = ''
        self.stationBDistrict = ''
        self.arriveTime = '10'
        self.Id,self.mileage,self.projectId = CreateLine().create_line(self.sendProvince, self.sendCity,
                                                self.sendDistrict, self.arriveProvince,self.arriveCity,
                                                self.arriveDistrict, self.stationAProvince,self.stationACity,
                                                self.stationADistrict, self.stationBProvince, self.stationBCity,
                                                self.stationBDistrict, self.arriveTime)[0]

    def tearDown(self):
        self.logger.info('############################ TestLineUpdate END ############################')


    def test_line_update_mileage_success(self):
        '''修改线路公里数'''
        mileage = '150'
        response = LineUpdate().line_update(self.Id,self.sendProvince,self.sendCity,self.arriveProvince,self.arriveCity,
                                            mileage,self.arriveTime,self.projectId)
        self.logger.info('根据ID获取线路返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('根据ID获取线路返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()