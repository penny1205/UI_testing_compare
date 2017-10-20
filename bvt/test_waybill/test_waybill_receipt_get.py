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
from interface.waybill.waybill_receipt_upload import WayBillReceiptUpload
from interface.waybill.waybill_receipt_get import WayBillReceiptGet
from bvt.common.create_waybill import CreateWayBill


class TestWayBillReceiptGet(unittest.TestCase):
    '''获取回单详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('####################### TestReceiptUploadWayBill START #######################')
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

        self.wayBillId = CreateWayBill().create_waybill(carType, applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中原物流项目', startTime,
                                                        endTime, '中原物流', 'ZYWL20171020', phone, '张经理', '赵师傅',
                                                        mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard,
                                                        photoTransPort, carNo, carLength, carModel, '10')[0]
        self.receipt_0 = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'logo.png'

    def tearDown(self):
        self.logger.info('######################## TestReceiptUploadWayBill END ########################')
        pass

    def test_waybill_receipt_get_success(self):
        '''获取回单详情'''
        WayBillDepartureConfirm().waybill_departure_confirm(self.wayBillId)
        waybill_transport_detail = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']
        WayBillArrivalConfirm().waybill_arrival_confirm(self.wayBillId,waybill_transport_detail['transportCash']['destAmt'],
                                                        waybill_transport_detail['transportCash']['destAmtMemo'])
        WayBillReceiptUpload().waybill_receipt_upload(self.wayBillId, 'Y', 'Y', 'N', '回单上传测试', 'C',self.receipt_0)
        response = WayBillReceiptGet().waybill_receipt_get(self.wayBillId)
        self.logger.info('获取回单详情回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取回单详情返回结果：{0}'.format(response.json()))
        waybill_arrived_detail = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']
        self.logger.info('获取回单详情的运单号是：{0}'.format(waybill_arrived_detail['transportCashDetail']['tmsBillCode']))
        self.assertEqual(waybill_arrived_detail['transportCash']['billStatus'], 'H')
        self.assertEqual(waybill_arrived_detail['transportCash']['transStatus'], 'A')

if __name__ == "__main__":
    unittest.main()
