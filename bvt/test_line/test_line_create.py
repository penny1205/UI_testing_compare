#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
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
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.phone = DataUtil().createmoble()
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'

    def tearDown(self):
        self.logger.info('############################ TestLineCreate END ############################')

    def test_Line_create_success(self):
        '''新增线路'''
        Id = CreateLine().create_line(self.sendProvince,self.sendCity, self.arriveProvince,self.arriveCity,'5',
                                      '德邦空运',self.startTime,self.endTime, '德邦','DB201710200001',self.phone,
                                      '黄经理')[0]
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