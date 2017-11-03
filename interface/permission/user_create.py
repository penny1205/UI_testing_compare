#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class UserCreate(object):
    '''
    新增账号
    /api/tms/system/createTmsUser
    '''
    __slots__ = ('__userCreateApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userCreateApiUrl = 'https://{0}:{1}{2}/api/tms/system/createTmsUser'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_create(self,roleId='',username='',loginId='',mobile=''):
         '''新增账号'''
         try:
             payload ={
                 'partnerNo': self.partnerNo,
                 'role':  roleId,
                 'name': username,
                 'loginId': loginId,
                 'mobile': mobile,
             }
             response = HttpClient().post_form(self.__userCreateApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception:
             return None