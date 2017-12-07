#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.settings.SMS_settings_get import SMSSettingsGet

class TestSMSSettingsGet(unittest.TestCase):
    ''' 获取短信设置'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSystemParamsGet START ###########################')


    def tearDown(self):
        self.logger.info('############################ TestSystemParamsGet END ############################')

    def test_SMS_settings_get_success(self):
        '''获取短信设置'''
        response = SMSSettingsGet().SMS_settings_get()
        self.logger.info('获取短信设置返回状态码：{0}'.format(response))
        self.logger.info('获取短信设置返回结果是：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)


if __name__ == '__main__':
    unittest.main()