#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class CostSettingsUpdate(object):
    '''
    收入成本参数配置修改(与添加)
    /api/tms/finance/saveOrUpdateIncomeCostConfig
    '''
    __slots__ = ('__costSettingsUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__costSettingsUpdateApiUrl = 'https://{0}:{1}{2}/api/tms/finance/saveOrUpdateIncomeCostConfig'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def cost_settings_update(self,Id='',carType='',sendCity='',arriveCity='',carLength='',carModel='',kilometers='',
                             calculateType='',perIncome='',projectId='',oilCost='',roadCost='',repairCost='',
                             depreciationCost='',insurance='',personCost='',taxRate='',otherCost='',infoCost=''):
         '''收入成本参数配置修改(与添加)'''
         try:
             payload = {
                 'id': Id,  # 收入成本参数配置表主键(添加时不需要传入，修改时需要传入)
                 # 必须参数
                 'carType': carType,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'carLength': carLength,
                 'carModel': carModel,
                 'kilometers': kilometers,
                 'calculateType': calculateType,
                 'perIncome': perIncome,  # 每单位计费的收入
                 # 非必须参数
                 'projectId': projectId,
                 'oilCost': oilCost,
                 'roadCost': roadCost,
                 'repairCost': repairCost,
                 'depreciationCost': depreciationCost,
                 'insurance': insurance,
                 'personCost': personCost,
                 'taxRate': taxRate,
                 'otherCost': otherCost,
                 'infoCost': infoCost,
             }
             response = HttpClient().post_json(self.__costSettingsUpdateApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception:
             raise
             # return None