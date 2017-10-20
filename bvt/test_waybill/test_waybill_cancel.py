import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
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
        startTime = time.strftime('%Y-%M-%d')
        endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        phone = DataUtil().createmoble()
        mobile = DataUtil().createmoble()
        idNo = DataUtil().genneratorIdNo()
        carNo = DataUtil().genneratorCarNo()
        carLength = DataUtil().genneratorCarLength()
        carModel = DataUtil().genneratorCarTypeInfo()
        photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
        photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
        photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
        photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'

        self.wayBillId  = CreateWayBill().create_waybill(carType, applyDate, photoAirWay,'北京', '北京', '', '天津',
                                                         '天津', '', '1000', '10', '0.01','0.02', '0.03', '0.04', '1',
                                                         '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                         '10000', '100000','20', '30', '40', '50', 'DD001', 'YK001',
                                                         'LSVAM4187C2184847', '6222810001000','中原物流项目',startTime,
                                                         endTime, '中原物流','ZYWL20171020', phone, '张经理', '赵师傅',
                                                         mobile, idNo, photoIdFront,photoIdReserve, photoDriverCard,
                                                         photoTransPort,carNo,carLength, carModel, '10')[0]

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
