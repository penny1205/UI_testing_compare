#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_detail_get import WayBillDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_arrival_confirm import WayBillArrivalConfirm
from interface.waybill.waybill_receipt_upload import WayBillReceiptUpload
from interface.waybill.waybill_receipt_comfirm import WayBillReceiptConfirm
from bvt.common.create_waybill import CreateWayBill

class TestReceiptConfirmWayBill(unittest.TestCase):
    '''回单确认'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('####################### TestReceiptConfirmWayBill START #######################')

        global carType,applyDate,sendCity,arriveCity,wayBillId,mobile,name,idNo,carNo
        carType = str(random.randint(1,2))
        applyDate = time.strftime('%Y-%m-%d')
        sendCity = '北京'
        arriveCity = '天津'
        wayBillId,mobile,name,idNo,carNo = CreateWayBill().create_waybill(carType,applyDate,'北京',sendCity,'天津',
            arriveCity,'1000','10','0.01','0.02','0.03','0.04','1','测试','TMS','快递','10', '10', '10', '10', '10')

        global receipt_0
        receipt_0 = FileUtil.getProjectObsPath() + '/image/logo.png'


    def tearDown(self):
        self.logger.info('######################## TestReceiptConfirmWayBill END ########################')
        pass

    def test_receipt_confirm_waybill_success(self):
        '''回单确认'''
        WayBillDepartureConfirm().waybill_departure_confirm(wayBillId)
        waybill_transport_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        WayBillArrivalConfirm().waybill_arrival_confirm(wayBillId,waybill_transport_detail['transportCash']['destAmt'],
                                                        waybill_transport_detail['transportCash']['destAmtMemo'])
        WayBillReceiptUpload().waybill_receipt_upload(wayBillId,'Y','Y','N','回单上传测试','C',receipt_0)
        waybill_arrived_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        response = WayBillReceiptConfirm().waybill_receipt_confirm(wayBillId,
                   waybill_arrived_detail['transportCash']['retAmt'],'金额变动','有异常')
        self.logger.info('回单确认返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        waybill_completed_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        self.logger.info('回单确认的运单号是：{0}'.format(waybill_completed_detail['transportCashDetail']['tmsBillCode']))
        self.assertEqual(waybill_completed_detail['transportCash']['billStatus'], 'S')
        self.assertEqual(waybill_completed_detail['transportCash']['transStatus'],'C')

if __name__ == "__main__":
    unittest.main()