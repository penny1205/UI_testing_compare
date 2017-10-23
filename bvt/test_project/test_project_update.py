#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from util.db.dbutil import DBUtil
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from interface.project.project_update import ProjectUpdate
from interface.project.project_select import ProjectSelect
from interface.project.project_get import ProjectGet
from bvt.common.create_project import CreateProject

class TestProjectUpdate(unittest.TestCase):
    '''修改项目'''
    def setUp(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.logger.info('########################### TestProjectUpdate START ###########################')
        self.projectName = '测试项目'
        self.startTime = time.strftime('%Y-%M-%d')
        self.endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 86400))
        self.customerName = '测试之家'
        self.customerCode = 'CSZJ201710200001'
        self.phone = DataUtil().createmoble()
        self.projectId = CreateProject().create_project(self.projectName,self.startTime,self.endTime,self.customerName,
                                                        self.customerCode,self.phone,'黄经理')


    def tearDown(self):
        self.logger.info('############################ TestProjectUpdate END ############################')


    def test_project_update_projectName_success(self):
        '''修改项目名称'''
        project_list = ProjectSelect().project_select(projectStatus='0',projectName=self.projectName).json()[
            'content'][ 'dataList']
        if project_list != [] and len(project_list) == 1:
            for project in project_list:
                self.customerId = project['custId']
        else:
            self.logger.error('Please check the results of the project for error')

        self.projectName_update = '修改项目'
        project_update_list = ProjectSelect().project_select(projectStatus='0', projectName=self.projectName_update).json()[
            'content']['dataList']
        if project_update_list != [] and len(project_update_list) == 1:
            sql = 'DELETE FROM YD_TMS_PROJECT WHERE projectName = \'{0}\'and partnerNo = \'{1}\''.format(
                self.projectName_update, self.config['partnerNo'])
            self.DBUtil = DBUtil(host=self.config['db_host'], port=self.config['db_port'],
                                 user=self.config['db_user'], passwd=self.config['db_passwd'],
                                 dbname=self.config['db_dbname'], charset=self.config['db_charset'])
            self.DBUtil.execute_sql(sql)
        else:
            self.logger.error('Please check the results of the project for error')

        response = ProjectUpdate().project_update(projectId=self.projectId,updateType='1',
                                                  projectName=self.projectName_update,custId=self.customerId,
                                                  startTime =self.startTime,endTime=self.endTime)
        self.logger.info('修改项目名称返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('修改项目名称返回：{0}'.format(response.json()))
        response_get = ProjectGet().project_get(self.projectId)
        self.assertEqual(self.projectName_update, response_get.json()['content']['projectName'], 'Project updated fail!')


if __name__ == '__main__':
    unittest.main()