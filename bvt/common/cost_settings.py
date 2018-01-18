#__author__ = 'pan'
# -*- coding:utf-8 -*-

import time
import random
from util.log.log import Log
from interface.settings.cost_settings_update import CostSettingsUpdate
from interface.settings.cost_settings_select import CostSettingsSelect
from interface.settings.cost_settings_delete import CostSettingsDelete
from interface.line.line_mileage_more_get import LineMileageMoreGet
from interface.project.project_select import ProjectSelect
from bvt.common.create_project import CreateProject

class CostSettings(object):
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
            CostSettings.my_print('新建的项目是: {0}'.format(project))
        else:
            project = random.sample(project_list, 1)[0]
            CostSettings.my_print('选择的项目是: {0}'.format(project))
        return project

    def create_cost_settings(self,Id, carType, sendProvince, sendCity, sendDistrict, arriveProvince, arriveCity,
                             arriveDistrict, stationAProvince, stationACity, stationADistrict, stationBProvince,
                             stationBCity, stationBDistrict, carLength, carModel, calculateType,
                             perIncome, oilCost, roadCost, repairCost, depreciationCost, insurance,
                             personCost, taxRate, otherCost, infoCost):
        '''新增成本参数配置'''

        try:
            project = CostSettings().project_choice()
            # 计算距离
            self.mileage = LineMileageMoreGet().line_mileage_more_get(sendProvince,sendCity,sendDistrict,stationAProvince,
                                        stationACity,stationADistrict,stationBProvince,stationBCity,stationBDistrict,
                                        arriveProvince,arriveCity,arriveDistrict).json()['content']
            response = CostSettingsUpdate().cost_settings_update(Id, carType, sendProvince, sendCity, sendDistrict,
                    arriveProvince, arriveCity, arriveDistrict, stationAProvince, stationACity, stationADistrict,
                    stationBProvince, stationBCity, stationBDistrict, carLength, carModel, self.mileage,calculateType,
                    perIncome, project['projectId'],oilCost, roadCost, repairCost,depreciationCost, insurance,
                    personCost, taxRate, otherCost, infoCost)
            self.logger.error('新增成本参数配置返回:{0}'.format(response.json()))
            if response.json()['code'] == 0:
                return response.json()['content'],self.mileage,project['projectId']
            elif response.json()['code'] == 9180111:
                cost_settings_list = CostSettingsSelect().cost_settings_select(sendCity=sendCity, arriveCity=arriveCity,
                                    carType=carType,carLength=carLength,carModel=carModel,
                                    projectId = project['projectId']).json()['content']['dataList']
                for cost_settings in cost_settings_list:
                    CostSettingsDelete().cost_settings_delete(cost_settings['id'])
                Id1 = CostSettingsUpdate().cost_settings_update(Id, carType, sendProvince, sendCity, sendDistrict,
                    arriveProvince, arriveCity, arriveDistrict, stationAProvince, stationACity, stationADistrict,
                    stationBProvince, stationBCity, stationBDistrict, carLength, carModel, self.mileage,calculateType,
                    perIncome, project['projectId'],oilCost, roadCost, repairCost,depreciationCost, insurance,
                    personCost, taxRate, otherCost, infoCost).json()['content']
                return  Id1,self.mileage,project['projectId']
            else:
                self.logger.error('新增成本参数配置返回错误:{0}'.format(response.json()))
                return None,None,None
        except Exception as e:
            self.logger.error('新增成本参数配置发生异常:{0}'.format(e))
            return None