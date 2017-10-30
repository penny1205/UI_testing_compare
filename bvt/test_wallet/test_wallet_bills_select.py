#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from interface.wallet.wallet_bills_select import WalletBillsSelect

class TestWalletBillsSelect(unittest.TestCase):
    '''交易记录查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineSelect START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestLineSelect END ############################')


    def test_wallet_bills_select_type_success(self):
        '''交易记录查询'''
        type = random.choice([1,2,3])
        response = WalletBillsSelect().wallet_bills_select(type=type)
        self.logger.info('交易记录查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('交易记录查询返回结果是：{0}'.format(response.json()))


if __name__ == '__main__':
    unittest.main()