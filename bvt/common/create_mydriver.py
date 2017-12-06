#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from interface.driver.mydriver_create import MyDriverCreate
from interface.driver.mydriver_select import MyDriverSelect
from interface.driver.mydriver_delete import MyDriverDelete

class CreateMyDriver(object):
    '''我的司机 新增司机'''

    def __init__(self):
        self.logger = Log()

    def create_my_driver(self,mobile,name,idNo,photoDriverCard,frontIdCard,backIdCard):
        '''我的司机 新增司机'''
        try:
            response = MyDriverCreate().my_driver_create(mobile=mobile,name=name,idNo=idNo,
                                    photoDriverCard =photoDriverCard,frontIdCard=frontIdCard,backIdCard=backIdCard)
            self.logger.info('新增的司机手机号是: {0},身份证号是：{1}'.format(mobile,idNo))
            #判断手机号、身份证号是否重复
            if response.json()['code'] == 0:
                return response.json()['content']
            elif response.json()['code'] == 9060009 or response.json()['code'] == 9060010:
                my_driver_list = MyDriverSelect().my_driver_select(mobile).json()['content']['dataList']
                driverId = my_driver_list(0)['driverId']
                MyDriverDelete().my_driver_delete(driverId=driverId)
                driverId = MyDriverCreate().my_driver_create(mobile=mobile,name=name,idNo=idNo,
                                                             photoDriverCard =photoDriverCard,frontIdCard=frontIdCard,
                                                             backIdCard=backIdCard).json()['content']
                return driverId
            else:
                self.logger.info('新增司机返回错误:{0}'.format(response.json()))
                return None
        except Exception as e:
            self.logger.error('新增司机发生异常:{0}'.format(e))
            return None