#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
from interface.waybill.waybill_detail_get import WayBillDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_arrival_confirm import WayBillArrivalConfirm
from bvt.common.create_waybill import CreateWayBill

class TestWayBillArrivalConfirm(unittest.TestCase):
    '''到达确认'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('####################### TestArrivalConfirmWayBill START #######################')
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

        self.wayBillId  = CreateWayBill().create_waybill(carType, applyDate, photoAirWay,'北京', '北京', '', '天津',
                                                         '天津', '', '1000', '10', '0.01','0.02', '0.03', '0.04', '1',
                                                         '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                         '10000', '100000','20', '30', '40', '50', 'DD001', 'YK001',
                                                         'LSVAM4187C2184847', '6222810001000','中原物流项目',startTime,
                                                         endTime, '中原物流','ZYWL20171020', phone, '张经理', '赵师傅',
                                                         mobile, idNo, photoIdFront,photoIdReserve, photoDriverCard,
                                                         photoTransPort,carNo,carLength, carModel, '10')[0]

    def tearDown(self):
        self.logger.info('######################## TestArrivalConfirmWayBill END ########################')
        pass

    def test_waybill_arrival_confirm_success(self):
        '''到达确认'''
        WayBillDepartureConfirm().waybill_departure_confirm(self.wayBillId)
        waybill_transport_detail = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']
        response = WayBillArrivalConfirm().waybill_arrival_confirm(self.wayBillId,
                                                                   waybill_transport_detail['transportCash']['destAmt'],
                                                            waybill_transport_detail['transportCash']['destAmtMemo'])
        self.logger.info('到达确认返回状态码：{0}'.format(response))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        waybill_arrived_detail = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']
        self.logger.info('到达确认的运单号是：{0}'.format(waybill_arrived_detail['transportCashDetail']['tmsBillCode']))
        self.assertEqual(waybill_arrived_detail['transportCash']['billStatus'], 'D')
        self.assertEqual(waybill_arrived_detail['transportCash']['transStatus'], 'A')

if __name__ == "__main__":
    unittest.main()