#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
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
            CreateCostSettings.my_print('新建的项目是: {0}'.format(project))
        else:
            project = random.sample(project_list, 1)[0]
            CreateCostSettings.my_print('选择的项目是: {0}'.format(project))
        return project

    def create_cost_settings(self, carType, sendProvince, sendCity, arriveProvince, arriveCity,carLength, carModel,
                             calculateType, perIncome, oilCost, roadCost, repairCost,depreciationCost, insurance,
                             personCost, taxRate, otherCost, infoCost):
        '''新增成本参数配置'''

        try:
            project = CreateCostSettings().project_choice()
            # 计算距离
            self.kilometers = LineDistanceGet().line_get(sendCity, arriveCity, sendProvince + sendCity,
                                                         arriveProvince + arriveCity).json()['content']
            response = CostSettingsUpdate().cost_settings_update('', carType, sendCity,arriveCity,
                                                                 carLength, carModel, self.kilometers,calculateType,
                                                                 perIncome, project['projectId'],oilCost, roadCost,
                                                                 repairCost,depreciationCost, insurance, personCost,
                                                                 taxRate, otherCost, infoCost)
            return  response.json()['content'],self.kilometers,project['projectId']
        except Exception:
            self.logger.error('新增成本参数配置发生异常:{0}'.format(Exception))
            return None