#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from interface.driver.mycar_create import MyCarCreate
from interface.driver.mycar_select import MyCarSelect
from interface.driver.mycar_delete import MyCarDelete

class CreateMyCar(object):
    '''我的车辆 新增车辆'''

    def __init__(self):
        self.logger = Log()

    def create_my_car(self,carNo,carModel,carLength,carLoad,carAge,buycarTime,carBrand,photoDriverCard,photoCar):
        '''我的车辆 新增车辆'''
        try:
            response = MyCarCreate().my_car_create(carNo=carNo,carModel=carModel,carLength=carLength,carLoad=carLoad,
                                                   carAge=carAge,buycarTime=buycarTime,carBrand=carBrand,
                                                   photoDriverCard=photoDriverCard,photoCar=photoCar)
            self.logger.info('新增的车辆车牌号是: {0}'.format(carNo))
            # 判断新增车辆车牌号是否重复
            if response.json()['code'] == 0:
                return response.json()['content']
            elif response.json()['code'] == 9050011:
                my_car_list = MyCarSelect().my_car_select(carNo=carNo).json()['content']['dataList']
                carId = my_car_list(0)['carId']
                MyCarDelete().my_car_delete(carId=carId)
                carId = MyCarCreate().my_car_create(carNo=carNo, carModel=carModel, carLength=carLength, carLoad=carLoad,
                                            carAge=carAge, buycarTime=buycarTime, carBrand=carBrand,
                                            photoDriverCard=photoDriverCard, photoCar=photoCar).json()['content']
                return carId
            else:
                self.logger.info('新增车辆返回错误:{0}'.format(response.json()))
                return None
        except Exception:
            self.logger.error('新增车辆发生异常:{0}'.format(Exception))
            return None