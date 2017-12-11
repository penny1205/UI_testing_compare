#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.line.line_select import LineSelect
from bvt.common.create_line import CreateLine

class TestLineSelect(unittest.TestCase):
    '''查询线路'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineSelect START ###########################')
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
        self.Id = CreateLine().create_line(self.sendProvince, self.sendCity, self.sendDistrict, self.arriveProvince,
                                           self.arriveCity, self.arriveDistrict, self.stationAProvince,
                                           self.stationACity,
                                           self.stationADistrict, self.stationBProvince, self.stationBCity,
                                           self.stationBDistrict, self.arriveTime)[0]
        self.logger.info('新增线路Id是：{0}'.format(self.Id))

    def tearDown(self):
        self.logger.info('############################ TestLineSelect END ############################')


    def test_line_select_sendCity_arriveCity_success(self):
        '''按照出发城市到达城市查询线路时效列表'''
        response = LineSelect().line_select(sendCity= self.sendCity,arriveCity=self.arriveCity)
        self.logger.info('按照出发城市到达城市查询线路时效列表返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('按照出发城市到达城市查询线路时效列表返回结果是：{0}'.format(response.json()))

        line_list = response.json()['content']['dataList']
        if line_list != []:
            L = []
            for line in line_list:
                L.append(str(line['id']))
            self.assertIn(self.Id, L, 'Line created fail!')
        else:
            self.logger.error('Please check the results of the Line for empty')

if __name__ == '__main__':
    unittest.main()