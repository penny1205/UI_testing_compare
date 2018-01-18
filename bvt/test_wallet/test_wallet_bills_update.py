#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from interface.wallet.wallet_bills_update import WalletBillsUpdate
from interface.wallet.wallet_bills_select import WalletBillsSelect

class TestWalletBillsUpdate(unittest.TestCase):
    '''修改交易状态'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestLineSelect START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestLineSelect END ############################')


    def test_wallet_bills_Update_success(self):
        '''修改交易状态'''
        type = random.choice([1,2])
        bills_list = WalletBillsSelect().wallet_bills_select(type=type).json()['content']['dataList']
        if bills_list == None:
            self.logger.info('There is no transaction record for the wallet!')
        else:
            bills_choice = random.choice(bills_list)
            self.logger.info('查询交易记录的流水号是{0},交易类型是{1}'.format(bills_choice['serialNumber'],bills_choice['type']))
            response = WalletBillsUpdate().wallet_bills_update(bills_choice['serialNumber'],bills_choice['type'])
            self.logger.info('交易记录查询返回状态码：{0}'.format(response))
            self.assertEqual(response.status_code, 200)
            self.logger.info('交易记录查询返回结果是：{0}'.format(response.json()))
            self.assertEqual(response.json()['code'], 0)

if __name__ == '__main__':
    unittest.main()