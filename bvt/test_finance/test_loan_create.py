#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from interface.finance.loan_select import LoanSelect
from bvt.common.create_loan import CreateLoan

class TestLoanCreate(unittest.TestCase):
    '''创建大额贷款记录'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLoanCreate START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestLoanCreate END ############################')

    def test_loan_create_success(self):
        '''创建大额贷款记录'''
        loanAmount = random.randint(0, 9999999999)
        remarks = '申请贷款{0}'.format(loanAmount)
        demandLoanDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        Id = CreateLoan().create_loan(loanAmount,remarks,demandLoanDate)[0]
        loan_list = LoanSelect().loan_select(loanAmount = loanAmount).json()['content']['dataList']
        if loan_list != []:
            L = []
            for loan in loan_list:
                L.append((loan['id']))
            self.assertIn(Id, L, 'LargerLoan created fail!')
        else:
            self.logger.error('Please check the results of LargerLoan for empty')

if __name__ == '__main__':
    unittest.main()