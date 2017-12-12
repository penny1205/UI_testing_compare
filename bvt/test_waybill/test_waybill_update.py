#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_update import WayBillUpdate
from interface.waybill.waybill_detail_get import WayBillDetailGet
from bvt.common.create_waybill import CreateWayBill

class TestWayBillUpdate(unittest.TestCase):
    '''修改运单 '''

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestUpdateWayBill START ###########################')
        self.carType = str(random.randint(1, 2))
        self.applyDate = time.strftime('%Y-%m-%d')
        self.photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.photoIdFront = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'frontIdCard.jpg'
        self.photoIdReserve = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'backIdCard.jpg'
        self.photoDriverCard = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoDriverCard.jpg'
        self.photoTransPort = FileUtil.getProjectObsPath() + os.path.sep + 'image' + os.path.sep + 'photoTransPort.jpg'
        self.wayBillId, self.mobile, self.name, self.idNo,self.carNo,self.carLength, self.carModel, self.projectName, \
        self.projectId, self.supplierName, self.supplierId= CreateWayBill().create_waybill(
            self.carType, self.applyDate, self.photoAirWay, '北京', '北京', '', '天津', '天津', '', '1000', '10', '0.01',
            '0.02', '0.03', '0.04', '1', '备注我要录单测试', 'TMS',
            '零担', '10', '100', '1000', '10000', '100000', '20', '30','40', '50', 'DD001', 'YK001', 'LSVAM4187C2184847',
            '6222810001000', '中国银行','张三')

    def tearDown(self):
        self.logger.info('############################ TestUpdateWayBill END ############################')

    def test_waybill_update_applyDate_success(self):
        '''修改运单的发车时间'''
        self.applyDate_update = time.strftime('%Y-%m-%d', time.localtime(time.time() + 172800))
        response = WayBillUpdate().waybill_update(self.wayBillId,self.carType,self.applyDate_update,
                                                  self.projectName,self.projectId, self.supplierName, self.supplierId,
                                                  self.name, self.idNo, self.mobile, self.carNo,self.carLength,
                                                  self.carModel,self.photoAirWay,'', '北京', '北京', '', '天津', '天津',
                                                  '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                  '备注我要录单测试', 'TMS','零担', '10', '100', '1000', '10000',
                                                  '100000','20', '30', '40', '50', 'DD001', 'YK001', 'LSVAM4187C2184847',
                                                  '6222810001000', '中国银行', '张三')
        self.logger.info('请求url：{0} '.format(response.request.url))
        self.logger.info('请求body：{0} '.format(response.request.body))
        self.logger.info('修改运单的发车时间返回状态码：{0}'.format(response))
        self.logger.info('修改运单的发车时间返回：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        response_get = WayBillDetailGet().waybill_detail_get(self.wayBillId)
        self.assertEqual(self.applyDate_update, response_get.json()['content']['transportCash']['applyDate'],
                         'Waybill updated fail!')

if __name__ == "__main__":
    unittest.main()