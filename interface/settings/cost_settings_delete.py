#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class CostSettingsDelete(object):
    '''
    收入成本参数配置删除
    /api/tms/finance/deleteIncomeCostConfigById
    '''
    __slots__ = ('__costSettingsDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__costSettingsDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/finance/deleteIncomeCostConfigById'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def cost_settings_delete(self,id=''):
         '''收入成本参数配置删除'''
         try:
             payload = {
                 'id': id,
             }
             response = HttpClient().get(self.__costSettingsDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('收入成本参数配置删除发生异常:{0}'.format(e))
             return None