# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.payment.approval_toal_amt_get import ApprovalTotalAmtGet


class TestApprovalTotalAmtGet(unittest.TestCase):
    ''' 获取今日借款中金额 '''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestApprovalTotalAmtGet START ###########################')

    def tearDown(self):
        self.logger.info('########################### TestApprovalTotalAmtGet END ###########################')

    def test_approval_total_amt_get_success(self):
        '''获取今日借款中金额'''
        response = ApprovalTotalAmtGet().approval_total_amt_get()
        self.logger.info('获取今日借款中金额返回状态码：{0}'.format(response))
        self.logger.info('获取今日借款中金额返回结果：{0}'.format(response.json()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)

if __name__ == '__main__':
    unittest.main()