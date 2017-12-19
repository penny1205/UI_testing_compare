# -*- coding:utf-8 -*-

import unittest
import datetime
from util.log.log import Log
from interface.payment.payment_receipt_select import PaymentReceiptSelect


class TestPaymentReceiptSelect(unittest.TestCase):
    """尾款支付列表查询"""
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestPaymentReceiptSelect START ###########################')
        self.lastDate = str(datetime.date.today())
        self.firstDate = str(datetime.date.today().replace(day=1))
        pass

    def tearDown(self):
        self.logger.info('########################### TestPaymentReceiptSelect END ###########################')
        pass

    # def test_vague_Select_ReceipPayList(self):
    #     """ 尾款支付列表查询--模糊查询 """
    #
    #     mobile = DataUtil().createmoble()
    #     response = PaymentReceiptSelect().payment_receipt_select(searchMode='global', globalCondition=mobile)
    #     self.logger.info('支付列表模糊查询返回状态码：{0}'.format(response))
    #     self.logger.info('支付列表模糊查询条件： {0} .支付列表查询的结果：{1}' .format(str(mobile), response.json()))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['code'], 0)

    def test_payment_receipt_select_precise_success(self):
        """ 尾款支付列表查询--精确查询 """
        response = PaymentReceiptSelect().payment_receipt_select(applyDateFirst=self.firstDate, applyDateLast=self.lastDate)
        self.logger.info('支付列表精确查询返回状态码：{0}'.format(response))
        self.logger.info('支付列表精确查询条件(发车日期区间)：{0}--{1} .支付列表查询的结果：{2}'
                         .format(self.firstDate, self.lastDate, response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)



