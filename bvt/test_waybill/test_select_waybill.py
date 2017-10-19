#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import re
import random
import unittest
from util.log.log import Log
from interface.waybill.waybill_select import WayBillSelect
from bvt.common.create_waybill import CreateWayBill

class TestSelectWayBill(unittest.TestCase):
    '''运单查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSelectWayBill START ###########################')

        global carType,applyDate,sendCity,arriveCity,wayBillId,mobile,name,idNo,carNo
        carType =str(random.randint(1,2))
        applyDate = time.strftime('%Y-%m-%d')
        sendCity = '北京'
        arriveCity = '天津'
        wayBillId,mobile,name,idNo,carNo = CreateWayBill().create_waybill(carType,applyDate,'北京',sendCity,'天津',
            arriveCity,'1000','10','0.01','0.02','0.03','0.04','1','我要录单','TMS','快递','10', '10', '10', '10', '10')

    def tearDown(self):
        self.logger.info('############################ TestSelectWayBill END ############################')
        pass


    def test_vague_select_waybill_success(self):
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

    def test_applyDate_select_waybill_success(self):
        '''按用车日期查询'''
        response = WayBillSelect().waybill_select(rows='1000',applyDateFirst=applyDate,applyDateLast=applyDate)
        self.logger.info('运单查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的查询条件用车日期是：{0}，查询结果是：{1}'.format(applyDate, response.json()))
        waybill_list = response.json()['content']['dataList']
        if waybill_list != None:
            L = []
            for waybill in waybill_list:
                L.append(waybill['id'])
            self.assertIn(wayBillId,L)

    def test_carType_select_waybill_success(self):
        '''按用车性质查询'''
        response = WayBillSelect().waybill_select(rows='1000',carType=carType)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入的查询条件用车性质是：{0}，查询结果是：{1}'.format(carType, response.json()))
        waybill_list = response.json()['content']['dataList']
        if waybill_list != None:
            L = []
            for waybill in waybill_list:
                L.append(waybill['id'])
            self.assertIn(wayBillId,L)

    # def test_carType_select_waybill_success(self):
    #     '''按查询'''
    #     response = WayBillSelect().waybill_select(rows='1000', carType=carType)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['code'], 0)
    #     self.logger.info('输入的查询条件用车性质是：{0}，查询结果是：{1}'.format(carType,response.json()))
    #     waybill_list = response.json()['content']['dataList']
    #     if waybill_list != None:
    #         L = []
    #         for waybill in waybill_list:
    #             L.append(waybill['id'])
    #         self.assertIn(wayBillId, L)


if __name__ == '__main__':
    unittest.main()