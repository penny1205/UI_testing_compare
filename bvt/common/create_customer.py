#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from util.db.dbutil import DBUtil
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from interface.project.customer_create import CustomerCreate
from interface.project.customer_select import CustomerSelect

class CreateCustomer(object):
    '''新增项目'''

    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()

    def create_customer(self,customerName,customerCode,phone,customerDeveloper):
        '''新增项目'''
        try:
            response = CustomerCreate().customer_create(customerName=customerName,customerCode=customerCode,phone=phone,
                                                        customerDeveloper=customerDeveloper)
            self.logger.info('新增的项目名称是: {0}'.format(customerName))
            # 判断客户名称和客户编号是否重复
            if response.json()['code'] == 9020103:
                customer_list = CustomerSelect().customer_select(customerName=customerName).json()['content']['dataList']
                if customer_list != []:
                    for customer in customer_list:
                        DBUtil().conn_get(host=self.config['db_host'], port=self.config['db_port'],
                                          user=self.config['db_user'],passwd=self.config['db_passwd'],
                                          dbname=self.config['db_dbname'])
                        sql = 'DELETE FROM YD_TMS_CUSTOMER WHERE customerName = '
                        DBUtil().execute_sql()

            elif response.json()['code'] == 9020104:
                customer_list = CustomerSelect().customer_select(customerName=customerName)
                return
            else:
                return response.json()['content']
        except Exception:
            return None