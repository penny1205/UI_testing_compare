#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_delete import WayBillDelete
from interface.waybill.waybill_deleted_empty import WayBillDeletedEmpty
from interface.waybill.waybill_deleted_select import WayBillDeletedSelect
from interface.waybill.waybill_detail_get import WayBillDetailGet
from bvt.common.create_waybill import CreateWayBill
from bvt.common.settings import Settings

class TestWayBillDeletedEmpty(unittest.TestCase):
    '''清空/恢复回收站'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestGetDetailWayBill START ###########################')
        self.carType = str(random.randint(1, 2))
        self.applyDate = time.strftime('%Y-%m-%d')
        photoAirWay = FileUtil.getProjectObsPath() + '/image/photoAirWay.jpg'
        self.wayBillId = CreateWayBill().create_waybill(self.carType, self.applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行','张三')[0]
        Settings().system_params_update()
        WayBillDelete().waybill_delete(self.wayBillId)

    def tearDown(self):
        self.logger.info('############################ TestGetDetailWayBill END ############################')
        pass


    def test_waybill_deleted_empty_success(self):
        '''清空回收站'''
        response = WayBillDeletedEmpty().waybill_deleted_empty(1)
        self.logger.info('清空回收站返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('清空回收站查询结果是：{0}'.format(response.json()))
        waybill_deleted_list =  WayBillDeletedSelect().waybill_deleted_select().json()['content']['dataList']
        if waybill_deleted_list != []:
            self.logger.error('Empty recycle bin failed!')

    # def test_waybill_deleted_restore_success(self):
    #     '''恢复回收站'''
    #     response = WayBillDeletedEmpty().waybill_deleted_empty(2)
    #     self.logger.info('恢复回收站返回状态码：{0}'.format(response))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['code'], 0)
    #     self.logger.info('恢复回收站查询结果是：{0}'.format(response.json()))
    #     waybill_deleted_list = WayBillDeletedSelect().waybill_deleted_select().json()['content']['dataList']
    #     if waybill_deleted_list != []:
    #         self.logger.error('Restore recycle bin failed!')
    #     wayBill = WayBillDetailGet().waybill_detail_get(self.wayBillId).json()['content']
    #     self.assertEqual(wayBill['transportCash']['delStatus'],0,'Restore recycle bin failed!')

if __name__ == '__main__':
    unittest.main()