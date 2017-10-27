# -*- coding:utf-8 -*-

import unittest
import datetime
from util.log.log import Log
from interface.payment.payment_list_export import PaymentListExport


class ExportPaymentList(unittest.TestCase):
    """ 支付列表导出 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestExportPaymentList START ###########################')
        self.lastDate = str(datetime.date.today())
        self.firstDate = str(datetime.date.today().replace(day=1))
        pass

    def tearDown(self):
        self.logger.info('########################### TestExportPaymentList END ###########################')
        pass

    def test_Export_Paymentlist(self):
        response = PaymentListExport().payment_list_export(applyDateFirst=self.firstDate, applyDateLast=self.lastDate)
        self.assertEqual(response.status_code, 200)

