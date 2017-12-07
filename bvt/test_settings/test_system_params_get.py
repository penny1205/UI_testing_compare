#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
import json
from util.log.log import Log
from interface.settings.system_params_settings_get import SystemParamsSettingsGet

class TestSystemParamsGet(unittest.TestCase):
    ''' 获得系统属性配置信息'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSystemParamsGet START ###########################')


    def tearDown(self):
        self.logger.info('############################ TestSystemParamsGet END ############################')


    def test_system_params_get_success(self):
        '''获得系统属性配置信息'''
        response = SystemParamsSettingsGet().system_params_settings_get()
        self.logger.info('获得系统属性配置信息返回状态码：{0}'.format(response))
        self.logger.info('获得系统属性配置信息返回结果是：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)


    # def test_1(self):
    #     settings = SystemParamsSettingsGet().system_params_settings_get().json()['content']
    #     for k, v in json.loads(settings['cargoParamsSet']).items():
    #         if v:
    #             print(k)
    #     for k, v in json.loads(settings['userDefinedFee']).items():
    #         if v:
    #             print(k)
    #     for k, v in json.loads(settings['carParamsSet']).items():
    #         if v:
    #             print(k)






if __name__ == '__main__':
    unittest.main()