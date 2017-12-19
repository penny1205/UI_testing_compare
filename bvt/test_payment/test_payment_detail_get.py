# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.payment.payment_detail_get import PaymentDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from bvt.common.create_waybill import CreateWayBill


class TestPaymentDetailGet(unittest.TestCase):
    ''' 运单支付详情获取 '''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestPaymentDetailGet START ###########################')
        self.wayBillId = CreateWayBill().create_waybill_register().json()['content']
        self.logger.info('创建的运单号是：%s' % self.wayBillId)
        self.driverConfirm = WayBillDepartureConfirm().waybill_departure_confirm(billId=self.wayBillId)
        self.logger.info('确认发车操作完成。')

    def tearDown(self):
        self.logger.info('########################### TestPaymentDetailGet END ###########################')

    def test_payment_detail_get(self):
        '''  获取运单支付详情 '''
        response = PaymentDetailGet().payment_detail_get(self.wayBillId)
        print(response.json())
        self.logger.info('支付详情查询的结果：{0}' .format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

if __name__ == '__main__':
    unittest.main()