#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_warn import WayBillWarn
from interface.waybill.waybill_detail_get import WayBillDetailGet
from bvt.common.create_waybill import CreateWayBill

class TestWayBillWarn(unittest.TestCase):
    '''运单预警'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestDepartureConfirmWayBill START ########################')
        carType = str(random.randint(1, 2))
        applyDate = time.strftime('%Y-%m-%d')
        photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.wayBillId = CreateWayBill().create_waybill(carType,applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行', '张三')[0]

        wayBillNo = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']['transportCashDetail']['tmsBillCode']
        self.logger.info('运单预警的运单号是：{0}'.format(wayBillNo))

    def tearDown(self):
        self.logger.info('######################### TestDepartureConfirmWayBill END #########################')
        pass

    def test_waybill_warn_success(self):
        '''运单预警'''
        lat = random.uniform(0,90)
        lng = random.uniform(0,180)
        response = WayBillWarn().waybill_warn(self.wayBillId,lat,lng)
        self.logger.info('运单预警返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('运单预警返回结果：{0}'.format(response.json()))

if __name__ == "__main__":
    unittest.main()