#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
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

        self.wayBillId = CreateWayBill().create_waybill(carType, applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行','张三',
                                                        '中原物流项目', startTime,
                                                        endTime, '中原物流', 'ZYWL20171020', phone, '张经理', '赵师傅',
                                                        mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard,
                                                        photoTransPort, carNo, carLength, carModel, '10')[0]
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
        filename = FileUtil.getProjectObsPath() + '/file/' + 'waybill_tracking_trajectory_export.xlsx.'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('定位信息批量导出文件名称：{0}'.format(filename))

if __name__ == "__main__":
    unittest.main()