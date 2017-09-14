#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from parameterized import parameterized
from util.log.log import Log
from interface.waybill.waybill_select import WayBillSelect
from bvt.common.createwaybill import CreateWayBill

class TestCreateWayBill(unittest.TestCase):
    '''我要录单'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWayBill START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWayBill END ############################')
        pass

    @parameterized.expand([
        ('2','2017-09-14','北京','北京','天津','天津','1000','10','0.01','0.02','0.03','0.04','1'
         ,'备注我要录单测试','TMS','快递','10','10','10','10','10'),
    ])
    def test_waybill_success(self,carType,applyDate,sendProvince,sendCity,arriveProvince,arriveCity,
                             income,totalAmt,preAmt,oilAmt,destAmt,lastAmt,hasReceipt,content,source,
                             cargoName,cargoWeight,cargoVolume,cargoNumberOfCases,cargoWorth,insuranceCosts):
        '''我要录单成功'''

        waybillCreated,mobile = CreateWayBill().create_waybill(carType,applyDate,sendProvince,sendCity,arriveProvince,arriveCity,
                                                               income,totalAmt,preAmt,oilAmt,destAmt,lastAmt,hasReceipt,
                                                               content,source,cargoName,cargoWeight,cargoVolume,
                                                               cargoNumberOfCases,cargoWorth,insuranceCosts)
        waybill_list = WayBillSelect().waybill_select(normalCondition=mobile,searchStatus=True).json()['content']['dataList']
        if waybill_list == None:
            self.logger.info('Waybill created fail!')
        else:
            L = []
            for waybill in waybill_list:
                L.append(waybill['id'])
            self.assertIn(waybillCreated,L,'Waybill created fail!')

if __name__ == "__main__":
    unittest.main()