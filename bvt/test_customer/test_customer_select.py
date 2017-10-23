#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.customer.customer_select import CustomerSelect
from bvt.common.create_customer import CreateCustomer

class TestCustomerSelect(unittest.TestCase):
    ''' 查询客户列表'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCustomerGet START ###########################')
        self.customerName = '中原物流'
        self.customerCode = 'ZYWL201710200001'
        self.phone = DataUtil().createmoble()
        self.customerId = CreateCustomer().create_customer(self.customerName, self.customerCode, self.phone, '张经理')

    def tearDown(self):
        self.logger.info('############################ TestCustomerGet END ############################')


    def test_customer_select_customerName_success(self):
        '''按客户名称查询客户列表'''
        response = CustomerSelect().customer_select(customerName=self.customerName)
        self.logger.info('按客户名称查询客户列表返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入客户名称：{0}，按客户名称查询客户列表返回结果是：{1}'.format(self.customerName,
                                                                  response.json()))


if __name__ == '__main__':
    unittest.main()