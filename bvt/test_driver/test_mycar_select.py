#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.mycar_select import MyCarSelect
from bvt.common.create_mycar import CreateMyCar

class TestMyCarSelect(unittest.TestCase):
    '''查询车辆'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMyCarSelect START ###########################')
        self.carNo = DataUtil().genneratorCarNo()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.carLength = DataUtil().genneratorCarLength()
        self.buycarTime = time.strftime('%Y-%m-%d')
        self.photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
        self.photoCar = 'http://yudian.ufile.ucloud.com.cn/69eec140-f95d-4af7-9aaf-c57b8442d799.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=bPzioEVJ8i4E3iXi+Yx7KQSeHvw='
        self.carId = CreateMyCar().create_my_car(self.carNo, self.carModel, self.carLength, '10', '', self.buycarTime,
                                                 '长城',self.photoDriverCard, self.photoCar)


    def tearDown(self):
        self.logger.info('############################ TestMyCarSelect END ############################')

    def test_my_car_select_carNo_success(self):
        '''按车牌号查询车辆'''
        response =  MyCarSelect().my_car_select(carNo=self.carNo)
        self.logger.info('按车牌号查询车辆返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的查询条件车牌号是：{0}，查询结果是：{1}'.format(self.carNo, response.json()))
        my_car_list = response.json()['content']['dataList']
        if my_car_list != None:
            L = []
            for my_car in my_car_list:
                L.append(str(my_car['carId']))
            self.assertIn(self.carId, L, 'MyCar selected fail!')
        else:
            self.logger.error('Please check the results of the myCar for empty!')


if __name__ == '__main__':
    unittest.main()