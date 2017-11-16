#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class UserPasswordUpdate(object):
    '''
    重置账号密码
    /api/tms/system/updatePassword
    '''
    __slots__ = ('__userPasswordUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userPasswordUpdateApiUrl = 'https://{0}:{1}{2}/api/tms/system/updatePassword'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_password_update(self,userId='',mobile=''):
         '''重置账号密码'''
         try:
             payload ={
                 'loginId': userId,
                 'mobile': mobile,
             }
             response = HttpClient().post_form(self.__userPasswordUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None