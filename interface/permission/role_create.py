#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class RoleCreate(object):
    '''
    新增角色
    /api/tms/system/createRole
    '''
    __slots__ = ('__roleCreateApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__roleCreateApiUrl = 'https://{0}:{1}{2}/api/tms/system/createRole'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def role_create(self,roleName='',menuJson=''):
         '''新增角色'''
         try:
             payload ={
                 'partnerNo': self.partnerNo,
                 'roleName':  roleName,
                 'menuJson': menuJson,
             }
             response = HttpClient().post_json(self.__roleCreateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None