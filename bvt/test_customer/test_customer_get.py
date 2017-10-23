#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.customer.customer_get import CustomerGet
from bvt.common.create_customer import CreateCustomer

class TestCustomerGet(unittest.TestCase):
    ''' 获取客户详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCustomerGet START ###########################')
        self.customerName = '中原物流'
        self.customerCode = 'ZYWL201710200001'
        self.phone = DataUtil().createmoble()
        self.customerId = CreateCustomer().create_customer(self.customerName, self.customerCode, self.phone, '张经理')

    def tearDown(self):
        self.logger.info('############################ TestCustomerGet END ############################')


    def test_customer_create_success(self):
        '''获取客户详情'''
        response = CustomerGet().customer_get(self.customerId)
        self.logger.info('获取客户详情返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取客户详情返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()