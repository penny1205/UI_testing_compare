#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
from util.log.log import Log
from interface.waybill.waybill_detail_get import WayBillDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_arrival_confirm import WayBillArrivalConfirm
from bvt.common.createwaybill import CreateWayBill

class TestArrivalConfirmWayBill(unittest.TestCase):
    '''到达确认'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSelectWayBill START ###########################')

        global carType,applyDate,sendCity,arriveCity,wayBillId,mobile,name,idNo,carNo
        carType = str(random.randint(1,2))
        applyDate = time.strftime('%Y-%m-%d')
        sendCity = '北京'
        arriveCity = '天津'
        wayBillId,mobile,name,idNo,carNo = CreateWayBill().create_waybill(carType,applyDate,'北京',sendCity,'天津',
            arriveCity,'1000','10','0.01','0.02','0.03','0.04','1','测试','TMS','快递','10', '10', '10', '10', '10')

    def tearDown(self):
        self.logger.info('############################ TestSelectWayBill END ############################')
        pass

    def test_arrival_confirm_waybill_success(self):
        '''到达确认'''
        WayBillDepartureConfirm().waybill_departure_confirm(wayBillId)
        waybill_transport_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        response = WayBillArrivalConfirm().waybill_arrival_confirm(wayBillId,waybill_transport_detail['transportCash']['destAmt'],
                                                                   waybill_transport_detail['transportCash']['destAmtMemo'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        waybill_arrived_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        self.logger.info('到达确认的运单号是：{0}'.format(waybill_arrived_detail['transportCashDetail']['tmsBillCode']))
        self.assertEqual(waybill_arrived_detail['transportCash']['billStatus'], 'D')
        self.assertEqual(waybill_arrived_detail['transportCash']['transStatus'], 'A')

if __name__ == "__main__":
    unittest.main()