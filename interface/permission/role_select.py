#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class RoleSelect(object):
    '''
    角色列表查询
    /api/tms/system/listRoles
    '''
    __slots__ = ('__roleSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__roleSelectApiUrl = 'https://{0}:{1}{2}/api/tms/system/listRoles'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def role_select(self,currentPage='1',rows='10',roleName=''):
         '''角色列表查询'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'roleName': roleName,
             }
             response = HttpClient().get(self.__roleSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('角色列表查询发生异常:{0}'.format(e))
             return None