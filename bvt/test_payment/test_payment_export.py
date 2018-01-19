# -*- coding:utf-8 -*-

import unittest
import time
from util.log.log import Log
from interface.payment.payment_export import PaymentExport


class TestPaymentExport(unittest.TestCase):
    """ 支付列表导出 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestPaymentExport START ###########################')
        self.lastDate = time.strftime('%Y-%m-%d')
        self.firstDate = time.strftime('%Y-%m-%d')

    def tearDown(self):
        self.logger.info('########################### TestPaymentExport END ###########################')

    def test_payment_export(self):
        response = PaymentExport().payment_export(applyDateFirst=self.firstDate, applyDateLast=self.lastDate)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()