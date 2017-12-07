#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class SystemParamsSettingsGet(object):
    '''
    获得系统属性配置信息
    /api/tms/system/getSystemParamsSet
    '''
    __slots__ = ('__systemParamsSettingsGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__systemParamsSettingsGetApiUrl = "https://{0}:{1}{2}/api/tms/system/getSystemParamsSet".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def system_params_settings_get(self):
         '''获得系统属性配置信息'''
         try:
             response = HttpClient().get(self.__systemParamsSettingsGetApiUrl,self.__head_dict)
             return response
         except Exception as e:
             Log().error('获得系统属性配置信息发生异常:{0}'.format(e))
             return None