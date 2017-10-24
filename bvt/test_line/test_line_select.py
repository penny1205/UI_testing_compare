#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from interface.line.line_select import LineSelect
from bvt.common.create_line import CreateLine

class TestLineSelect(unittest.TestCase):
    '''查询线路'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineSelect START ###########################')
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
        self.logger.info('############################ TestLineSelect END ############################')


    def test_line_select_sendCity_arriveCity_success(self):
        '''按照出发城市到达城市查询线路时效列表'''
        response = LineSelect().line_select(sendCity= self.sendCity,arriveCity=self.arriveCity)
        self.logger.info('按照出发城市到达城市查询线路时效列表返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('按照出发城市到达城市查询线路时效列表返回结果是：{0}'.format(response.json()))

        line_list = LineSelect().line_select(sendCity=self.sendCity, arriveCity=self.arriveCity).json()['content'][
            'dataList']
        if line_list != []:
            L = []
            for line in line_list:
                L.append(str(line['id']))
            self.assertIn(self.Id, L, 'Line created fail!')
        else:
            self.logger.error('Please check the results of the Line for empty')

if __name__ == '__main__':
    unittest.main()