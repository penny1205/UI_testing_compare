#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class RoleGet(object):
    '''
    角色详情
    /api/tms/system/getRole
    '''
    __slots__ = ('__roleDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__roleDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/system/getRole'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def role_get(self,roleId=''):
         '''角色详情'''
         try:
             payload ={
                 'roleId': roleId,
             }
             response = HttpClient().get(self.__roleDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('角色详情发生异常:{0}'.format(e))
             return None