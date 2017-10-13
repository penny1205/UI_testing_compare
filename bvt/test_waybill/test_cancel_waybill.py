import unittest
import datetime
from util.log.log import Log
from interface.waybill.waybill_cancel import WayBillCancel
from bvt.common.create_waybill import CreateWayBill


class TestCancelWayBillCase(unittest.TestCase):
    """取消运单"""

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCancelWayBill START ###########################')
        time = str(datetime.date.today())
        self.wayBillId = CreateWayBill().create_waybill('2', time, '北京', '北京', '天津', '天津', '1000', '10',
                                                        '0.01', '0.02', '0.03', '0.04', '1', '备注我要录单测试',
                                                        'TMS', '快递', '10', '10', '10', '10', '10')[0]

        self.logger.info('创建的运单号是：%s' % self.wayBillId)
        pass

    def tearDown(self):
        self.logger.info('########################### TestCancelWayBill END ############################')
        pass

    def test_bvt_normal_cancel(self):
        response = WayBillCancel().waybill_cancel(self.wayBillId)
        self.logger.info('取消运单返回状态码：{0}'.format(response))
        self.logger.info('取消运单的结果：%s' % response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
#
# if __name__ == "__main__":
#     unittest.main()