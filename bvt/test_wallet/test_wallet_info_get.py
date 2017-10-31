#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.wallet.wallet_info_get import WalletInfoGet

class TestWalletInfoGet(unittest.TestCase):
    '''获取企业钱包信息'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWalletInfoGet START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWalletInfoGet END ############################')

    def test_wallet_info_get_success(self):
        '''获取企业钱包信息'''
        response = WalletInfoGet().wallet_info_get()
        self.logger.info('获取企业钱包信息返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取企业钱包信息返回结果是：{0}'.format(response.json()))
        print(response.json()['content'])

if __name__ == '__main__':
    unittest.main()