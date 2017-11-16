#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.finance.loan_create import LoanCreate
from interface.finance.bank_account_get import BankAccountGet

class CreateLoan(object):
    '''创建大额贷款记录'''

    def __init__(self):
        self.logger = Log()

    def create_loan(self,loanAmount,remarks,demandLoanDate):
        '''创建大额贷款记录'''
        try:
            bank_account_list = BankAccountGet().bank_account_get().json()['content']
            bank_account = random.choice(bank_account_list)
            response = LoanCreate().loan_create(loanAmount,bank_account['acctName'],bank_account['cardNo'],
                                                bank_account['bankName'],remarks,demandLoanDate)
            self.logger.info('新增贷款的收款账号是: {0}'.format(bank_account['cardNo']))
            return response.json()['content'],bank_account['acctName'],bank_account['cardNo'],bank_account['bankName']
        except Exception:
            self.logger.error('创建大额贷款记录发生异常:{0}'.format(Exception))
            return None