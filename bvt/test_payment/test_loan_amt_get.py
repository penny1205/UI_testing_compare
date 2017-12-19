# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.payment.loan_amt_get import LoanAmtGet


class TestLoanAmtGet(unittest.TestCase):
    ''' 可借款金额统计 '''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLoanAmtGet START ###########################')

    def tearDown(self):
        self.logger.info('########################### TestLoanAmtGet END ###########################')

    def test_count_amt_get(self):
        '''可借款金额统计'''
        response = LoanAmtGet().loan_amt_get()
        self.logger.info('可借款金额统计返回状态码：{0}'.format(response))
        self.logger.info('可借款金额统计返回结果是：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

if __name__ == '__main__':
    unittest.main()
