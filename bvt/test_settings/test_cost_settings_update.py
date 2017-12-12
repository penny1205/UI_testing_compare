#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.settings.cost_settings_get import CostSettingsGet
from bvt.common.cost_settings import CostSettings

class TestCostSettingsUpdate(unittest.TestCase):
    ''' 收入成本参数配置修改(与添加)'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSystemParamsGet START ###########################')
        self.carType = random.sample([1,2], 1)[0]
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
        self.carLength = DataUtil().genneratorCarLength()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.calculateType = random.sample([1,2,3,4], 1)[0]
        self.perIncome = random.uniform(0,99999)
        self.oilCost = random.uniform(0,99999)
        self.roadCost = random.uniform(0,99999)
        self.repairCost = random.uniform(0,99999)
        self.depreciationCost = random.uniform(0,99999)
        self.insurance = random.uniform(0,99999)
        self.personCost = random.uniform(0,99999)
        self.taxRate = random.uniform(0,100)
        self.otherCost = random.uniform(0,99999)
        self.infoCost = random.uniform(0,99999)
        self.Id, self.kilometers, self.projectId = CostSettings().create_cost_settings('',
            self.carType, self.sendProvince, self.sendCity, self.arriveDistrict, self.arriveProvince, self.arriveCity,
            self.arriveDistrict, self.stationAProvince, self.stationACity, self.stationADistrict, self.stationBProvince,
            self.stationBCity, self.stationBDistrict, self.carLength, self.carModel, self.calculateType, self.perIncome,
            self.oilCost, self.roadCost, self.repairCost, self.depreciationCost, self.insurance, self.personCost,
            self.taxRate, self.otherCost, self.infoCost)

    def tearDown(self):
        self.logger.info('############################ TestSystemParamsGet END ############################')

    def test_cost_settings_update_calculateType_success(self):
        '''修改收入成本参数配置的计费方式'''
        self.calculateType_update = random.sample([1,2,3,4], 1)[0]
        CostSettings().create_cost_settings(self.Id,
            self.carType, self.sendProvince, self.sendCity, self.arriveDistrict, self.arriveProvince, self.arriveCity,
            self.arriveDistrict, self.stationAProvince, self.stationACity, self.stationADistrict, self.stationBProvince,
            self.stationBCity, self.stationBDistrict, self.carLength, self.carModel, self.calculateType_update, self.perIncome,
            self.oilCost, self.roadCost, self.repairCost, self.depreciationCost, self.insurance, self.personCost,
            self.taxRate, self.otherCost, self.infoCost)
        cost_settings = CostSettingsGet().cost_settings_get(self.Id).json()['content']
        if cost_settings['calculateType'] == self.calculateType_update:
            pass
        else:
            self.logger.error('修改收入成本参数配置的计费方式失败')

if __name__ == '__main__':
    unittest.main()