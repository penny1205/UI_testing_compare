#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_detail_get import WayBillDetailGet
from bvt.common.create_waybill import CreateWayBill

class TestWayBillDetailGet(unittest.TestCase):
    '''获取运单详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestGetDetailWayBill START ###########################')
        self.carType = str(random.randint(1, 2))
        self.applyDate = time.strftime('%Y-%m-%d')
        photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.wayBillId = CreateWayBill().create_waybill(self.carType, self.applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行','张三')[0]

    def tearDown(self):
        self.logger.info('############################ TestGetDetailWayBill END ############################')
        pass


    def test_waybill_detail_get_success(self):
        '''获取运单详情'''
        response = WayBillDetailGet().waybill_detail_get(self.wayBillId)
        self.logger.info('获取运单详情返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.logger.info('模获取运单详情查询结果是：{0}'.format(response.json()))
        self.assertEqual(response.json()['code'], 0)


if __name__ == '__main__':
    unittest.main()