# -*- coding:utf-8 -*-

import unittest
import datetime
import random
from util.log.log import Log
from interface.payment.payment_countAmt_get import CountAmtGet


class GetCountAmt(unittest.TestCase):
    """ 待支付合计金额统计 """
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestGetCountAmt START ###########################')
        self.lastDate = str(datetime.date.today())
        self.firstDate = str(datetime.date.today().replace(day=1))
        self.countname = random.sample(['amtFee', 'cash', 'oilFee', 'destAmtConfirm', 'retAmtConfirm'], 1)
        self.isCanLoan = random.sample(['', '0', '1'], 1)
        pass

    def tearDown(self):
        self.logger.info('########################### TestGetCountAmt END ###########################')
        pass

    def test_countAmt_get(self):
        response = CountAmtGet().count_amt_get(countName=self.countname, applyDateFirst=self.firstDate,
                                               applyDateLast=self.lastDate, sendCity='北京', arriveCity='天津',
                                               isCanLoan=self.isCanLoan)
        self.logger.info('查询结果：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

