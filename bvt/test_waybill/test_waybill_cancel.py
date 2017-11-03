import time
import random
import unittest
from util.file.fileutil import FileUtil
from util.log.log import Log
from interface.waybill.waybill_cancel import WayBillCancel
from bvt.common.create_waybill import CreateWayBill


class TestWayBillCancel(unittest.TestCase):
    """取消运单"""

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCancelWayBill START ###########################')
        carType = str(random.randint(1, 2))
        applyDate = time.strftime('%Y-%m-%d')
        photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.wayBillId  = CreateWayBill().create_waybill(carType, applyDate, photoAirWay,'北京', '北京', '', '天津',
                                                         '天津', '', '1000', '10', '0.01','0.02', '0.03', '0.04', '1',
                                                         '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                         '10000', '100000','20', '30', '40', '50', 'DD001', 'YK001',
                                                         'LSVAM4187C2184847', '6222810001000', '中国银行','张三')[0]

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

if __name__ == "__main__":
    unittest.main()
