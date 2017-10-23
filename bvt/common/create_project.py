#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.log.log import Log
from util.db.dbutil import DBUtil
from util.file.fileutil import FileUtil
from util.config.yaml.readyaml import ReadYaml
from interface.project.project_create import ProjectCreate
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
                return None
        except Exception:
            return None