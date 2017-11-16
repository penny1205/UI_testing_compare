# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from bvt.common.create_waybill import CreateWayBill
from interface.payment.payment_singlePay import PaymentSinglePay
from interface.waybill.waybill_driver_confirm import WayBillDriverConfirm


class SinglePay(unittest.TestCase):
    """ 运费支付 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSinglePay START ###########################')

    def tearDown(self):
        self.logger.info('########################### TestSinglePay END ###########################')

    def test_singlePay_KEKING_TO_COMPANY(self):
        """ 运费支付方式：贷款付商户 """
        waybillID = CreateWayBill().create_waybill_register().json()['content']
        self.logger.info('新建运单，生成的运单号为{0}'.format(waybillID))
        confirmMsg = WayBillDriverConfirm().waybill_driver_confirm(waybillID, totalAmt='0.05', preAmt='0.01',
                                                                   oilAmt='0.01', destAmt='0.01', lastAmt='0.01')
        self.logger.info('运单{0}，进行司机确认发车操作，返回信息：{1}'.format(waybillID, confirmMsg))
        response = PaymentSinglePay().single_pay(waybillID, paymentMethod=3, amountType=9, amount='0.05')
        self.logger.info('贷款付商户支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

    def test_singlePay_KEKING_TO_DRIVER(self):
        """ 运费支付方式：白条付司机 """
        waybillID = CreateWayBill().create_waybill_register().json()['content']
        self.logger.info('新建运单，生成的运单号为{0}'.format(waybillID))
        confirmMsg = WayBillDriverConfirm().waybill_driver_confirm(waybillID, totalAmt='0.05', preAmt='0.01',
                                                                   oilAmt='0.01', destAmt='0.01', lastAmt='0.01')
        self.logger.info('运单{0}，进行司机确认发车操作，返回信息：{1}'.format(waybillID, confirmMsg))
        response = PaymentSinglePay().single_pay(waybillID, paymentMethod=1, amountType=1, amount='0.01')
        self.logger.info('白条付司机支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

    def test_singlePay_WALLET_TO_DRIVER(self):
        """ 运费支付方式：钱包支付 """
        waybillID = CreateWayBill().create_waybill_register().json()['content']
        self.logger.info('新建运单，生成的运单号为{0}'.format(waybillID))
        confirmMsg = WayBillDriverConfirm().waybill_driver_confirm(waybillID, totalAmt='0.05', preAmt='0.01',
                                                                   oilAmt='0.01', destAmt='0.01', lastAmt='0.01')
        self.logger.info('运单{0}，进行司机确认发车操作，返回信息：{1}'.format(waybillID, confirmMsg))
        response = PaymentSinglePay().single_pay(waybillID, paymentMethod=2, amountType=1, amount='0.01',
                                                 password='123321')
        self.logger.info('钱包付司机支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

    def test_singlePay_KEKING_TO_DRIVER(self):
        """ 运费支付方式：线下支付 """
        waybillID = CreateWayBill().create_waybill_register().json()['content']
        self.logger.info('新建运单，生成的运单号为{0}'.format(waybillID))
        confirmMsg = WayBillDriverConfirm().waybill_driver_confirm(waybillID, totalAmt='0.05', preAmt='0.01',
                                                                   oilAmt='0.01', destAmt='0.01', lastAmt='0.01')
        self.logger.info('运单{0}，进行司机确认发车操作，返回信息：{1}'.format(waybillID, confirmMsg))
        response = PaymentSinglePay().single_pay(waybillID, paymentMethod=4, amountType=1, amount='0.01')
        self.logger.info('线下支付结果：{}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
