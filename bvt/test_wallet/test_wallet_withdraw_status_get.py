#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.wallet.wallet_withdraw_status_get import WalletWithdrawStatusGet

class TestWalletWithdrawStatusGet(unittest.TestCase):
    '''获取钱包提现状态'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWalletRecharge START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWalletRecharge END ############################')


    def test_wallet_withdraw_status_get_success(self):
        '''获取钱包提现状态'''
        response = WalletWithdrawStatusGet().wallet_withdraw_status_get()
        self.logger.info('获取钱包提现状态返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取钱包提现状态返回结果是：{0}'.format(response.json()))


if __name__ == '__main__':
    unittest.main()