#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
from util.log.log import Log
from util.db.dbutil import DBUtil
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from interface.project.project_create import ProjectCreate
from interface.project.project_select import ProjectSelect
from bvt.common.create_customer import CreateCustomer

class CreateProject(object):
    '''新增项目'''

    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()

    def create_project(self,projectName,startTime,endTime,customerName,customerCode,phone,customerDeveloper):
        '''新增项目'''
        try:
            customerId = CreateCustomer().create_customer(customerName=customerName,customerCode=customerCode,
                                                          phone=phone,customerDeveloper=customerDeveloper)
            response = ProjectCreate().project_create(projectName=projectName,custId=customerId,startTime=startTime,
                                                      endTime=endTime)
            self.logger.info('新增的项目名称是: {0}'.format(projectName))
            # 判断项目名称是否重复
            if response.json()['code'] == 0:
               return response.json()['content']
            elif response.json()['code'] == 9020502:
                sql = 'DELETE FROM YD_TMS_PROJECT WHERE projectName = \'{0}\'and partnerNo = \'{1}\''.format(
                    projectName,self.config['partnerNo'])
                self.DBUtil = DBUtil(host=self.config['db_host'], port=self.config['db_port'],
                                     user=self.config['db_user'], passwd=self.config['db_passwd'],
                                     dbname=self.config['db_dbname'], charset=self.config['db_charset'])
                self.DBUtil.execute_sql(sql)
                projectId = ProjectCreate().project_create(projectName=projectName,custId=customerId,startTime=startTime,
                                                           endTime=endTime).json()['content']
                return projectId
            else:
                self.logger.info('新增的项目名称返回错误:{0}'.format(response.json()))
                return None
        except Exception as e:
            self.logger.error('新增项目发生异常:{0}'.format(e))
            return None

    #选择项目
    def project_choice(self,projectName='德邦物流', customerName='德邦集团', customerCode='DB20171101100',
                       phone='13077327043', customerDeveloper='张经理'):
        project_list = ProjectSelect().project_select(rows='1000', projectStatus='1').json()['content']['dataList']
        if project_list == []:
            startTime = time.strftime('%Y-%m-%d')
            endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 2592000))
            projectId = CreateProject().create_project(projectName, startTime, endTime, customerName, customerCode,
                                                       phone, customerDeveloper)
            project = {'projectId': projectId, 'projectName': projectName}
            self.logger.info('新建的项目是: {0}'.format(project))
        else:
            project = random.sample(project_list, 1)[0]
            self.logger.info('选择的项目是: {0}'.format(project))
        return project

    ##选择项目数据权限
    def project_data_permission_choice(self):
        project_list = ProjectSelect().project_select(rows='1000', projectStatus='1').json()['content']['dataList']
        if project_list == []:
            projectId = ''
            self.logger.info('项目数据权限选择不限')
        else:
            project = random.sample(project_list, 1)[0]
            projectId =project['projectId']
            self.logger.info('项目数据权限选择: {0}'.format(project['projectName']))
        return projectId