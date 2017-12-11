#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
from util.log.log import Log
from interface.line.line_create import LineCreate
from interface.line.line_select import LineSelect
from interface.line.line_delete import LineDelete
from interface.project.project_select import ProjectSelect
from interface.line.line_mileage_more_get import LineMileageMoreGet
from bvt.common.create_project import CreateProject

class CreateLine(object):
    '''新增线路'''

    def __init__(self):
        self.logger = Log()

    @staticmethod
    def my_print(msg):
        logger = Log()
        logger.info(msg)

    # 选择项目
    @staticmethod
    def project_choice(projectName='德邦物流', customerName='德邦集团', customerCode='DB20171101100',
                       phone='13077327043', customerDeveloper='张经理'):
        project_list = ProjectSelect().project_select(rows='1000', projectStatus='1').json()['content']['dataList']
        if project_list == []:
            startTime = time.strftime('%Y-%m-%d')
            endTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 2592000))
            projectId = CreateProject().create_project(projectName, startTime, endTime, customerName, customerCode,
                                                       phone, customerDeveloper)
            project = {'projectId': projectId, 'projectName': projectName}
            CreateLine.my_print('新建的项目是: {0}'.format(project))
        else:
            project = random.sample(project_list, 1)[0]
            CreateLine.my_print('选择的项目是: {0}'.format(project))
        return project

    def create_line(self,sendProvince,sendCity,sendDistrict,arriveProvince,arriveCity,arriveDistrict,stationAProvince,
                    stationACity,stationADistrict,stationBProvince,stationBCity,stationBDistrict,arriveTime):
        '''新增线路'''
        try:
            project = CreateLine().project_choice()

            mileage = LineMileageMoreGet().line_mileage_more_get(sendProvince,sendCity,sendDistrict,stationAProvince,
                                        stationACity,stationADistrict,stationBProvince,stationBCity,stationBDistrict,
                                        arriveProvince,arriveCity,arriveDistrict).json()['content']

            response = LineCreate().line_create(sendProvince,sendCity,sendDistrict,arriveProvince,arriveCity,
                                                arriveDistrict,stationAProvince,stationACity,stationADistrict,
                                                stationBProvince,stationBCity,stationBDistrict,mileage,arriveTime,
                                                project['projectId'])

            # 判断线路是否已经创建
            if response.json()['code'] == 0:
                print(response.json()['content'],mileage,project['projectId'])
                return response.json()['content'],mileage,project['projectId']
            elif response.json()['code'] == 9020707:
                line_list = LineSelect().line_select(projectId=project['projectId'],sendCity=sendCity,
                                                     arriveCity=arriveCity).json()['content']['dataList']
                for line in line_list:
                    LineDelete().line_delete(line['id'])
                Id = LineCreate().line_create(sendProvince,sendCity,sendDistrict,arriveProvince,arriveCity,
                                                arriveDistrict,stationAProvince,stationACity,stationADistrict,
                                                stationBProvince,stationBCity,stationBDistrict,mileage,arriveTime,
                                                project['projectId']).json()['content']
                return Id,mileage,project['projectId']
            else:
                self.logger.error('新增线路返回错误:{0}'.format(response.json()))
                return None,None,None
        except Exception as e:
            self.logger.error('新增线路公共模块发生异常:{0}'.format(e))
            return None