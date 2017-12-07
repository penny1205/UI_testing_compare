#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class SMSSettingsGet(object):
    '''
    获取短信设置
    /api/tms/system/sms/getSetting
    '''
    __slots__ = ('__SMSSettingsGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__SMSSettingsGetApiUrl = "https://{0}:{1}{2}/api/tms/system/sms/getSetting".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def SMS_settings_get(self):
         '''获取短信设置'''
         try:
             response = HttpClient().get(self.__SMSSettingsGetApiUrl,self.__head_dict)
             return response
         except Exception as e:
             Log().error('获取短信设置发生异常:{0}'.format(e))
             return None