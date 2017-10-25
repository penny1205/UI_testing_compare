#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class UserDelete(object):
    '''
    删除账号
    /api/tms/system/deleteTmsUser
    '''
    __slots__ = ('__userDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/system/deleteTmsUser'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_delete(self,userId=''):
         '''删除账号'''
         try:
             payload ={
                 'id': userId,
             }
             response = HttpClient().post_form(self.__userDeleteApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None