#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
from interface.waybill.waybill_select import WayBillSelect
from bvt.common.create_waybill import CreateWayBill

class TestWayBillCreate(unittest.TestCase):
    '''我要录单 '''

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCreateWayBill START ###########################')
        self.applyDate = time.strftime('%Y-%m-%d')
        self.photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.phone = DataUtil().createmoble()
        self.mobile = DataUtil().createmoble()
        self.idNo = DataUtil().genneratorIdNo()
        self.carNo = DataUtil().genneratorCarNo()
        self.carLength = DataUtil().genneratorCarLength()
        self.carModel = DataUtil().genneratorCarTypeInfo()
        self.photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
        self.photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
        self.photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
        self.photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'


    def tearDown(self):
        self.logger.info('############################ TestCreateWayBill END ############################')
        pass

    def test_waybill_create_company_success(self):
        '''我要录单 创建公司车运单'''

        wayBillId,mobile = CreateWayBill().create_waybill('1',self.applyDate,self.photoAirWay,
                                                          '北京','北京','','天津','天津','', '1000', '10', '0.01',
                                                          '0.02', '0.03', '0.04', '1', '备注我要录单测试','TMS',
                                                          '零担' ,'10', '100', '1000', '10000', '100000', '20','30',
                                                          '40','50','DD001','YK001','LSVAM4187C2184847','6222810001000',
                                                          '中国银行','张三', '中原物流项目',self.startTime,self.endTime,
                                                          '中原物流', 'ZYWL20171020',self.phone,'张经理',
                                                          '赵师傅',self.mobile,self.idNo,self.photoIdFront,
                                                          self.photoIdReserve, self.photoDriverCard, self.photoTransPort,
                                                          self.carNo,self.carLength, self.carModel, '10')[:2]

        waybill_list = WayBillSelect().waybill_select(normalCondition=mobile,searchStatus=True).json()['content']['dataList']
        L = []
        for waybill in waybill_list:
            L.append(waybill['id'])
        self.assertIn(wayBillId, L, 'Waybill created fail!')

    def test_waybill_create_outside_driver_success(self):
        '''我要录单 创建外请车运单'''
        wayBillId,mobile = CreateWayBill().create_waybill('2',self.applyDate,self.photoAirWay,
                                                          '北京','北京','','天津','天津','', '1000', '10', '0.01',
                                                          '0.02', '0.03', '0.04', '1', '备注我要录单测试','TMS',
                                                          '零担' ,'10', '100', '1000', '10000', '100000', '20','30',
                                                          '40','50','DD001','YK001','LSVAM4187C2184847','6222810001000',
                                                          '中国银行', '张三','中原物流项目',self.startTime,self.endTime,'中原物流',
                                                          'ZYWL20171020',self.phone,'张经理',
                                                          '赵师傅',self.mobile,self.idNo,self.photoIdFront,
                                                          self.photoIdReserve, self.photoDriverCard, self.photoTransPort,
                                                          self.carNo,self.carLength, self.carModel, '10')[:2]

        waybill_list = WayBillSelect().waybill_select(normalCondition=mobile,searchStatus=True).json()['content']['dataList']
        L = []
        for waybill in waybill_list:
            L.append(waybill['id'])
        self.assertIn(wayBillId, L, 'Waybill created fail!')

if __name__ == "__main__":
    unittest.main()