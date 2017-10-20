#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.project.project_select import ProjectSelect
from bvt.common.create_project import CreateProject

class TestProjectSelect(unittest.TestCase):
    ''' 查询项目列表'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestProjectSelect START ###########################')
        self.projectName = '测试项目'
        self.beginTime = time.strftime('%Y-%m-%d')
        self.endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()+86400))
        self.customerName = '测试之家'
        self.customerCode = 'CSZJ201710200001'
        self.phone = DataUtil().createmoble()
        self.projectId = CreateProject().create_project(self.projectName,self.beginTime,self.endTime,self.customerName,
                                                        self.customerCode,self.phone,'黄经理')

    def tearDown(self):
        self.logger.info('############################ TestProjectSelect END ############################')


    def test_project_create_projectName_success(self):
        '''按项目名称查询项目列表'''
        response = ProjectSelect().project_select(projectStatus='0',projectName=self.projectName)
        self.logger.info('按项目名称查询项目列表返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('输入项目名称：{0}，按项目名称查询项目列表返回结果是：{1}'.format(self.projectName,
                                                                  response.json()))
        project_list = ProjectSelect().project_select(projectName=self.projectName, projectStatus='0').json()[
            'content']['dataList']
        if project_list != []:
            L = []
            for project in project_list:
                L.append(str(project['projectId']))
            self.assertIn(self.projectId, L, 'project selected fail!')
        else:
            self.logger.error('Please check the results of the project for empty')

if __name__ == '__main__':
    unittest.main()