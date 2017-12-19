# -*- coding:utf-8 -*-

import unittest
import random
from util.log.log import Log
from bvt.common.create_waybill import CreateWayBill
from interface.payment.defined_fee_update import DefinedFeeUpdate
from bvt.common.settings import Settings
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_detail_get import WayBillDetailGet


class TestDefinedFeeUpdate(unittest.TestCase):
    ''' 更新用户配置自定义费用字段 '''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDefinedFeeUpdate START ###########################')
        Settings().system_params_update()
        self.logger.info('更新系统属性配置信息')
        self.waybillID = CreateWayBill().create_waybill_register(handlingFee='1', deliveryFee='1', oilCardDeposit='1',
                                                                 otherFee='1').json()['content']
        self.logger.info('新建运单，录入的自定义费用项数值均为1，生成的运单号为{0}'.format(self.waybillID))
        confirmMsg=WayBillDepartureConfirm().waybill_departure_confirm(self.waybillID).json()
        self.logger.info('运单{0}，进行确认发车，返回信息：{1}'.format(self.waybillID, confirmMsg))
        self.handlingFee = random.randint(1, 100)
        self.deliveryFee = random.randint(1, 100)
        self.oilCardDeposit = random.randint(1, 100)
        self.otherFee = random.randint(1, 100)

    def tearDown(self):
        self.logger.info('########################### TestDefinedFeeUpdate END ###########################')

    def test_defined_fee_update_success(self):
        response = DefinedFeeUpdate().defined_fee_update(self.waybillID, handlingFee=self.handlingFee,
                                                                deliveryFee=self.deliveryFee,
                                                                oilCardDeposit=self.oilCardDeposit,
                                                                otherFee=self.otherFee)
        self.logger.info('修改运单自定义费用金额为10.')
        self.logger.info('修改结果：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        wayBillDetail = WayBillDetailGet().waybill_detail_get(self.waybillID).json()['content']['transportCashDetail']
        self.logger.info('修改后的运单详情：{0}'.format(wayBillDetail))
        self.assertEqual(wayBillDetail['handlingFee'], self.handlingFee)
        self.assertEqual(wayBillDetail['deliveryFee'], self.deliveryFee)
        self.assertEqual(wayBillDetail['oilCardDeposit'], self.oilCardDeposit)
        self.assertEqual(wayBillDetail['otherFee'], self.otherFee)

if __name__ == '__main__':
    unittest.main()