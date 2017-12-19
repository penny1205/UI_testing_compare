# -*- coding:utf-8 -*-

import unittest
import datetime
from util.log.log import Log
from interface.payment.payment_export import PaymentExport


class TestPaymentExport(unittest.TestCase):
    """ 支付列表导出 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestPaymentExport START ###########################')
        self.lastDate = str(datetime.date.today())
        self.firstDate = str(datetime.date.today().replace(day=1))

    def tearDown(self):
        self.logger.info('########################### TestPaymentExport END ###########################')

    def test_payment_export(self):
        response = PaymentExport().payment_export(applyDateFirst=self.firstDate, applyDateLast=self.lastDate)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()