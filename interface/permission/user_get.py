#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class UserGet(object):
    '''
    账号详情
    /api/tms/system/getTmsUserById
    '''
    __slots__ = ('__userDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/system/getTmsUserById'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_get(self,userId=''):
         '''账号详情'''
         try:
             payload ={
                 'loginId': userId,
             }
             response = HttpClient().get(self.__userDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None