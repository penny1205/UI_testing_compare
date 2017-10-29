#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class CostSettingsSelect(object):
    '''
    收入成本参数配置列表查询
    /api/tms/finance/getIncomeCostConfigList
    '''
    __slots__ = ('__costSettingsSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__costSettingsSelectApiUrl = 'https://{0}:{1}{2}/api/tms/finance/getIncomeCostConfigList'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def cost_settings_select(self,currentPage='1',rows='10',sendCity='',arriveCity='',carType='',carLength='',carModel='',
                             projectId=''):
         '''收入成本参数配置列表查询'''
         try:
             payload = {
                 'currentPage': currentPage,
                 'rows': rows,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'carType': carType,
                 'carLength': carLength,
                 'carModel': carModel,
                 'projectId': projectId,
             }
             response = HttpClient().post_json(self.__costSettingsSelectApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None