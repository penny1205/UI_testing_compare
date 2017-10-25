#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.settings.cost_settings_update import CostSettingsUpdate
from interface.line.line_distance_get import LineDistanceGet
from interface.project.project_select import ProjectSelect
from bvt.common.create_project import CreateProject

class CreateCostSettings(object):
    '''新增成本参数配置'''

    def __init__(self):
        self.logger = Log()

    def create_cost_settings(self, carType, sendProvince, sendCity, arriveProvince, arriveCity,carLength, carModel,
                             calculateType, perIncome, oilCost, roadCost, repairCost,depreciationCost, insurance,
                             personCost, taxRate, otherCost, infoCost,
                             projectName,startTime,endTime,customerName,customerCode,phone,customerDeveloper):
        '''新增项目'''
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

            # 计算距离
            self.kilometers = LineDistanceGet().line_get(sendCity, arriveCity, sendProvince + sendCity,
                                                         arriveProvince + arriveCity).json()['content']
            response = CostSettingsUpdate().cost_settings_update('', carType, sendCity,arriveCity,
                                                                 carLength, carModel, self.kilometers,calculateType,
                                                                 perIncome, self.project['projectId'],oilCost, roadCost,
                                                                 repairCost,depreciationCost, insurance, personCost,
                                                                 taxRate, otherCost, infoCost)
            return  response.json()['content'],self.kilometers,self.project['projectId']
        except Exception:
            return None