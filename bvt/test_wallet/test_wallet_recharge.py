#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from interface.wallet.wallet_recharge import WalletRecharge

class TestWalletRecharge(unittest.TestCase):
    '''钱包充值申请'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWalletRecharge START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWalletRecharge END ############################')


    def test_wallet_recharge_success(self):
        '''钱包充值申请'''
        moneyOrder = round(random.uniform(0,0.01),2)
        self.logger.info('钱包充值金额：{0}'.format(moneyOrder))
        response = WalletRecharge().wallet_recharge(moneyOrder)
        self.logger.info('钱包充值申请返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 1)
        self.logger.info('钱包充值申请返回结果是：{0}'.format(response.json()))


if __name__ == '__main__':
    unittest.main()