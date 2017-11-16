#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from util.db.dbutil import DBUtil
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from interface.customer.customer_create import CustomerCreate

class CreateCustomer(object):
    '''新增客户'''

    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()

    def create_customer(self,customerName,customerCode,phone,customerDeveloper):
        '''新增客户'''
        try:
            response = CustomerCreate().customer_create(customerName=customerName,customerCode=customerCode,phone=phone,
                                                        customerDeveloper=customerDeveloper)
            self.logger.info('新增的客户名称是: {0}'.format(customerName))
            # 判断客户名称和客户编号是否重复
            if response.json()['code'] == 0:
                return response.json()['content']
            elif response.json()['code'] == 9020103:
                sql = 'DELETE FROM YD_TMS_CUSTOMER WHERE customerName = \'{0}\' and partnerNo = \'{1}\''.format(
                    customerName,self.config['partnerNo'])
                self.DBUtil = DBUtil(host=self.config['db_host'], port=self.config['db_port'],
                                     user=self.config['db_user'],passwd=self.config['db_passwd'],
                                     dbname=self.config['db_dbname'],charset=self.config['db_charset'])
                self.DBUtil.execute_sql(sql)
                customerId = CustomerCreate().customer_create(customerName=customerName,customerCode=customerCode,
                                                              phone=phone,customerDeveloper=customerDeveloper).json()[
                    'content']
                return customerId
            elif response.json()['code'] == 9020104:
                sql = 'DELETE FROM YD_TMS_CUSTOMER WHERE customerCode = \'{0}\'and partnerNo = \'{1}\''.format(
                    customerCode,self.config['partnerNo'])
                self.DBUtil = DBUtil(host=self.config['db_host'], port=self.config['db_port'],
                                     user=self.config['db_user'], passwd=self.config['db_passwd'],
                                     dbname=self.config['db_dbname'],charset=self.config['db_charset'])
                self.DBUtil.execute_sql(sql)
                customerId = CustomerCreate().customer_create(customerName=customerName,
                                                              customerCode=customerCode, phone=phone,
                                                              customerDeveloper=customerDeveloper).json()['content']
                return customerId
            else:
                self.logger.info('新增客户返回错误:{0}'.format(response.json()))
                return None
        except Exception:
            self.logger.error('新增客户发生异常:{0}'.format(Exception))
            return None