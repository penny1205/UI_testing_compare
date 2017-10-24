#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.line.line_create import LineCreate
from interface.line.line_select import LineSelect
from interface.line.line_delete import LineDelete
from interface.project.project_select import ProjectSelect
from interface.line.line_distance_get import LineDistanceGet
from bvt.common.create_project import CreateProject

class CreateLine(object):
    '''新增线路'''

    def __init__(self):
        self.logger = Log()

    def create_line(self,sendProvince,sendCity,arriveProvince,arriveCity,arriveTime,
                    projectName, startTime, endTime, customerName, customerCode, phone,customerDeveloper):
        '''新增线路'''
        try:
            # 选择项目
            project_list = ProjectSelect().project_select(rows='1000', projectStatus='1').json()['content']['dataList']
            if project_list == []:
                projectId = CreateProject().create_project(projectName, startTime, endTime, customerName, customerCode,
                                                           phone,customerDeveloper)
                self.project = {'projectId': projectId, 'projectName': projectName}
                self.logger.info('新建的项目是: {0}'.format(self.project))
            else:
                self.project = random.sample(project_list, 1)[0]
                self.logger.info('选择的项目是: {0}'.format(self.project))

            mileage = LineDistanceGet().line_get(sendCity,arriveCity,sendProvince+sendCity,
                                                 arriveProvince+arriveCity).json()['content']

            response = LineCreate().line_create(sendProvince,sendCity,arriveProvince,arriveCity,mileage,arriveTime,
                                                self.project['projectId'])

            # 判断线路是否已经创建
            if response.json()['code'] == 0:
                print(response.json()['content'],mileage,self.project['projectId'])
                return response.json()['content'],mileage,self.project['projectId']
            elif response.json()['code'] == 9020707:
                line_list = LineSelect().line_select(projectId=self.project['projectId'],sendCity=sendCity,
                                                     arriveCity=arriveCity).json()['content']['dataList']
                if len(line_list) == 1:
                    LineDelete().line_delete(line_list[0]['id'])
                    Id = LineCreate().line_create(sendProvince, sendCity, arriveProvince, arriveCity, mileage,
                                                  arriveTime, self.project['projectId']).json()['content']
                    return Id,mileage,self.project['projectId']
                else:
                    self.logger.error('项目中该线路已经存在判断错误！')
                    return None,None,None
            else:
                return None,None,None
        except Exception:
            return None