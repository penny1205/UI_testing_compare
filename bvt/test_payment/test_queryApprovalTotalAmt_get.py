# -*- coding:utf-8 -*-

import unittest
import datetime
import random
from util.log.log import Log
from interface.payment.payment_queryApprovalTotalAmt_get import QueryApprovalTotalAmtGet


class GetQueryApprovalTotalAmt(unittest.TestCase):
    """ 查询出当日未从可借款金额中扣除的贷款总额 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestGetQueryApprovalTotalAmt START ###########################')
        pass

    def tearDown(self):
        self.logger.info('########################### TestGetQueryApprovalTotalAmt END ###########################')
        pass

    def test_queryApprovalTotalAmt_get(self):
        response = QueryApprovalTotalAmtGet().queryapprovaltotalamt_get()
        self.logger.info('查询结果：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
