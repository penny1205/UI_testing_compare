#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.finance.bank_account_get import BankAccountGet

class TestBankAccountGet(unittest.TestCase):
    '''根据partnerNo获取开户行信息'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestBankAccountGet START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestBankAccountGet END ############################')

    def test_bank_account_get_success(self):
        '''根据partnerNo获取开户行信息'''
        response = BankAccountGet().bank_account_get()
        self.logger.info('根据partnerNo获取开户行信息返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('根据partnerNo获取开户行信息返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()