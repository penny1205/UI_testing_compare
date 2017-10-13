#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.mycar_select import MyCarSelect
from bvt.common.create_mycar import CreateMyCar

class TestMyCarCreate(unittest.TestCase):
    '''新增车辆'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMyCarCreate START ###########################')
        self.carNo = DataUtil().genneratorCarNo()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.carLength = DataUtil().genneratorCarLength()
        self.buycarTime = time.strftime('%Y-%m-%d')
        self.photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
        self.photoCar = 'http://yudian.ufile.ucloud.com.cn/69eec140-f95d-4af7-9aaf-c57b8442d799.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=bPzioEVJ8i4E3iXi+Yx7KQSeHvw='

    def tearDown(self):
        self.logger.info('############################ TestMyCarCreate END ############################')

    def test_my_car_create_success(self):
        '''新增车辆'''
        carId = CreateMyCar().create_my_car(self.carNo, self.carModel,self.carLength ,'10','',self.buycarTime,'长城',
                                            self.photoDriverCard,self.photoCar)
        my_car_list = MyCarSelect().my_car_select(carNo=self.carNo).json()['content']['dataList']
        if my_car_list != None:
            L = []
            for my_car in my_car_list:
                L.append(str(my_car['carId']))
            self.assertIn(carId, L, 'MyCar created fail!')
        else:
            self.logger.error('Please check the results of the myCar for empty!')

if __name__ == '__main__':
    unittest.main()