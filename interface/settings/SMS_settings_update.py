#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class SMSSettingsUpdate(object):
    '''
    修改短信设置
    /api/tms/system/sms/updateSetting
    '''
    __slots__ = ('__SMSSettingsUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__SMSSettingsUpdateApiUrl = "https://{0}:{1}{2}/api/tms/system/sms/updateSetting".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def SMS_settings_update(self,name='',mobile='',sendContent='',sendTime=''):
         '''修改短信设置'''
         try:
             payload = {
                 'receiver': [{'name': name, 'mobile': mobile}],
                 'sendContent': sendContent,
                 'sendTime': sendTime,
             }
             response = HttpClient().post_json(self.__SMSSettingsUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None