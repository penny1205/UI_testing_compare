#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
import os
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_detail_get import WayBillDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_arrival_confirm import WayBillArrivalConfirm
from interface.waybill.waybill_receipt_upload import WayBillReceiptUpload
from bvt.common.createwaybill import CreateWayBill


class TestReceiptUploadWayBill(unittest.TestCase):
    """回单上传"""
    def setUp(self):
        self.logger = Log()
        self.logger.info('####################### TestReceiptUploadWayBill START #######################')

        global carType,applyDate,sendCity,arriveCity,wayBillId,mobile,name,idNo,carNo
        carType = str(random.randint(1,2))
        applyDate = time.strftime('%Y-%m-%d')
        sendCity = '北京'
        arriveCity = '天津'
        wayBillId,mobile,name,idNo,carNo = CreateWayBill().create_waybill(carType,applyDate,'北京',sendCity,'天津',
            arriveCity,'1000','10','0.01','0.02','0.03','0.04','1','测试','TMS','快递','10', '10', '10', '10', '10')

        global receipt_0
        receipt_0 = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'logo.png'

    def tearDown(self):
        self.logger.info('######################## TestReceiptUploadWayBill END ########################')
        pass

    def test_receipt_upload_waybill_success(self):
        """回单上传"""
        WayBillDepartureConfirm().waybill_departure_confirm(wayBillId)
        waybill_transport_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        WayBillArrivalConfirm().waybill_arrival_confirm(wayBillId,waybill_transport_detail['transportCash']['destAmt'],
                                                        waybill_transport_detail['transportCash']['destAmtMemo'])
        response = WayBillReceiptUpload().waybill_receipt_upload(wayBillId, 'Y', 'Y', 'N', '回单上传测试', 'C', receipt_0)
        self.logger.info('回单上传返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        waybill_arrived_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        self.logger.info('回单上传的运单号是：{0}'.format(waybill_arrived_detail['transportCashDetail']['tmsBillCode']))
        self.assertEqual(waybill_arrived_detail['transportCash']['billStatus'], 'H')
        self.assertEqual(waybill_arrived_detail['transportCash']['transStatus'], 'A')

if __name__ == "__main__":
    unittest.main()
