#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class RoleDelete(object):
    '''
    删除角色
    /api/tms/system/deleteRole
    '''
    __slots__ = ('__roleDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__roleDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/system/deleteRole'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def role_delete(self,roleId=''):
         '''删除角色'''
         try:
             payload ={
                 'roleId': roleId,
             }
             response = HttpClient().post_form(self.__roleDeleteApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None