# -*- coding:utf-8 -*-

import unittest
import datetime
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.payment.payment_PayDetail_get import PaymentPayDetailGet
from interface.waybill.waybill_driver_confirm import WayBillDriverConfirm
from bvt.common.create_waybill import CreateWayBill


class GetPayDetail(unittest.TestCase):
    """ 运单支付详情获取 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDeleteWayBill START ###########################')
        time = str(datetime.date.today())
        self.wayBillId = CreateWayBill().create_waybill('2', time, '北京', '北京', '天津', '天津', '1000', '10',
                                                        '0.01', '0.02', '0.03', '0.04', '1', '备注我要录单测试',
                                                        'TMS', '快递', '10', '10', '10', '10', '10')[0]
        self.logger.info('创建的运单号是：%s' % self.wayBillId)
        self.driverConfirm = WayBillDriverConfirm().waybill_driver_confirm(billId=self.wayBillId, totalAmt='10',
                                                                           preAmt='1', oilAmt='1', destAmt='1', lastAmt='1')
        self.logger.info('司机确认发车操作完成。')
        pass

    def tearDown(self):
        self.logger.info('########################### TestSelectPaymentList END ###########################')
        pass

    def test_get_PaymentDetail(self):
        """  获取运单支付详情 """

        response = PaymentPayDetailGet().payment_detail_get(self.wayBillId)
        self.logger.info('支付详情查询的结果：{0}' .format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
