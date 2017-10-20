#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.customer.customer_select import CustomerSelect
from bvt.common.create_customer import CreateCustomer

class TestCustomerCreate(unittest.TestCase):
    '''新增客户'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestCustomerCreate START ###########################')
        self.customerName = '中原物流'
        self.customerCode = 'ZYWL201710200001'
        self.phone = DataUtil().createmoble()


    def tearDown(self):
        self.logger.info('############################ TestCustomerCreate END ############################')


    def test_customer_create_success(self):
        '''新增客户'''
        CreateCustomer().create_customer(self.customerName,self.customerCode,self.phone,'张经理')
        customer_list = CustomerSelect().customer_select(customerName=self.customerName,customerStatus='0').json()['content']['dataList']
        if customer_list != []:
            L = []
            for customer in customer_list:
                L.append(str(customer['customerName']))
            self.assertIn(self.customerName, L, 'Customer created fail!')
        else:
            self.logger.error('Please check the results of the customer for empty')

if __name__ == '__main__':
    unittest.main()