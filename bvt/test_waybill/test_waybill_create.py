#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_select import WayBillSelect
from bvt.common.create_waybill import CreateWayBill
from interface.waybill.waybill_driver_confirm import WayBillDriverConfirm

class TestWayBillCreate(unittest.TestCase):
    '''我要录单 '''

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCreateWayBill START ###########################')
        self.applyDate = time.strftime('%Y-%m-%d')
        self.photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'

    def tearDown(self):
        self.logger.info('############################ TestCreateWayBill END ############################')
        pass

    def test_waybill_create_company_success(self):
        '''我要录单 创建公司车运单'''

        wayBillId,mobile,name,idNo,carNo = CreateWayBill().create_waybill('1',self.applyDate,self.photoAirWay,
                                                          '北京','北京','','天津','天津','', '1000', '10', '0.01',
                                                          '0.02', '0.03', '0.04', '1', '备注我要录单测试','TMS',
                                                          '零担' ,'10', '100', '1000', '10000', '100000', '20','30',
                                                          '40','50','DD001','YK001','LSVAM4187C2184847','6222810001000',
                                                          '中国银行合肥分行','张三')[:5]
        waybill_list = WayBillSelect().waybill_select(normalCondition=carNo,searchStatus=True).json()['content']['dataList']
        L = []
        for waybill in waybill_list:
            L.append(waybill['id'])
        self.assertIn(wayBillId, L, 'Waybill created fail!')

    def test_waybill_create_outside_driver_success(self):
        '''我要录单 创建外请车运单'''
        wayBillId, mobile, name, idNo, carNo = CreateWayBill().create_waybill('2',self.applyDate,self.photoAirWay,
                                                          '北京','北京','','天津','天津','', '1000', '10', '0.01',
                                                          '0.02', '0.03', '0.04', '1', '备注我要录单测试','TMS',
                                                          '零担' ,'10', '100', '1000', '10000', '100000', '20','30',
                                                          '40','50','DD001','YK001','LSVAM4187C2184847','6222810001000',
                                                          '中国银行', '张三')[:5]

        waybill_list = WayBillSelect().waybill_select(normalCondition=carNo,searchStatus=True).json()['content']['dataList']
        L = []
        for waybill in waybill_list:
            L.append(waybill['id'])
        self.assertIn(wayBillId, L, 'Waybill created fail!')


    # def test_wabill_create_register_driver(self):
    #     '''已注册司机创建运单并司机发车确认'''
    #     count =0
    #     while count < 150:
    #         waybillID = CreateWayBill().create_waybill_register().json()['content']
    #         self.logger.info('新建运单，生成的运单ID为{0}'.format(waybillID))
    #         WayBillDriverConfirm().waybill_driver_confirm(waybillID, totalAmt='0.05', preAmt='0.01',
    #                                                                    oilAmt='0.01', destAmt='0.01', lastAmt='0.01')
    #         count +=1

if __name__ == "__main__":
    unittest.main()