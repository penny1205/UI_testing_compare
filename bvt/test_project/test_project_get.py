#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.project.project_get import ProjectGet
from bvt.common.create_project import CreateProject

class TestProjectGet(unittest.TestCase):
    ''' 获取項目详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestProjectGet START ###########################')
        self.projectName = '测试项目'
        self.beginTime = time.strftime('%Y-%m-%d')
        self.endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()+86400))
        self.customerName = '测试之家'
        self.customerCode = 'CSZJ201710200001'
        self.phone = DataUtil().createmoble()
        self.projectId = CreateProject().create_project(self.projectName,self.beginTime,self.endTime,self.customerName,
                                                        self.customerCode,self.phone,'黄经理')

    def tearDown(self):
        self.logger.info('############################ TestProjectGet END ############################')


    def test_project_create_success(self):
        '''获取項目详情'''
        response = ProjectGet().project_get(self.projectId)
        self.logger.info('获取項目详情返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取項目详情返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()