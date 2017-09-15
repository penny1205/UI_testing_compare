#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from interface.waybill.waybill_select import WayBillSelect
from bvt.common.createwaybill import CreateWayBill

class TestCreateWayBill(unittest.TestCase):
    '''我要录单 '''

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCreateWayBill START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestCreateWayBill END ############################')
        pass

    def test_create_company_waybill_success(self):
        '''我要录单 创建公司车运单'''
        applyDate = time.strftime('%Y-%m-%d')
        wayBillId,mobile = CreateWayBill().create_waybill('1',applyDate,'北京','北京','天津','天津', '1000', '10',
                                                               '0.01', '0.02', '0.03', '0.04', '1', '备注我要录单测试',
                                                               'TMS', '快递', '10', '10', '10', '10', '10')[:2]

        waybill_list = WayBillSelect().waybill_select(normalCondition=mobile,searchStatus=True).json()['content']['dataList']
        L = []
        for waybill in waybill_list:
            L.append(waybill['id'])
        self.assertIn(wayBillId, L, 'Waybill created fail!')

    def test_create_outside_driver_waybill_success(self):
        '''我要录单 创建外请车运单'''
        applyDate = time.strftime('%Y-%m-%d')
        wayBillId,mobile = CreateWayBill().create_waybill('2',applyDate,'天津','天津','北京','北京', '1000', '10',
                                                               '0.01', '0.02', '0.03', '0.04', '1', '备注我要录单测试',
                                                               'TMS', '快递', '10', '10', '10', '10', '10')[:2]

        waybill_list = WayBillSelect().waybill_select(normalCondition=mobile,searchStatus=True).json()['content']['dataList']
        L = []
        for waybill in waybill_list:
            L.append(waybill['id'])
        self.assertIn(wayBillId, L, 'Waybill created fail!')

if __name__ == "__main__":
    unittest.main()