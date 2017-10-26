#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from interface.finance.loan_update import LoanUpdate
from bvt.common.create_loan import CreateLoan

class TestLoanUpdate(unittest.TestCase):
    '''修改大额贷款记录'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLoanUpdate START ###########################')
        self.loanAmount = random.randint(0, 9999999999)
        self.remarks = '申请贷款{0}'.format(self.loanAmount)
        demandLoanDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.Id,self.recipientName,self.recipientAccount,self.depositBank = CreateLoan().create_loan(
            self.loanAmount, self.remarks, demandLoanDate)

    def tearDown(self):
        self.logger.info('############################ TestLoanUpdate END ############################')

    def test_loan_update_success(self):
        '''修改大额贷款记录'''
        self.demandLoanDate_update = time.strftime('%Y-%m-%d')
        response = LoanUpdate().loan_update(self.Id,self.loanAmount,self.recipientName,self.recipientAccount,
                                            self.depositBank,self.remarks,self.demandLoanDate_update)
        self.logger.info('删除大额贷款记录返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('删除大额贷款记录返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()