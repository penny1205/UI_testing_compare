#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.wallet.wallet_bills_export import WalletBillsExport

class TestWalletBillsExport(unittest.TestCase):
    '''交易记录导出'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWalletBillsExport START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWalletBillsExport END ############################')


    def test_wallet_bills_export_success(self):
        '''交易记录导出'''
        response = WalletBillsExport().wallet_bills_export(type=3)
        self.assertEqual(response.status_code, 200)
        filename = FileUtil.getProjectObsPath() + '/file/' + 'wallet_bills_export.xlsx.'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('交易记录导出文件是：{0}'.format(filename))

if __name__ == '__main__':
    unittest.main()