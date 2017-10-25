#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from interface.finance.loan_delete import LoanDelete
from bvt.common.create_loan import CreateLoan

class TestLoanDelete(unittest.TestCase):
    '''删除大额贷款记录'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLoanDelete START ###########################')
        loanAmount = random.randint(0, 9999999999)
        remarks = '申请贷款{0}'.format(loanAmount)
        demandLoanDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.Id = CreateLoan().create_loan(loanAmount,remarks,demandLoanDate)[0]

    def tearDown(self):
        self.logger.info('############################ TestLoanDelete END ############################')

    def test_loan_delete_success(self):
        '''删除大额贷款记录'''
        response = LoanDelete().loan_delete(self.Id)
        self.logger.info('删除大额贷款记录返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('删除大额贷款记录返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()