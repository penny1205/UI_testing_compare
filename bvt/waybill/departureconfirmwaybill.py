#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
from util.log.log import Log
from interface.waybill.waybill_detail_get import WayBillDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from bvt.common.createwaybill import CreateWayBill

class TestDepartureConfirmWayBill(unittest.TestCase):
    '''发车确认'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestDepartureConfirmWayBill START ########################')

        global carType,applyDate,sendCity,arriveCity,wayBillId,mobile,name,idNo,carNo
        carType = str(random.randint(1,2))
        applyDate = time.strftime('%Y-%m-%d')
        sendCity = '北京'
        arriveCity = '天津'
        wayBillId,mobile,name,idNo,carNo = CreateWayBill().create_waybill(carType,applyDate,'北京',sendCity,'天津',
            arriveCity,'1000','10','0.01','0.02','0.03','0.04','1','测试','TMS','快递','10', '10', '10', '10', '10')

    def tearDown(self):
        self.logger.info('######################### TestDepartureConfirmWayBill END #########################')
        pass

    def test_departure_confirm_waybill_success(self):
        '''发车确认'''
        response = WayBillDepartureConfirm().waybill_departure_confirm(wayBillId)
        self.logger.info('发车确认返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        waybill_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        self.logger.info('发车确认的运单号是：{0}'.format(waybill_detail['transportCashDetail']['tmsBillCode']))
        self.assertEqual(waybill_detail['transportCash']['billStatus'],'X')

if __name__ == "__main__":
    unittest.main()