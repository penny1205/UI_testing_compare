# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from bvt.common.create_waybill import CreateWayBill
from interface.payment.payment_single import PaymentSingle

class TestPaymentSingle(unittest.TestCase):
    ''' 运费支付 单条支付'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestPaymentSingle START ###########################')

    def tearDown(self):
        self.logger.info('########################### TestPaymentSingle END ###########################')

    def test_singlePay_KEKING_TO_COMPANY(self):
        ''' 运费支付方式：贷款付商户 '''
        waybillID = CreateWayBill().create_waybill_register()
        response = PaymentSingle().payment_single(waybillID, paymentMethod=3, amountType=9, amount='0.05')
        self.logger.info('贷款付商户支付返回状态码：{0}'.format(response))
        self.logger.info('贷款付商户支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

    def test_singlePay_KEKING_TO_DRIVER(self):
        ''' 运费支付方式：白条付司机 '''
        waybillID = CreateWayBill().create_waybill_register()
        response = PaymentSingle().payment_single(waybillID, paymentMethod=1, amountType=1, amount='0.01')
        self.logger.info('白条付司机支付返回状态码：{0}'.format(response))
        self.logger.info('白条付司机支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

    # def test_singlePay_WALLET_TO_DRIVER(self):
    #     ''' 运费支付方式：钱包支付 '''
    #     waybillID = CreateWayBill().create_waybill_register()
    #     response = PaymentSingle().payment_single(waybillID, paymentMethod=2, amountType=1, amount='0.01',
    #                                              password='123321')
    #     self.logger.info('钱包付司机支付结果：{}'.format(response.json()))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['code'], 0)

    def test_singlePay_OFFLINE(self):
        ''' 运费支付方式：线下支付 '''
        waybillID = CreateWayBill().create_waybill_register()
        response = PaymentSingle().payment_single(waybillID, paymentMethod=4, amountType=1, amount='0.01')
        self.logger.info('线下支付返回状态码：{0}'.format(response))
        self.logger.info('线下支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

if __name__ == '__main__':
    unittest.main()