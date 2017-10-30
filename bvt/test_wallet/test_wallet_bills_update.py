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
        '''交易记录查询'''
        type = random.choice([1,2,3])
        bills_list = WalletBillsSelect().wallet_bills_select(type=type).json()['content']['dataList']
        if bills_list == []:
            self.logger.info('There is no transaction record for the wallet!')
        else:
            L = []
            for bills in bills_list:
                L.append(bills)
            bills_choice = random.choice(L)
            self.logger.info('查询交易记录的流水号是{0},交易类型是{1}'.format(bills_choice['serialNumber'],bills_choice['type']))
            response = WalletBillsUpdate().wallet_bills_update(bills_choice['serialNumber'],bills_choice['type'])
            self.logger.info('交易记录查询返回状态码：{0}'.format(response))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['code'], 0)
            self.logger.info('交易记录查询返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()