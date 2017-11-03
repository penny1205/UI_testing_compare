#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_tracking_trajectory_create import WayBillTrackingTrajectoryCreate
from interface.waybill.waybill_tracking_trajectory_select import WayBillTrackingTrajectorySelect
from interface.waybill.waybill_detail_get import WayBillDetailGet
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTrackingTrajectorySelect(unittest.TestCase):
    '''查询手动运单跟踪轨迹'''
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
        self.logger.info('查询手动运单跟踪轨迹的运单号是：{0}'.format(wayBillNo))
        self.address = '合肥蜀山区道路拥堵'
        WayBillTrackingTrajectoryCreate().waybill_tracking_trajectory_create(self.wayBillId, self.address)

    def tearDown(self):
        self.logger.info('######################### TestDepartureConfirmWayBill END #########################')
        pass

    def test_waybill_tracking_trajectory_select_success(self):
        '''查询手动运单跟踪轨迹'''
        response = WayBillTrackingTrajectorySelect().waybill_tracking_trajectory_select(self.wayBillId)
        self.logger.info('查询手动运单跟踪轨迹返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('查询手动运单跟踪轨迹返回结果：{0}'.format(response.json()))
        self.assertEqual( self.address,response.json()['content'][0]['address'],'查询手动运单跟踪轨迹失败！')

if __name__ == "__main__":
    unittest.main()