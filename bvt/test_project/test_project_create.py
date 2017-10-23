#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.project.project_select import ProjectSelect
from bvt.common.create_project import CreateProject

class TestProjectCreate(unittest.TestCase):
    '''新增项目'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestProjectCreate START ###########################')
        self.projectName = '测试项目'
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.customerName = '测试之家'
        self.customerCode = 'CSZJ201710200001'
        self.phone = DataUtil().createmoble()


    def tearDown(self):
        self.logger.info('############################ TestProjectCreate END ############################')


    def test_project_create_success(self):
        '''新增项目'''
        CreateProject().create_project(self.projectName,self.startTime,self.endTime,self.customerName,self.customerCode,
                                       self.phone,'黄经理')
        project_list = ProjectSelect().project_select(projectName=self.projectName,projectStatus='0').json()['content']['dataList']
        if project_list != []:
            L = []
            for project in project_list:
                L.append(str(project['projectName']))
            self.assertIn(self.projectName, L, 'project created fail!')
        else:
            self.logger.error('Please check the results of the project for empty')

if __name__ == '__main__':
    unittest.main()