#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.mycar_update import MyCarUpdate
from interface.driver.mycar_get import MyDCarGet
from bvt.common.create_mycar import CreateMyCar

class TestMyCarUpdate(unittest.TestCase):
    '''修改车辆'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMyCarUpdate START ###########################')
        self.carNo = DataUtil().genneratorCarNo()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.carLength = DataUtil().genneratorCarLength()
        self.buycarTime = time.strftime('%Y-%m-%d')
        self.photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
        self.photoCar = 'http://yudian.ufile.ucloud.com.cn/69eec140-f95d-4af7-9aaf-c57b8442d799.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=bPzioEVJ8i4E3iXi+Yx7KQSeHvw='
        self.carId = CreateMyCar().create_my_car(self.carNo, self.carModel, self.carLength, '10', '', self.buycarTime,
                                                 '长城',self.photoDriverCard, self.photoCar)


    def tearDown(self):
        self.logger.info('############################ TestMyCarUpdate END ############################')

    def test_my_car_update_carNo_success(self):
        '''修改车牌号'''
        self.carNo_update = DataUtil().genneratorCarNo()
        response = MyCarUpdate().my_car_update(self.carId,self.carNo_update, self.carModel, self.carLength, '10', '',
                                               self.buycarTime,'长城',self.photoDriverCard, self.photoCar)
        self.logger.info('修改车牌号返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('修改的车辆是：{0}'.format(response.json()))
        response_get = MyDCarGet().my_car_get(self.carId)
        self.assertEqual(self.carNo_update,response_get.json()['content']['carNo'], 'MyCar updated fail!')

if __name__ == '__main__':
    unittest.main()