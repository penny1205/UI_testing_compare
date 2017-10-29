# -*- coding:utf-8 -*-

import unittest
import datetime
import random
from util.log.log import Log
from interface.payment.payment_loanAmt_get import LoanAmtGet


class GetLoanAmt(unittest.TestCase):
    """ 商户可借款金额统计 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestGetLoanAmt START ###########################')
        pass

    def tearDown(self):
        self.logger.info('########################### TestGetLoanAmt END ###########################')
        pass

    def test_countAmt_get(self):
        response = LoanAmtGet().loan_amt_get()
        self.logger.info('查询结果：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
