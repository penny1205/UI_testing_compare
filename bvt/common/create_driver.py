#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from interface.driver.driver_create import DriverCreate
from interface.driver.driver_uncertificate_create import DriverUnCertificateCreate
from interface.driver.driver_relevance_create import DriverRelevanceCreate
from interface.driver.driver_relevance_select import DriverRelevanceSelect
from interface.driver.driver_relevance_delete import DriverRelevanceDelete

class CreateDriver(object):
    '''新增外请车'''

    def __init__(self):
        self.logger = Log()

    def create_driver(self,name, mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard,
                         photoTransPort,carNo, carLength, carModel, carLoad):
        '''新增外请车'''
        try:
            response = DriverCreate().driver_create(name=name, mobile=mobile, idNo=idNo,photoIdFront=photoIdFront,
                        photoIdReserve=photoIdReserve, photoDriverCard=photoDriverCard,photoTransPort=photoTransPort,
                        carNo=carNo, carLength=carLength, carModel=carModel, carLoad=carLoad)
            self.logger.info('新增外请车的司机手机号是: {0}'.format(mobile))
            # Id YD_TMS_APP_DRIVER表主键；loginId 外请车车主id
            # 手机号未认证未关联
            if response.json()['code'] == 0:
                driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=mobile).json()['content'][
                    'dataList']
                for driver in driver_list:
                    Id = response.json()['content']
                    if str(driver['tmsDriverId']) == Id:
                         loginId = driver_list[0]['loginId']
                         return loginId,Id

            #手机号仅且存在已认证已关联外请车
            elif response.json()['code'] == 1:
                Id = DriverUnCertificateCreate().driver_unCertificate_create(name=name, mobile=mobile, idNo=idNo,
                        photoIdFront=photoIdFront,photoIdReserve=photoIdReserve, photoDriverCard=photoDriverCard,
                        photoTransPort=photoTransPort,carNo=carNo, carLength=carLength, carModel=carModel,
                        carLoad=carLoad).json()['content']
                driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=mobile).json()['content'][
                    'dataList']
                for driver in driver_list:
                    if str(driver['tmsDriverId']) == Id:
                        loginId = driver['loginId']
                        return loginId,Id

            # 手机号仅且存在已认证未关联外请车 or 手机号存在已认证未关联和未认证已关联两条外请车
            elif response.json()['code'] == 2 or response.json()['code'] == 3:
                DriverRelevanceCreate().driver_relevance_create(response.json()['content']['loginId'])
                driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=mobile).json()['content'][
                    'dataList']
                for driver in driver_list:
                    if driver['loginId'] == response.json()['content']['loginId']:
                        loginId = driver['loginId']
                        Id = driver['tmsDriverId']
                        return loginId, Id

            # 手机号仅且存在未认证已关联外请车 or 手机号存在已认证已关联和未认证已关联两条外请车
            elif response.json()['code'] == 9060006:
                driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=mobile).json()['content'][
                    'dataList']
                for driver in driver_list:
                    if driver['certificate'] == 'N':
                        DriverRelevanceDelete().driver_relevance_delete(id=driver['tmsDriverId'])
                Id = DriverUnCertificateCreate().driver_unCertificate_create(name=name, mobile=mobile, idNo=idNo,
                    photoIdFront=photoIdFront,photoIdReserve=photoIdReserve, photoDriverCard=photoDriverCard,
                    photoTransPort=photoTransPort,carNo=carNo, carLength=carLength,carModel=carModel,
                    carLoad=carLoad).json()['content']
                driver_list = DriverRelevanceSelect().driver_relevance_select(mobile=mobile).json()['content'][
                    'dataList']
                for driver in driver_list:
                    if str(driver['tmsDriverId']) == Id:
                        loginId = driver['loginId']
                        return loginId,Id
            else:
                return None,None
        except Exception:
            raise
            # return None