#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.settings.SMS_settings_update import SMSSettingsUpdate

class TestSMSSettingsUpdate(unittest.TestCase):
    ''' 修改短信设置'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSystemParamsGet START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestSystemParamsGet END ############################')

    def test_SMS_settings_update_success(self):
        '''修改短信设置'''
        mobile = DataUtil().createmoble()
        name = 'penny'
        sendContent = random.sample(['1','2','3','4'], 1)[0]
        sendTime = time.strftime('%H:%M:%S')
        response = SMSSettingsUpdate().SMS_settings_update(name,mobile,sendContent,sendTime)
        self.logger.info('修改短信设置返回状态码：{0}'.format(response))
        self.logger.info('修改短信设置返回结果是：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)


if __name__ == '__main__':
    unittest.main()