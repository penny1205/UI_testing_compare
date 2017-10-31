#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.wallet.wallet_loan_select import WalletLoanSelect

class TestWalletLoanSelect(unittest.TestCase):
    '''可借款金额统计'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWalletLoanSelect START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWalletLoanSelect END ############################')


    def test_wallet_loan_select_type_success(self):
        '''可借款金额统计'''
        response = WalletLoanSelect().wallet_loan_select()
        self.logger.info('可借款金额统计返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('可借款金额统计返回结果是：{0}'.format(response.json()))


if __name__ == '__main__':
    unittest.main()