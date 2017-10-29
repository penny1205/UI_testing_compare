#__author__ = 'pan'
# -*- coding:utf-8 -*-

import re
import os
import time
import random
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from util.data.datautil import DataUtil
from interface.waybill.waybill_select import WayBillSelect
from bvt.common.create_waybill import CreateWayBill

class TestWayBillSelect(unittest.TestCase):
    '''运单查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSelectWayBill START ###########################')
        self.carType = str(random.randint(1, 2))
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

        self.wayBillId = CreateWayBill().create_waybill(self.carType, self.applyDate, photoAirWay, '北京', '北京', '', '天津',
                                                        '天津', '', '1000', '10', '0.01', '0.02', '0.03', '0.04', '1',
                                                        '备注我要录单测试', 'TMS', '零担', '10', '100', '1000',
                                                        '10000', '100000', '20', '30', '40', '50', 'DD001', 'YK001',
                                                        'LSVAM4187C2184847', '6222810001000', '中国银行','张三',
                                                        '中原物流项目', startTime,
                                                        endTime, '中原物流', 'ZYWL20171020', phone, '张经理', '赵师傅',
                                                        mobile, idNo, photoIdFront, photoIdReserve, photoDriverCard,
                                                        photoTransPort, carNo, carLength, carModel, '10')[0]

    def tearDown(self):
        self.logger.info('############################ TestSelectWayBill END ############################')
        pass


    def test_waybill_select_vague_success(self):
        '''运单查询 模糊查询'''
        vague = '13077327099'
        response = WayBillSelect().waybill_select(normalCondition=vague, searchStatus=True)
        self.logger.info('运单查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('模糊查询输入的查询条件是：{0}，查询结果是：{1}'.format(vague, response.json()))
        waybill_list = response.json()['content']['dataList']
        if (vague != '') and (vague != None):
            if waybill_list != None:
                L = []
                for waybill in waybill_list:
                    for k, v in waybill.items():
                        match = re.search(vague, str(v))
                        if match is not None:
                            L.append(True)
                        else:
                            L.append(False)
                self.assertIn(False, L)
        else:
            pass

    def test_waybil_selectl_applyDate_success(self):
        '''按用车日期查询'''
        response = WayBillSelect().waybill_select(rows='1000',applyDateFirst=self.applyDate,applyDateLast=self.applyDate)
        self.logger.info('运单查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的查询条件用车日期是：{0}，查询结果是：{1}'.format(self.applyDate, response.json()))
        waybill_list = response.json()['content']['dataList']
        if waybill_list != None:
            L = []
            for waybill in waybill_list:
                L.append(waybill['id'])
            self.assertIn(self.wayBillId,L)

    def test_waybill_select_carType_success(self):
        '''按用车性质查询'''
        response = WayBillSelect().waybill_select(rows='1000',carType=self.carType)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的查询条件用车性质是：{0}，查询结果是：{1}'.format(self.carType, response.json()))
        waybill_list = response.json()['content']['dataList']
        if waybill_list != None:
            L = []
            for waybill in waybill_list:
                L.append(waybill['id'])
            self.assertIn(self.wayBillId,L)


if __name__ == '__main__':
    unittest.main()