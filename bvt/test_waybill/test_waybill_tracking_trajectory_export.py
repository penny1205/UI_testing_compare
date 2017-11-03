#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_tracking_trajectory_export import WayBillTrackingTrajectoryExport
from interface.waybill.waybill_detail_get import WayBillDetailGet
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTrackingTrajectoryExport(unittest.TestCase):
    '''运单跟踪 定位信息批量导出'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestDepartureConfirmWayBill START ########################')
        carType = str(random.randint(1, 2))
        applyDate = time.strftime('%Y-%m-%d')
        photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.wayBillId = CreateWayBill().create_waybill(carType, applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行','张三')[0]
        wayBillNo = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']['transportCashDetail']['tmsBillCode']
        self.logger.info('定位信息批量导出的运单号是：{0}'.format(wayBillNo))

    def tearDown(self):
        self.logger.info('######################### TestDepartureConfirmWayBill END #########################')
        pass

    def test_waybill_tracking_trajectory_export_success(self):
        '''运单跟踪 定位信息批量导出'''
        sendDateFirst = time.strftime('%Y-%m-%d')
        sendDateLast = time.strftime('%Y-%m-%d')
        response = WayBillTrackingTrajectoryExport().waybill_tracking_trajectory_export(sendDateFirst=sendDateFirst,sendDateLast=sendDateLast)
        self.logger.info('定位信息批量导出返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        filename = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_tracking_trajectory_export.xlsx.'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('定位信息批量导出文件名称：{0}'.format(filename))

if __name__ == "__main__":
    unittest.main()