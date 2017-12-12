#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

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

    def cost_settings_update(self,Id='',carType='',sendProvince='',sendCity='',sendDistrict='',arriveProvince='',
                             arriveCity='',arriveDistrict='',stationAProvince='',stationACity='',stationADistrict='',
                             stationBProvince='',stationBCity='',stationBDistrict='',
                             carLength='',carModel='',kilometers='',
                             calculateType='',perIncome='',projectId='',oilCost='',roadCost='',repairCost='',
                             depreciationCost='',insurance='',personCost='',taxRate='',otherCost='',infoCost=''):
         '''收入成本参数配置修改(与添加)'''
         try:
             payload = {
                 'id': Id,  # 收入成本参数配置表主键(添加时不需要传入，修改时需要传入)
                 'carType': carType,
                 'sendProvince':sendProvince,
                 'sendCity': sendCity,
                 'sendDistrict':sendDistrict,
                 'arriveProvince':arriveProvince,
                 'arriveCity': arriveCity,
                 'arriveDistrict':arriveDistrict,
                 'stationAProvince':stationAProvince,
                 'stationACity':stationACity,
                 'stationADistrict':stationADistrict,
                 'stationBProvince':stationBProvince,
                 'stationBCity':stationBCity,
                 'stationBDistrict':stationBDistrict,
                 'carLength': carLength,
                 'carModel': carModel,
                 'kilometers': kilometers,
                 'calculateType': calculateType,
                 'perIncome': perIncome,  # 每单位计费的收入
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
         except Exception as e:
             Log().error('收入成本参数配置修改(与添加)发生异常:{0}'.format(e))
             return None