#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.customer.customer_update import CustomerUpdate
from interface.customer.customer_get import CustomerGet
from bvt.common.create_customer import CreateCustomer

class TestCustomerUpdate(unittest.TestCase):
    '''修改客户'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCustomerCreate START ###########################')
        self.customerName = '中原物流'
        self.customerCode = 'ZYWL201710200001'
        self.phone = DataUtil().createmoble()
        self.customerId = CreateCustomer().create_customer(self.customerName, self.customerCode, self.phone,'张经理')


    def tearDown(self):
        self.logger.info('############################ TestCustomerCreate END ############################')


    def test_customer_create_customerName_success(self):
        '''修改客户名称'''
        self.customerName_update = '高通物流'
        response = CustomerUpdate().customer_update(self.customerId,'1',self.customerName_update,self.customerCode,
                                                    self.phone, '张经理')
        self.logger.info('修改客户名称返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('修改客户名称返回：{0}'.format(response.json()))
        response_get = CustomerGet().customer_get(self.customerId)
        self.assertEqual(self.customerName_update, response_get.json()['content']['customerName'],
                         'Customer updated fail!')

if __name__ == '__main__':
    unittest.main()