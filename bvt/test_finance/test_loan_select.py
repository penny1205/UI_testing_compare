# __author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import time
import unittest
from util.log.log import Log
from interface.finance.loan_select import LoanSelect
from bvt.common.create_loan import CreateLoan


class TestLoanSelect(unittest.TestCase):
    '''查询大额贷款记录'''

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLoanSelect START ###########################')
        self.loanAmount = random.randint(0, 9999999999)
        remarks = '申请贷款{0}'.format(self.loanAmount)
        demandLoanDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.Id = CreateLoan().create_loan(self.loanAmount,remarks,demandLoanDate)[0]

    def tearDown(self):
        self.logger.info('############################ TestLoanSelect END ############################')

    def test_loan_select_loanAmount_success(self):
        '''按贷款金额查询大额贷款记录'''
        response = LoanSelect().loan_select(loanAmount=self.loanAmount)
        self.logger.info('按贷款金额查询大额贷款记录返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('按贷款金额查询大额贷款记录返回结果是：{0}'.format(response.json()))
        loan_list = response.json()['content']['dataList']
        if loan_list != []:
            L = []
            for loan in loan_list:
                L.append((loan['id']))
            self.assertIn(self.Id, L, 'LargerLoan selected fail!')
        else:
            self.logger.error('Please check the results of LargerLoan for empty')


if __name__ == '__main__':
    unittest.main()