import unittest
import datetime
from util.log.log import Log
from interface.waybill.waybill_delete import WayBillDelete
from bvt.common.createwaybill import CreateWayBill


class DeleteWayBillCase(unittest.TestCase):
    """删除运单"""
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestDeleteWayBill START ###########################')
        time = str(datetime.date.today())
        self.wayBillId = CreateWayBill().create_waybill('2', time, '北京', '北京', '天津', '天津', '1000', '10',
                                                        '0.01', '0.02', '0.03', '0.04', '1', '备注我要录单测试',
                                                        'TMS', '快递', '10', '10', '10', '10', '10')[0]
        self.logger.info('创建的运单号是：%s' % self.wayBillId)
        pass

    def tearDown(self):
        self.logger.info('########################### TestDeleteWayBill END ###########################')
        pass

    # '''ddt demo'''
    # from parameterized import parameterized
    # from biz.waybill.mockparamsdata import MockParamsData
    # @parameterized.expand(MockParamsData.generate(1))
    def test_bvt_normal_delete(self):
        response = WayBillDelete().waybill_delete(self.wayBillId)
        self.logger.info('删除运单的结果：%s' % response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
