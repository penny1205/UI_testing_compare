#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.mycar_get import MyDCarGet
from bvt.common.create_mycar import CreateMyCar

class TestMyCarGet(unittest.TestCase):
    '''查看车辆详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMyCarGet START ###########################')
        self.carNo = DataUtil().genneratorCarNo()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.carLength = DataUtil().genneratorCarLength()
        self.buycarTime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
        self.photoCar = 'http://yudian.ufile.ucloud.com.cn/69eec140-f95d-4af7-9aaf-c57b8442d799.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=bPzioEVJ8i4E3iXi+Yx7KQSeHvw='
        self.carId = CreateMyCar().create_my_car(self.carNo, self.carModel, self.carLength, '10', '', self.buycarTime,
                                                 '长城',self.photoDriverCard, self.photoCar)


    def tearDown(self):
        self.logger.info('############################ TestMyCarGet END ############################')

    def test_my_car_get_success(self):
        '''查看车辆详情'''
        response = MyDCarGet().my_car_get(self.carId)
        self.logger.info('查看车辆详情返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('查看车辆详情是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()