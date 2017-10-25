#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.settings.cost_settings_get import CostSettingsGet
from bvt.common.create_cost_settings import CreateCostSettings

class TestCostSettingsGet(unittest.TestCase):
    ''' 获取收入成本参数配置详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSystemParamsGet START ###########################')
        self.carType = random.sample([1,2], 1)[0]
        self.sendProvince = '浙江'
        self.sendCity = '杭州'
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'
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
        #若是没有项目，创建新项目
        self.projectName = '德邦空运'
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.customerName = '德邦'
        self.customerCode = 'DB201710200001'
        self.phone = DataUtil().createmoble()
        self.Id ,self.kilometers,self.projectId= CreateCostSettings().create_cost_settings(
            self.carType, self.sendProvince, self.sendCity,self.arriveProvince, self.arriveCity,self.carLength,
            self.carModel,self.calculateType, self.perIncome, self.oilCost, self.roadCost, self.repairCost,
            self.depreciationCost, self.insurance, self.personCost, self.taxRate, self.otherCost, self.infoCost,
            self.projectName,self.startTime,self.endTime,self.customerName,self.customerCode,self.phone,'黄经理')

    def tearDown(self):
        self.logger.info('############################ TestSystemParamsGet END ############################')

    def test_cost_settings_get_success(self):
        '''获取收入成本参数配置详情'''
        response = CostSettingsGet().cost_settings_get(self.Id)
        self.logger.info('获取收入成本参数配置详情返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取收入成本参数配置详情返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()