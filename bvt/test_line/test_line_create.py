#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.line.line_select import LineSelect
from bvt.common.create_line import CreateLine

class TestLineCreate(unittest.TestCase):
    '''新增线路'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineCreate START ###########################')
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

    def tearDown(self):
        self.logger.info('############################ TestLineCreate END ############################')

    def test_Line_create_success(self):
        '''新增线路'''
        Id = CreateLine().create_line(self.sendProvince,self.sendCity,self.sendDistrict,self.arriveProvince,
                                      self.arriveCity,self.arriveDistrict,self.stationAProvince,self.stationACity,
                                      self.stationADistrict,self.stationBProvince,self.stationBCity,
                                      self.stationBDistrict,self.arriveTime)[0]
        line_list = LineSelect().line_select(sendCity=self.sendCity,arriveCity=self.arriveCity).json()['content']['dataList']
        if line_list != []:
            L = []
            for line in line_list:
                L.append(str(line['id']))
            self.assertIn(Id, L, 'Line created fail!')
        else:
            self.logger.error('Please check the results of the Line for empty')

if __name__ == '__main__':
    unittest.main()