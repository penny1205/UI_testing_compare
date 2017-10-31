#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import os
import time
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
from interface.waybill.waybill_detail_get import WayBillDetailGet
from interface.waybill.waybill_departure_confirm import WayBillDepartureConfirm
from interface.waybill.waybill_arrival_confirm import WayBillArrivalConfirm
from interface.waybill.waybill_receipt_upload import WayBillReceiptUpload
from interface.waybill.waybill_receipt_comfirm_V2 import WayBillReceiptConfirm
from bvt.common.create_waybill import CreateWayBill
from interface.statement.statement_export import StatementExport

class TestStatementExport(unittest.TestCase):
    '''客户/供应商对账单导出'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('######################## TestProfitReportSelect START ########################')
        carType = str(random.randint(1, 2))
        self.applyDate = time.strftime('%Y-%m-%d')
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
        receipt_0 = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'logo.png'

        wayBillId = CreateWayBill().create_waybill(carType, self.applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行', '张三',
                                                        '中原物流项目', startTime,
                                                        endTime, '中原物流', 'ZYWL20171020', phone, '张经理', '赵师傅',
                                                        mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard,
                                                        photoTransPort, carNo, carLength, carModel, '10')[0]
        WayBillDepartureConfirm().waybill_departure_confirm(wayBillId)
        waybill_transport_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        self.wayBillNo = waybill_transport_detail['transportCash']['tmsBillCode']
        WayBillArrivalConfirm().waybill_arrival_confirm(wayBillId,
                                                        waybill_transport_detail['transportCash']['destAmt'],
                                                        waybill_transport_detail['transportCash']['destAmtMemo'])
        WayBillReceiptUpload().waybill_receipt_upload(wayBillId, 'Y', 'Y', 'N', '回单上传测试', 'C', receipt_0)
        waybill_arrived_detail = WayBillDetailGet().waybill_detail_get(wayBillId).json()['content']
        WayBillReceiptConfirm().waybill_receipt_confirm(wayBillId, waybill_arrived_detail['transportCash']['retAmt'],
                                                        '金额变动', '有异常',receipt_0)


    def tearDown(self):
        self.logger.info('######################## TestProfitReportSelect END #########################')


    def test_statement_export_success(self):
        '''客户/供应商对账单导出'''
        billType = random.randint(1, 2)
        response = StatementExport().statement_export(billType=billType,applyDateFirst=self.applyDate ,
                                                      applyDateLast=self.applyDate )
        self.logger.info('客户/供应商对账单导出返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        filename = FileUtil.getProjectObsPath() + '/file/' + 'statement_export.xlsx.'
        with open(filename, 'wb') as writeIn:
            writeIn.write(response.content)
        self.logger.info('客户/供应商对账单导出文件是：{0}'.format(filename))


if __name__ == '__main__':
    unittest.main()